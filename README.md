#  點擴散函數 (Point Spread Function)

## 介紹

這個程式碼適用於計算空間中的相位與振幅分布，在自由空間中傳播的能量場圖。

Input : 工作波長與一組相位和振幅的分布。

Operation process : 將 Input 轉換成複數進行表示，並使用惠更斯-菲涅耳原理 (Huygens–Fresnel principle) 進行運算。

Output : 將記錄傳播過程的每個網格的複數，複數代表自由空間中，相位與振幅疊加的結果。

因此

* 將 Output 取「絕對值」即可取得傳播過程中的「振幅 (Amplitude)」分布。
* 將 Output 取「絕對值平方」即可取得傳播過程中的「能量 (Power)」分布。
* 將 Output 取「相位角」即可取得傳播過程中的「相位 (Phase)」分布。

## 範例

程式碼內有寫一個可以依據聚焦長度與工作波長生成完美聚焦的相位分布。裡面的範例是

* 聚焦長度 (Focus length) = 50 units
* 工作波長 (Wavelength) = 0.5 units

根據上述條件生成出來的相位分布如下圖:

![image](https://github.com/YiChenLai/Point-Spread-Function/blob/master/image/phase%20distribution.png)

同時，預設每一個點的振幅皆為 1。

以上的振幅與相位分布為 Input 條件。

經過計算之後可以得到以下結果 : 

* 振幅分布

![image](https://github.com/YiChenLai/Point-Spread-Function/blob/master/image/Amplitude%20field.png)

* 能量分布

![image](https://github.com/YiChenLai/Point-Spread-Function/blob/master/image/Power%20field.png)

* 相位分布

![image](https://github.com/YiChenLai/Point-Spread-Function/blob/master/image/Phase%20field.png) 







