Yifan Ge
gyifan1@jhu.edu.cn

Streaming Version:
==================
I use Python to write the streaming version. The mapper is fof.mapper.py and the reducer is fof.reducer.py.
1. First upload the two Python sources to S3, for me the locations are s3n://yifan-jhu/fof.mapper.py and s3n://yifan-jhu/fof.reducer.py.
2. Open up Elactic MapReduce Management Console, press the Create New Job Flow button to create a new job flow. Name the job flow and choose Streaming as the job type in the pop-up dialog. And specify the input/output locations, and the mapper/reducer locations. The input location is s3n://friends1000 and the output location should be some directory in my own bucket like s3n://yifan-jhu/outputstreaming.
3. Specify the location of log files in the next dialog, press continue and wait for the job to start.
4. After the job has successfully completed, go to my bucket to check the output and log files.

Custom Jar Version:
===================
As AWS only support Java 6, I change the compiler compliance level to 1.6 in Project Property in Eclipse. I use Eclipse to export a runnable jar archive (fof.jar).
1. Upload fof.jar to S3, my location is s3n://yifan-jhu/fof.jar
2. Open Elactic MapReduce Management Console and create a custom JAR job. Specify the argument as s3n://friends1000 s3n://yifan-jhu/outputjar, and start the job.
3. After the job has successfully completed, go to my bucket to check the output and log files.

Output Locations:
=================
Streaming version: s3n://yifan-jhu/outputstreaming
Custom jar version: s3n://yifan-jhu/outputjar
