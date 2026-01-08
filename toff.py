from switchbot import SwitchBot
import keyboard as kb,time, winreg

token = "トークン"
secret = "シークレット"

bulb_id = "操作したい電球のID"

time.sleep(
	winreg.EnumValue(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Control\Power\User\PowerSchemes\8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c\238c9fa8-0aad-41ed-83f4-97be242c8f20\29f6c1db-86da-48c5-9fdb-f2b67b1f44da"),0)[1] # PCがスリープするまでの時間をレジストリから取得
	-60*4 # タスクスケジューラー側で、最後の操作から4分経過後にアイドル状態と判定される
	-20 # APIの実行がスリープに間に合うように
	)

sb = SwitchBot(token=token, secret=secret)
bulb = sb.device(id=bulb_id)

bulb.command("turn_off")
print("turned off")

# 電球が消えてから、PCがスリープ状態に入る前に操作した場合、再度自動で点灯させる
kb.read_key()
bulb.command("turn_on")