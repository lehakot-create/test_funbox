import redis


class RedisConnector:
    conn = redis.StrictRedis(host='redis',
                             decode_responses=True)

    def write_links(self, receiving_time: int, list_url):
        for url in list_url:
            self.conn.rpush(str(receiving_time), url)

    def get_links(self, time_range: dict):
        if int(time_range['from']) > int(time_range['to']):
            raise "параметр 'from' должен быть меньше параметра 'to'"
        return_list = []
        for key in range(int(time_range['from']), int(time_range['to']) + 1):
            return_list.extend(self.conn.lrange(str(key), 0, -1))
        return return_list
