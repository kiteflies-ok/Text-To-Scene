from fastapi import Request, HTTPException
import redis
import os

redis_client = redis.Redis.from_url(os.getenv("REDIS_URL"))

async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    rate_limit = 10  # Requests per minute
    
    current = redis_client.get(client_ip)
    if current and int(current) > rate_limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    
    redis_client.incr(client_ip, 1)
    redis_client.expire(client_ip, 60)
    return await call_next(request)