# ticketWatch
scrapy python3でのwebスクレイピング

チケットの在庫を監視して、ラインに在庫状況を通知するアプリを作成したかったが、「難しいっ」てなったので単純なWEBアプリに変更

spiderを追加することでスクレイピングするサイトを追加できる
```
scrapy genspider スパイダー名 スクレイピングするサイトのURL
```

scrapy-doを使用　参考サイト：https://qiita.com/gengogo5/items/597fa9e39a628b658c06
プロジェクトディレクトリ(/Apps/ticketWatch)で下記コマンド実行
```
scrapy-do -n scrapy-do
```
