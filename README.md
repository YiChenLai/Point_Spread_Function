#  點擴散函數 (Point-Spread-Function)

這個程式碼適用於計算空間中的相位與振幅分布，在自由空間中傳播的能量場圖。

Input : 一組相位與振幅的分布

Operation process : 將 Input 轉換成複數進行表示，並使用惠更斯-菲涅耳原理 (Huygens–Fresnel principle) 進行運算

Output : 將記錄傳播過程的每個網格的複數，複數代表自由空間中，相位與振幅疊加的結果。

因此

* 將 Output 取「絕對值」即可取得傳播過程中的「振幅 (Amplitude)」分布。
* 將 Output 取「絕對值平方」即可取得傳播過程中的「能量 (Power)」分布。
* 將 Output 取「相位角」即可取得傳播過程中的「相位 (Phase)」分布。