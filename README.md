# Hadoop Docker Lab Setup

This project demonstrates setting up a Hadoop cluster using Docker containers and creating Java applications to interact with HDFS.

## Project Structure

```
Lab Big data 0/
├── docker-compose.yml          # Docker container configuration
├── demo/                       # Maven Java project
│   ├── pom.xml                # Maven dependencies and build configuration
│   ├── src/
│   │   └── main/
│   │       └── java/
│   │           └── edu/
│   │               └── ensias/
│   │                   └── hadoop/
│   │                       ├── Main.java
│   │                       └── hdfslab/
│   │                           ├── HadoopFileStatus.java
│   │                           └── HDFSWrite.java
│   └── target/
│       ├── HDFSWrite.jar      # Generated JAR file
│       └── classes/           # Compiled Java classes
└── README.md                  # This documentation
```

## Docker Setup

### Container Configuration
- **hadoop-master**: Main Hadoop node with NameNode and ResourceManager
  - Ports: 9870 (NameNode UI), 8088 (ResourceManager UI), 8080 (Spark UI), 9000 (NameNode IPC)
  - Shared volume: `C:/Users/mouad/Documents/hadoop_project:/shared_volume`
- **hadoop-slave1**: Worker node (port 8040:8042)
- **hadoop-slave2**: Worker node (port 8041:8042)

### Starting the Cluster
```bash
docker-compose up -d
```

### Accessing the Master Container
```bash
docker exec -it hadoop-master bash
```

## Hadoop Services

### Starting HDFS and YARN
```bash
# Inside the hadoop-master container
start-dfs.sh
start-yarn.sh
```

### Verifying Services
```bash
hdfs dfsadmin -report
```

## HDFS Operations

### Creating Directories
```bash
# Create user directory structure
hdfs dfs -mkdir -p /user/root/input

# Create general input directory
hdfs dfs -mkdir -p /input
```

### File Operations
```bash
# Upload files to HDFS
hdfs dfs -put /shared_volume/purchases.txt /user/root/input/

# List files in HDFS
hdfs dfs -ls /user/root/input/

# Read file content
hdfs dfs -cat /user/root/input/purchases.txt

# Download files from HDFS
hdfs dfs -get /user/root/bonjour.txt /shared_volume/
```

## Java Applications

### HDFSWrite Class
A Java application that creates files in HDFS with custom content.

**Location**: `demo/src/main/java/edu/ensias/hadoop/hdfslab/HDFSWrite.java`

**Functionality**:
- Takes two arguments: file path and message
- Creates a file in HDFS if it doesn't exist
- Writes "Bonjour tout le monde !" and the provided message

### Building the JAR
```bash
# In Windows Command Prompt, navigate to demo directory
cd "C:\Users\mouad\OneDrive - um5.ac.ma\Desktop\Lab Big data 0\demo"

# Build the project
mvn clean compile package

# Copy JAR to shared volume
copy target\HDFSWrite.jar "C:\Users\mouad\Documents\hadoop_project\"
```

### Running the Application
```bash
# Inside hadoop-master container
hadoop jar /shared_volume/HDFSWrite.jar /user/root/bonjour.txt "Hello HDFS!"
hadoop jar /shared_volume/HDFSWrite.jar /user/root/input/bonjour.txt "Hello HDFS!"
```
<img width="1069" height="220" alt="image" src="https://github.com/user-attachments/assets/2ce2405d-91ce-4172-9957-6f3c992e6b64" />

## Maven Configuration

### Dependencies
- `hadoop-hdfs` (3.2.0)
- `hadoop-common` (3.2.0) 
- `hadoop-mapreduce-client-core` (3.2.0)

### Build Configuration
- Java version: 1.8
- Main class: `edu.ensias.hadoop.hdfslab.HDFSWrite`
- Final JAR name: `HDFSWrite.jar`

## Shared Volume

The shared volume allows file exchange between Windows host and Docker containers:
- **Host path**: `C:/Users/mouad/Documents/hadoop_project`
- **Container path**: `/shared_volume`

Files placed in either location are accessible from both environments.

## Web Interfaces

- **Hadoop NameNode UI**: http://localhost:9870
- **Hadoop ResourceManager UI**: http://localhost:8088
- **Spark Master UI**: http://localhost:8080
- **MapReduce History Server**: http://localhost:19888

## Troubleshooting

### Common Issues

1. **HDFS Connection Refused**
   - Ensure HDFS services are started: `start-dfs.sh`
   - Check if NameNode is running: `jps`

2. **Shared Volume Empty**
   - Verify Docker Desktop file sharing permissions
   - Check that files exist in local directory
   - Restart containers if needed

3. **JAR Execution Errors**
   - Rebuild JAR: `mvn clean package`
   - Verify main class configuration in pom.xml
   - Check JAR contents: `jar -tf HDFSWrite.jar`

## Accomplished Tasks

✅ Docker Compose configuration for Hadoop cluster  
✅ HDFS service setup and configuration  
✅ Java application development (HDFSWrite)  
✅ Maven build configuration  
✅ JAR file creation and deployment  
✅ HDFS file operations (create, read, upload, download)  
✅ Shared volume configuration between host and containers  
✅ Successful execution of Hadoop jobs  

## Next Steps

- Implement MapReduce jobs for data processing
- Add more data processing applications
- Configure Spark for big data analytics
- Add data visualization components
