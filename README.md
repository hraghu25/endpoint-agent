# endpoint-agent
This agent will monitor URLs 


--Execute the below command on Mac OS Terminal

python agent.py --config_file=config.yaml


--Create Binary file using pyinstaller 

pyinstaller --onefile=agent.py

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


--Binary file execution

./agent --config_file=config.yaml
