using System.IO;
using System.Text;
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class FileInfo : MonoBehaviour
{
    public int data;
    public int flag = 1;
    private int count;              // カウンター
    void Start()
    {
        // カウンターを初期化
        count = 0;


        // コルーチンの設定
        StartCoroutine(move());
    }

    private IEnumerator move()
    {
        while (true)
        {
            // コルーチンはゲームオブジェクトが非アクティブ
            // になると勝手に止まるので、無限ループでもOK
            string text = ContentOfTxtFile(@"C:\Users\hidek\data.txt");
            Debug.Log(text);
            data = int.Parse(text);   // intに変換
            // カウントアップ
            count++;

            // ログ出力
            Debug.Log(count + "回目の実行です。");

            // 10秒間に1度実行する設定
            yield return new WaitForSeconds(10);
        }
    }

    public static string ContentOfTxtFile(string iPath)
    {
        //Textファイルが存在するなら読み取って、無いならnullを返却
        if (File.Exists(iPath)) return ReadText(iPath);

        Debug.LogError("Txt file not found");
        return null;
    }

    #region ReadText
    private static string ReadText(string iPath)
    {
        // テキスト読み込み処理
        using var fs = new FileStream(iPath, FileMode.Open, FileAccess.Read, FileShare.ReadWrite);
        using var reader = new StreamReader(fs, Encoding.UTF8);
        string textContent = reader.ReadToEnd();
        return textContent;
    }
    #endregion


}