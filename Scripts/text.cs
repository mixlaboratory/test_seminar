using UnityEngine;
using UnityEngine.UI;

public class text : MonoBehaviour
{
    // UI Text指定用
    public Text TextFrame;
    // 表示する変数
    public int num;
    //Manager Manager = GetComponent<Manager>();               //FileInfoからデータを持ってくる
    //num += Manager.num;                                       //sumにFileInfoのsumを入れる

    // Use this for initialization
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        
        TextFrame.text = string.Format("×{0}", num);
    }
}