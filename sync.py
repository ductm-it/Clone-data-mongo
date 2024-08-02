from pymongo import MongoClient

# Kết nối đến máy chủ MongoDB nguồn
source_client = MongoClient('mongodb://mongoadmin:8d361b8eebe4f724@192.168.26.63:27018/')
source_db = source_client['live_worldfone']

# Kết nối đến máy chủ MongoDB đích
target_client = MongoClient('mongodb://localhost:27017/')
target_db = target_client['live_worldfone_local']

# Lấy danh sách các collection trong cơ sở dữ liệu nguồn
collections = source_db.list_collection_names()

# Sao chép từng collection từ cơ sở dữ liệu nguồn sang cơ sở dữ liệu đích
for collection_name in collections:
    source_collection = source_db[collection_name]
    target_collection = target_db[collection_name]
    
    # Lấy tất cả các tài liệu từ collection nguồn
    documents = list(source_collection.find())
    
    # Chèn các tài liệu vào collection đích nếu có tài l:
    if documents:
        target_collection.insert_many(documents)
print("Sao chép cơ sở dữ liệu hoàn tất.")

