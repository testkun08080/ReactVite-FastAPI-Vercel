# ReactVIte-FastAPI-Vercel

# 概要
フロントエンドにReactとVite(+Tailwind) を使ったものと、
バックエンドにFastAPIを使ったアプリをVercel上でホスティングするまでの工程を記したものです。
それぞれサンプル用のレポジトリを用意したので、それぞれをモジュールとしてクローンして、vercelへデプロイします。

それぞれのレポは以下をご覧ください
- フロントエンド　https://github.com/testkun08080/ReactVite-vercel.git
- バックエンド https://github.com/testkun08080/FastAPI-vercel.git
  
#### テンプレートを使って、とりあえずデプロイしたい方

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/import/git?s=https://github.com/testkun08080/ReactVite-FastAPI-Vercel)

#### サンプルページ
https://react-vite-fast-api-vercel.vercel.app/


### 注釈
バックエンドはapiをルートにしないと、vercel上でうまく起動できなかったため、apiとしています。
※何か他の方法があると思いますが、ひとまずapiという名前にしておきます。
requirements.txtも、ルートフォルダ以下に置かないとインストールがうまくいきませんでした。


## 前提条件
- npm Node.js 20+ (インストールは[こちら](https://nodejs.org/en/download/))
- Python 3.12+ (vercelの最新が3.12対応のため - 2025/6/3)
- uv (インストールは[こちら](https://docs.astral.sh/uv/getting-started/installation/))
- Vercel CLI (インストールは[こちら](https://vercel.com/docs/cli#installing-vercel-cli/))


## Vercel CLI を使ってテストからデプロイ/ホスティングまで

1. **クローン**
    ```bash
    git clone https://github.com/testkun08080/ReactVite-FastAPI-Vercel.git
    cd ReactVite-FastAPI-Vercel
   ```
2. **モジュールをインストール**
    ```bash
    cd app
    npm install
    cd ..
3. **ローカルでテスト**
    ```bash
    vercel dev
   ```
4. **vercelへデプロイ（プレビューとして）**
    ```bash
    vercel
   ```
5. **、vercelへデプロイ（プロダクトとして）**
    ```bash
    vercel --prod
   ```