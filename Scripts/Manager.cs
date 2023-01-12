using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Manager : MonoBehaviour
{
    // Start is called before the first frame update
    //-----------------------------------------------------------
    //やってほしいこと:「StartCoroutine(update(Heart_ur))」(拡大メソッド)を次のハート生成までにif文で2つ
    //                  次のハート生成時に1つ入れてほしい
    //----------------------------------------------------------
    public int sum = 0;           //Managerで使うデータ
    int heart_flag = 0;     //左上に増やすかどうか
    int num = 0;

    void Start()
    {
        StartCoroutine(deta());
    }
    public IEnumerator deta()
    {



        while (true)
        {
            GameObject obj = (GameObject)Resources.Load("Heart");
            FileInfo FileInfo = GetComponent<FileInfo>();               //FileInfoからデータを持ってくる
            sum = FileInfo.data + sum;                                       //sumにFileInfoのsumを入れる



            if (sum > 1800)
            {

                sum = 0;
                heart_flag = 1;
                if (heart_flag == 1)
                {
                    GameObject mini_Heart = (GameObject)Instantiate(obj, new Vector3(-12.0f, 16.5f, -8.0f), Quaternion.Euler(-90, 0, 0));
                    mini_Heart.transform.localScale = new Vector3(0.5f, 0.5f, 0.5f);
                    mini_Heart.GetComponent<Renderer>().material.color = Color.red;
                    num++;
                    text text = GetComponent<text>();
                    text.num++;
                    heart_flag = 0;
                }
            }
            yield return new WaitForSeconds(10.0f);                     //1秒後に以下を実行 ok
            Debug.Log(sum);
        }
    }
                                                                                                          
          
            



    public IEnumerator update(GameObject name)                     //5秒間拡大
    {
        yield return new WaitForSeconds(1.0f);                     //1秒後に以下を実行 ok
        name.transform.localScale += new Vector3(0.1f, 0.1f, 0.1f);
        yield return new WaitForSeconds(1.0f);                     //1秒後に以下を実行 ok
        name.transform.localScale += new Vector3(0.1f, 0.1f, 0.1f);
        yield return new WaitForSeconds(1.0f);                     //1秒後に以下を実行 ok
        name.transform.localScale += new Vector3(0.1f, 0.1f, 0.1f);
        yield return new WaitForSeconds(1.0f);                     //1秒後に以下を実行 ok
        name.transform.localScale += new Vector3(0.1f, 0.1f, 0.1f);
        yield return new WaitForSeconds(1.0f);                     //1秒後に以下を実行 ok
        name.transform.localScale += new Vector3(0.1f, 0.1f, 0.1f);

        Debug.Log("大きくなった");                          //確認ok


    }

   
    

    

    
    
    
    
    

    
    
}

