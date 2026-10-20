storage_gb = float(input("Enter storage capacity in Gegabytes (GB): "))
storage_mb = storage_gab*1024
storage_tb = storage_gb/1024 #added feature: convert to terabytes
print(f"Result: {storage_gb} GB = {storage_mb} MB")
print(f"Result: {storage_gb} GB = {storage_tb:.4f} TB")
