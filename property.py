import redis

redis_server = redis.Redis(host='localhost', port=6379)

schedule_frequency = 1                  # scheduler frequency in sec