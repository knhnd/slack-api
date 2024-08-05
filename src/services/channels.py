class Channels:
    def get_all_channel_names(app):
        channels = []
        # データが大きすぎる場合，一括でデータを取得できないので複数のページに分割して取得
        # カーソルは現在処理を行っているページとそのデータの位置を特定する
        cursor = None
        while True:
            result = app.client.conversations_list(
                types="public_channel,private_channel",
                cursor=cursor,
                limit=1000  # 1度に取得するチャンネル数の限度
            )
            channels.extend(result["channels"])
            cursor = result.get("response_metadata", {}).get("next_cursor")
            # カーソルがなければ（次のページがなければ）全件取得完了なので処理を終了
            if not cursor:
                break
        # チャンネル名だけを抽出
        channel_names = [channel["name"] for channel in channels]
        return channel_names
