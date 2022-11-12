# 小鸡翻肛性别检测    
onnx加速运行   
python demo_onnx.py即可   
# 操作指南   
首先点击配置参数进行相机的设备搜索与串口的搜索    
![image](https://user-images.githubusercontent.com/52809781/201456050-3610ba2a-7286-44ab-ad0a-9695371665f4.png)    
点击搜索列表即可完成设备检索，也可进行设别的选择与参数的修改      
![image](https://user-images.githubusercontent.com/52809781/201456112-b87225e7-7b4a-4bd0-895c-734ea7b2a6dd.png)    
设置完成后，回到主页点击开启工业摄像头    
然后点击开始预测便会进行实时预测     
默认状态下程序已开启串口通信监督功能给予相关操作便可    

# 小鸡翻肛门检测的打包方式   
运行   
'''nuitka --standalone --show-progress --show-memory --enable-plugin=pyqt5 --output-dir=out demo_onnx.py'''   
