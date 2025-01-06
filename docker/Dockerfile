# イメージ
FROM python:3

# workspaceディレクトリを作成
WORKDIR /workspace

# workspaceにrequirements.txtをコピー
COPY requirements.txt /workspace/

# requirements.txtのパッケージをインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt