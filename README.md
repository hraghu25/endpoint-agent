## endpoint-agent
This agent will monitor URLs 


### Execute the below command on Mac OS Terminal

```bash
python agent.py --config_file=config.yaml
```


### Create Binary file using pyinstaller 

```bash
pyinstaller --onefile=agent.py
```

Output
```
113 INFO: PyInstaller: 5.13.1
113 INFO: Python: 3.11.0
130 INFO: Platform: macOS-13.5-arm64-arm-64bit
130 INFO: wrote /Users/....../
134 INFO: Extending PYTHONPATH with paths
['/Users/...../url-monitoring-solutions']
237 INFO: checking Analysis
238 INFO: Building because /Users/......./url-monitoring-solutions/agent.py changed
238 INFO: Initializing module dependency graph...
239 INFO: Caching module graph hooks...
244 INFO: Analyzing base_library.zip ...
791 INFO: Loading module hook 'hook-heapq.py' from '/Users/...../url-monitoring-solutions/env/lib/python3.11/site-packages/PyInstaller/hooks'...
835 INFO: Loading module hook 'hook-encodings.py' from '/Users/....../url-monitoring-solutions/env/lib/python3.11/site-packages/PyInstaller/hooks'...
1537 INFO: Loading module hook 'hook-pickle.py' from '/Users/...../url-monitoring-solutions/env/lib/python3.11/site-packages/PyInstaller/hooks'...
2357 INFO: Caching module dependency graph...
2394 INFO: running Analysis Analysis-00.toc
2399 INFO: Analyzing /Users/...../url-monitoring-solutions/agent.py
2674 INFO: Loading module hook 'hook-charset_normalizer.py' from '/Users/...../url-monitoring-solutions/env/lib/python3.11/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
2746 INFO: Loading module hook 'hook-certifi.py' from '/Users/....../url-monitoring-solutions/env/lib/python3.11/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
2877 INFO: Processing module hooks...
2882 INFO: Looking for ctypes DLLs
2887 INFO: Analyzing run-time hooks ...
2888 INFO: Including run-time hook '/Users/....../url-monitoring-solutions/env/lib/python3.11/site-packages/PyInstaller/hooks/rthooks/pyi_rth_inspect.py'
2891 INFO: Looking for dynamic libraries
3111 INFO: Looking for eggs
3112 INFO: Using Python library /Library/Frameworks/Python.framework/Versions/3.11/Python
3113 INFO: Warnings written to /Users/....../url-monitoring-solutions/build/agent/warn-agent.txt
3120 INFO: Graph cross-reference written to /Users/....../url-monitoring-solutions/build/agent/xref-agent.html
3124 INFO: checking PYZ
3126 INFO: EXE target arch: arm64
3126 INFO: Code signing identity: None
3126 INFO: checking PKG
3127 INFO: Building because toc changed
3127 INFO: Building PKG (CArchive) agent.pkg
5309 INFO: Building PKG (CArchive) agent.pkg completed successfully.
5310 INFO: Bootloader /Users/...../url-monitoring-solutions/env/lib/python3.11/site-packages/PyInstaller/bootloader/Darwin-64bit/run
5311 INFO: checking EXE
5312 INFO: Building because toc changed
5312 INFO: Building EXE from EXE-00.toc
5312 INFO: Copying bootloader EXE to /Users/....../url-monitoring-solutions/dist/agent
5313 INFO: Converting EXE to target arch (arm64)
5335 INFO: Removing signature(s) from EXE
5352 INFO: Appending PKG archive to EXE
5354 INFO: Fixing EXE headers for code signing
```

### Binary file execution

```bash
./agent --config_file=config.yaml
```


### When you execute or set the binary as a service, one would notice below output

```bash
[DEBUG] 2023-08-27 17:45:26.807610 :: Received HTTP status code for https://www.google.com is 200
[INFO] 2023-08-27 17:45:26.808134 :: Response code for https://www.google.com is 200
[DEBUG] 2023-08-27 17:45:30.321454 :: Received HTTP status code for https://www.openai.com is 308
[ERROR] 2023-08-27 17:45:30.321616 :: Failed to get response for https://www.openai.com code 308
[DEBUG] 2023-08-27 17:45:34.017672 :: Received HTTP status code for https://www.facebook.com is 200
[INFO] 2023-08-27 17:45:34.018207 :: Response code for https://www.facebook.com is 200
[DEBUG] 2023-08-27 17:47:09.616587 :: Received HTTP status code for https://www.google.com is 200
[INFO] 2023-08-27 17:47:09.617012 :: Response code for https://www.google.com is 200
[DEBUG] 2023-08-27 17:47:12.897992 :: Received HTTP status code for https://www.openai.com is 308
[ERROR] 2023-08-27 17:47:12.898603 :: Failed to get response for https://www.openai.com code 308
[DEBUG] 2023-08-27 17:47:16.611970 :: Received HTTP status code for https://www.facebook.com is 200
[INFO] 2023-08-27 17:47:16.612573 :: Response code for https://www.facebook.com is 200
[DEBUG] 2023-08-27 17:51:03.309841 :: Received HTTP status code for https://www.google.com is 200
[INFO] 2023-08-27 17:51:03.310677 :: Response code for https://www.google.com is 200
[DEBUG] 2023-08-27 17:51:06.490530 :: Received HTTP status code for https://www.openai.com is 308
[ERROR] 2023-08-27 17:51:06.491293 :: Failed to get response for https://www.openai.com code 308
[DEBUG] 2023-08-27 17:51:10.003583 :: Received HTTP status code for https://www.facebook.com is 200
[INFO] 2023-08-27 17:51:10.004045 :: Response code for https://www.facebook.com is 200
[DEBUG] 2023-08-27 18:10:07.155949 :: Received HTTP status code for https://www.google.com is 200
[INFO] 2023-08-27 18:10:07.157695 :: Response code for https://www.google.com is 200
[DEBUG] 2023-08-27 18:10:10.456037 :: Received HTTP status code for https://www.openai.com is 308
[ERROR] 2023-08-27 18:10:10.456409 :: Failed to get response for https://www.openai.com code 308
[DEBUG] 2023-08-27 18:10:13.955365 :: Received HTTP status code for https://www.facebook.com is 200
[INFO] 2023-08-27 18:10:13.955871 :: Response code for https://www.facebook.com is 200
[DEBUG] 2023-08-27 18:28:04.647245 :: Received HTTP status code for https://www.google.com is 200
[INFO] 2023-08-27 18:28:04.648141 :: Response code for https://www.google.com is 200
[DEBUG] 2023-08-27 18:28:07.911662 :: Received HTTP status code for https://www.openai.com is 308
[ERROR] 2023-08-27 18:28:07.912428 :: Failed to get response for https://www.openai.com code 308
[DEBUG] 2023-08-27 18:28:11.311613 :: Received HTTP status code for https://www.facebook.com is 200
[INFO] 2023-08-27 18:28:11.311780 :: Response code for https://www.facebook.com is 200
[DEBUG] 2023-08-27 18:28:19.038927 :: Received HTTP status code for https://www.google.com is 200
[INFO] 2023-08-27 18:28:19.039716 :: Response code for https://www.google.com is 200
[DEBUG] 2023-08-27 18:28:22.130553 :: Received HTTP status code for https://www.openai.com is 308
[ERROR] 2023-08-27 18:28:22.130933 :: Failed to get response for https://www.openai.com code 308
[DEBUG] 2023-08-27 18:28:25.508465 :: Received HTTP status code for https://www.facebook.com is 200
[INFO] 2023-08-27 18:28:25.509138 :: Response code for https://www.facebook.com is 200
[DEBUG] 2023-08-27 18:31:54.952327 :: Received HTTP status code for https://www.google.com is 200
[INFO] 2023-08-27 18:31:54.952913 :: Response code for https://www.google.com is 200
[DEBUG] 2023-08-27 18:31:58.219887 :: Received HTTP status code for https://www.openai.com is 308
[ERROR] 2023-08-27 18:31:58.220638 :: Failed to get response for https://www.openai.com code 308
[DEBUG] 2023-08-27 18:32:01.739785 :: Received HTTP status code for https://www.facebook.com is 200
[INFO] 2023-08-27 18:32:01.740603 :: Response code for https://www.facebook.com is 200
```

