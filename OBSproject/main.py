import obspython as obs

def save_scene_button(props, prop):
        print(obs.obs_save_sources())
        return
def load_scene_button():
        print("シーンのロードをしました")
        return

def script_properties():
        props = obs.obs_properties_create()
        if obs.obs_properties_add_button(props,"save_button", "シーン設定を保存", save_scene_button) is None:
                obs.script_log(obs.LOG_ERROR, "保存ボタンの追加に失敗しました。")
        if obs.obs_properties_add_button(props, "load_button", "シーン設定をロード", load_scene_button) is None:
                obs.script_log(obs.LOG_ERROR, "ロードボタンの追加に失敗しました。")
        return props