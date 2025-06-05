# ReactVIte-FastAPI-Vercel

# 概要
フロントエンドにReactとVite(+Tailwind) を使ったものと、
バックエンドにFastAPIを使ったアプリをVercel上でホスティングするまでの工程を記したものです。
それぞれサンプル用のレポジトリを用意したので、それぞれをモジュールとしてクローンして、vercelへデプロイします。

それぞれのレポは以下をご覧ください
- フロントエンド　https://github.com/testkun08080/ReactVite-vercel.git
- バックエンド https://github.com/testkun08080/FastAPI-vercel.git

### 注釈
バックエンドはapiをルートにしないと、vercel上でうまく起動できなかったため、apiとしています。
※何か他の方法があると思いますが、ひとまずapiという名前にしておきます。
requirements.txtも、ルートフォルダ以下に置かないとインストールがうまくいきませんでした。


## 前提条件
それぞれのレポを参考にしてみてください。
---

## Vercel CLI を使ってテストからデプロイ/ホスティングまで

1. **ローカルでテスト**
    ```bash
    vercel dev
   ```

2. **vercelへデプロイ（プレビューとして）**
    ```bash
    vercel
   ```

3. **、vercelへデプロイ（プロダクトとして）**
    ```bash
    vercel --prod
   ```