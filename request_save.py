from property import redis_server
import csv

r = redis_server
# saving the redis list data in CSV
with open ('vedio_details.csv','w') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(['title',r.lpop('title')])
        writer.writerow(['Video tags',r.lpop('Video tags')])
        writer.writerow(['Views',r.lpop('Views')])
        writer.writerow(['Upload Date',r.lpop('Upload Date')])
        writer.writerow(['channel Title',r.lpop('channel Title')])
        writer.writerow(['Channel Subscribers',r.lpop('Channel Subscribers')])
        writer.writerow(['Video Duration',r.lpop('Video Duration')])
        writer.writerow(['Description',r.lpop('Description')])

        print("data saved  in csv file succefully!!!")