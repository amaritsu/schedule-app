# SimpleDockerTemplate

シンプルなDocker+Djangoのテンプレートです。

- FastAPIはこちら→[FastAPITemplate](https://github.com/SIX1-REPO/FastAPITemplate)

- さらにリッチな環境はこちら（メンテされてないかも）→[DockerTemplate](https://github.com/SIX1-REPO/DockerTemplate)

**作業が終わったらこのファイル（README.md）を削除して、各プロジェクトに合わせて作り直してください。**

## プロジェクトの始め方

1. [このページ](https://github.com/SIX1-REPO/SimpleDockerTemplate)の**Use this Template**を選択し、**Create a new repository**を押す。
   
    ![usage-1](https://github.com/SIX1-REPO/SimpleDockerTemplate/assets/69144657/e9676368-f044-41a4-8c54-40bdedaa0de4)

2. プロジェクト名を入力し，**Create repository**を選択。

   ![usage-2](https://github.com/SIX1-REPO/SimpleDockerTemplate/assets/69144657/b5aaafce-bf2f-4e9d-9f4a-1dd1818636e9)

## アプリの起動

### VSCodeのdevcontainerから（推奨）

devcontainerを使うと、シックスワン全体で共通の設定を使用することができます。

1. [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)の拡張機能をインストールする。

2. コマンドパレット（Windowsは`Ctrl+Shift+P`）を開き、**Dev Containers: Open Folder in Container...** を選択。

3. コンテナが立ち上がるまでしばらく待つ。

4. マイグレーションを実行。

    ```sh
    python manage.py migrate
    ```

5. サーバーを起動。（`python manage.py runserver 0.0.0.0:8000`と同じです）

    ```sh
    make run
    ```

- [http://localhost:8000/](http://localhost:8000/) にアクセスして確認。

### Codespacesから（推奨）

devcontainerの動作が遅い場合は、[GitHub Codespaces](https://github.co.jp/features/codespaces)を試してみましょう。
クラウド上で作業できるので、自分のPCのスペックに影響されません。

1. 先程作ったリポジトリのページで、編集したいブランチを開き、右上の
   **Code** → **Codespaces** → **Create codespace on main** を選択

    ![codespaces-browser-1](https://github.com/SIX1-REPO/SimpleDockerTemplate/assets/69144657/ea3b4599-78a4-459d-87d0-4650ae58f957)

2. コンテナが立ち上がるまでしばらく待つ。

3. devcontainerと同様に、マイグレーションしてサーバーを起動できる。

    ```sh
    python manage.py migrate
    make run
    ```

4. VSCodeのデスクトップアプリを利用する場合は、左上のハンバーガーメニュー（三本線のマーク）を開き、**Open in VS Code Desktop**を選択。

### コマンドラインから

※開発環境の差異を減らすため、出来るだけ上記の2つのいずれかを使用してください。

1. Dockerを立ち上げる。

    ```sh
    docker-compose build
    docker-compose up -d
    ```

2. [http://localhost:8000/](http://localhost:8000/) にアクセスして確認。

## CI/CD

### プロジェクト名の設定

Renderにデプロイするサービス名などを設定します。**必ず最初に行ってください**。

`your_project_name` にプロジェクト名を入力してください。

```sh
PROJECT_NAME=your_project_name
grep -rl six1_template | xargs sed -i "s/six1_template/$PROJECT_NAME/g"
```

### Renderにデプロイ

このテンプレートにはRenderの設定ファイル（`render.yaml`）が含まれているため、すぐにデプロイすることができます。

1. Renderの[Blueprintsのページ](https://dashboard.render.com/blueprints)を開き、**New Blueprint Instance**を押す。

2. リポジトリ一覧が出てくるので、先程作ったリポジトリを選択する。

3. **Blueprint Name** を設定する。

4. `DJANGO_SETTINGS_MODULE`は、`config.settings.prod`に設定する。（本番用の設定）

5. 全て入力したら**Apply** を押す。

![blueprint-main](https://github.com/SIX1-REPO/SimpleDockerTemplate/assets/69144657/40813769-57bb-4a9f-bfc8-795fac12e234)

### 開発用ブランチの設定（任意）

長期にわたるプロジェクトでは、Git-flowを採用して開発用ブランチを作ることがあります。
以下の手順で開発用ブランチに紐づいたサーバーが作れます。

1. まだ作っていなければ、開発用ブランチを作成してプッシュする（ここでは`dev`ブランチとする）

    ```sh
    git branch dev
    git push -u origin dev
    ```

2. 先程と同様にBlueprintを設定する。ただし、**Branch**は開発用ブランチを選択する。

3. **Create New Resources**を選択する。

![blueprint-dev-1](https://github.com/SIX1-REPO/SimpleDockerTemplate/assets/69144657/5e59bcd1-8592-41b9-b911-d005889db5ee)

3. サービス名が変わったことを確認して、**Apply**を押す。

![blueprint-dev-2](https://github.com/SIX1-REPO/SimpleDockerTemplate/assets/69144657/6c8ae519-7c11-420b-9612-ba0e86f9d79d)


### CircleCIの設定

プッシュするたびにCircleCIでlintとtestを行い、成功すればチェックマークが付きます。

- CircleCIを開き、[シックスワンのプロジェクトページ](https://app.circleci.com/projects/project-dashboard/github/SIX1-REPO/)に移動する。

- リポジトリを選択し、**Fastest** が選択された状態で **Set Up Project** をクリックする。

![image](https://user-images.githubusercontent.com/69144657/212475464-f81c1207-0bca-4dfa-ad36-b7cca01e0974.png)

## Tips

### devcontainerの機能

devcontainerやCodespacesを使用することで、様々な恩恵を受けることができます。

- ローカルを汚さない
- 全員が同じ環境で開発できる
- CircleCIと同等のlintツールが自動的に実行され、ハイライトやコードの整形が行われる
- etc...

### CircleCIでlintエラーが出た場合は

まずはエラー箇所を確認します。コンテナ内で以下のコマンドを実行してください。

```sh
make lint
```

一部のエラーは以下のコマンドで自動的に修正できます。

```sh
make format
```

それでも消えないエラーは手動で修正してください。円滑なチーム開発にご協力をお願いします。

なお、どうしても修正できないエラーは`noqa`を使って無視することができます。詳細は調べてください。最終手段として適切に活用しましょう。

### django-debug-toolbar

Djangoのパフォーマンスをチェックできます。ローカルと開発用サーバーで有効化されています。動作が遅いと感じたら、「**時間**」タブや「**SQL**」タブを見てみましょう。

### Poetry

パッケージ管理ツールにPoetryを使用しています。基本的には、`pip install` の代わりに `poetry add` を使うことだけ覚えておけば十分です。

```sh
poetry add <パッケージ名>
```

pipと比較すると以下の点が便利です。

- `pip install`したあとに`requirements.txt`に書き忘れることがない（自動で`pyproject.toml`に追加される）
- lockファイルがある
- 開発環境用のパッケージを別で管理できる
