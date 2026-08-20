# Q5 — Mini scenario (realistic DevOps check)

# Write a script with server_name = "web01", cpu = 88, disk = 70, memory = 95. Using if/elif/else logic, print an overall status:
# "Critical" if any single metric is above 90
# "Warning" if any metric is above 75 but none above 90
# "Healthy" otherwise

server_name="web01"
cpu=88
disk=70
memory=95
if cpu > 90 or disk > 90 or memory > 90:
 print("Critical")
elif cpu > 75 or disk > 75 or memory > 75:
 print("Warning")
else:
 print("Healthy")





#  Wrong method
 # server_name="web01"
# disk=70
# cpu=88
# memory=95
# if disk > 90:
#       if cpu > 90:
#         if memory > 90:
#             print("overall status:Critical")
#         else:
#                print("Healthy")
#                if disk < 90:
#                     if cpu < 90:       
#                          if memory < 90:
#                                 print("overall status Warning")
#                          else:
#                               print("overall status Healthy")


 


                                                           
                               

                                                                      
                                         





                                
                                                  
                                                                      
    
          
