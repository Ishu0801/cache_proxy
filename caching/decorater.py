import functools
import inspect
import caching.keys as key  # for now they have dummy function 
import caching.lfu_system as lfu  #for now they have dummy function
import caching.sequrity as seq

def cacheable(public : bool):
    def decorater(func):
        #Taking the parameter from the func signature
        parameter = inspect.signature(func).parameters

        #validating the request
        if "request" not in parameter:
            raise TypeError(f"Given function {func.__name__} should contain 'request' as parameter.")

        #securing the signature of function
        @functools.wraps(func)
        async def wrapper(*args,**kwargs):  #main wrapper

            #taking the main request from the function parameter
            request = kwargs.get("request")

            if public == False:
                #taking the jwt from the header
                token = request.headers.get("Authorization","").removeprefix("Bearer ").strip()
                payload = seq.decode_token(token)
                user_component = payload.get("sub") if payload else None
            else:
                user_component = None

            #taking path paramete and query parameter form the request
            path_param = request.url.path
            query_param = request.query_params

            #genrating the cache key for LFU
            cache_key = key.key_genrater(path_param = path_param,
                                         query_param = query_param,
                                         jwt_token = user_component)

            #checking if cache key exist or not 
            data = lfu.cacheing_system.find(cache_key = cache_key)

            if data:
                return data

            #conditional execution execute only if data is not present in cache
            incoming_data = await func(*args,**kwargs)

            #storing the data againt the dey for future usage
            lfu.cacheing_system.store(cache_key= cache_key,data = incoming_data)

            return incoming_data

        #correting the signature
        wrapper.__signature__ = inspect.signature(func)

        return wrapper
    
    return decorater



            

