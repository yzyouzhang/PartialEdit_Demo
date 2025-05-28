# This is a Python script to pull files from the PartialEdit folder and save them into the sample folder.

import os
import random

# control random seed
random.seed(42)

original_folder = "/work/hdd/bcza/yzyouzhang/VCTK-Corpus/wav16_silence_trimmed"
E1_folder = "/work/hdd/bcza/yzyouzhang/PartialEdit/Publish_version/E1"
E1C_folder = "/work/hdd/bcza/yzyouzhang/PartialEdit/Publish_version/E1-Codec"
E2_folder = "/work/hdd/bcza/yzyouzhang/VCTK-Corpus/E2"
E2C_folder = "/work/hdd/bcza/yzyouzhang/VCTK-Corpus/E2-Codec"
original_txt_folder = "/work/hdd/bcza/yzyouzhang/VCTK-Corpus/txt"
modified_txt_folder = "/work/hdd/bcza/yzyouzhang/VCTK-Corpus/modified_txt"

list_of_spks = os.listdir(original_folder)

print(list_of_spks)

utt_ids = ['%03d' % i for i in range(1, 430)]  # Assuming utt_ids are from 001 to 100

# randomly sample a string with spk_utt
def sample_spk_utt(spk, utt_ids):
    utt_id = random.choice(utt_ids)
    spk_utt_id = f"{spk}_{utt_id}"

    # print all the filenames
    original_wav_path = os.path.join(original_folder, spk, f"{spk_utt_id}.wav")
    original_txt_path = os.path.join(original_txt_folder, spk, f"{spk_utt_id}.txt")
    E1_wav_path = os.path.join(E1_folder, spk, f"{spk_utt_id}_edited_partial_16k.wav")
    E1C_wav_path = os.path.join(E1C_folder, spk, f"{spk_utt_id}_edited_16k.wav")
    E2_wav_path = os.path.join(E2_folder, spk, f"{spk_utt_id}_edited_partial_16k.wav")
    E2C_wav_path = os.path.join(E2C_folder, spk, f"{spk_utt_id}_edited_16k.wav")
    modified_txt_path = os.path.join(modified_txt_folder, spk, f"{spk_utt_id}_modified.txt")
    

    # verify that all files exist
    if not all(os.path.exists(path) for path in [original_wav_path, original_txt_path, E1_wav_path, E1C_wav_path, E2_wav_path, E2C_wav_path, modified_txt_path]):
        # print(f"One or more files for {spk_utt_id} do not exist.")
        # print the missing files
        # missing_files = [path for path in [original_wav_path, original_txt_path, E1_wav_path, E1C_wav_path, E2_wav_path, E2C_wav_path, modified_txt_path] if not os.path.exists(path)]
        # print("Missing files:", missing_files)
        return None
    else:
        original_txt = open(original_txt_path, 'r').read().strip()
        modified_txt = open(modified_txt_path, 'r').read().strip()
        print(f"Sampled {spk_utt_id}:")
        print(f"Original: {original_txt}")
        print(f"Modified: {modified_txt}")

        # cp files to sample folder
        sample_folder = "./PartialEdit_sample"
        new_original_folder = os.path.join(sample_folder, "original", spk)
        new_original_txt_folder = os.path.join(sample_folder, "original_txt", spk)
        new_E1_folder = os.path.join(sample_folder, "E1", spk)
        new_E1C_folder = os.path.join(sample_folder, "E1-Codec", spk)
        new_E2_folder = os.path.join(sample_folder, "E2", spk)
        new_E2C_folder = os.path.join(sample_folder, "E2-Codec", spk)
        new_modified_txt_folder = os.path.join(sample_folder, "modified_txt", spk)
        os.makedirs(new_original_folder, exist_ok=True)
        os.makedirs(new_original_txt_folder, exist_ok=True)
        os.makedirs(new_E1_folder, exist_ok=True)
        os.makedirs(new_E1C_folder, exist_ok=True)
        os.makedirs(new_E2_folder, exist_ok=True)
        os.makedirs(new_E2C_folder, exist_ok=True)
        os.makedirs(new_modified_txt_folder, exist_ok=True)

        new_original_wav_path = os.path.join(new_original_folder, f"{spk_utt_id}.wav")
        new_original_txt_path = os.path.join(new_original_txt_folder, f"{spk_utt_id}.txt")
        new_E1_wav_path = os.path.join(new_E1_folder, f"{spk_utt_id}_edited_partial_16k.wav")
        new_E1C_wav_path = os.path.join(new_E1C_folder, f"{spk_utt_id}_edited_16k.wav")
        new_E2_wav_path = os.path.join(new_E2_folder, f"{spk_utt_id}_edited_partial_16k.wav")
        new_E2C_wav_path = os.path.join(new_E2C_folder, f"{spk_utt_id}_edited_16k.wav")
        new_modified_txt_path = os.path.join(new_modified_txt_folder, f"{spk_utt_id}_modified.txt")
        os.system(f"cp {original_wav_path} {new_original_wav_path}")
        os.system(f"cp {original_txt_path} {new_original_txt_path}")
        os.system(f"cp {E1_wav_path} {new_E1_wav_path}")
        os.system(f"cp {E1C_wav_path} {new_E1C_wav_path}")
        os.system(f"cp {E2_wav_path} {new_E2_wav_path}")
        os.system(f"cp {E2C_wav_path} {new_E2C_wav_path}")
        os.system(f"cp {modified_txt_path} {new_modified_txt_path}")

        ''' generate the html chuncks by following the format:
        <tr>
              <td class="media-cell">
                <p><strong>p232_159</strong>: We have to move <strong>forward</strong></p>
                <audio controls>
                  <source src="./static/audios/real_chime5/S01_P01_01_mix_soloaudio.wav" type="audio/wav">
                </audio>
              </td>
              <td class="media-cell">
                <p>We have to move <strong>backward</strong></p>
                <audio controls>
                  <source src="./PartialEdit_sample/E1/p232/p232_159_edited_partial_16k.wav" type="audio/wav">
                </audio>
              </td>
              <td class="media-cell">
                <p>We have to move <strong>backward</strong></p>
                <audio controls>
                  <source src="./PartialEdit_sample/E1-Codec/p232/p232_159_edited_16k.wav" type="audio/wav">
                </audio>
              </td>
              <td class="media-cell">
                <p>We have to move <strong>backward</strong></p>
                <audio controls>
                  <source src="./PartialEdit_sample/E2/p232/p232_159_edited_partial_16k.wav" type="audio/wav">
                </audio>
              </td>
              <td class="media-cell">
                <p>We have to move <strong>backward</strong></p>
                <audio controls>
                  <source src="./PartialEdit_sample/E2-Codec/p232/p232_159_edited_16k.wav" type="audio/wav">
                </audio>
              </td>
            </tr>
            '''
        html_chunk = f"""
            <tr>
            <td class="media-cell">
                <p><strong>{spk_utt_id}</strong>: {original_txt}</p>
                <audio controls>
                  <source src="{new_original_wav_path}" type="audio/wav">
                </audio>
              </td>
              <td class="media-cell">
                <p>{modified_txt}</p>
                <audio controls>
                  <source src="{new_E1_wav_path}" type="audio/wav">
                </audio>
              </td>
              <td class="media-cell">
                <p>{modified_txt}</p>
                <audio controls>
                  <source src="{new_E1C_wav_path}" type="audio/wav">
                </audio>
              </td>
              <td class="media-cell">
                <p>{modified_txt}</p>
                <audio controls>
                  <source src="{new_E2_wav_path}" type="audio/wav">
                </audio>
              </td>
              <td class="media-cell">
                <p>{modified_txt}</p>
                <audio controls>
                  <source src="{new_E2C_wav_path}" type="audio/wav">
                </audio>
              </td>
            </tr>
            """

        with open("sampled_data.html", "a") as f:
            f.write(html_chunk)


        pass

if __name__ == "__main__":
    # for _ in range(5):
    spk = 'p232' #random.choice(list_of_spks)
    for _ in range(4):
        sample_spk_utt(spk, utt_ids)
    
    print("Sampled 100 speaker-utterance pairs.")

