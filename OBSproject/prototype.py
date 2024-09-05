import obspython as obs

setting_files = "scene_settings.json"
scene_name = "シーン"
def save_scene_button(props, prop):
        test = obs.obs_data_create()
        if obs.obs_data_save_json(test,setting_files):
                print("シーン設定が保存されました")
                # print(obs.obs_data_get_json(test))
        else:
                print("シーンの保存が出来ませんでした")
        obs.obs_data_release(test)
        return
def load_scene_button(props,prop):
        print("シーンのロードをしました")
        return

def script_properties():
        props = obs.obs_properties_create()
        if obs.obs_properties_add_button(props,         "save_button", "シーン設定を保存", save_scene_button) is None:
                obs.script_log(obs.LOG_ERROR, "保存ボタンの追加に失敗しました。")
        if obs.obs_properties_add_button(props, "load_button", "シーン設定をロード", load_scene_button) is None:
                obs.script_log(obs.LOG_ERROR, "ロードボタンの追加に失敗しました。")
        return props

