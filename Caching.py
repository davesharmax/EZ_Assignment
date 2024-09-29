import redis
import json

# Connect to Redis
cache = redis.Redis(host='your-redis-url', port=6379, db=0)

def get_cached_response(user_input):
    # Check if the response is already cached
    cached_response = cache.get(user_input)
    if cached_response:
        return json.loads(cached_response)
    return None

def save_response_to_cache(user_input, response):
    # Save the new response in the cache with a TTL (e.g., 1 hour)
    cache.setex(user_input, 3600, json.dumps(response))

# Usage
user_input = "Hello, how are you?"
cached = get_cached_response(user_input)
if cached:
    print("Returning cached response:", cached)
else:
    # Call your LLM service and get a new response
    response = llm_service(user_input)
    save_response_to_cache(user_input, response)
    print("Returning new response:", response)
