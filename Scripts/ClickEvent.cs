using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ClickEvent : MonoBehaviour
{
    public GameObject mainCamera;      //メインカメラ格納用
    public GameObject subCamera;       //サブカメラ格納用 


    void Start() {
        //メインカメラとサブカメラをそれぞれ取得
        mainCamera = GameObject.Find("MainCamera");
        subCamera = GameObject.Find("SubCamera");

        //サブカメラを非アクティブにする
        subCamera.SetActive(false);
    }

    void Update() {
        //スペースキーが押されている間、サブカメラをアクティブにする
        if (Input.GetKey("space"))
        {
            //サブカメラをアクティブに設定
            mainCamera.SetActive(false);
            subCamera.SetActive(true);
        }
        if (Input.GetKey("d"))
        {
            //メインカメラをアクティブに設定
            subCamera.SetActive(false);
            mainCamera.SetActive(true);
        }
        if (Input.GetKey("q"))
        {
            UnityEditor.EditorApplication.isPlaying = false;//ゲームプレイ終了
        }
    }

    //関数：オブジェクトをクリックした場合の動作
    public void OnClickObject(string button)
    {
        switch (button)
        {
            case "sound":
                mainCamera.SetActive(false);
                subCamera.SetActive(true);
                //オブジェクトを消す
                Debug.Log("クリック");
                break;

            case "exit":
                UnityEditor.EditorApplication.isPlaying = false;//ゲームプレイ終了
                Debug.Log("終了クリック");
                break;

            case "stamp":
                Debug.Log("スタンプクリック");
                break;

            case "back":
                Debug.Log("バック");
                mainCamera.SetActive(true);
                subCamera.SetActive(false);
                break;
        }
        
    }
}
