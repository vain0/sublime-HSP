# Sublime-HSP
Sublime Text でのHSP3の開発を支援するパッケージ。

## インストール/Install
0. Sublime Text を起動する。
0. `Ctrl+Shift+P` でコマンドパレットを開く。
0. `Package Control: Add Repository` を実行。
0. 入力欄にURL `http://github.com/vain0/sublime-HSP` を貼り付けて決定。
0. 再び `Ctrl+Shift+P`。
0. `Package Control: Install Package` を実行。
0. **Sublime-HSP** パッケージを探す。

## 設定/Settings
### ビルドシステム/Build System
0. [HSP3用簡易コマンドライン コンパイラ cHspComp](http://lldev.jp/hsp/app/chspcomp/) をダウンロード。
0. 展開したファイルにある chspcomp.exe をHSPのフォルダに入れる。
0. chspcmp へのパスを通す。

* `Ctrl+B` でコンパイル+実行 (スクリプトエディタの `F5`) ができる。

### HDL
0. `Preferences` > `Package Settings` > `Sublime-HSP` > `Settings - User` で設定ファイルを開く。
0. 次のように入力して保存。
  * `C:\\hsp` はHSPフォルダへのパスに置き換える。
  * バックスラッシュは2重に必要なことに注意。(スラッシュ `/` でもよい。)

```json
{
    "hsp_dir": "C:\\hsp"
}
```

* `.hsp` ファイルを開いているときは、スクリプトエディタと同様に `F1` キーでHDLを引ける。
  * デフォルトでは Windows 用の設定しか用意していない。

## 注意点
* 拡張子は `.hsp` を使おう。
  * `.as` は ActionScript と衝突してしまう。

## 権利/Rights
このリポジトリは [potato4d 氏のリポジトリ](https://github.com/potato4d/sublime-HSP) のFork。オリジナルの権利表記は LICENSE ファイルを参照。

(c) 2015 Potato4d

Fork した者、vain0 による編集点もMITライセンスに従う。権利表記は同ファイルに併記してある。
