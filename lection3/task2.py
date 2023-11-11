import psutil
import GPUtil
gpus = GPUtil.getGPUs()
gpusList = []
for gpu in gpus:
    gpuName = gpu.name
    gpuLoad = gpu.load*100
    gpuFreeMemory = gpu.memoryFree
    gpuTotalMemory = gpu.memoryTotal
    gpusList.append([gpuName,gpuLoad,gpuTotalMemory,gpuFreeMemory])


print("number of logical CPUs : ",psutil.cpu_count(), '\n',
      "CPU frequency : ", psutil.cpu_freq()[0], '\n',
      "RAM :", psutil.virtual_memory()[0], '\n',
      "swap memory : ", psutil.swap_memory()[0], '\n',
      "boot time : ", int(psutil.boot_time()), "seconds", '\n',
      "computer name : ", psutil.users()[0][0], '\n',
      "GPU name : ", gpusList[0][0], '\n',
      "GPU load : ", gpusList[0][1], "%", '\n',
      "GPU total memory : ", gpusList[0][2], "MB", '\n',
      "GPU free memory : ", gpusList[0][3], "MB", '\n',
      )