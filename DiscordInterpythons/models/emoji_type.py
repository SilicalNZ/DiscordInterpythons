from enum import Enum


discord_emoji_converter = {
    "100": "๐ฏ",
    "1234": "๐ข",
    "grinning": "๐",
    "smiley": "๐",
    "smile": "๐",
    "grin": "๐",
    "laughing": "๐",
    "satisfied": "๐",
    "sweat_smile": "๐",
    "joy": "๐",
    "rofl": "๐คฃ",
    "rolling_on_the_floor_laughing": "๐คฃ",
    "relaxed": "โบ",
    "blush": "๐",
    "innocent": "๐",
    "slight_smile": "๐",
    "slightly_smiling_face": "๐",
    "upside_down": "๐",
    "upside_down_face": "๐",
    "wink": "๐",
    "relieved": "๐",
    "heart_eyes": "๐",
    "smiling_face_with_3_hearts": "๐ฅฐ",
    "kissing_heart": "๐",
    "kissing": "๐",
    "kissing_smiling_eyes": "๐",
    "kissing_closed_eyes": "๐",
    "yum": "๐",
    "stuck_out_tongue": "๐",
    "stuck_out_tongue_closed_eyes": "๐",
    "stuck_out_tongue_winking_eye": "๐",
    "zany_face": "๐คช",
    "face_with_raised_eyebrow": "๐คจ",
    "face_with_monocle": "๐ง",
    "nerd": "๐ค",
    "nerd_face": "๐ค",
    "sunglasses": "๐",
    "star_struck": "๐คฉ",
    "partying_face": "๐ฅณ",
    "smirk": "๐",
    "unamused": "๐",
    "disappointed": "๐",
    "pensive": "๐",
    "worried": "๐",
    "confused": "๐",
    "slight_frown": "๐",
    "slightly_frowning_face": "๐",
    "frowning2": "โน",
    "white_frowning_face": "โน",
    "persevere": "๐ฃ",
    "confounded": "๐",
    "tired_face": "๐ซ",
    "weary": "๐ฉ",
    "pleading_face": "๐ฅบ",
    "cry": "๐ข",
    "sob": "๐ญ",
    "triumph": "๐ค",
    "angry": "๐ ",
    "rage": "๐ก",
    "face_with_symbols_over_mouth": "๐คฌ",
    "exploding_head": "๐คฏ",
    "flushed": "๐ณ",
    "hot_face": "๐ฅต",
    "cold_face": "๐ฅถ",
    "scream": "๐ฑ",
    "fearful": "๐จ",
    "cold_sweat": "๐ฐ",
    "disappointed_relieved": "๐ฅ",
    "sweat": "๐",
    "hugging": "๐ค",
    "hugging_face": "๐ค",
    "thinking": "๐ค",
    "thinking_face": "๐ค",
    "face_with_hand_over_mouth": "๐คญ",
    "yawning_face": "๐ฅฑ",
    "shushing_face": "๐คซ",
    "lying_face": "๐คฅ",
    "liar": "๐คฅ",
    "no_mouth": "๐ถ",
    "neutral_face": "๐",
    "expressionless": "๐",
    "grimacing": "๐ฌ",
    "rolling_eyes": "๐",
    "face_with_rolling_eyes": "๐",
    "hushed": "๐ฏ",
    "frowning": "๐ฆ",
    "anguished": "๐ง",
    "open_mouth": "๐ฎ",
    "astonished": "๐ฒ",
    "sleeping": "๐ด",
    "drooling_face": "๐คค",
    "drool": "๐คค",
    "sleepy": "๐ช",
    "dizzy_face": "๐ต",
    "zipper_mouth": "๐ค",
    "zipper_mouth_face": "๐ค",
    "woozy_face": "๐ฅด",
    "nauseated_face": "๐คข",
    "sick": "๐คข",
    "face_vomiting": "๐คฎ",
    "sneezing_face": "๐คง",
    "sneeze": "๐คง",
    "mask": "๐ท",
    "thermometer_face": "๐ค",
    "face_with_thermometer": "๐ค",
    "head_bandage": "๐ค",
    "face_with_head_bandage": "๐ค",
    "money_mouth": "๐ค",
    "money_mouth_face": "๐ค",
    "cowboy": "๐ค ",
    "face_with_cowboy_hat": "๐ค ",
    "smiling_imp": "๐",
    "imp": "๐ฟ",
    "japanese_ogre": "๐น",
    "japanese_goblin": "๐บ",
    "clown": "๐คก",
    "clown_face": "๐คก",
    "poop": "๐ฉ",
    "shit": "๐ฉ",
    "hankey": "๐ฉ",
    "poo": "๐ฉ",
    "ghost": "๐ป",
    "skull": "๐",
    "skeleton": "๐",
    "skull_crossbones": "โ ",
    "skull_and_crossbones": "โ ",
    "alien": "๐ฝ",
    "space_invader": "๐พ",
    "robot": "๐ค",
    "robot_face": "๐ค",
    "jack_o_lantern": "๐",
    "smiley_cat": "๐บ",
    "smile_cat": "๐ธ",
    "joy_cat": "๐น",
    "heart_eyes_cat": "๐ป",
    "smirk_cat": "๐ผ",
    "kissing_cat": "๐ฝ",
    "scream_cat": "๐",
    "crying_cat_face": "๐ฟ",
    "pouting_cat": "๐พ",
    "palms_up_together": "๐คฒ",
    "palms_up_together_tone1": "๐คฒ๐ป",
    "palms_up_together_light_skin_tone": "๐คฒ๐ป",
    "palms_up_together_tone2": "๐คฒ๐ผ",
    "palms_up_together_medium_light_skin_tone": "๐คฒ๐ผ",
    "palms_up_together_tone3": "๐คฒ๐ฝ",
    "palms_up_together_medium_skin_tone": "๐คฒ๐ฝ",
    "palms_up_together_tone4": "๐คฒ๐พ",
    "palms_up_together_medium_dark_skin_tone": "๐คฒ๐พ",
    "palms_up_together_tone5": "๐คฒ๐ฟ",
    "palms_up_together_dark_skin_tone": "๐คฒ๐ฟ",
    "open_hands": "๐",
    "open_hands_tone1": "๐๐ป",
    "open_hands_tone2": "๐๐ผ",
    "open_hands_tone3": "๐๐ฝ",
    "open_hands_tone4": "๐๐พ",
    "open_hands_tone5": "๐๐ฟ",
    "raised_hands": "๐",
    "raised_hands_tone1": "๐๐ป",
    "raised_hands_tone2": "๐๐ผ",
    "raised_hands_tone3": "๐๐ฝ",
    "raised_hands_tone4": "๐๐พ",
    "raised_hands_tone5": "๐๐ฟ",
    "clap": "๐",
    "clap_tone1": "๐๐ป",
    "clap_tone2": "๐๐ผ",
    "clap_tone3": "๐๐ฝ",
    "clap_tone4": "๐๐พ",
    "clap_tone5": "๐๐ฟ",
    "handshake": "๐ค",
    "shaking_hands": "๐ค",
    "thumbsup": "๐",
    "+1": "๐",
    "thumbup": "๐",
    "thumbsup_tone1": "๐๐ป",
    "+1_tone1": "๐๐ป",
    "thumbup_tone1": "๐๐ป",
    "thumbsup_tone2": "๐๐ผ",
    "+1_tone2": "๐๐ผ",
    "thumbup_tone2": "๐๐ผ",
    "thumbsup_tone3": "๐๐ฝ",
    "+1_tone3": "๐๐ฝ",
    "thumbup_tone3": "๐๐ฝ",
    "thumbsup_tone4": "๐๐พ",
    "+1_tone4": "๐๐พ",
    "thumbup_tone4": "๐๐พ",
    "thumbsup_tone5": "๐๐ฟ",
    "+1_tone5": "๐๐ฟ",
    "thumbup_tone5": "๐๐ฟ",
    "thumbsdown": "๐",
    "-1": "๐",
    "thumbdown": "๐",
    "thumbsdown_tone1": "๐๐ป",
    "_1_tone1": "๐๐ป",
    "thumbdown_tone1": "๐๐ป",
    "thumbsdown_tone2": "๐๐ผ",
    "_1_tone2": "๐๐ผ",
    "thumbdown_tone2": "๐๐ผ",
    "thumbsdown_tone3": "๐๐ฝ",
    "_1_tone3": "๐๐ฝ",
    "thumbdown_tone3": "๐๐ฝ",
    "thumbsdown_tone4": "๐๐พ",
    "_1_tone4": "๐๐พ",
    "thumbdown_tone4": "๐๐พ",
    "thumbsdown_tone5": "๐๐ฟ",
    "_1_tone5": "๐๐ฟ",
    "thumbdown_tone5": "๐๐ฟ",
    "punch": "๐",
    "punch_tone1": "๐๐ป",
    "punch_tone2": "๐๐ผ",
    "punch_tone3": "๐๐ฝ",
    "punch_tone4": "๐๐พ",
    "punch_tone5": "๐๐ฟ",
    "fist": "โ",
    "fist_tone1": "โ๐ป",
    "fist_tone2": "โ๐ผ",
    "fist_tone3": "โ๐ฝ",
    "fist_tone4": "โ๐พ",
    "fist_tone5": "โ๐ฟ",
    "left_facing_fist": "๐ค",
    "left_fist": "๐ค",
    "left_facing_fist_tone1": "๐ค๐ป",
    "left_fist_tone1": "๐ค๐ป",
    "left_facing_fist_tone2": "๐ค๐ผ",
    "left_fist_tone2": "๐ค๐ผ",
    "left_facing_fist_tone3": "๐ค๐ฝ",
    "left_fist_tone3": "๐ค๐ฝ",
    "left_facing_fist_tone4": "๐ค๐พ",
    "left_fist_tone4": "๐ค๐พ",
    "left_facing_fist_tone5": "๐ค๐ฟ",
    "left_fist_tone5": "๐ค๐ฟ",
    "right_facing_fist": "๐ค",
    "right_fist": "๐ค",
    "right_facing_fist_tone1": "๐ค๐ป",
    "right_fist_tone1": "๐ค๐ป",
    "right_facing_fist_tone2": "๐ค๐ผ",
    "right_fist_tone2": "๐ค๐ผ",
    "right_facing_fist_tone3": "๐ค๐ฝ",
    "right_fist_tone3": "๐ค๐ฝ",
    "right_facing_fist_tone4": "๐ค๐พ",
    "right_fist_tone4": "๐ค๐พ",
    "right_facing_fist_tone5": "๐ค๐ฟ",
    "right_fist_tone5": "๐ค๐ฟ",
    "fingers_crossed": "๐ค",
    "hand_with_index_and_middle_finger_crossed": "๐ค",
    "fingers_crossed_tone1": "๐ค๐ป",
    "hand_with_index_and_middle_fingers_crossed_tone1": "๐ค๐ป",
    "fingers_crossed_tone2": "๐ค๐ผ",
    "hand_with_index_and_middle_fingers_crossed_tone2": "๐ค๐ผ",
    "fingers_crossed_tone3": "๐ค๐ฝ",
    "hand_with_index_and_middle_fingers_crossed_tone3": "๐ค๐ฝ",
    "fingers_crossed_tone4": "๐ค๐พ",
    "hand_with_index_and_middle_fingers_crossed_tone4": "๐ค๐พ",
    "fingers_crossed_tone5": "๐ค๐ฟ",
    "hand_with_index_and_middle_fingers_crossed_tone5": "๐ค๐ฟ",
    "v": "โ",
    "v_tone1": "โ๐ป",
    "v_tone2": "โ๐ผ",
    "v_tone3": "โ๐ฝ",
    "v_tone4": "โ๐พ",
    "v_tone5": "โ๐ฟ",
    "love_you_gesture": "๐ค",
    "love_you_gesture_tone1": "๐ค๐ป",
    "love_you_gesture_light_skin_tone": "๐ค๐ป",
    "love_you_gesture_tone2": "๐ค๐ผ",
    "love_you_gesture_medium_light_skin_tone": "๐ค๐ผ",
    "love_you_gesture_tone3": "๐ค๐ฝ",
    "love_you_gesture_medium_skin_tone": "๐ค๐ฝ",
    "love_you_gesture_tone4": "๐ค๐พ",
    "love_you_gesture_medium_dark_skin_tone": "๐ค๐พ",
    "love_you_gesture_tone5": "๐ค๐ฟ",
    "love_you_gesture_dark_skin_tone": "๐ค๐ฟ",
    "metal": "๐ค",
    "sign_of_the_horns": "๐ค",
    "metal_tone1": "๐ค๐ป",
    "sign_of_the_horns_tone1": "๐ค๐ป",
    "metal_tone2": "๐ค๐ผ",
    "sign_of_the_horns_tone2": "๐ค๐ผ",
    "metal_tone3": "๐ค๐ฝ",
    "sign_of_the_horns_tone3": "๐ค๐ฝ",
    "metal_tone4": "๐ค๐พ",
    "sign_of_the_horns_tone4": "๐ค๐พ",
    "metal_tone5": "๐ค๐ฟ",
    "sign_of_the_horns_tone5": "๐ค๐ฟ",
    "ok_hand": "๐",
    "ok_hand_tone1": "๐๐ป",
    "ok_hand_tone2": "๐๐ผ",
    "ok_hand_tone3": "๐๐ฝ",
    "ok_hand_tone4": "๐๐พ",
    "ok_hand_tone5": "๐๐ฟ",
    "pinching_hand": "๐ค",
    "pinching_hand_tone1": "๐ค๐ป",
    "pinching_hand_light_skin_tone": "๐ค๐ป",
    "pinching_hand_tone2": "๐ค๐ผ",
    "pinching_hand_medium_light_skin_tone": "๐ค๐ผ",
    "pinching_hand_tone3": "๐ค๐ฝ",
    "pinching_hand_medium_skin_tone": "๐ค๐ฝ",
    "pinching_hand_tone4": "๐ค๐พ",
    "pinching_hand_medium_dark_skin_tone": "๐ค๐พ",
    "pinching_hand_tone5": "๐ค๐ฟ",
    "pinching_hand_dark_skin_tone": "๐ค๐ฟ",
    "point_left": "๐",
    "point_left_tone1": "๐๐ป",
    "point_left_tone2": "๐๐ผ",
    "point_left_tone3": "๐๐ฝ",
    "point_left_tone4": "๐๐พ",
    "point_left_tone5": "๐๐ฟ",
    "point_right": "๐",
    "point_right_tone1": "๐๐ป",
    "point_right_tone2": "๐๐ผ",
    "point_right_tone3": "๐๐ฝ",
    "point_right_tone4": "๐๐พ",
    "point_right_tone5": "๐๐ฟ",
    "point_up_2": "๐",
    "point_up_2_tone1": "๐๐ป",
    "point_up_2_tone2": "๐๐ผ",
    "point_up_2_tone3": "๐๐ฝ",
    "point_up_2_tone4": "๐๐พ",
    "point_up_2_tone5": "๐๐ฟ",
    "point_down": "๐",
    "point_down_tone1": "๐๐ป",
    "point_down_tone2": "๐๐ผ",
    "point_down_tone3": "๐๐ฝ",
    "point_down_tone4": "๐๐พ",
    "point_down_tone5": "๐๐ฟ",
    "point_up": "โ",
    "point_up_tone1": "โ๐ป",
    "point_up_tone2": "โ๐ผ",
    "point_up_tone3": "โ๐ฝ",
    "point_up_tone4": "โ๐พ",
    "point_up_tone5": "โ๐ฟ",
    "raised_hand": "โ",
    "raised_hand_tone1": "โ๐ป",
    "raised_hand_tone2": "โ๐ผ",
    "raised_hand_tone3": "โ๐ฝ",
    "raised_hand_tone4": "โ๐พ",
    "raised_hand_tone5": "โ๐ฟ",
    "raised_back_of_hand": "๐ค",
    "back_of_hand": "๐ค",
    "raised_back_of_hand_tone1": "๐ค๐ป",
    "back_of_hand_tone1": "๐ค๐ป",
    "raised_back_of_hand_tone2": "๐ค๐ผ",
    "back_of_hand_tone2": "๐ค๐ผ",
    "raised_back_of_hand_tone3": "๐ค๐ฝ",
    "back_of_hand_tone3": "๐ค๐ฝ",
    "raised_back_of_hand_tone4": "๐ค๐พ",
    "back_of_hand_tone4": "๐ค๐พ",
    "raised_back_of_hand_tone5": "๐ค๐ฟ",
    "back_of_hand_tone5": "๐ค๐ฟ",
    "hand_splayed": "๐",
    "raised_hand_with_fingers_splayed": "๐",
    "hand_splayed_tone1": "๐๐ป",
    "raised_hand_with_fingers_splayed_tone1": "๐๐ป",
    "hand_splayed_tone2": "๐๐ผ",
    "raised_hand_with_fingers_splayed_tone2": "๐๐ผ",
    "hand_splayed_tone3": "๐๐ฝ",
    "raised_hand_with_fingers_splayed_tone3": "๐๐ฝ",
    "hand_splayed_tone4": "๐๐พ",
    "raised_hand_with_fingers_splayed_tone4": "๐๐พ",
    "hand_splayed_tone5": "๐๐ฟ",
    "raised_hand_with_fingers_splayed_tone5": "๐๐ฟ",
    "vulcan": "๐",
    "raised_hand_with_part_between_middle_and_ring_fingers": "๐",
    "vulcan_tone1": "๐๐ป",
    "raised_hand_with_part_between_middle_and_ring_fingers_tone1": "๐๐ป",
    "vulcan_tone2": "๐๐ผ",
    "raised_hand_with_part_between_middle_and_ring_fingers_tone2": "๐๐ผ",
    "vulcan_tone3": "๐๐ฝ",
    "raised_hand_with_part_between_middle_and_ring_fingers_tone3": "๐๐ฝ",
    "vulcan_tone4": "๐๐พ",
    "raised_hand_with_part_between_middle_and_ring_fingers_tone4": "๐๐พ",
    "vulcan_tone5": "๐๐ฟ",
    "raised_hand_with_part_between_middle_and_ring_fingers_tone5": "๐๐ฟ",
    "wave": "๐",
    "wave_tone1": "๐๐ป",
    "wave_tone2": "๐๐ผ",
    "wave_tone3": "๐๐ฝ",
    "wave_tone4": "๐๐พ",
    "wave_tone5": "๐๐ฟ",
    "call_me": "๐ค",
    "call_me_hand": "๐ค",
    "call_me_tone1": "๐ค๐ป",
    "call_me_hand_tone1": "๐ค๐ป",
    "call_me_tone2": "๐ค๐ผ",
    "call_me_hand_tone2": "๐ค๐ผ",
    "call_me_tone3": "๐ค๐ฝ",
    "call_me_hand_tone3": "๐ค๐ฝ",
    "call_me_tone4": "๐ค๐พ",
    "call_me_hand_tone4": "๐ค๐พ",
    "call_me_tone5": "๐ค๐ฟ",
    "call_me_hand_tone5": "๐ค๐ฟ",
    "muscle": "๐ช",
    "muscle_tone1": "๐ช๐ป",
    "muscle_tone2": "๐ช๐ผ",
    "muscle_tone3": "๐ช๐ฝ",
    "muscle_tone4": "๐ช๐พ",
    "muscle_tone5": "๐ช๐ฟ",
    "mechanical_arm": "๐ฆพ",
    "middle_finger": "๐",
    "reversed_hand_with_middle_finger_extended": "๐",
    "middle_finger_tone1": "๐๐ป",
    "reversed_hand_with_middle_finger_extended_tone1": "๐๐ป",
    "middle_finger_tone2": "๐๐ผ",
    "reversed_hand_with_middle_finger_extended_tone2": "๐๐ผ",
    "middle_finger_tone3": "๐๐ฝ",
    "reversed_hand_with_middle_finger_extended_tone3": "๐๐ฝ",
    "middle_finger_tone4": "๐๐พ",
    "reversed_hand_with_middle_finger_extended_tone4": "๐๐พ",
    "middle_finger_tone5": "๐๐ฟ",
    "reversed_hand_with_middle_finger_extended_tone5": "๐๐ฟ",
    "writing_hand": "โ",
    "writing_hand_tone1": "โ๐ป",
    "writing_hand_tone2": "โ๐ผ",
    "writing_hand_tone3": "โ๐ฝ",
    "writing_hand_tone4": "โ๐พ",
    "writing_hand_tone5": "โ๐ฟ",
    "pray": "๐",
    "pray_tone1": "๐๐ป",
    "pray_tone2": "๐๐ผ",
    "pray_tone3": "๐๐ฝ",
    "pray_tone4": "๐๐พ",
    "pray_tone5": "๐๐ฟ",
    "foot": "๐ฆถ",
    "foot_tone1": "๐ฆถ๐ป",
    "foot_light_skin_tone": "๐ฆถ๐ป",
    "foot_tone2": "๐ฆถ๐ผ",
    "foot_medium_light_skin_tone": "๐ฆถ๐ผ",
    "foot_tone3": "๐ฆถ๐ฝ",
    "foot_medium_skin_tone": "๐ฆถ๐ฝ",
    "foot_tone4": "๐ฆถ๐พ",
    "foot_medium_dark_skin_tone": "๐ฆถ๐พ",
    "foot_tone5": "๐ฆถ๐ฟ",
    "foot_dark_skin_tone": "๐ฆถ๐ฟ",
    "leg": "๐ฆต",
    "leg_tone1": "๐ฆต๐ป",
    "leg_light_skin_tone": "๐ฆต๐ป",
    "leg_tone2": "๐ฆต๐ผ",
    "leg_medium_light_skin_tone": "๐ฆต๐ผ",
    "leg_tone3": "๐ฆต๐ฝ",
    "leg_medium_skin_tone": "๐ฆต๐ฝ",
    "leg_tone4": "๐ฆต๐พ",
    "leg_medium_dark_skin_tone": "๐ฆต๐พ",
    "leg_tone5": "๐ฆต๐ฟ",
    "leg_dark_skin_tone": "๐ฆต๐ฟ",
    "mechanical_leg": "๐ฆฟ",
    "lipstick": "๐",
    "kiss": "๐",
    "lips": "๐",
    "tooth": "๐ฆท",
    "bone": "๐ฆด",
    "tongue": "๐",
    "ear": "๐",
    "ear_tone1": "๐๐ป",
    "ear_tone2": "๐๐ผ",
    "ear_tone3": "๐๐ฝ",
    "ear_tone4": "๐๐พ",
    "ear_tone5": "๐๐ฟ",
    "ear_with_hearing_aid": "๐ฆป",
    "ear_with_hearing_aid_tone1": "๐ฆป๐ป",
    "ear_with_hearing_aid_light_skin_tone": "๐ฆป๐ป",
    "ear_with_hearing_aid_tone2": "๐ฆป๐ผ",
    "ear_with_hearing_aid_medium_light_skin_tone": "๐ฆป๐ผ",
    "ear_with_hearing_aid_tone3": "๐ฆป๐ฝ",
    "ear_with_hearing_aid_medium_skin_tone": "๐ฆป๐ฝ",
    "ear_with_hearing_aid_tone4": "๐ฆป๐พ",
    "ear_with_hearing_aid_medium_dark_skin_tone": "๐ฆป๐พ",
    "ear_with_hearing_aid_tone5": "๐ฆป๐ฟ",
    "ear_with_hearing_aid_dark_skin_tone": "๐ฆป๐ฟ",
    "nose": "๐",
    "nose_tone1": "๐๐ป",
    "nose_tone2": "๐๐ผ",
    "nose_tone3": "๐๐ฝ",
    "nose_tone4": "๐๐พ",
    "nose_tone5": "๐๐ฟ",
    "footprints": "๐ฃ",
    "eye": "๐",
    "eyes": "๐",
    "brain": "๐ง ",
    "speaking_head": "๐ฃ",
    "speaking_head_in_silhouette": "๐ฃ",
    "bust_in_silhouette": "๐ค",
    "busts_in_silhouette": "๐ฅ",
    "baby": "๐ถ",
    "baby_tone1": "๐ถ๐ป",
    "baby_tone2": "๐ถ๐ผ",
    "baby_tone3": "๐ถ๐ฝ",
    "baby_tone4": "๐ถ๐พ",
    "baby_tone5": "๐ถ๐ฟ",
    "girl": "๐ง",
    "girl_tone1": "๐ง๐ป",
    "girl_tone2": "๐ง๐ผ",
    "girl_tone3": "๐ง๐ฝ",
    "girl_tone4": "๐ง๐พ",
    "girl_tone5": "๐ง๐ฟ",
    "child": "๐ง",
    "child_tone1": "๐ง๐ป",
    "child_light_skin_tone": "๐ง๐ป",
    "child_tone2": "๐ง๐ผ",
    "child_medium_light_skin_tone": "๐ง๐ผ",
    "child_tone3": "๐ง๐ฝ",
    "child_medium_skin_tone": "๐ง๐ฝ",
    "child_tone4": "๐ง๐พ",
    "child_medium_dark_skin_tone": "๐ง๐พ",
    "child_tone5": "๐ง๐ฟ",
    "child_dark_skin_tone": "๐ง๐ฟ",
    "boy": "๐ฆ",
    "boy_tone1": "๐ฆ๐ป",
    "boy_tone2": "๐ฆ๐ผ",
    "boy_tone3": "๐ฆ๐ฝ",
    "boy_tone4": "๐ฆ๐พ",
    "boy_tone5": "๐ฆ๐ฟ",
    "woman": "๐ฉ",
    "woman_tone1": "๐ฉ๐ป",
    "woman_tone2": "๐ฉ๐ผ",
    "woman_tone3": "๐ฉ๐ฝ",
    "woman_tone4": "๐ฉ๐พ",
    "woman_tone5": "๐ฉ๐ฟ",
    "adult": "๐ง",
    "adult_tone1": "๐ง๐ป",
    "adult_light_skin_tone": "๐ง๐ป",
    "adult_tone2": "๐ง๐ผ",
    "adult_medium_light_skin_tone": "๐ง๐ผ",
    "adult_tone3": "๐ง๐ฝ",
    "adult_medium_skin_tone": "๐ง๐ฝ",
    "adult_tone4": "๐ง๐พ",
    "adult_medium_dark_skin_tone": "๐ง๐พ",
    "adult_tone5": "๐ง๐ฟ",
    "adult_dark_skin_tone": "๐ง๐ฟ",
    "man": "๐จ",
    "man_tone1": "๐จ๐ป",
    "man_tone2": "๐จ๐ผ",
    "man_tone3": "๐จ๐ฝ",
    "man_tone4": "๐จ๐พ",
    "man_tone5": "๐จ๐ฟ",
    "woman_curly_haired": "๐ฉ๐ฆฑ",
    "woman_curly_haired_tone1": "๐ฉ๐ป๐ฆฑ",
    "woman_curly_haired_light_skin_tone": "๐ฉ๐ป๐ฆฑ",
    "woman_curly_haired_tone2": "๐ฉ๐ผ๐ฆฑ",
    "woman_curly_haired_medium_light_skin_tone": "๐ฉ๐ผ๐ฆฑ",
    "woman_curly_haired_tone3": "๐ฉ๐ฝ๐ฆฑ",
    "woman_curly_haired_medium_skin_tone": "๐ฉ๐ฝ๐ฆฑ",
    "woman_curly_haired_tone4": "๐ฉ๐พ๐ฆฑ",
    "woman_curly_haired_medium_dark_skin_tone": "๐ฉ๐พ๐ฆฑ",
    "woman_curly_haired_tone5": "๐ฉ๐ฟ๐ฆฑ",
    "woman_curly_haired_dark_skin_tone": "๐ฉ๐ฟ๐ฆฑ",
    "man_curly_haired": "๐จ๐ฆฑ",
    "man_curly_haired_tone1": "๐จ๐ป๐ฆฑ",
    "man_curly_haired_light_skin_tone": "๐จ๐ป๐ฆฑ",
    "man_curly_haired_tone2": "๐จ๐ผ๐ฆฑ",
    "man_curly_haired_medium_light_skin_tone": "๐จ๐ผ๐ฆฑ",
    "man_curly_haired_tone3": "๐จ๐ฝ๐ฆฑ",
    "man_curly_haired_medium_skin_tone": "๐จ๐ฝ๐ฆฑ",
    "man_curly_haired_tone4": "๐จ๐พ๐ฆฑ",
    "man_curly_haired_medium_dark_skin_tone": "๐จ๐พ๐ฆฑ",
    "man_curly_haired_tone5": "๐จ๐ฟ๐ฆฑ",
    "man_curly_haired_dark_skin_tone": "๐จ๐ฟ๐ฆฑ",
    "woman_red_haired": "๐ฉ๐ฆฐ",
    "woman_red_haired_tone1": "๐ฉ๐ป๐ฆฐ",
    "woman_red_haired_light_skin_tone": "๐ฉ๐ป๐ฆฐ",
    "woman_red_haired_tone2": "๐ฉ๐ผ๐ฆฐ",
    "woman_red_haired_medium_light_skin_tone": "๐ฉ๐ผ๐ฆฐ",
    "woman_red_haired_tone3": "๐ฉ๐ฝ๐ฆฐ",
    "woman_red_haired_medium_skin_tone": "๐ฉ๐ฝ๐ฆฐ",
    "woman_red_haired_tone4": "๐ฉ๐พ๐ฆฐ",
    "woman_red_haired_medium_dark_skin_tone": "๐ฉ๐พ๐ฆฐ",
    "woman_red_haired_tone5": "๐ฉ๐ฟ๐ฆฐ",
    "woman_red_haired_dark_skin_tone": "๐ฉ๐ฟ๐ฆฐ",
    "man_red_haired": "๐จ๐ฆฐ",
    "man_red_haired_tone1": "๐จ๐ป๐ฆฐ",
    "man_red_haired_light_skin_tone": "๐จ๐ป๐ฆฐ",
    "man_red_haired_tone2": "๐จ๐ผ๐ฆฐ",
    "man_red_haired_medium_light_skin_tone": "๐จ๐ผ๐ฆฐ",
    "man_red_haired_tone3": "๐จ๐ฝ๐ฆฐ",
    "man_red_haired_medium_skin_tone": "๐จ๐ฝ๐ฆฐ",
    "man_red_haired_tone4": "๐จ๐พ๐ฆฐ",
    "man_red_haired_medium_dark_skin_tone": "๐จ๐พ๐ฆฐ",
    "man_red_haired_tone5": "๐จ๐ฟ๐ฆฐ",
    "man_red_haired_dark_skin_tone": "๐จ๐ฟ๐ฆฐ",
    "blond_haired_woman": "๐ฑโ",
    "blond_haired_woman_tone1": "๐ฑ๐ปโ",
    "blond_haired_woman_light_skin_tone": "๐ฑ๐ปโ",
    "blond_haired_woman_tone2": "๐ฑ๐ผโ",
    "blond_haired_woman_medium_light_skin_tone": "๐ฑ๐ผโ",
    "blond_haired_woman_tone3": "๐ฑ๐ฝโ",
    "blond_haired_woman_medium_skin_tone": "๐ฑ๐ฝโ",
    "blond_haired_woman_tone4": "๐ฑ๐พโ",
    "blond_haired_woman_medium_dark_skin_tone": "๐ฑ๐พโ",
    "blond_haired_woman_tone5": "๐ฑ๐ฟโ",
    "blond_haired_woman_dark_skin_tone": "๐ฑ๐ฟโ",
    "blond_haired_person": "๐ฑ",
    "person_with_blond_hair": "๐ฑ",
    "blond_haired_person_tone1": "๐ฑ๐ป",
    "person_with_blond_hair_tone1": "๐ฑ๐ป",
    "blond_haired_person_tone2": "๐ฑ๐ผ",
    "person_with_blond_hair_tone2": "๐ฑ๐ผ",
    "blond_haired_person_tone3": "๐ฑ๐ฝ",
    "person_with_blond_hair_tone3": "๐ฑ๐ฝ",
    "blond_haired_person_tone4": "๐ฑ๐พ",
    "person_with_blond_hair_tone4": "๐ฑ๐พ",
    "blond_haired_person_tone5": "๐ฑ๐ฟ",
    "person_with_blond_hair_tone5": "๐ฑ๐ฟ",
    "blond_haired_man": "๐ฑโ",
    "blond_haired_man_tone1": "๐ฑ๐ปโ",
    "blond_haired_man_light_skin_tone": "๐ฑ๐ปโ",
    "blond_haired_man_tone2": "๐ฑ๐ผโ",
    "blond_haired_man_medium_light_skin_tone": "๐ฑ๐ผโ",
    "blond_haired_man_tone3": "๐ฑ๐ฝโ",
    "blond_haired_man_medium_skin_tone": "๐ฑ๐ฝโ",
    "blond_haired_man_tone4": "๐ฑ๐พโ",
    "blond_haired_man_medium_dark_skin_tone": "๐ฑ๐พโ",
    "blond_haired_man_tone5": "๐ฑ๐ฟโ",
    "blond_haired_man_dark_skin_tone": "๐ฑ๐ฟโ",
    "woman_white_haired": "๐ฉ๐ฆณ",
    "woman_white_haired_tone1": "๐ฉ๐ป๐ฆณ",
    "woman_white_haired_light_skin_tone": "๐ฉ๐ป๐ฆณ",
    "woman_white_haired_tone2": "๐ฉ๐ผ๐ฆณ",
    "woman_white_haired_medium_light_skin_tone": "๐ฉ๐ผ๐ฆณ",
    "woman_white_haired_tone3": "๐ฉ๐ฝ๐ฆณ",
    "woman_white_haired_medium_skin_tone": "๐ฉ๐ฝ๐ฆณ",
    "woman_white_haired_tone4": "๐ฉ๐พ๐ฆณ",
    "woman_white_haired_medium_dark_skin_tone": "๐ฉ๐พ๐ฆณ",
    "woman_white_haired_tone5": "๐ฉ๐ฟ๐ฆณ",
    "woman_white_haired_dark_skin_tone": "๐ฉ๐ฟ๐ฆณ",
    "man_white_haired": "๐จ๐ฆณ",
    "man_white_haired_tone1": "๐จ๐ป๐ฆณ",
    "man_white_haired_light_skin_tone": "๐จ๐ป๐ฆณ",
    "man_white_haired_tone2": "๐จ๐ผ๐ฆณ",
    "man_white_haired_medium_light_skin_tone": "๐จ๐ผ๐ฆณ",
    "man_white_haired_tone3": "๐จ๐ฝ๐ฆณ",
    "man_white_haired_medium_skin_tone": "๐จ๐ฝ๐ฆณ",
    "man_white_haired_tone4": "๐จ๐พ๐ฆณ",
    "man_white_haired_medium_dark_skin_tone": "๐จ๐พ๐ฆณ",
    "man_white_haired_tone5": "๐จ๐ฟ๐ฆณ",
    "man_white_haired_dark_skin_tone": "๐จ๐ฟ๐ฆณ",
    "woman_bald": "๐ฉ๐ฆฒ",
    "woman_bald_tone1": "๐ฉ๐ป๐ฆฒ",
    "woman_bald_light_skin_tone": "๐ฉ๐ป๐ฆฒ",
    "woman_bald_tone2": "๐ฉ๐ผ๐ฆฒ",
    "woman_bald_medium_light_skin_tone": "๐ฉ๐ผ๐ฆฒ",
    "woman_bald_tone3": "๐ฉ๐ฝ๐ฆฒ",
    "woman_bald_medium_skin_tone": "๐ฉ๐ฝ๐ฆฒ",
    "woman_bald_tone4": "๐ฉ๐พ๐ฆฒ",
    "woman_bald_medium_dark_skin_tone": "๐ฉ๐พ๐ฆฒ",
    "woman_bald_tone5": "๐ฉ๐ฟ๐ฆฒ",
    "woman_bald_dark_skin_tone": "๐ฉ๐ฟ๐ฆฒ",
    "man_bald": "๐จ๐ฆฒ",
    "man_bald_tone1": "๐จ๐ป๐ฆฒ",
    "man_bald_light_skin_tone": "๐จ๐ป๐ฆฒ",
    "man_bald_tone2": "๐จ๐ผ๐ฆฒ",
    "man_bald_medium_light_skin_tone": "๐จ๐ผ๐ฆฒ",
    "man_bald_tone3": "๐จ๐ฝ๐ฆฒ",
    "man_bald_medium_skin_tone": "๐จ๐ฝ๐ฆฒ",
    "man_bald_tone4": "๐จ๐พ๐ฆฒ",
    "man_bald_medium_dark_skin_tone": "๐จ๐พ๐ฆฒ",
    "man_bald_tone5": "๐จ๐ฟ๐ฆฒ",
    "man_bald_dark_skin_tone": "๐จ๐ฟ๐ฆฒ",
    "bearded_person": "๐ง",
    "bearded_person_tone1": "๐ง๐ป",
    "bearded_person_light_skin_tone": "๐ง๐ป",
    "bearded_person_tone2": "๐ง๐ผ",
    "bearded_person_medium_light_skin_tone": "๐ง๐ผ",
    "bearded_person_tone3": "๐ง๐ฝ",
    "bearded_person_medium_skin_tone": "๐ง๐ฝ",
    "bearded_person_tone4": "๐ง๐พ",
    "bearded_person_medium_dark_skin_tone": "๐ง๐พ",
    "bearded_person_tone5": "๐ง๐ฟ",
    "bearded_person_dark_skin_tone": "๐ง๐ฟ",
    "older_woman": "๐ต",
    "grandma": "๐ต",
    "older_woman_tone1": "๐ต๐ป",
    "grandma_tone1": "๐ต๐ป",
    "older_woman_tone2": "๐ต๐ผ",
    "grandma_tone2": "๐ต๐ผ",
    "older_woman_tone3": "๐ต๐ฝ",
    "grandma_tone3": "๐ต๐ฝ",
    "older_woman_tone4": "๐ต๐พ",
    "grandma_tone4": "๐ต๐พ",
    "older_woman_tone5": "๐ต๐ฟ",
    "grandma_tone5": "๐ต๐ฟ",
    "older_adult": "๐ง",
    "older_adult_tone1": "๐ง๐ป",
    "older_adult_light_skin_tone": "๐ง๐ป",
    "older_adult_tone2": "๐ง๐ผ",
    "older_adult_medium_light_skin_tone": "๐ง๐ผ",
    "older_adult_tone3": "๐ง๐ฝ",
    "older_adult_medium_skin_tone": "๐ง๐ฝ",
    "older_adult_tone4": "๐ง๐พ",
    "older_adult_medium_dark_skin_tone": "๐ง๐พ",
    "older_adult_tone5": "๐ง๐ฟ",
    "older_adult_dark_skin_tone": "๐ง๐ฟ",
    "older_man": "๐ด",
    "older_man_tone1": "๐ด๐ป",
    "older_man_tone2": "๐ด๐ผ",
    "older_man_tone3": "๐ด๐ฝ",
    "older_man_tone4": "๐ด๐พ",
    "older_man_tone5": "๐ด๐ฟ",
    "man_with_chinese_cap": "๐ฒ",
    "man_with_gua_pi_mao": "๐ฒ",
    "man_with_chinese_cap_tone1": "๐ฒ๐ป",
    "man_with_gua_pi_mao_tone1": "๐ฒ๐ป",
    "man_with_chinese_cap_tone2": "๐ฒ๐ผ",
    "man_with_gua_pi_mao_tone2": "๐ฒ๐ผ",
    "man_with_chinese_cap_tone3": "๐ฒ๐ฝ",
    "man_with_gua_pi_mao_tone3": "๐ฒ๐ฝ",
    "man_with_chinese_cap_tone4": "๐ฒ๐พ",
    "man_with_gua_pi_mao_tone4": "๐ฒ๐พ",
    "man_with_chinese_cap_tone5": "๐ฒ๐ฟ",
    "man_with_gua_pi_mao_tone5": "๐ฒ๐ฟ",
    "person_wearing_turban": "๐ณ",
    "man_with_turban": "๐ณ",
    "person_wearing_turban_tone1": "๐ณ๐ป",
    "man_with_turban_tone1": "๐ณ๐ป",
    "person_wearing_turban_tone2": "๐ณ๐ผ",
    "man_with_turban_tone2": "๐ณ๐ผ",
    "person_wearing_turban_tone3": "๐ณ๐ฝ",
    "man_with_turban_tone3": "๐ณ๐ฝ",
    "person_wearing_turban_tone4": "๐ณ๐พ",
    "man_with_turban_tone4": "๐ณ๐พ",
    "person_wearing_turban_tone5": "๐ณ๐ฟ",
    "man_with_turban_tone5": "๐ณ๐ฟ",
    "woman_wearing_turban": "๐ณโ",
    "woman_wearing_turban_tone1": "๐ณ๐ปโ",
    "woman_wearing_turban_light_skin_tone": "๐ณ๐ปโ",
    "woman_wearing_turban_tone2": "๐ณ๐ผโ",
    "woman_wearing_turban_medium_light_skin_tone": "๐ณ๐ผโ",
    "woman_wearing_turban_tone3": "๐ณ๐ฝโ",
    "woman_wearing_turban_medium_skin_tone": "๐ณ๐ฝโ",
    "woman_wearing_turban_tone4": "๐ณ๐พโ",
    "woman_wearing_turban_medium_dark_skin_tone": "๐ณ๐พโ",
    "woman_wearing_turban_tone5": "๐ณ๐ฟโ",
    "woman_wearing_turban_dark_skin_tone": "๐ณ๐ฟโ",
    "man_wearing_turban": "๐ณโ",
    "man_wearing_turban_tone1": "๐ณ๐ปโ",
    "man_wearing_turban_light_skin_tone": "๐ณ๐ปโ",
    "man_wearing_turban_tone2": "๐ณ๐ผโ",
    "man_wearing_turban_medium_light_skin_tone": "๐ณ๐ผโ",
    "man_wearing_turban_tone3": "๐ณ๐ฝโ",
    "man_wearing_turban_medium_skin_tone": "๐ณ๐ฝโ",
    "man_wearing_turban_tone4": "๐ณ๐พโ",
    "man_wearing_turban_medium_dark_skin_tone": "๐ณ๐พโ",
    "man_wearing_turban_tone5": "๐ณ๐ฟโ",
    "man_wearing_turban_dark_skin_tone": "๐ณ๐ฟโ",
    "woman_with_headscarf": "๐ง",
    "woman_with_headscarf_tone1": "๐ง๐ป",
    "woman_with_headscarf_light_skin_tone": "๐ง๐ป",
    "woman_with_headscarf_tone2": "๐ง๐ผ",
    "woman_with_headscarf_medium_light_skin_tone": "๐ง๐ผ",
    "woman_with_headscarf_tone3": "๐ง๐ฝ",
    "woman_with_headscarf_medium_skin_tone": "๐ง๐ฝ",
    "woman_with_headscarf_tone4": "๐ง๐พ",
    "woman_with_headscarf_medium_dark_skin_tone": "๐ง๐พ",
    "woman_with_headscarf_tone5": "๐ง๐ฟ",
    "woman_with_headscarf_dark_skin_tone": "๐ง๐ฟ",
    "police_officer": "๐ฎ",
    "cop": "๐ฎ",
    "police_officer_tone1": "๐ฎ๐ป",
    "cop_tone1": "๐ฎ๐ป",
    "police_officer_tone2": "๐ฎ๐ผ",
    "cop_tone2": "๐ฎ๐ผ",
    "police_officer_tone3": "๐ฎ๐ฝ",
    "cop_tone3": "๐ฎ๐ฝ",
    "police_officer_tone4": "๐ฎ๐พ",
    "cop_tone4": "๐ฎ๐พ",
    "police_officer_tone5": "๐ฎ๐ฟ",
    "cop_tone5": "๐ฎ๐ฟ",
    "woman_police_officer": "๐ฎโ",
    "woman_police_officer_tone1": "๐ฎ๐ปโ",
    "woman_police_officer_light_skin_tone": "๐ฎ๐ปโ",
    "woman_police_officer_tone2": "๐ฎ๐ผโ",
    "woman_police_officer_medium_light_skin_tone": "๐ฎ๐ผโ",
    "woman_police_officer_tone3": "๐ฎ๐ฝโ",
    "woman_police_officer_medium_skin_tone": "๐ฎ๐ฝโ",
    "woman_police_officer_tone4": "๐ฎ๐พโ",
    "woman_police_officer_medium_dark_skin_tone": "๐ฎ๐พโ",
    "woman_police_officer_tone5": "๐ฎ๐ฟโ",
    "woman_police_officer_dark_skin_tone": "๐ฎ๐ฟโ",
    "man_police_officer": "๐ฎโ",
    "man_police_officer_tone1": "๐ฎ๐ปโ",
    "man_police_officer_light_skin_tone": "๐ฎ๐ปโ",
    "man_police_officer_tone2": "๐ฎ๐ผโ",
    "man_police_officer_medium_light_skin_tone": "๐ฎ๐ผโ",
    "man_police_officer_tone3": "๐ฎ๐ฝโ",
    "man_police_officer_medium_skin_tone": "๐ฎ๐ฝโ",
    "man_police_officer_tone4": "๐ฎ๐พโ",
    "man_police_officer_medium_dark_skin_tone": "๐ฎ๐พโ",
    "man_police_officer_tone5": "๐ฎ๐ฟโ",
    "man_police_officer_dark_skin_tone": "๐ฎ๐ฟโ",
    "construction_worker": "๐ท",
    "construction_worker_tone1": "๐ท๐ป",
    "construction_worker_tone2": "๐ท๐ผ",
    "construction_worker_tone3": "๐ท๐ฝ",
    "construction_worker_tone4": "๐ท๐พ",
    "construction_worker_tone5": "๐ท๐ฟ",
    "woman_construction_worker": "๐ทโ",
    "woman_construction_worker_tone1": "๐ท๐ปโ",
    "woman_construction_worker_light_skin_tone": "๐ท๐ปโ",
    "woman_construction_worker_tone2": "๐ท๐ผโ",
    "woman_construction_worker_medium_light_skin_tone": "๐ท๐ผโ",
    "woman_construction_worker_tone3": "๐ท๐ฝโ",
    "woman_construction_worker_medium_skin_tone": "๐ท๐ฝโ",
    "woman_construction_worker_tone4": "๐ท๐พโ",
    "woman_construction_worker_medium_dark_skin_tone": "๐ท๐พโ",
    "woman_construction_worker_tone5": "๐ท๐ฟโ",
    "woman_construction_worker_dark_skin_tone": "๐ท๐ฟโ",
    "man_construction_worker": "๐ทโ",
    "man_construction_worker_tone1": "๐ท๐ปโ",
    "man_construction_worker_light_skin_tone": "๐ท๐ปโ",
    "man_construction_worker_tone2": "๐ท๐ผโ",
    "man_construction_worker_medium_light_skin_tone": "๐ท๐ผโ",
    "man_construction_worker_tone3": "๐ท๐ฝโ",
    "man_construction_worker_medium_skin_tone": "๐ท๐ฝโ",
    "man_construction_worker_tone4": "๐ท๐พโ",
    "man_construction_worker_medium_dark_skin_tone": "๐ท๐พโ",
    "man_construction_worker_tone5": "๐ท๐ฟโ",
    "man_construction_worker_dark_skin_tone": "๐ท๐ฟโ",
    "guard": "๐",
    "guardsman": "๐",
    "guard_tone1": "๐๐ป",
    "guardsman_tone1": "๐๐ป",
    "guard_tone2": "๐๐ผ",
    "guardsman_tone2": "๐๐ผ",
    "guard_tone3": "๐๐ฝ",
    "guardsman_tone3": "๐๐ฝ",
    "guard_tone4": "๐๐พ",
    "guardsman_tone4": "๐๐พ",
    "guard_tone5": "๐๐ฟ",
    "guardsman_tone5": "๐๐ฟ",
    "woman_guard": "๐โ",
    "woman_guard_tone1": "๐๐ปโ",
    "woman_guard_light_skin_tone": "๐๐ปโ",
    "woman_guard_tone2": "๐๐ผโ",
    "woman_guard_medium_light_skin_tone": "๐๐ผโ",
    "woman_guard_tone3": "๐๐ฝโ",
    "woman_guard_medium_skin_tone": "๐๐ฝโ",
    "woman_guard_tone4": "๐๐พโ",
    "woman_guard_medium_dark_skin_tone": "๐๐พโ",
    "woman_guard_tone5": "๐๐ฟโ",
    "woman_guard_dark_skin_tone": "๐๐ฟโ",
    "man_guard": "๐โ",
    "man_guard_tone1": "๐๐ปโ",
    "man_guard_light_skin_tone": "๐๐ปโ",
    "man_guard_tone2": "๐๐ผโ",
    "man_guard_medium_light_skin_tone": "๐๐ผโ",
    "man_guard_tone3": "๐๐ฝโ",
    "man_guard_medium_skin_tone": "๐๐ฝโ",
    "man_guard_tone4": "๐๐พโ",
    "man_guard_medium_dark_skin_tone": "๐๐พโ",
    "man_guard_tone5": "๐๐ฟโ",
    "man_guard_dark_skin_tone": "๐๐ฟโ",
    "detective": "๐ต",
    "spy": "๐ต",
    "sleuth_or_spy": "๐ต",
    "detective_tone1": "๐ต๐ป",
    "spy_tone1": "๐ต๐ป",
    "sleuth_or_spy_tone1": "๐ต๐ป",
    "detective_tone2": "๐ต๐ผ",
    "spy_tone2": "๐ต๐ผ",
    "sleuth_or_spy_tone2": "๐ต๐ผ",
    "detective_tone3": "๐ต๐ฝ",
    "spy_tone3": "๐ต๐ฝ",
    "sleuth_or_spy_tone3": "๐ต๐ฝ",
    "detective_tone4": "๐ต๐พ",
    "spy_tone4": "๐ต๐พ",
    "sleuth_or_spy_tone4": "๐ต๐พ",
    "detective_tone5": "๐ต๐ฟ",
    "spy_tone5": "๐ต๐ฟ",
    "sleuth_or_spy_tone5": "๐ต๐ฟ",
    "woman_detective": "๐ตโ",
    "woman_detective_tone1": "๐ต๐ปโ",
    "woman_detective_light_skin_tone": "๐ต๐ปโ",
    "woman_detective_tone2": "๐ต๐ผโ",
    "woman_detective_medium_light_skin_tone": "๐ต๐ผโ",
    "woman_detective_tone3": "๐ต๐ฝโ",
    "woman_detective_medium_skin_tone": "๐ต๐ฝโ",
    "woman_detective_tone4": "๐ต๐พโ",
    "woman_detective_medium_dark_skin_tone": "๐ต๐พโ",
    "woman_detective_tone5": "๐ต๐ฟโ",
    "woman_detective_dark_skin_tone": "๐ต๐ฟโ",
    "man_detective": "๐ตโ",
    "man_detective_tone1": "๐ต๐ปโ",
    "man_detective_light_skin_tone": "๐ต๐ปโ",
    "man_detective_tone2": "๐ต๐ผโ",
    "man_detective_medium_light_skin_tone": "๐ต๐ผโ",
    "man_detective_tone3": "๐ต๐ฝโ",
    "man_detective_medium_skin_tone": "๐ต๐ฝโ",
    "man_detective_tone4": "๐ต๐พโ",
    "man_detective_medium_dark_skin_tone": "๐ต๐พโ",
    "man_detective_tone5": "๐ต๐ฟโ",
    "man_detective_dark_skin_tone": "๐ต๐ฟโ",
    "woman_health_worker": "๐ฉโ",
    "woman_health_worker_tone1": "๐ฉ๐ปโ",
    "woman_health_worker_light_skin_tone": "๐ฉ๐ปโ",
    "woman_health_worker_tone2": "๐ฉ๐ผโ",
    "woman_health_worker_medium_light_skin_tone": "๐ฉ๐ผโ",
    "woman_health_worker_tone3": "๐ฉ๐ฝโ",
    "woman_health_worker_medium_skin_tone": "๐ฉ๐ฝโ",
    "woman_health_worker_tone4": "๐ฉ๐พโ",
    "woman_health_worker_medium_dark_skin_tone": "๐ฉ๐พโ",
    "woman_health_worker_tone5": "๐ฉ๐ฟโ",
    "woman_health_worker_dark_skin_tone": "๐ฉ๐ฟโ",
    "man_health_worker": "๐จโ",
    "man_health_worker_tone1": "๐จ๐ปโ",
    "man_health_worker_light_skin_tone": "๐จ๐ปโ",
    "man_health_worker_tone2": "๐จ๐ผโ",
    "man_health_worker_medium_light_skin_tone": "๐จ๐ผโ",
    "man_health_worker_tone3": "๐จ๐ฝโ",
    "man_health_worker_medium_skin_tone": "๐จ๐ฝโ",
    "man_health_worker_tone4": "๐จ๐พโ",
    "man_health_worker_medium_dark_skin_tone": "๐จ๐พโ",
    "man_health_worker_tone5": "๐จ๐ฟโ",
    "man_health_worker_dark_skin_tone": "๐จ๐ฟโ",
    "woman_farmer": "๐ฉ๐พ",
    "woman_farmer_tone1": "๐ฉ๐ป๐พ",
    "woman_farmer_light_skin_tone": "๐ฉ๐ป๐พ",
    "woman_farmer_tone2": "๐ฉ๐ผ๐พ",
    "woman_farmer_medium_light_skin_tone": "๐ฉ๐ผ๐พ",
    "woman_farmer_tone3": "๐ฉ๐ฝ๐พ",
    "woman_farmer_medium_skin_tone": "๐ฉ๐ฝ๐พ",
    "woman_farmer_tone4": "๐ฉ๐พ๐พ",
    "woman_farmer_medium_dark_skin_tone": "๐ฉ๐พ๐พ",
    "woman_farmer_tone5": "๐ฉ๐ฟ๐พ",
    "woman_farmer_dark_skin_tone": "๐ฉ๐ฟ๐พ",
    "man_farmer": "๐จ๐พ",
    "man_farmer_tone1": "๐จ๐ป๐พ",
    "man_farmer_light_skin_tone": "๐จ๐ป๐พ",
    "man_farmer_tone2": "๐จ๐ผ๐พ",
    "man_farmer_medium_light_skin_tone": "๐จ๐ผ๐พ",
    "man_farmer_tone3": "๐จ๐ฝ๐พ",
    "man_farmer_medium_skin_tone": "๐จ๐ฝ๐พ",
    "man_farmer_tone4": "๐จ๐พ๐พ",
    "man_farmer_medium_dark_skin_tone": "๐จ๐พ๐พ",
    "man_farmer_tone5": "๐จ๐ฟ๐พ",
    "man_farmer_dark_skin_tone": "๐จ๐ฟ๐พ",
    "woman_cook": "๐ฉ๐ณ",
    "woman_cook_tone1": "๐ฉ๐ป๐ณ",
    "woman_cook_light_skin_tone": "๐ฉ๐ป๐ณ",
    "woman_cook_tone2": "๐ฉ๐ผ๐ณ",
    "woman_cook_medium_light_skin_tone": "๐ฉ๐ผ๐ณ",
    "woman_cook_tone3": "๐ฉ๐ฝ๐ณ",
    "woman_cook_medium_skin_tone": "๐ฉ๐ฝ๐ณ",
    "woman_cook_tone4": "๐ฉ๐พ๐ณ",
    "woman_cook_medium_dark_skin_tone": "๐ฉ๐พ๐ณ",
    "woman_cook_tone5": "๐ฉ๐ฟ๐ณ",
    "woman_cook_dark_skin_tone": "๐ฉ๐ฟ๐ณ",
    "man_cook": "๐จ๐ณ",
    "man_cook_tone1": "๐จ๐ป๐ณ",
    "man_cook_light_skin_tone": "๐จ๐ป๐ณ",
    "man_cook_tone2": "๐จ๐ผ๐ณ",
    "man_cook_medium_light_skin_tone": "๐จ๐ผ๐ณ",
    "man_cook_tone3": "๐จ๐ฝ๐ณ",
    "man_cook_medium_skin_tone": "๐จ๐ฝ๐ณ",
    "man_cook_tone4": "๐จ๐พ๐ณ",
    "man_cook_medium_dark_skin_tone": "๐จ๐พ๐ณ",
    "man_cook_tone5": "๐จ๐ฟ๐ณ",
    "man_cook_dark_skin_tone": "๐จ๐ฟ๐ณ",
    "woman_student": "๐ฉ๐",
    "woman_student_tone1": "๐ฉ๐ป๐",
    "woman_student_light_skin_tone": "๐ฉ๐ป๐",
    "woman_student_tone2": "๐ฉ๐ผ๐",
    "woman_student_medium_light_skin_tone": "๐ฉ๐ผ๐",
    "woman_student_tone3": "๐ฉ๐ฝ๐",
    "woman_student_medium_skin_tone": "๐ฉ๐ฝ๐",
    "woman_student_tone4": "๐ฉ๐พ๐",
    "woman_student_medium_dark_skin_tone": "๐ฉ๐พ๐",
    "woman_student_tone5": "๐ฉ๐ฟ๐",
    "woman_student_dark_skin_tone": "๐ฉ๐ฟ๐",
    "man_student": "๐จ๐",
    "man_student_tone1": "๐จ๐ป๐",
    "man_student_light_skin_tone": "๐จ๐ป๐",
    "man_student_tone2": "๐จ๐ผ๐",
    "man_student_medium_light_skin_tone": "๐จ๐ผ๐",
    "man_student_tone3": "๐จ๐ฝ๐",
    "man_student_medium_skin_tone": "๐จ๐ฝ๐",
    "man_student_tone4": "๐จ๐พ๐",
    "man_student_medium_dark_skin_tone": "๐จ๐พ๐",
    "man_student_tone5": "๐จ๐ฟ๐",
    "man_student_dark_skin_tone": "๐จ๐ฟ๐",
    "woman_singer": "๐ฉ๐ค",
    "woman_singer_tone1": "๐ฉ๐ป๐ค",
    "woman_singer_light_skin_tone": "๐ฉ๐ป๐ค",
    "woman_singer_tone2": "๐ฉ๐ผ๐ค",
    "woman_singer_medium_light_skin_tone": "๐ฉ๐ผ๐ค",
    "woman_singer_tone3": "๐ฉ๐ฝ๐ค",
    "woman_singer_medium_skin_tone": "๐ฉ๐ฝ๐ค",
    "woman_singer_tone4": "๐ฉ๐พ๐ค",
    "woman_singer_medium_dark_skin_tone": "๐ฉ๐พ๐ค",
    "woman_singer_tone5": "๐ฉ๐ฟ๐ค",
    "woman_singer_dark_skin_tone": "๐ฉ๐ฟ๐ค",
    "man_singer": "๐จ๐ค",
    "man_singer_tone1": "๐จ๐ป๐ค",
    "man_singer_light_skin_tone": "๐จ๐ป๐ค",
    "man_singer_tone2": "๐จ๐ผ๐ค",
    "man_singer_medium_light_skin_tone": "๐จ๐ผ๐ค",
    "man_singer_tone3": "๐จ๐ฝ๐ค",
    "man_singer_medium_skin_tone": "๐จ๐ฝ๐ค",
    "man_singer_tone4": "๐จ๐พ๐ค",
    "man_singer_medium_dark_skin_tone": "๐จ๐พ๐ค",
    "man_singer_tone5": "๐จ๐ฟ๐ค",
    "man_singer_dark_skin_tone": "๐จ๐ฟ๐ค",
    "woman_teacher": "๐ฉ๐ซ",
    "woman_teacher_tone1": "๐ฉ๐ป๐ซ",
    "woman_teacher_light_skin_tone": "๐ฉ๐ป๐ซ",
    "woman_teacher_tone2": "๐ฉ๐ผ๐ซ",
    "woman_teacher_medium_light_skin_tone": "๐ฉ๐ผ๐ซ",
    "woman_teacher_tone3": "๐ฉ๐ฝ๐ซ",
    "woman_teacher_medium_skin_tone": "๐ฉ๐ฝ๐ซ",
    "woman_teacher_tone4": "๐ฉ๐พ๐ซ",
    "woman_teacher_medium_dark_skin_tone": "๐ฉ๐พ๐ซ",
    "woman_teacher_tone5": "๐ฉ๐ฟ๐ซ",
    "woman_teacher_dark_skin_tone": "๐ฉ๐ฟ๐ซ",
    "man_teacher": "๐จ๐ซ",
    "man_teacher_tone1": "๐จ๐ป๐ซ",
    "man_teacher_light_skin_tone": "๐จ๐ป๐ซ",
    "man_teacher_tone2": "๐จ๐ผ๐ซ",
    "man_teacher_medium_light_skin_tone": "๐จ๐ผ๐ซ",
    "man_teacher_tone3": "๐จ๐ฝ๐ซ",
    "man_teacher_medium_skin_tone": "๐จ๐ฝ๐ซ",
    "man_teacher_tone4": "๐จ๐พ๐ซ",
    "man_teacher_medium_dark_skin_tone": "๐จ๐พ๐ซ",
    "man_teacher_tone5": "๐จ๐ฟ๐ซ",
    "man_teacher_dark_skin_tone": "๐จ๐ฟ๐ซ",
    "woman_factory_worker": "๐ฉ๐ญ",
    "woman_factory_worker_tone1": "๐ฉ๐ป๐ญ",
    "woman_factory_worker_light_skin_tone": "๐ฉ๐ป๐ญ",
    "woman_factory_worker_tone2": "๐ฉ๐ผ๐ญ",
    "woman_factory_worker_medium_light_skin_tone": "๐ฉ๐ผ๐ญ",
    "woman_factory_worker_tone3": "๐ฉ๐ฝ๐ญ",
    "woman_factory_worker_medium_skin_tone": "๐ฉ๐ฝ๐ญ",
    "woman_factory_worker_tone4": "๐ฉ๐พ๐ญ",
    "woman_factory_worker_medium_dark_skin_tone": "๐ฉ๐พ๐ญ",
    "woman_factory_worker_tone5": "๐ฉ๐ฟ๐ญ",
    "woman_factory_worker_dark_skin_tone": "๐ฉ๐ฟ๐ญ",
    "man_factory_worker": "๐จ๐ญ",
    "man_factory_worker_tone1": "๐จ๐ป๐ญ",
    "man_factory_worker_light_skin_tone": "๐จ๐ป๐ญ",
    "man_factory_worker_tone2": "๐จ๐ผ๐ญ",
    "man_factory_worker_medium_light_skin_tone": "๐จ๐ผ๐ญ",
    "man_factory_worker_tone3": "๐จ๐ฝ๐ญ",
    "man_factory_worker_medium_skin_tone": "๐จ๐ฝ๐ญ",
    "man_factory_worker_tone4": "๐จ๐พ๐ญ",
    "man_factory_worker_medium_dark_skin_tone": "๐จ๐พ๐ญ",
    "man_factory_worker_tone5": "๐จ๐ฟ๐ญ",
    "man_factory_worker_dark_skin_tone": "๐จ๐ฟ๐ญ",
    "woman_technologist": "๐ฉ๐ป",
    "woman_technologist_tone1": "๐ฉ๐ป๐ป",
    "woman_technologist_light_skin_tone": "๐ฉ๐ป๐ป",
    "woman_technologist_tone2": "๐ฉ๐ผ๐ป",
    "woman_technologist_medium_light_skin_tone": "๐ฉ๐ผ๐ป",
    "woman_technologist_tone3": "๐ฉ๐ฝ๐ป",
    "woman_technologist_medium_skin_tone": "๐ฉ๐ฝ๐ป",
    "woman_technologist_tone4": "๐ฉ๐พ๐ป",
    "woman_technologist_medium_dark_skin_tone": "๐ฉ๐พ๐ป",
    "woman_technologist_tone5": "๐ฉ๐ฟ๐ป",
    "woman_technologist_dark_skin_tone": "๐ฉ๐ฟ๐ป",
    "man_technologist": "๐จ๐ป",
    "man_technologist_tone1": "๐จ๐ป๐ป",
    "man_technologist_light_skin_tone": "๐จ๐ป๐ป",
    "man_technologist_tone2": "๐จ๐ผ๐ป",
    "man_technologist_medium_light_skin_tone": "๐จ๐ผ๐ป",
    "man_technologist_tone3": "๐จ๐ฝ๐ป",
    "man_technologist_medium_skin_tone": "๐จ๐ฝ๐ป",
    "man_technologist_tone4": "๐จ๐พ๐ป",
    "man_technologist_medium_dark_skin_tone": "๐จ๐พ๐ป",
    "man_technologist_tone5": "๐จ๐ฟ๐ป",
    "man_technologist_dark_skin_tone": "๐จ๐ฟ๐ป",
    "woman_office_worker": "๐ฉ๐ผ",
    "woman_office_worker_tone1": "๐ฉ๐ป๐ผ",
    "woman_office_worker_light_skin_tone": "๐ฉ๐ป๐ผ",
    "woman_office_worker_tone2": "๐ฉ๐ผ๐ผ",
    "woman_office_worker_medium_light_skin_tone": "๐ฉ๐ผ๐ผ",
    "woman_office_worker_tone3": "๐ฉ๐ฝ๐ผ",
    "woman_office_worker_medium_skin_tone": "๐ฉ๐ฝ๐ผ",
    "woman_office_worker_tone4": "๐ฉ๐พ๐ผ",
    "woman_office_worker_medium_dark_skin_tone": "๐ฉ๐พ๐ผ",
    "woman_office_worker_tone5": "๐ฉ๐ฟ๐ผ",
    "woman_office_worker_dark_skin_tone": "๐ฉ๐ฟ๐ผ",
    "man_office_worker": "๐จ๐ผ",
    "man_office_worker_tone1": "๐จ๐ป๐ผ",
    "man_office_worker_light_skin_tone": "๐จ๐ป๐ผ",
    "man_office_worker_tone2": "๐จ๐ผ๐ผ",
    "man_office_worker_medium_light_skin_tone": "๐จ๐ผ๐ผ",
    "man_office_worker_tone3": "๐จ๐ฝ๐ผ",
    "man_office_worker_medium_skin_tone": "๐จ๐ฝ๐ผ",
    "man_office_worker_tone4": "๐จ๐พ๐ผ",
    "man_office_worker_medium_dark_skin_tone": "๐จ๐พ๐ผ",
    "man_office_worker_tone5": "๐จ๐ฟ๐ผ",
    "man_office_worker_dark_skin_tone": "๐จ๐ฟ๐ผ",
    "woman_mechanic": "๐ฉ๐ง",
    "woman_mechanic_tone1": "๐ฉ๐ป๐ง",
    "woman_mechanic_light_skin_tone": "๐ฉ๐ป๐ง",
    "woman_mechanic_tone2": "๐ฉ๐ผ๐ง",
    "woman_mechanic_medium_light_skin_tone": "๐ฉ๐ผ๐ง",
    "woman_mechanic_tone3": "๐ฉ๐ฝ๐ง",
    "woman_mechanic_medium_skin_tone": "๐ฉ๐ฝ๐ง",
    "woman_mechanic_tone4": "๐ฉ๐พ๐ง",
    "woman_mechanic_medium_dark_skin_tone": "๐ฉ๐พ๐ง",
    "woman_mechanic_tone5": "๐ฉ๐ฟ๐ง",
    "woman_mechanic_dark_skin_tone": "๐ฉ๐ฟ๐ง",
    "man_mechanic": "๐จ๐ง",
    "man_mechanic_tone1": "๐จ๐ป๐ง",
    "man_mechanic_light_skin_tone": "๐จ๐ป๐ง",
    "man_mechanic_tone2": "๐จ๐ผ๐ง",
    "man_mechanic_medium_light_skin_tone": "๐จ๐ผ๐ง",
    "man_mechanic_tone3": "๐จ๐ฝ๐ง",
    "man_mechanic_medium_skin_tone": "๐จ๐ฝ๐ง",
    "man_mechanic_tone4": "๐จ๐พ๐ง",
    "man_mechanic_medium_dark_skin_tone": "๐จ๐พ๐ง",
    "man_mechanic_tone5": "๐จ๐ฟ๐ง",
    "man_mechanic_dark_skin_tone": "๐จ๐ฟ๐ง",
    "woman_scientist": "๐ฉ๐ฌ",
    "woman_scientist_tone1": "๐ฉ๐ป๐ฌ",
    "woman_scientist_light_skin_tone": "๐ฉ๐ป๐ฌ",
    "woman_scientist_tone2": "๐ฉ๐ผ๐ฌ",
    "woman_scientist_medium_light_skin_tone": "๐ฉ๐ผ๐ฌ",
    "woman_scientist_tone3": "๐ฉ๐ฝ๐ฌ",
    "woman_scientist_medium_skin_tone": "๐ฉ๐ฝ๐ฌ",
    "woman_scientist_tone4": "๐ฉ๐พ๐ฌ",
    "woman_scientist_medium_dark_skin_tone": "๐ฉ๐พ๐ฌ",
    "woman_scientist_tone5": "๐ฉ๐ฟ๐ฌ",
    "woman_scientist_dark_skin_tone": "๐ฉ๐ฟ๐ฌ",
    "man_scientist": "๐จ๐ฌ",
    "man_scientist_tone1": "๐จ๐ป๐ฌ",
    "man_scientist_light_skin_tone": "๐จ๐ป๐ฌ",
    "man_scientist_tone2": "๐จ๐ผ๐ฌ",
    "man_scientist_medium_light_skin_tone": "๐จ๐ผ๐ฌ",
    "man_scientist_tone3": "๐จ๐ฝ๐ฌ",
    "man_scientist_medium_skin_tone": "๐จ๐ฝ๐ฌ",
    "man_scientist_tone4": "๐จ๐พ๐ฌ",
    "man_scientist_medium_dark_skin_tone": "๐จ๐พ๐ฌ",
    "man_scientist_tone5": "๐จ๐ฟ๐ฌ",
    "man_scientist_dark_skin_tone": "๐จ๐ฟ๐ฌ",
    "woman_artist": "๐ฉ๐จ",
    "woman_artist_tone1": "๐ฉ๐ป๐จ",
    "woman_artist_light_skin_tone": "๐ฉ๐ป๐จ",
    "woman_artist_tone2": "๐ฉ๐ผ๐จ",
    "woman_artist_medium_light_skin_tone": "๐ฉ๐ผ๐จ",
    "woman_artist_tone3": "๐ฉ๐ฝ๐จ",
    "woman_artist_medium_skin_tone": "๐ฉ๐ฝ๐จ",
    "woman_artist_tone4": "๐ฉ๐พ๐จ",
    "woman_artist_medium_dark_skin_tone": "๐ฉ๐พ๐จ",
    "woman_artist_tone5": "๐ฉ๐ฟ๐จ",
    "woman_artist_dark_skin_tone": "๐ฉ๐ฟ๐จ",
    "man_artist": "๐จ๐จ",
    "man_artist_tone1": "๐จ๐ป๐จ",
    "man_artist_light_skin_tone": "๐จ๐ป๐จ",
    "man_artist_tone2": "๐จ๐ผ๐จ",
    "man_artist_medium_light_skin_tone": "๐จ๐ผ๐จ",
    "man_artist_tone3": "๐จ๐ฝ๐จ",
    "man_artist_medium_skin_tone": "๐จ๐ฝ๐จ",
    "man_artist_tone4": "๐จ๐พ๐จ",
    "man_artist_medium_dark_skin_tone": "๐จ๐พ๐จ",
    "man_artist_tone5": "๐จ๐ฟ๐จ",
    "man_artist_dark_skin_tone": "๐จ๐ฟ๐จ",
    "woman_firefighter": "๐ฉ๐",
    "woman_firefighter_tone1": "๐ฉ๐ป๐",
    "woman_firefighter_light_skin_tone": "๐ฉ๐ป๐",
    "woman_firefighter_tone2": "๐ฉ๐ผ๐",
    "woman_firefighter_medium_light_skin_tone": "๐ฉ๐ผ๐",
    "woman_firefighter_tone3": "๐ฉ๐ฝ๐",
    "woman_firefighter_medium_skin_tone": "๐ฉ๐ฝ๐",
    "woman_firefighter_tone4": "๐ฉ๐พ๐",
    "woman_firefighter_medium_dark_skin_tone": "๐ฉ๐พ๐",
    "woman_firefighter_tone5": "๐ฉ๐ฟ๐",
    "woman_firefighter_dark_skin_tone": "๐ฉ๐ฟ๐",
    "man_firefighter": "๐จ๐",
    "man_firefighter_tone1": "๐จ๐ป๐",
    "man_firefighter_light_skin_tone": "๐จ๐ป๐",
    "man_firefighter_tone2": "๐จ๐ผ๐",
    "man_firefighter_medium_light_skin_tone": "๐จ๐ผ๐",
    "man_firefighter_tone3": "๐จ๐ฝ๐",
    "man_firefighter_medium_skin_tone": "๐จ๐ฝ๐",
    "man_firefighter_tone4": "๐จ๐พ๐",
    "man_firefighter_medium_dark_skin_tone": "๐จ๐พ๐",
    "man_firefighter_tone5": "๐จ๐ฟ๐",
    "man_firefighter_dark_skin_tone": "๐จ๐ฟ๐",
    "woman_pilot": "๐ฉโ",
    "woman_pilot_tone1": "๐ฉ๐ปโ",
    "woman_pilot_light_skin_tone": "๐ฉ๐ปโ",
    "woman_pilot_tone2": "๐ฉ๐ผโ",
    "woman_pilot_medium_light_skin_tone": "๐ฉ๐ผโ",
    "woman_pilot_tone3": "๐ฉ๐ฝโ",
    "woman_pilot_medium_skin_tone": "๐ฉ๐ฝโ",
    "woman_pilot_tone4": "๐ฉ๐พโ",
    "woman_pilot_medium_dark_skin_tone": "๐ฉ๐พโ",
    "woman_pilot_tone5": "๐ฉ๐ฟโ",
    "woman_pilot_dark_skin_tone": "๐ฉ๐ฟโ",
    "man_pilot": "๐จโ",
    "man_pilot_tone1": "๐จ๐ปโ",
    "man_pilot_light_skin_tone": "๐จ๐ปโ",
    "man_pilot_tone2": "๐จ๐ผโ",
    "man_pilot_medium_light_skin_tone": "๐จ๐ผโ",
    "man_pilot_tone3": "๐จ๐ฝโ",
    "man_pilot_medium_skin_tone": "๐จ๐ฝโ",
    "man_pilot_tone4": "๐จ๐พโ",
    "man_pilot_medium_dark_skin_tone": "๐จ๐พโ",
    "man_pilot_tone5": "๐จ๐ฟโ",
    "man_pilot_dark_skin_tone": "๐จ๐ฟโ",
    "woman_astronaut": "๐ฉ๐",
    "woman_astronaut_tone1": "๐ฉ๐ป๐",
    "woman_astronaut_light_skin_tone": "๐ฉ๐ป๐",
    "woman_astronaut_tone2": "๐ฉ๐ผ๐",
    "woman_astronaut_medium_light_skin_tone": "๐ฉ๐ผ๐",
    "woman_astronaut_tone3": "๐ฉ๐ฝ๐",
    "woman_astronaut_medium_skin_tone": "๐ฉ๐ฝ๐",
    "woman_astronaut_tone4": "๐ฉ๐พ๐",
    "woman_astronaut_medium_dark_skin_tone": "๐ฉ๐พ๐",
    "woman_astronaut_tone5": "๐ฉ๐ฟ๐",
    "woman_astronaut_dark_skin_tone": "๐ฉ๐ฟ๐",
    "man_astronaut": "๐จ๐",
    "man_astronaut_tone1": "๐จ๐ป๐",
    "man_astronaut_light_skin_tone": "๐จ๐ป๐",
    "man_astronaut_tone2": "๐จ๐ผ๐",
    "man_astronaut_medium_light_skin_tone": "๐จ๐ผ๐",
    "man_astronaut_tone3": "๐จ๐ฝ๐",
    "man_astronaut_medium_skin_tone": "๐จ๐ฝ๐",
    "man_astronaut_tone4": "๐จ๐พ๐",
    "man_astronaut_medium_dark_skin_tone": "๐จ๐พ๐",
    "man_astronaut_tone5": "๐จ๐ฟ๐",
    "man_astronaut_dark_skin_tone": "๐จ๐ฟ๐",
    "woman_judge": "๐ฉโ",
    "woman_judge_tone1": "๐ฉ๐ปโ",
    "woman_judge_light_skin_tone": "๐ฉ๐ปโ",
    "woman_judge_tone2": "๐ฉ๐ผโ",
    "woman_judge_medium_light_skin_tone": "๐ฉ๐ผโ",
    "woman_judge_tone3": "๐ฉ๐ฝโ",
    "woman_judge_medium_skin_tone": "๐ฉ๐ฝโ",
    "woman_judge_tone4": "๐ฉ๐พโ",
    "woman_judge_medium_dark_skin_tone": "๐ฉ๐พโ",
    "woman_judge_tone5": "๐ฉ๐ฟโ",
    "woman_judge_dark_skin_tone": "๐ฉ๐ฟโ",
    "man_judge": "๐จโ",
    "man_judge_tone1": "๐จ๐ปโ",
    "man_judge_light_skin_tone": "๐จ๐ปโ",
    "man_judge_tone2": "๐จ๐ผโ",
    "man_judge_medium_light_skin_tone": "๐จ๐ผโ",
    "man_judge_tone3": "๐จ๐ฝโ",
    "man_judge_medium_skin_tone": "๐จ๐ฝโ",
    "man_judge_tone4": "๐จ๐พโ",
    "man_judge_medium_dark_skin_tone": "๐จ๐พโ",
    "man_judge_tone5": "๐จ๐ฟโ",
    "man_judge_dark_skin_tone": "๐จ๐ฟโ",
    "bride_with_veil": "๐ฐ",
    "bride_with_veil_tone1": "๐ฐ๐ป",
    "bride_with_veil_tone2": "๐ฐ๐ผ",
    "bride_with_veil_tone3": "๐ฐ๐ฝ",
    "bride_with_veil_tone4": "๐ฐ๐พ",
    "bride_with_veil_tone5": "๐ฐ๐ฟ",
    "man_in_tuxedo": "๐คต",
    "man_in_tuxedo_tone1": "๐คต๐ป",
    "tuxedo_tone1": "๐คต๐ป",
    "man_in_tuxedo_tone2": "๐คต๐ผ",
    "tuxedo_tone2": "๐คต๐ผ",
    "man_in_tuxedo_tone3": "๐คต๐ฝ",
    "tuxedo_tone3": "๐คต๐ฝ",
    "man_in_tuxedo_tone4": "๐คต๐พ",
    "tuxedo_tone4": "๐คต๐พ",
    "man_in_tuxedo_tone5": "๐คต๐ฟ",
    "tuxedo_tone5": "๐คต๐ฟ",
    "princess": "๐ธ",
    "princess_tone1": "๐ธ๐ป",
    "princess_tone2": "๐ธ๐ผ",
    "princess_tone3": "๐ธ๐ฝ",
    "princess_tone4": "๐ธ๐พ",
    "princess_tone5": "๐ธ๐ฟ",
    "prince": "๐คด",
    "prince_tone1": "๐คด๐ป",
    "prince_tone2": "๐คด๐ผ",
    "prince_tone3": "๐คด๐ฝ",
    "prince_tone4": "๐คด๐พ",
    "prince_tone5": "๐คด๐ฟ",
    "superhero": "๐ฆธ",
    "superhero_tone1": "๐ฆธ๐ป",
    "superhero_light_skin_tone": "๐ฆธ๐ป",
    "superhero_tone2": "๐ฆธ๐ผ",
    "superhero_medium_light_skin_tone": "๐ฆธ๐ผ",
    "superhero_tone3": "๐ฆธ๐ฝ",
    "superhero_medium_skin_tone": "๐ฆธ๐ฝ",
    "superhero_tone4": "๐ฆธ๐พ",
    "superhero_medium_dark_skin_tone": "๐ฆธ๐พ",
    "superhero_tone5": "๐ฆธ๐ฟ",
    "superhero_dark_skin_tone": "๐ฆธ๐ฟ",
    "woman_superhero": "๐ฆธโ",
    "woman_superhero_tone1": "๐ฆธ๐ปโ",
    "woman_superhero_light_skin_tone": "๐ฆธ๐ปโ",
    "woman_superhero_tone2": "๐ฆธ๐ผโ",
    "woman_superhero_medium_light_skin_tone": "๐ฆธ๐ผโ",
    "woman_superhero_tone3": "๐ฆธ๐ฝโ",
    "woman_superhero_medium_skin_tone": "๐ฆธ๐ฝโ",
    "woman_superhero_tone4": "๐ฆธ๐พโ",
    "woman_superhero_medium_dark_skin_tone": "๐ฆธ๐พโ",
    "woman_superhero_tone5": "๐ฆธ๐ฟโ",
    "woman_superhero_dark_skin_tone": "๐ฆธ๐ฟโ",
    "man_superhero": "๐ฆธโ",
    "man_superhero_tone1": "๐ฆธ๐ปโ",
    "man_superhero_light_skin_tone": "๐ฆธ๐ปโ",
    "man_superhero_tone2": "๐ฆธ๐ผโ",
    "man_superhero_medium_light_skin_tone": "๐ฆธ๐ผโ",
    "man_superhero_tone3": "๐ฆธ๐ฝโ",
    "man_superhero_medium_skin_tone": "๐ฆธ๐ฝโ",
    "man_superhero_tone4": "๐ฆธ๐พโ",
    "man_superhero_medium_dark_skin_tone": "๐ฆธ๐พโ",
    "man_superhero_tone5": "๐ฆธ๐ฟโ",
    "man_superhero_dark_skin_tone": "๐ฆธ๐ฟโ",
    "supervillain": "๐ฆน",
    "supervillain_tone1": "๐ฆน๐ป",
    "supervillain_light_skin_tone": "๐ฆน๐ป",
    "supervillain_tone2": "๐ฆน๐ผ",
    "supervillain_medium_light_skin_tone": "๐ฆน๐ผ",
    "supervillain_tone3": "๐ฆน๐ฝ",
    "supervillain_medium_skin_tone": "๐ฆน๐ฝ",
    "supervillain_tone4": "๐ฆน๐พ",
    "supervillain_medium_dark_skin_tone": "๐ฆน๐พ",
    "supervillain_tone5": "๐ฆน๐ฟ",
    "supervillain_dark_skin_tone": "๐ฆน๐ฟ",
    "woman_supervillain": "๐ฆนโ",
    "woman_supervillain_tone1": "๐ฆน๐ปโ",
    "woman_supervillain_light_skin_tone": "๐ฆน๐ปโ",
    "woman_supervillain_tone2": "๐ฆน๐ผโ",
    "woman_supervillain_medium_light_skin_tone": "๐ฆน๐ผโ",
    "woman_supervillain_tone3": "๐ฆน๐ฝโ",
    "woman_supervillain_medium_skin_tone": "๐ฆน๐ฝโ",
    "woman_supervillain_tone4": "๐ฆน๐พโ",
    "woman_supervillain_medium_dark_skin_tone": "๐ฆน๐พโ",
    "woman_supervillain_tone5": "๐ฆน๐ฟโ",
    "woman_supervillain_dark_skin_tone": "๐ฆน๐ฟโ",
    "man_supervillain": "๐ฆนโ",
    "man_supervillain_tone1": "๐ฆน๐ปโ",
    "man_supervillain_light_skin_tone": "๐ฆน๐ปโ",
    "man_supervillain_tone2": "๐ฆน๐ผโ",
    "man_supervillain_medium_light_skin_tone": "๐ฆน๐ผโ",
    "man_supervillain_tone3": "๐ฆน๐ฝโ",
    "man_supervillain_medium_skin_tone": "๐ฆน๐ฝโ",
    "man_supervillain_tone4": "๐ฆน๐พโ",
    "man_supervillain_medium_dark_skin_tone": "๐ฆน๐พโ",
    "man_supervillain_tone5": "๐ฆน๐ฟโ",
    "man_supervillain_dark_skin_tone": "๐ฆน๐ฟโ",
    "mrs_claus": "๐คถ",
    "mother_christmas": "๐คถ",
    "mrs_claus_tone1": "๐คถ๐ป",
    "mother_christmas_tone1": "๐คถ๐ป",
    "mrs_claus_tone2": "๐คถ๐ผ",
    "mother_christmas_tone2": "๐คถ๐ผ",
    "mrs_claus_tone3": "๐คถ๐ฝ",
    "mother_christmas_tone3": "๐คถ๐ฝ",
    "mrs_claus_tone4": "๐คถ๐พ",
    "mother_christmas_tone4": "๐คถ๐พ",
    "mrs_claus_tone5": "๐คถ๐ฟ",
    "mother_christmas_tone5": "๐คถ๐ฟ",
    "santa": "๐",
    "santa_tone1": "๐๐ป",
    "santa_tone2": "๐๐ผ",
    "santa_tone3": "๐๐ฝ",
    "santa_tone4": "๐๐พ",
    "santa_tone5": "๐๐ฟ",
    "mage": "๐ง",
    "mage_tone1": "๐ง๐ป",
    "mage_light_skin_tone": "๐ง๐ป",
    "mage_tone2": "๐ง๐ผ",
    "mage_medium_light_skin_tone": "๐ง๐ผ",
    "mage_tone3": "๐ง๐ฝ",
    "mage_medium_skin_tone": "๐ง๐ฝ",
    "mage_tone4": "๐ง๐พ",
    "mage_medium_dark_skin_tone": "๐ง๐พ",
    "mage_tone5": "๐ง๐ฟ",
    "mage_dark_skin_tone": "๐ง๐ฟ",
    "woman_mage": "๐งโ",
    "woman_mage_tone1": "๐ง๐ปโ",
    "woman_mage_light_skin_tone": "๐ง๐ปโ",
    "woman_mage_tone2": "๐ง๐ผโ",
    "woman_mage_medium_light_skin_tone": "๐ง๐ผโ",
    "woman_mage_tone3": "๐ง๐ฝโ",
    "woman_mage_medium_skin_tone": "๐ง๐ฝโ",
    "woman_mage_tone4": "๐ง๐พโ",
    "woman_mage_medium_dark_skin_tone": "๐ง๐พโ",
    "woman_mage_tone5": "๐ง๐ฟโ",
    "woman_mage_dark_skin_tone": "๐ง๐ฟโ",
    "man_mage": "๐งโ",
    "man_mage_tone1": "๐ง๐ปโ",
    "man_mage_light_skin_tone": "๐ง๐ปโ",
    "man_mage_tone2": "๐ง๐ผโ",
    "man_mage_medium_light_skin_tone": "๐ง๐ผโ",
    "man_mage_tone3": "๐ง๐ฝโ",
    "man_mage_medium_skin_tone": "๐ง๐ฝโ",
    "man_mage_tone4": "๐ง๐พโ",
    "man_mage_medium_dark_skin_tone": "๐ง๐พโ",
    "man_mage_tone5": "๐ง๐ฟโ",
    "man_mage_dark_skin_tone": "๐ง๐ฟโ",
    "elf": "๐ง",
    "elf_tone1": "๐ง๐ป",
    "elf_light_skin_tone": "๐ง๐ป",
    "elf_tone2": "๐ง๐ผ",
    "elf_medium_light_skin_tone": "๐ง๐ผ",
    "elf_tone3": "๐ง๐ฝ",
    "elf_medium_skin_tone": "๐ง๐ฝ",
    "elf_tone4": "๐ง๐พ",
    "elf_medium_dark_skin_tone": "๐ง๐พ",
    "elf_tone5": "๐ง๐ฟ",
    "elf_dark_skin_tone": "๐ง๐ฟ",
    "woman_elf": "๐งโ",
    "woman_elf_tone1": "๐ง๐ปโ",
    "woman_elf_light_skin_tone": "๐ง๐ปโ",
    "woman_elf_tone2": "๐ง๐ผโ",
    "woman_elf_medium_light_skin_tone": "๐ง๐ผโ",
    "woman_elf_tone3": "๐ง๐ฝโ",
    "woman_elf_medium_skin_tone": "๐ง๐ฝโ",
    "woman_elf_tone4": "๐ง๐พโ",
    "woman_elf_medium_dark_skin_tone": "๐ง๐พโ",
    "woman_elf_tone5": "๐ง๐ฟโ",
    "woman_elf_dark_skin_tone": "๐ง๐ฟโ",
    "man_elf": "๐งโ",
    "man_elf_tone1": "๐ง๐ปโ",
    "man_elf_light_skin_tone": "๐ง๐ปโ",
    "man_elf_tone2": "๐ง๐ผโ",
    "man_elf_medium_light_skin_tone": "๐ง๐ผโ",
    "man_elf_tone3": "๐ง๐ฝโ",
    "man_elf_medium_skin_tone": "๐ง๐ฝโ",
    "man_elf_tone4": "๐ง๐พโ",
    "man_elf_medium_dark_skin_tone": "๐ง๐พโ",
    "man_elf_tone5": "๐ง๐ฟโ",
    "man_elf_dark_skin_tone": "๐ง๐ฟโ",
    "vampire": "๐ง",
    "vampire_tone1": "๐ง๐ป",
    "vampire_light_skin_tone": "๐ง๐ป",
    "vampire_tone2": "๐ง๐ผ",
    "vampire_medium_light_skin_tone": "๐ง๐ผ",
    "vampire_tone3": "๐ง๐ฝ",
    "vampire_medium_skin_tone": "๐ง๐ฝ",
    "vampire_tone4": "๐ง๐พ",
    "vampire_medium_dark_skin_tone": "๐ง๐พ",
    "vampire_tone5": "๐ง๐ฟ",
    "vampire_dark_skin_tone": "๐ง๐ฟ",
    "woman_vampire": "๐งโ",
    "woman_vampire_tone1": "๐ง๐ปโ",
    "woman_vampire_light_skin_tone": "๐ง๐ปโ",
    "woman_vampire_tone2": "๐ง๐ผโ",
    "woman_vampire_medium_light_skin_tone": "๐ง๐ผโ",
    "woman_vampire_tone3": "๐ง๐ฝโ",
    "woman_vampire_medium_skin_tone": "๐ง๐ฝโ",
    "woman_vampire_tone4": "๐ง๐พโ",
    "woman_vampire_medium_dark_skin_tone": "๐ง๐พโ",
    "woman_vampire_tone5": "๐ง๐ฟโ",
    "woman_vampire_dark_skin_tone": "๐ง๐ฟโ",
    "man_vampire": "๐งโ",
    "man_vampire_tone1": "๐ง๐ปโ",
    "man_vampire_light_skin_tone": "๐ง๐ปโ",
    "man_vampire_tone2": "๐ง๐ผโ",
    "man_vampire_medium_light_skin_tone": "๐ง๐ผโ",
    "man_vampire_tone3": "๐ง๐ฝโ",
    "man_vampire_medium_skin_tone": "๐ง๐ฝโ",
    "man_vampire_tone4": "๐ง๐พโ",
    "man_vampire_medium_dark_skin_tone": "๐ง๐พโ",
    "man_vampire_tone5": "๐ง๐ฟโ",
    "man_vampire_dark_skin_tone": "๐ง๐ฟโ",
    "zombie": "๐ง",
    "woman_zombie": "๐งโ",
    "man_zombie": "๐งโ",
    "genie": "๐ง",
    "woman_genie": "๐งโ",
    "man_genie": "๐งโ",
    "merperson": "๐ง",
    "merperson_tone1": "๐ง๐ป",
    "merperson_light_skin_tone": "๐ง๐ป",
    "merperson_tone2": "๐ง๐ผ",
    "merperson_medium_light_skin_tone": "๐ง๐ผ",
    "merperson_tone3": "๐ง๐ฝ",
    "merperson_medium_skin_tone": "๐ง๐ฝ",
    "merperson_tone4": "๐ง๐พ",
    "merperson_medium_dark_skin_tone": "๐ง๐พ",
    "merperson_tone5": "๐ง๐ฟ",
    "merperson_dark_skin_tone": "๐ง๐ฟ",
    "mermaid": "๐งโ",
    "mermaid_tone1": "๐ง๐ปโ",
    "mermaid_light_skin_tone": "๐ง๐ปโ",
    "mermaid_tone2": "๐ง๐ผโ",
    "mermaid_medium_light_skin_tone": "๐ง๐ผโ",
    "mermaid_tone3": "๐ง๐ฝโ",
    "mermaid_medium_skin_tone": "๐ง๐ฝโ",
    "mermaid_tone4": "๐ง๐พโ",
    "mermaid_medium_dark_skin_tone": "๐ง๐พโ",
    "mermaid_tone5": "๐ง๐ฟโ",
    "mermaid_dark_skin_tone": "๐ง๐ฟโ",
    "merman": "๐งโ",
    "merman_tone1": "๐ง๐ปโ",
    "merman_light_skin_tone": "๐ง๐ปโ",
    "merman_tone2": "๐ง๐ผโ",
    "merman_medium_light_skin_tone": "๐ง๐ผโ",
    "merman_tone3": "๐ง๐ฝโ",
    "merman_medium_skin_tone": "๐ง๐ฝโ",
    "merman_tone4": "๐ง๐พโ",
    "merman_medium_dark_skin_tone": "๐ง๐พโ",
    "merman_tone5": "๐ง๐ฟโ",
    "merman_dark_skin_tone": "๐ง๐ฟโ",
    "fairy": "๐ง",
    "fairy_tone1": "๐ง๐ป",
    "fairy_light_skin_tone": "๐ง๐ป",
    "fairy_tone2": "๐ง๐ผ",
    "fairy_medium_light_skin_tone": "๐ง๐ผ",
    "fairy_tone3": "๐ง๐ฝ",
    "fairy_medium_skin_tone": "๐ง๐ฝ",
    "fairy_tone4": "๐ง๐พ",
    "fairy_medium_dark_skin_tone": "๐ง๐พ",
    "fairy_tone5": "๐ง๐ฟ",
    "fairy_dark_skin_tone": "๐ง๐ฟ",
    "woman_fairy": "๐งโ",
    "woman_fairy_tone1": "๐ง๐ปโ",
    "woman_fairy_light_skin_tone": "๐ง๐ปโ",
    "woman_fairy_tone2": "๐ง๐ผโ",
    "woman_fairy_medium_light_skin_tone": "๐ง๐ผโ",
    "woman_fairy_tone3": "๐ง๐ฝโ",
    "woman_fairy_medium_skin_tone": "๐ง๐ฝโ",
    "woman_fairy_tone4": "๐ง๐พโ",
    "woman_fairy_medium_dark_skin_tone": "๐ง๐พโ",
    "woman_fairy_tone5": "๐ง๐ฟโ",
    "woman_fairy_dark_skin_tone": "๐ง๐ฟโ",
    "man_fairy": "๐งโ",
    "man_fairy_tone1": "๐ง๐ปโ",
    "man_fairy_light_skin_tone": "๐ง๐ปโ",
    "man_fairy_tone2": "๐ง๐ผโ",
    "man_fairy_medium_light_skin_tone": "๐ง๐ผโ",
    "man_fairy_tone3": "๐ง๐ฝโ",
    "man_fairy_medium_skin_tone": "๐ง๐ฝโ",
    "man_fairy_tone4": "๐ง๐พโ",
    "man_fairy_medium_dark_skin_tone": "๐ง๐พโ",
    "man_fairy_tone5": "๐ง๐ฟโ",
    "man_fairy_dark_skin_tone": "๐ง๐ฟโ",
    "angel": "๐ผ",
    "angel_tone1": "๐ผ๐ป",
    "angel_tone2": "๐ผ๐ผ",
    "angel_tone3": "๐ผ๐ฝ",
    "angel_tone4": "๐ผ๐พ",
    "angel_tone5": "๐ผ๐ฟ",
    "pregnant_woman": "๐คฐ",
    "expecting_woman": "๐คฐ",
    "pregnant_woman_tone1": "๐คฐ๐ป",
    "expecting_woman_tone1": "๐คฐ๐ป",
    "pregnant_woman_tone2": "๐คฐ๐ผ",
    "expecting_woman_tone2": "๐คฐ๐ผ",
    "pregnant_woman_tone3": "๐คฐ๐ฝ",
    "expecting_woman_tone3": "๐คฐ๐ฝ",
    "pregnant_woman_tone4": "๐คฐ๐พ",
    "expecting_woman_tone4": "๐คฐ๐พ",
    "pregnant_woman_tone5": "๐คฐ๐ฟ",
    "expecting_woman_tone5": "๐คฐ๐ฟ",
    "breast_feeding": "๐คฑ",
    "breast_feeding_tone1": "๐คฑ๐ป",
    "breast_feeding_light_skin_tone": "๐คฑ๐ป",
    "breast_feeding_tone2": "๐คฑ๐ผ",
    "breast_feeding_medium_light_skin_tone": "๐คฑ๐ผ",
    "breast_feeding_tone3": "๐คฑ๐ฝ",
    "breast_feeding_medium_skin_tone": "๐คฑ๐ฝ",
    "breast_feeding_tone4": "๐คฑ๐พ",
    "breast_feeding_medium_dark_skin_tone": "๐คฑ๐พ",
    "breast_feeding_tone5": "๐คฑ๐ฟ",
    "breast_feeding_dark_skin_tone": "๐คฑ๐ฟ",
    "person_bowing": "๐",
    "bow": "๐",
    "person_bowing_tone1": "๐๐ป",
    "bow_tone1": "๐๐ป",
    "person_bowing_tone2": "๐๐ผ",
    "bow_tone2": "๐๐ผ",
    "person_bowing_tone3": "๐๐ฝ",
    "bow_tone3": "๐๐ฝ",
    "person_bowing_tone4": "๐๐พ",
    "bow_tone4": "๐๐พ",
    "person_bowing_tone5": "๐๐ฟ",
    "bow_tone5": "๐๐ฟ",
    "woman_bowing": "๐โ",
    "woman_bowing_tone1": "๐๐ปโ",
    "woman_bowing_light_skin_tone": "๐๐ปโ",
    "woman_bowing_tone2": "๐๐ผโ",
    "woman_bowing_medium_light_skin_tone": "๐๐ผโ",
    "woman_bowing_tone3": "๐๐ฝโ",
    "woman_bowing_medium_skin_tone": "๐๐ฝโ",
    "woman_bowing_tone4": "๐๐พโ",
    "woman_bowing_medium_dark_skin_tone": "๐๐พโ",
    "woman_bowing_tone5": "๐๐ฟโ",
    "woman_bowing_dark_skin_tone": "๐๐ฟโ",
    "man_bowing": "๐โ",
    "man_bowing_tone1": "๐๐ปโ",
    "man_bowing_light_skin_tone": "๐๐ปโ",
    "man_bowing_tone2": "๐๐ผโ",
    "man_bowing_medium_light_skin_tone": "๐๐ผโ",
    "man_bowing_tone3": "๐๐ฝโ",
    "man_bowing_medium_skin_tone": "๐๐ฝโ",
    "man_bowing_tone4": "๐๐พโ",
    "man_bowing_medium_dark_skin_tone": "๐๐พโ",
    "man_bowing_tone5": "๐๐ฟโ",
    "man_bowing_dark_skin_tone": "๐๐ฟโ",
    "person_tipping_hand": "๐",
    "information_desk_person": "๐",
    "person_tipping_hand_tone1": "๐๐ป",
    "information_desk_person_tone1": "๐๐ป",
    "person_tipping_hand_tone2": "๐๐ผ",
    "information_desk_person_tone2": "๐๐ผ",
    "person_tipping_hand_tone3": "๐๐ฝ",
    "information_desk_person_tone3": "๐๐ฝ",
    "person_tipping_hand_tone4": "๐๐พ",
    "information_desk_person_tone4": "๐๐พ",
    "person_tipping_hand_tone5": "๐๐ฟ",
    "information_desk_person_tone5": "๐๐ฟ",
    "woman_tipping_hand": "๐โ",
    "woman_tipping_hand_tone1": "๐๐ปโ",
    "woman_tipping_hand_light_skin_tone": "๐๐ปโ",
    "woman_tipping_hand_tone2": "๐๐ผโ",
    "woman_tipping_hand_medium_light_skin_tone": "๐๐ผโ",
    "woman_tipping_hand_tone3": "๐๐ฝโ",
    "woman_tipping_hand_medium_skin_tone": "๐๐ฝโ",
    "woman_tipping_hand_tone4": "๐๐พโ",
    "woman_tipping_hand_medium_dark_skin_tone": "๐๐พโ",
    "woman_tipping_hand_tone5": "๐๐ฟโ",
    "woman_tipping_hand_dark_skin_tone": "๐๐ฟโ",
    "man_tipping_hand": "๐โ",
    "man_tipping_hand_tone1": "๐๐ปโ",
    "man_tipping_hand_light_skin_tone": "๐๐ปโ",
    "man_tipping_hand_tone2": "๐๐ผโ",
    "man_tipping_hand_medium_light_skin_tone": "๐๐ผโ",
    "man_tipping_hand_tone3": "๐๐ฝโ",
    "man_tipping_hand_medium_skin_tone": "๐๐ฝโ",
    "man_tipping_hand_tone4": "๐๐พโ",
    "man_tipping_hand_medium_dark_skin_tone": "๐๐พโ",
    "man_tipping_hand_tone5": "๐๐ฟโ",
    "man_tipping_hand_dark_skin_tone": "๐๐ฟโ",
    "person_gesturing_no": "๐",
    "no_good": "๐",
    "person_gesturing_no_tone1": "๐๐ป",
    "no_good_tone1": "๐๐ป",
    "person_gesturing_no_tone2": "๐๐ผ",
    "no_good_tone2": "๐๐ผ",
    "person_gesturing_no_tone3": "๐๐ฝ",
    "no_good_tone3": "๐๐ฝ",
    "person_gesturing_no_tone4": "๐๐พ",
    "no_good_tone4": "๐๐พ",
    "person_gesturing_no_tone5": "๐๐ฟ",
    "no_good_tone5": "๐๐ฟ",
    "woman_gesturing_no": "๐โ",
    "woman_gesturing_no_tone1": "๐๐ปโ",
    "woman_gesturing_no_light_skin_tone": "๐๐ปโ",
    "woman_gesturing_no_tone2": "๐๐ผโ",
    "woman_gesturing_no_medium_light_skin_tone": "๐๐ผโ",
    "woman_gesturing_no_tone3": "๐๐ฝโ",
    "woman_gesturing_no_medium_skin_tone": "๐๐ฝโ",
    "woman_gesturing_no_tone4": "๐๐พโ",
    "woman_gesturing_no_medium_dark_skin_tone": "๐๐พโ",
    "woman_gesturing_no_tone5": "๐๐ฟโ",
    "woman_gesturing_no_dark_skin_tone": "๐๐ฟโ",
    "man_gesturing_no": "๐โ",
    "man_gesturing_no_tone1": "๐๐ปโ",
    "man_gesturing_no_light_skin_tone": "๐๐ปโ",
    "man_gesturing_no_tone2": "๐๐ผโ",
    "man_gesturing_no_medium_light_skin_tone": "๐๐ผโ",
    "man_gesturing_no_tone3": "๐๐ฝโ",
    "man_gesturing_no_medium_skin_tone": "๐๐ฝโ",
    "man_gesturing_no_tone4": "๐๐พโ",
    "man_gesturing_no_medium_dark_skin_tone": "๐๐พโ",
    "man_gesturing_no_tone5": "๐๐ฟโ",
    "man_gesturing_no_dark_skin_tone": "๐๐ฟโ",
    "person_gesturing_ok": "๐",
    "ok_woman": "๐",
    "person_gesturing_ok_tone1": "๐๐ป",
    "ok_woman_tone1": "๐๐ป",
    "person_gesturing_ok_tone2": "๐๐ผ",
    "ok_woman_tone2": "๐๐ผ",
    "person_gesturing_ok_tone3": "๐๐ฝ",
    "ok_woman_tone3": "๐๐ฝ",
    "person_gesturing_ok_tone4": "๐๐พ",
    "ok_woman_tone4": "๐๐พ",
    "person_gesturing_ok_tone5": "๐๐ฟ",
    "ok_woman_tone5": "๐๐ฟ",
    "woman_gesturing_ok": "๐โ",
    "woman_gesturing_ok_tone1": "๐๐ปโ",
    "woman_gesturing_ok_light_skin_tone": "๐๐ปโ",
    "woman_gesturing_ok_tone2": "๐๐ผโ",
    "woman_gesturing_ok_medium_light_skin_tone": "๐๐ผโ",
    "woman_gesturing_ok_tone3": "๐๐ฝโ",
    "woman_gesturing_ok_medium_skin_tone": "๐๐ฝโ",
    "woman_gesturing_ok_tone4": "๐๐พโ",
    "woman_gesturing_ok_medium_dark_skin_tone": "๐๐พโ",
    "woman_gesturing_ok_tone5": "๐๐ฟโ",
    "woman_gesturing_ok_dark_skin_tone": "๐๐ฟโ",
    "man_gesturing_ok": "๐โ",
    "man_gesturing_ok_tone1": "๐๐ปโ",
    "man_gesturing_ok_light_skin_tone": "๐๐ปโ",
    "man_gesturing_ok_tone2": "๐๐ผโ",
    "man_gesturing_ok_medium_light_skin_tone": "๐๐ผโ",
    "man_gesturing_ok_tone3": "๐๐ฝโ",
    "man_gesturing_ok_medium_skin_tone": "๐๐ฝโ",
    "man_gesturing_ok_tone4": "๐๐พโ",
    "man_gesturing_ok_medium_dark_skin_tone": "๐๐พโ",
    "man_gesturing_ok_tone5": "๐๐ฟโ",
    "man_gesturing_ok_dark_skin_tone": "๐๐ฟโ",
    "person_raising_hand": "๐",
    "raising_hand": "๐",
    "person_raising_hand_tone1": "๐๐ป",
    "raising_hand_tone1": "๐๐ป",
    "person_raising_hand_tone2": "๐๐ผ",
    "raising_hand_tone2": "๐๐ผ",
    "person_raising_hand_tone3": "๐๐ฝ",
    "raising_hand_tone3": "๐๐ฝ",
    "person_raising_hand_tone4": "๐๐พ",
    "raising_hand_tone4": "๐๐พ",
    "person_raising_hand_tone5": "๐๐ฟ",
    "raising_hand_tone5": "๐๐ฟ",
    "woman_raising_hand": "๐โ",
    "woman_raising_hand_tone1": "๐๐ปโ",
    "woman_raising_hand_light_skin_tone": "๐๐ปโ",
    "woman_raising_hand_tone2": "๐๐ผโ",
    "woman_raising_hand_medium_light_skin_tone": "๐๐ผโ",
    "woman_raising_hand_tone3": "๐๐ฝโ",
    "woman_raising_hand_medium_skin_tone": "๐๐ฝโ",
    "woman_raising_hand_tone4": "๐๐พโ",
    "woman_raising_hand_medium_dark_skin_tone": "๐๐พโ",
    "woman_raising_hand_tone5": "๐๐ฟโ",
    "woman_raising_hand_dark_skin_tone": "๐๐ฟโ",
    "man_raising_hand": "๐โ",
    "man_raising_hand_tone1": "๐๐ปโ",
    "man_raising_hand_light_skin_tone": "๐๐ปโ",
    "man_raising_hand_tone2": "๐๐ผโ",
    "man_raising_hand_medium_light_skin_tone": "๐๐ผโ",
    "man_raising_hand_tone3": "๐๐ฝโ",
    "man_raising_hand_medium_skin_tone": "๐๐ฝโ",
    "man_raising_hand_tone4": "๐๐พโ",
    "man_raising_hand_medium_dark_skin_tone": "๐๐พโ",
    "man_raising_hand_tone5": "๐๐ฟโ",
    "man_raising_hand_dark_skin_tone": "๐๐ฟโ",
    "deaf_person": "๐ง",
    "deaf_person_tone1": "๐ง๐ป",
    "deaf_person_light_skin_tone": "๐ง๐ป",
    "deaf_person_tone2": "๐ง๐ผ",
    "deaf_person_medium_light_skin_tone": "๐ง๐ผ",
    "deaf_person_tone3": "๐ง๐ฝ",
    "deaf_person_medium_skin_tone": "๐ง๐ฝ",
    "deaf_person_tone4": "๐ง๐พ",
    "deaf_person_medium_dark_skin_tone": "๐ง๐พ",
    "deaf_person_tone5": "๐ง๐ฟ",
    "deaf_person_dark_skin_tone": "๐ง๐ฟ",
    "deaf_woman": "๐งโ",
    "deaf_woman_tone1": "๐ง๐ปโ",
    "deaf_woman_light_skin_tone": "๐ง๐ปโ",
    "deaf_woman_tone2": "๐ง๐ผโ",
    "deaf_woman_medium_light_skin_tone": "๐ง๐ผโ",
    "deaf_woman_tone3": "๐ง๐ฝโ",
    "deaf_woman_medium_skin_tone": "๐ง๐ฝโ",
    "deaf_woman_tone4": "๐ง๐พโ",
    "deaf_woman_medium_dark_skin_tone": "๐ง๐พโ",
    "deaf_woman_tone5": "๐ง๐ฟโ",
    "deaf_woman_dark_skin_tone": "๐ง๐ฟโ",
    "deaf_man": "๐งโ",
    "deaf_man_tone1": "๐ง๐ปโ",
    "deaf_man_light_skin_tone": "๐ง๐ปโ",
    "deaf_man_tone2": "๐ง๐ผโ",
    "deaf_man_medium_light_skin_tone": "๐ง๐ผโ",
    "deaf_man_tone3": "๐ง๐ฝโ",
    "deaf_man_medium_skin_tone": "๐ง๐ฝโ",
    "deaf_man_tone4": "๐ง๐พโ",
    "deaf_man_medium_dark_skin_tone": "๐ง๐พโ",
    "deaf_man_tone5": "๐ง๐ฟโ",
    "deaf_man_dark_skin_tone": "๐ง๐ฟโ",
    "person_facepalming": "๐คฆ",
    "face_palm": "๐คฆ",
    "facepalm": "๐คฆ",
    "person_facepalming_tone1": "๐คฆ๐ป",
    "face_palm_tone1": "๐คฆ๐ป",
    "facepalm_tone1": "๐คฆ๐ป",
    "person_facepalming_tone2": "๐คฆ๐ผ",
    "face_palm_tone2": "๐คฆ๐ผ",
    "facepalm_tone2": "๐คฆ๐ผ",
    "person_facepalming_tone3": "๐คฆ๐ฝ",
    "face_palm_tone3": "๐คฆ๐ฝ",
    "facepalm_tone3": "๐คฆ๐ฝ",
    "person_facepalming_tone4": "๐คฆ๐พ",
    "face_palm_tone4": "๐คฆ๐พ",
    "facepalm_tone4": "๐คฆ๐พ",
    "person_facepalming_tone5": "๐คฆ๐ฟ",
    "face_palm_tone5": "๐คฆ๐ฟ",
    "facepalm_tone5": "๐คฆ๐ฟ",
    "woman_facepalming": "๐คฆโ",
    "woman_facepalming_tone1": "๐คฆ๐ปโ",
    "woman_facepalming_light_skin_tone": "๐คฆ๐ปโ",
    "woman_facepalming_tone2": "๐คฆ๐ผโ",
    "woman_facepalming_medium_light_skin_tone": "๐คฆ๐ผโ",
    "woman_facepalming_tone3": "๐คฆ๐ฝโ",
    "woman_facepalming_medium_skin_tone": "๐คฆ๐ฝโ",
    "woman_facepalming_tone4": "๐คฆ๐พโ",
    "woman_facepalming_medium_dark_skin_tone": "๐คฆ๐พโ",
    "woman_facepalming_tone5": "๐คฆ๐ฟโ",
    "woman_facepalming_dark_skin_tone": "๐คฆ๐ฟโ",
    "man_facepalming": "๐คฆโ",
    "man_facepalming_tone1": "๐คฆ๐ปโ",
    "man_facepalming_light_skin_tone": "๐คฆ๐ปโ",
    "man_facepalming_tone2": "๐คฆ๐ผโ",
    "man_facepalming_medium_light_skin_tone": "๐คฆ๐ผโ",
    "man_facepalming_tone3": "๐คฆ๐ฝโ",
    "man_facepalming_medium_skin_tone": "๐คฆ๐ฝโ",
    "man_facepalming_tone4": "๐คฆ๐พโ",
    "man_facepalming_medium_dark_skin_tone": "๐คฆ๐พโ",
    "man_facepalming_tone5": "๐คฆ๐ฟโ",
    "man_facepalming_dark_skin_tone": "๐คฆ๐ฟโ",
    "person_shrugging": "๐คท",
    "shrug": "๐คท",
    "person_shrugging_tone1": "๐คท๐ป",
    "shrug_tone1": "๐คท๐ป",
    "person_shrugging_tone2": "๐คท๐ผ",
    "shrug_tone2": "๐คท๐ผ",
    "person_shrugging_tone3": "๐คท๐ฝ",
    "shrug_tone3": "๐คท๐ฝ",
    "person_shrugging_tone4": "๐คท๐พ",
    "shrug_tone4": "๐คท๐พ",
    "person_shrugging_tone5": "๐คท๐ฟ",
    "shrug_tone5": "๐คท๐ฟ",
    "woman_shrugging": "๐คทโ",
    "woman_shrugging_tone1": "๐คท๐ปโ",
    "woman_shrugging_light_skin_tone": "๐คท๐ปโ",
    "woman_shrugging_tone2": "๐คท๐ผโ",
    "woman_shrugging_medium_light_skin_tone": "๐คท๐ผโ",
    "woman_shrugging_tone3": "๐คท๐ฝโ",
    "woman_shrugging_medium_skin_tone": "๐คท๐ฝโ",
    "woman_shrugging_tone4": "๐คท๐พโ",
    "woman_shrugging_medium_dark_skin_tone": "๐คท๐พโ",
    "woman_shrugging_tone5": "๐คท๐ฟโ",
    "woman_shrugging_dark_skin_tone": "๐คท๐ฟโ",
    "man_shrugging": "๐คทโ",
    "man_shrugging_tone1": "๐คท๐ปโ",
    "man_shrugging_light_skin_tone": "๐คท๐ปโ",
    "man_shrugging_tone2": "๐คท๐ผโ",
    "man_shrugging_medium_light_skin_tone": "๐คท๐ผโ",
    "man_shrugging_tone3": "๐คท๐ฝโ",
    "man_shrugging_medium_skin_tone": "๐คท๐ฝโ",
    "man_shrugging_tone4": "๐คท๐พโ",
    "man_shrugging_medium_dark_skin_tone": "๐คท๐พโ",
    "man_shrugging_tone5": "๐คท๐ฟโ",
    "man_shrugging_dark_skin_tone": "๐คท๐ฟโ",
    "person_pouting": "๐",
    "person_with_pouting_face": "๐",
    "person_pouting_tone1": "๐๐ป",
    "person_with_pouting_face_tone1": "๐๐ป",
    "person_pouting_tone2": "๐๐ผ",
    "person_with_pouting_face_tone2": "๐๐ผ",
    "person_pouting_tone3": "๐๐ฝ",
    "person_with_pouting_face_tone3": "๐๐ฝ",
    "person_pouting_tone4": "๐๐พ",
    "person_with_pouting_face_tone4": "๐๐พ",
    "person_pouting_tone5": "๐๐ฟ",
    "person_with_pouting_face_tone5": "๐๐ฟ",
    "woman_pouting": "๐โ",
    "woman_pouting_tone1": "๐๐ปโ",
    "woman_pouting_light_skin_tone": "๐๐ปโ",
    "woman_pouting_tone2": "๐๐ผโ",
    "woman_pouting_medium_light_skin_tone": "๐๐ผโ",
    "woman_pouting_tone3": "๐๐ฝโ",
    "woman_pouting_medium_skin_tone": "๐๐ฝโ",
    "woman_pouting_tone4": "๐๐พโ",
    "woman_pouting_medium_dark_skin_tone": "๐๐พโ",
    "woman_pouting_tone5": "๐๐ฟโ",
    "woman_pouting_dark_skin_tone": "๐๐ฟโ",
    "man_pouting": "๐โ",
    "man_pouting_tone1": "๐๐ปโ",
    "man_pouting_light_skin_tone": "๐๐ปโ",
    "man_pouting_tone2": "๐๐ผโ",
    "man_pouting_medium_light_skin_tone": "๐๐ผโ",
    "man_pouting_tone3": "๐๐ฝโ",
    "man_pouting_medium_skin_tone": "๐๐ฝโ",
    "man_pouting_tone4": "๐๐พโ",
    "man_pouting_medium_dark_skin_tone": "๐๐พโ",
    "man_pouting_tone5": "๐๐ฟโ",
    "man_pouting_dark_skin_tone": "๐๐ฟโ",
    "person_frowning": "๐",
    "person_frowning_tone1": "๐๐ป",
    "person_frowning_tone2": "๐๐ผ",
    "person_frowning_tone3": "๐๐ฝ",
    "person_frowning_tone4": "๐๐พ",
    "person_frowning_tone5": "๐๐ฟ",
    "woman_frowning": "๐โ",
    "woman_frowning_tone1": "๐๐ปโ",
    "woman_frowning_light_skin_tone": "๐๐ปโ",
    "woman_frowning_tone2": "๐๐ผโ",
    "woman_frowning_medium_light_skin_tone": "๐๐ผโ",
    "woman_frowning_tone3": "๐๐ฝโ",
    "woman_frowning_medium_skin_tone": "๐๐ฝโ",
    "woman_frowning_tone4": "๐๐พโ",
    "woman_frowning_medium_dark_skin_tone": "๐๐พโ",
    "woman_frowning_tone5": "๐๐ฟโ",
    "woman_frowning_dark_skin_tone": "๐๐ฟโ",
    "man_frowning": "๐โ",
    "man_frowning_tone1": "๐๐ปโ",
    "man_frowning_light_skin_tone": "๐๐ปโ",
    "man_frowning_tone2": "๐๐ผโ",
    "man_frowning_medium_light_skin_tone": "๐๐ผโ",
    "man_frowning_tone3": "๐๐ฝโ",
    "man_frowning_medium_skin_tone": "๐๐ฝโ",
    "man_frowning_tone4": "๐๐พโ",
    "man_frowning_medium_dark_skin_tone": "๐๐พโ",
    "man_frowning_tone5": "๐๐ฟโ",
    "man_frowning_dark_skin_tone": "๐๐ฟโ",
    "person_getting_haircut": "๐",
    "haircut": "๐",
    "person_getting_haircut_tone1": "๐๐ป",
    "haircut_tone1": "๐๐ป",
    "person_getting_haircut_tone2": "๐๐ผ",
    "haircut_tone2": "๐๐ผ",
    "person_getting_haircut_tone3": "๐๐ฝ",
    "haircut_tone3": "๐๐ฝ",
    "person_getting_haircut_tone4": "๐๐พ",
    "haircut_tone4": "๐๐พ",
    "person_getting_haircut_tone5": "๐๐ฟ",
    "haircut_tone5": "๐๐ฟ",
    "woman_getting_haircut": "๐โ",
    "woman_getting_haircut_tone1": "๐๐ปโ",
    "woman_getting_haircut_light_skin_tone": "๐๐ปโ",
    "woman_getting_haircut_tone2": "๐๐ผโ",
    "woman_getting_haircut_medium_light_skin_tone": "๐๐ผโ",
    "woman_getting_haircut_tone3": "๐๐ฝโ",
    "woman_getting_haircut_medium_skin_tone": "๐๐ฝโ",
    "woman_getting_haircut_tone4": "๐๐พโ",
    "woman_getting_haircut_medium_dark_skin_tone": "๐๐พโ",
    "woman_getting_haircut_tone5": "๐๐ฟโ",
    "woman_getting_haircut_dark_skin_tone": "๐๐ฟโ",
    "man_getting_haircut": "๐โ",
    "man_getting_haircut_tone1": "๐๐ปโ",
    "man_getting_haircut_light_skin_tone": "๐๐ปโ",
    "man_getting_haircut_tone2": "๐๐ผโ",
    "man_getting_haircut_medium_light_skin_tone": "๐๐ผโ",
    "man_getting_haircut_tone3": "๐๐ฝโ",
    "man_getting_haircut_medium_skin_tone": "๐๐ฝโ",
    "man_getting_haircut_tone4": "๐๐พโ",
    "man_getting_haircut_medium_dark_skin_tone": "๐๐พโ",
    "man_getting_haircut_tone5": "๐๐ฟโ",
    "man_getting_haircut_dark_skin_tone": "๐๐ฟโ",
    "person_getting_massage": "๐",
    "massage": "๐",
    "person_getting_massage_tone1": "๐๐ป",
    "massage_tone1": "๐๐ป",
    "person_getting_massage_tone2": "๐๐ผ",
    "massage_tone2": "๐๐ผ",
    "person_getting_massage_tone3": "๐๐ฝ",
    "massage_tone3": "๐๐ฝ",
    "person_getting_massage_tone4": "๐๐พ",
    "massage_tone4": "๐๐พ",
    "person_getting_massage_tone5": "๐๐ฟ",
    "massage_tone5": "๐๐ฟ",
    "woman_getting_face_massage": "๐โ",
    "woman_getting_face_massage_tone1": "๐๐ปโ",
    "woman_getting_face_massage_light_skin_tone": "๐๐ปโ",
    "woman_getting_face_massage_tone2": "๐๐ผโ",
    "woman_getting_face_massage_medium_light_skin_tone": "๐๐ผโ",
    "woman_getting_face_massage_tone3": "๐๐ฝโ",
    "woman_getting_face_massage_medium_skin_tone": "๐๐ฝโ",
    "woman_getting_face_massage_tone4": "๐๐พโ",
    "woman_getting_face_massage_medium_dark_skin_tone": "๐๐พโ",
    "woman_getting_face_massage_tone5": "๐๐ฟโ",
    "woman_getting_face_massage_dark_skin_tone": "๐๐ฟโ",
    "man_getting_face_massage": "๐โ",
    "man_getting_face_massage_tone1": "๐๐ปโ",
    "man_getting_face_massage_light_skin_tone": "๐๐ปโ",
    "man_getting_face_massage_tone2": "๐๐ผโ",
    "man_getting_face_massage_medium_light_skin_tone": "๐๐ผโ",
    "man_getting_face_massage_tone3": "๐๐ฝโ",
    "man_getting_face_massage_medium_skin_tone": "๐๐ฝโ",
    "man_getting_face_massage_tone4": "๐๐พโ",
    "man_getting_face_massage_medium_dark_skin_tone": "๐๐พโ",
    "man_getting_face_massage_tone5": "๐๐ฟโ",
    "man_getting_face_massage_dark_skin_tone": "๐๐ฟโ",
    "person_in_steamy_room": "๐ง",
    "person_in_steamy_room_tone1": "๐ง๐ป",
    "person_in_steamy_room_light_skin_tone": "๐ง๐ป",
    "person_in_steamy_room_tone2": "๐ง๐ผ",
    "person_in_steamy_room_medium_light_skin_tone": "๐ง๐ผ",
    "person_in_steamy_room_tone3": "๐ง๐ฝ",
    "person_in_steamy_room_medium_skin_tone": "๐ง๐ฝ",
    "person_in_steamy_room_tone4": "๐ง๐พ",
    "person_in_steamy_room_medium_dark_skin_tone": "๐ง๐พ",
    "person_in_steamy_room_tone5": "๐ง๐ฟ",
    "person_in_steamy_room_dark_skin_tone": "๐ง๐ฟ",
    "woman_in_steamy_room": "๐งโ",
    "woman_in_steamy_room_tone1": "๐ง๐ปโ",
    "woman_in_steamy_room_light_skin_tone": "๐ง๐ปโ",
    "woman_in_steamy_room_tone2": "๐ง๐ผโ",
    "woman_in_steamy_room_medium_light_skin_tone": "๐ง๐ผโ",
    "woman_in_steamy_room_tone3": "๐ง๐ฝโ",
    "woman_in_steamy_room_medium_skin_tone": "๐ง๐ฝโ",
    "woman_in_steamy_room_tone4": "๐ง๐พโ",
    "woman_in_steamy_room_medium_dark_skin_tone": "๐ง๐พโ",
    "woman_in_steamy_room_tone5": "๐ง๐ฟโ",
    "woman_in_steamy_room_dark_skin_tone": "๐ง๐ฟโ",
    "man_in_steamy_room": "๐งโ",
    "man_in_steamy_room_tone1": "๐ง๐ปโ",
    "man_in_steamy_room_light_skin_tone": "๐ง๐ปโ",
    "man_in_steamy_room_tone2": "๐ง๐ผโ",
    "man_in_steamy_room_medium_light_skin_tone": "๐ง๐ผโ",
    "man_in_steamy_room_tone3": "๐ง๐ฝโ",
    "man_in_steamy_room_medium_skin_tone": "๐ง๐ฝโ",
    "man_in_steamy_room_tone4": "๐ง๐พโ",
    "man_in_steamy_room_medium_dark_skin_tone": "๐ง๐พโ",
    "man_in_steamy_room_tone5": "๐ง๐ฟโ",
    "man_in_steamy_room_dark_skin_tone": "๐ง๐ฟโ",
    "nail_care": "๐",
    "nail_care_tone1": "๐๐ป",
    "nail_care_tone2": "๐๐ผ",
    "nail_care_tone3": "๐๐ฝ",
    "nail_care_tone4": "๐๐พ",
    "nail_care_tone5": "๐๐ฟ",
    "selfie": "๐คณ",
    "selfie_tone1": "๐คณ๐ป",
    "selfie_tone2": "๐คณ๐ผ",
    "selfie_tone3": "๐คณ๐ฝ",
    "selfie_tone4": "๐คณ๐พ",
    "selfie_tone5": "๐คณ๐ฟ",
    "dancer": "๐",
    "dancer_tone1": "๐๐ป",
    "dancer_tone2": "๐๐ผ",
    "dancer_tone3": "๐๐ฝ",
    "dancer_tone4": "๐๐พ",
    "dancer_tone5": "๐๐ฟ",
    "man_dancing": "๐บ",
    "male_dancer": "๐บ",
    "man_dancing_tone1": "๐บ๐ป",
    "male_dancer_tone1": "๐บ๐ป",
    "man_dancing_tone2": "๐บ๐ผ",
    "male_dancer_tone2": "๐บ๐ผ",
    "man_dancing_tone3": "๐บ๐ฝ",
    "male_dancer_tone3": "๐บ๐ฝ",
    "man_dancing_tone5": "๐บ๐ฟ",
    "male_dancer_tone5": "๐บ๐ฟ",
    "man_dancing_tone4": "๐บ๐พ",
    "male_dancer_tone4": "๐บ๐พ",
    "people_with_bunny_ears_partying": "๐ฏ",
    "dancers": "๐ฏ",
    "women_with_bunny_ears_partying": "๐ฏโ",
    "men_with_bunny_ears_partying": "๐ฏโ",
    "levitate": "๐ด",
    "man_in_business_suit_levitating": "๐ด",
    "levitate_tone1": "๐ด๐ป",
    "man_in_business_suit_levitating_tone1": "๐ด๐ป",
    "man_in_business_suit_levitating_light_skin_tone": "๐ด๐ป",
    "levitate_tone2": "๐ด๐ผ",
    "man_in_business_suit_levitating_tone2": "๐ด๐ผ",
    "man_in_business_suit_levitating_medium_light_skin_tone": "๐ด๐ผ",
    "levitate_tone3": "๐ด๐ฝ",
    "man_in_business_suit_levitating_tone3": "๐ด๐ฝ",
    "man_in_business_suit_levitating_medium_skin_tone": "๐ด๐ฝ",
    "levitate_tone4": "๐ด๐พ",
    "man_in_business_suit_levitating_tone4": "๐ด๐พ",
    "man_in_business_suit_levitating_medium_dark_skin_tone": "๐ด๐พ",
    "levitate_tone5": "๐ด๐ฟ",
    "man_in_business_suit_levitating_tone5": "๐ด๐ฟ",
    "man_in_business_suit_levitating_dark_skin_tone": "๐ด๐ฟ",
    "person_walking": "๐ถ",
    "walking": "๐ถ",
    "person_walking_tone1": "๐ถ๐ป",
    "walking_tone1": "๐ถ๐ป",
    "person_walking_tone2": "๐ถ๐ผ",
    "walking_tone2": "๐ถ๐ผ",
    "person_walking_tone3": "๐ถ๐ฝ",
    "walking_tone3": "๐ถ๐ฝ",
    "person_walking_tone4": "๐ถ๐พ",
    "walking_tone4": "๐ถ๐พ",
    "person_walking_tone5": "๐ถ๐ฟ",
    "walking_tone5": "๐ถ๐ฟ",
    "woman_walking": "๐ถโ",
    "woman_walking_tone1": "๐ถ๐ปโ",
    "woman_walking_light_skin_tone": "๐ถ๐ปโ",
    "woman_walking_tone2": "๐ถ๐ผโ",
    "woman_walking_medium_light_skin_tone": "๐ถ๐ผโ",
    "woman_walking_tone3": "๐ถ๐ฝโ",
    "woman_walking_medium_skin_tone": "๐ถ๐ฝโ",
    "woman_walking_tone4": "๐ถ๐พโ",
    "woman_walking_medium_dark_skin_tone": "๐ถ๐พโ",
    "woman_walking_tone5": "๐ถ๐ฟโ",
    "woman_walking_dark_skin_tone": "๐ถ๐ฟโ",
    "man_walking": "๐ถโ",
    "man_walking_tone1": "๐ถ๐ปโ",
    "man_walking_light_skin_tone": "๐ถ๐ปโ",
    "man_walking_tone2": "๐ถ๐ผโ",
    "man_walking_medium_light_skin_tone": "๐ถ๐ผโ",
    "man_walking_tone3": "๐ถ๐ฝโ",
    "man_walking_medium_skin_tone": "๐ถ๐ฝโ",
    "man_walking_tone4": "๐ถ๐พโ",
    "man_walking_medium_dark_skin_tone": "๐ถ๐พโ",
    "man_walking_tone5": "๐ถ๐ฟโ",
    "man_walking_dark_skin_tone": "๐ถ๐ฟโ",
    "person_running": "๐",
    "runner": "๐",
    "person_running_tone1": "๐๐ป",
    "runner_tone1": "๐๐ป",
    "person_running_tone2": "๐๐ผ",
    "runner_tone2": "๐๐ผ",
    "person_running_tone3": "๐๐ฝ",
    "runner_tone3": "๐๐ฝ",
    "person_running_tone4": "๐๐พ",
    "runner_tone4": "๐๐พ",
    "person_running_tone5": "๐๐ฟ",
    "runner_tone5": "๐๐ฟ",
    "woman_running": "๐โ",
    "woman_running_tone1": "๐๐ปโ",
    "woman_running_light_skin_tone": "๐๐ปโ",
    "woman_running_tone2": "๐๐ผโ",
    "woman_running_medium_light_skin_tone": "๐๐ผโ",
    "woman_running_tone3": "๐๐ฝโ",
    "woman_running_medium_skin_tone": "๐๐ฝโ",
    "woman_running_tone4": "๐๐พโ",
    "woman_running_medium_dark_skin_tone": "๐๐พโ",
    "woman_running_tone5": "๐๐ฟโ",
    "woman_running_dark_skin_tone": "๐๐ฟโ",
    "man_running": "๐โ",
    "man_running_tone1": "๐๐ปโ",
    "man_running_light_skin_tone": "๐๐ปโ",
    "man_running_tone2": "๐๐ผโ",
    "man_running_medium_light_skin_tone": "๐๐ผโ",
    "man_running_tone3": "๐๐ฝโ",
    "man_running_medium_skin_tone": "๐๐ฝโ",
    "man_running_tone4": "๐๐พโ",
    "man_running_medium_dark_skin_tone": "๐๐พโ",
    "man_running_tone5": "๐๐ฟโ",
    "man_running_dark_skin_tone": "๐๐ฟโ",
    "person_standing": "๐ง",
    "person_standing_tone1": "๐ง๐ป",
    "person_standing_light_skin_tone": "๐ง๐ป",
    "person_standing_tone2": "๐ง๐ผ",
    "person_standing_medium_light_skin_tone": "๐ง๐ผ",
    "person_standing_tone3": "๐ง๐ฝ",
    "person_standing_medium_skin_tone": "๐ง๐ฝ",
    "person_standing_tone4": "๐ง๐พ",
    "person_standing_medium_dark_skin_tone": "๐ง๐พ",
    "person_standing_tone5": "๐ง๐ฟ",
    "person_standing_dark_skin_tone": "๐ง๐ฟ",
    "woman_standing": "๐งโ",
    "woman_standing_tone1": "๐ง๐ปโ",
    "woman_standing_light_skin_tone": "๐ง๐ปโ",
    "woman_standing_tone2": "๐ง๐ผโ",
    "woman_standing_medium_light_skin_tone": "๐ง๐ผโ",
    "woman_standing_tone3": "๐ง๐ฝโ",
    "woman_standing_medium_skin_tone": "๐ง๐ฝโ",
    "woman_standing_tone4": "๐ง๐พโ",
    "woman_standing_medium_dark_skin_tone": "๐ง๐พโ",
    "woman_standing_tone5": "๐ง๐ฟโ",
    "woman_standing_dark_skin_tone": "๐ง๐ฟโ",
    "man_standing": "๐งโ",
    "man_standing_tone1": "๐ง๐ปโ",
    "man_standing_light_skin_tone": "๐ง๐ปโ",
    "man_standing_tone2": "๐ง๐ผโ",
    "man_standing_medium_light_skin_tone": "๐ง๐ผโ",
    "man_standing_tone3": "๐ง๐ฝโ",
    "man_standing_medium_skin_tone": "๐ง๐ฝโ",
    "man_standing_tone4": "๐ง๐พโ",
    "man_standing_medium_dark_skin_tone": "๐ง๐พโ",
    "man_standing_tone5": "๐ง๐ฟโ",
    "man_standing_dark_skin_tone": "๐ง๐ฟโ",
    "person_kneeling": "๐ง",
    "person_kneeling_tone1": "๐ง๐ป",
    "person_kneeling_light_skin_tone": "๐ง๐ป",
    "person_kneeling_tone2": "๐ง๐ผ",
    "person_kneeling_medium_light_skin_tone": "๐ง๐ผ",
    "person_kneeling_tone3": "๐ง๐ฝ",
    "person_kneeling_medium_skin_tone": "๐ง๐ฝ",
    "person_kneeling_tone4": "๐ง๐พ",
    "person_kneeling_medium_dark_skin_tone": "๐ง๐พ",
    "person_kneeling_tone5": "๐ง๐ฟ",
    "person_kneeling_dark_skin_tone": "๐ง๐ฟ",
    "woman_kneeling": "๐งโ",
    "woman_kneeling_tone1": "๐ง๐ปโ",
    "woman_kneeling_light_skin_tone": "๐ง๐ปโ",
    "woman_kneeling_tone2": "๐ง๐ผโ",
    "woman_kneeling_medium_light_skin_tone": "๐ง๐ผโ",
    "woman_kneeling_tone3": "๐ง๐ฝโ",
    "woman_kneeling_medium_skin_tone": "๐ง๐ฝโ",
    "woman_kneeling_tone4": "๐ง๐พโ",
    "woman_kneeling_medium_dark_skin_tone": "๐ง๐พโ",
    "woman_kneeling_tone5": "๐ง๐ฟโ",
    "woman_kneeling_dark_skin_tone": "๐ง๐ฟโ",
    "man_kneeling": "๐งโ",
    "man_kneeling_tone1": "๐ง๐ปโ",
    "man_kneeling_light_skin_tone": "๐ง๐ปโ",
    "man_kneeling_tone2": "๐ง๐ผโ",
    "man_kneeling_medium_light_skin_tone": "๐ง๐ผโ",
    "man_kneeling_tone3": "๐ง๐ฝโ",
    "man_kneeling_medium_skin_tone": "๐ง๐ฝโ",
    "man_kneeling_tone4": "๐ง๐พโ",
    "man_kneeling_medium_dark_skin_tone": "๐ง๐พโ",
    "man_kneeling_tone5": "๐ง๐ฟโ",
    "man_kneeling_dark_skin_tone": "๐ง๐ฟโ",
    "woman_with_probing_cane": "๐ฉ๐ฆฏ",
    "woman_with_probing_cane_tone1": "๐ฉ๐ป๐ฆฏ",
    "woman_with_probing_cane_light_skin_tone": "๐ฉ๐ป๐ฆฏ",
    "woman_with_probing_cane_tone2": "๐ฉ๐ผ๐ฆฏ",
    "woman_with_probing_cane_medium_light_skin_tone": "๐ฉ๐ผ๐ฆฏ",
    "woman_with_probing_cane_tone3": "๐ฉ๐ฝ๐ฆฏ",
    "woman_with_probing_cane_medium_skin_tone": "๐ฉ๐ฝ๐ฆฏ",
    "woman_with_probing_cane_tone4": "๐ฉ๐พ๐ฆฏ",
    "woman_with_probing_cane_medium_dark_skin_tone": "๐ฉ๐พ๐ฆฏ",
    "woman_with_probing_cane_tone5": "๐ฉ๐ฟ๐ฆฏ",
    "woman_with_probing_cane_dark_skin_tone": "๐ฉ๐ฟ๐ฆฏ",
    "man_with_probing_cane": "๐จ๐ฆฏ",
    "man_with_probing_cane_tone1": "๐จ๐ป๐ฆฏ",
    "man_with_probing_cane_light_skin_tone": "๐จ๐ป๐ฆฏ",
    "man_with_probing_cane_tone2": "๐จ๐ผ๐ฆฏ",
    "man_with_probing_cane_medium_light_skin_tone": "๐จ๐ผ๐ฆฏ",
    "man_with_probing_cane_tone3": "๐จ๐ฝ๐ฆฏ",
    "man_with_probing_cane_medium_skin_tone": "๐จ๐ฝ๐ฆฏ",
    "man_with_probing_cane_tone4": "๐จ๐พ๐ฆฏ",
    "man_with_probing_cane_medium_dark_skin_tone": "๐จ๐พ๐ฆฏ",
    "man_with_probing_cane_tone5": "๐จ๐ฟ๐ฆฏ",
    "man_with_probing_cane_dark_skin_tone": "๐จ๐ฟ๐ฆฏ",
    "woman_in_motorized_wheelchair": "๐ฉ๐ฆผ",
    "woman_in_motorized_wheelchair_tone1": "๐ฉ๐ป๐ฆผ",
    "woman_in_motorized_wheelchair_light_skin_tone": "๐ฉ๐ป๐ฆผ",
    "woman_in_motorized_wheelchair_tone2": "๐ฉ๐ผ๐ฆผ",
    "woman_in_motorized_wheelchair_medium_light_skin_tone": "๐ฉ๐ผ๐ฆผ",
    "woman_in_motorized_wheelchair_tone3": "๐ฉ๐ฝ๐ฆผ",
    "woman_in_motorized_wheelchair_medium_skin_tone": "๐ฉ๐ฝ๐ฆผ",
    "woman_in_motorized_wheelchair_tone4": "๐ฉ๐พ๐ฆผ",
    "woman_in_motorized_wheelchair_medium_dark_skin_tone": "๐ฉ๐พ๐ฆผ",
    "woman_in_motorized_wheelchair_tone5": "๐ฉ๐ฟ๐ฆผ",
    "woman_in_motorized_wheelchair_dark_skin_tone": "๐ฉ๐ฟ๐ฆผ",
    "man_in_motorized_wheelchair": "๐จ๐ฆผ",
    "man_in_motorized_wheelchair_tone1": "๐จ๐ป๐ฆผ",
    "man_in_motorized_wheelchair_light_skin_tone": "๐จ๐ป๐ฆผ",
    "man_in_motorized_wheelchair_tone2": "๐จ๐ผ๐ฆผ",
    "man_in_motorized_wheelchair_medium_light_skin_tone": "๐จ๐ผ๐ฆผ",
    "man_in_motorized_wheelchair_tone3": "๐จ๐ฝ๐ฆผ",
    "man_in_motorized_wheelchair_medium_skin_tone": "๐จ๐ฝ๐ฆผ",
    "man_in_motorized_wheelchair_tone4": "๐จ๐พ๐ฆผ",
    "man_in_motorized_wheelchair_medium_dark_skin_tone": "๐จ๐พ๐ฆผ",
    "man_in_motorized_wheelchair_tone5": "๐จ๐ฟ๐ฆผ",
    "man_in_motorized_wheelchair_dark_skin_tone": "๐จ๐ฟ๐ฆผ",
    "woman_in_manual_wheelchair": "๐ฉ๐ฆฝ",
    "woman_in_manual_wheelchair_tone1": "๐ฉ๐ป๐ฆฝ",
    "woman_in_manual_wheelchair_light_skin_tone": "๐ฉ๐ป๐ฆฝ",
    "woman_in_manual_wheelchair_tone2": "๐ฉ๐ผ๐ฆฝ",
    "woman_in_manual_wheelchair_medium_light_skin_tone": "๐ฉ๐ผ๐ฆฝ",
    "woman_in_manual_wheelchair_tone3": "๐ฉ๐ฝ๐ฆฝ",
    "woman_in_manual_wheelchair_medium_skin_tone": "๐ฉ๐ฝ๐ฆฝ",
    "woman_in_manual_wheelchair_tone4": "๐ฉ๐พ๐ฆฝ",
    "woman_in_manual_wheelchair_medium_dark_skin_tone": "๐ฉ๐พ๐ฆฝ",
    "woman_in_manual_wheelchair_tone5": "๐ฉ๐ฟ๐ฆฝ",
    "woman_in_manual_wheelchair_dark_skin_tone": "๐ฉ๐ฟ๐ฆฝ",
    "man_in_manual_wheelchair": "๐จ๐ฆฝ",
    "man_in_manual_wheelchair_tone1": "๐จ๐ป๐ฆฝ",
    "man_in_manual_wheelchair_light_skin_tone": "๐จ๐ป๐ฆฝ",
    "man_in_manual_wheelchair_tone2": "๐จ๐ผ๐ฆฝ",
    "man_in_manual_wheelchair_medium_light_skin_tone": "๐จ๐ผ๐ฆฝ",
    "man_in_manual_wheelchair_tone3": "๐จ๐ฝ๐ฆฝ",
    "man_in_manual_wheelchair_medium_skin_tone": "๐จ๐ฝ๐ฆฝ",
    "man_in_manual_wheelchair_tone4": "๐จ๐พ๐ฆฝ",
    "man_in_manual_wheelchair_medium_dark_skin_tone": "๐จ๐พ๐ฆฝ",
    "man_in_manual_wheelchair_tone5": "๐จ๐ฟ๐ฆฝ",
    "man_in_manual_wheelchair_dark_skin_tone": "๐จ๐ฟ๐ฆฝ",
    "people_holding_hands": "๐ง๐ค๐ง",
    "couple": "๐ซ",
    "two_women_holding_hands": "๐ญ",
    "two_men_holding_hands": "๐ฌ",
    "couple_with_heart": "๐",
    "couple_with_heart_woman_man": "๐ฉโค๐จ",
    "couple_ww": "๐ฉโค๐ฉ",
    "couple_with_heart_ww": "๐ฉโค๐ฉ",
    "couple_mm": "๐จโค๐จ",
    "couple_with_heart_mm": "๐จโค๐จ",
    "couplekiss": "๐",
    "kiss_woman_man": "๐ฉโค๐๐จ",
    "kiss_ww": "๐ฉโค๐๐ฉ",
    "couplekiss_ww": "๐ฉโค๐๐ฉ",
    "kiss_mm": "๐จโค๐๐จ",
    "couplekiss_mm": "๐จโค๐๐จ",
    "family": "๐ช",
    "family_man_woman_boy": "๐จ๐ฉ๐ฆ",
    "family_mwg": "๐จ๐ฉ๐ง",
    "family_mwgb": "๐จ๐ฉ๐ง๐ฆ",
    "family_mwbb": "๐จ๐ฉ๐ฆ๐ฆ",
    "family_mwgg": "๐จ๐ฉ๐ง๐ง",
    "family_wwb": "๐ฉ๐ฉ๐ฆ",
    "family_wwg": "๐ฉ๐ฉ๐ง",
    "family_wwgb": "๐ฉ๐ฉ๐ง๐ฆ",
    "family_wwbb": "๐ฉ๐ฉ๐ฆ๐ฆ",
    "family_wwgg": "๐ฉ๐ฉ๐ง๐ง",
    "family_mmb": "๐จ๐จ๐ฆ",
    "family_mmg": "๐จ๐จ๐ง",
    "family_mmgb": "๐จ๐จ๐ง๐ฆ",
    "family_mmbb": "๐จ๐จ๐ฆ๐ฆ",
    "family_mmgg": "๐จ๐จ๐ง๐ง",
    "family_woman_boy": "๐ฉ๐ฆ",
    "family_woman_girl": "๐ฉ๐ง",
    "family_woman_girl_boy": "๐ฉ๐ง๐ฆ",
    "family_woman_boy_boy": "๐ฉ๐ฆ๐ฆ",
    "family_woman_girl_girl": "๐ฉ๐ง๐ง",
    "family_man_boy": "๐จ๐ฆ",
    "family_man_girl": "๐จ๐ง",
    "family_man_girl_boy": "๐จ๐ง๐ฆ",
    "family_man_boy_boy": "๐จ๐ฆ๐ฆ",
    "family_man_girl_girl": "๐จ๐ง๐ง",
    "yarn": "๐งถ",
    "thread": "๐งต",
    "coat": "๐งฅ",
    "lab_coat": "๐ฅผ",
    "safety_vest": "๐ฆบ",
    "womans_clothes": "๐",
    "shirt": "๐",
    "jeans": "๐",
    "shorts": "๐ฉณ",
    "necktie": "๐",
    "dress": "๐",
    "bikini": "๐",
    "one_piece_swimsuit": "๐ฉฑ",
    "kimono": "๐",
    "sari": "๐ฅป",
    "womans_flat_shoe": "๐ฅฟ",
    "high_heel": "๐ ",
    "sandal": "๐ก",
    "boot": "๐ข",
    "ballet_shoes": "๐ฉฐ",
    "mans_shoe": "๐",
    "athletic_shoe": "๐",
    "hiking_boot": "๐ฅพ",
    "briefs": "๐ฉฒ",
    "socks": "๐งฆ",
    "gloves": "๐งค",
    "scarf": "๐งฃ",
    "tophat": "๐ฉ",
    "billed_cap": "๐งข",
    "womans_hat": "๐",
    "mortar_board": "๐",
    "helmet_with_cross": "โ",
    "helmet_with_white_cross": "โ",
    "crown": "๐",
    "ring": "๐",
    "pouch": "๐",
    "purse": "๐",
    "handbag": "๐",
    "briefcase": "๐ผ",
    "school_satchel": "๐",
    "luggage": "๐งณ",
    "eyeglasses": "๐",
    "dark_sunglasses": "๐ถ",
    "goggles": "๐ฅฝ",
    "diving_mask": "๐คฟ",
    "closed_umbrella": "๐",
    "dog": "๐ถ",
    "cat": "๐ฑ",
    "mouse": "๐ญ",
    "hamster": "๐น",
    "rabbit": "๐ฐ",
    "fox": "๐ฆ",
    "fox_face": "๐ฆ",
    "bear": "๐ป",
    "panda_face": "๐ผ",
    "koala": "๐จ",
    "tiger": "๐ฏ",
    "lion_face": "๐ฆ",
    "lion": "๐ฆ",
    "cow": "๐ฎ",
    "pig": "๐ท",
    "pig_nose": "๐ฝ",
    "frog": "๐ธ",
    "monkey_face": "๐ต",
    "see_no_evil": "๐",
    "hear_no_evil": "๐",
    "speak_no_evil": "๐",
    "monkey": "๐",
    "chicken": "๐",
    "penguin": "๐ง",
    "bird": "๐ฆ",
    "baby_chick": "๐ค",
    "hatching_chick": "๐ฃ",
    "hatched_chick": "๐ฅ",
    "duck": "๐ฆ",
    "eagle": "๐ฆ",
    "owl": "๐ฆ",
    "bat": "๐ฆ",
    "wolf": "๐บ",
    "boar": "๐",
    "horse": "๐ด",
    "unicorn": "๐ฆ",
    "unicorn_face": "๐ฆ",
    "bee": "๐",
    "bug": "๐",
    "butterfly": "๐ฆ",
    "snail": "๐",
    "shell": "๐",
    "beetle": "๐",
    "ant": "๐",
    "mosquito": "๐ฆ",
    "cricket": "๐ฆ",
    "spider": "๐ท",
    "spider_web": "๐ธ",
    "scorpion": "๐ฆ",
    "turtle": "๐ข",
    "snake": "๐",
    "lizard": "๐ฆ",
    "t_rex": "๐ฆ",
    "sauropod": "๐ฆ",
    "octopus": "๐",
    "squid": "๐ฆ",
    "shrimp": "๐ฆ",
    "lobster": "๐ฆ",
    "oyster": "๐ฆช",
    "crab": "๐ฆ",
    "blowfish": "๐ก",
    "tropical_fish": "๐ ",
    "fish": "๐",
    "dolphin": "๐ฌ",
    "whale": "๐ณ",
    "whale2": "๐",
    "shark": "๐ฆ",
    "crocodile": "๐",
    "tiger2": "๐",
    "leopard": "๐",
    "zebra": "๐ฆ",
    "gorilla": "๐ฆ",
    "orangutan": "๐ฆง",
    "elephant": "๐",
    "hippopotamus": "๐ฆ",
    "rhino": "๐ฆ",
    "rhinoceros": "๐ฆ",
    "dromedary_camel": "๐ช",
    "camel": "๐ซ",
    "giraffe": "๐ฆ",
    "kangaroo": "๐ฆ",
    "water_buffalo": "๐",
    "ox": "๐",
    "cow2": "๐",
    "racehorse": "๐",
    "pig2": "๐",
    "ram": "๐",
    "llama": "๐ฆ",
    "sheep": "๐",
    "goat": "๐",
    "deer": "๐ฆ",
    "dog2": "๐",
    "guide_dog": "๐ฆฎ",
    "service_dog": "๐๐ฆบ",
    "poodle": "๐ฉ",
    "cat2": "๐",
    "rooster": "๐",
    "turkey": "๐ฆ",
    "peacock": "๐ฆ",
    "parrot": "๐ฆ",
    "swan": "๐ฆข",
    "flamingo": "๐ฆฉ",
    "dove": "๐",
    "dove_of_peace": "๐",
    "rabbit2": "๐",
    "sloth": "๐ฆฅ",
    "otter": "๐ฆฆ",
    "skunk": "๐ฆจ",
    "raccoon": "๐ฆ",
    "badger": "๐ฆก",
    "mouse2": "๐",
    "rat": "๐",
    "chipmunk": "๐ฟ",
    "hedgehog": "๐ฆ",
    "feet": "๐พ",
    "paw_prints": "๐พ",
    "dragon": "๐",
    "dragon_face": "๐ฒ",
    "cactus": "๐ต",
    "christmas_tree": "๐",
    "evergreen_tree": "๐ฒ",
    "deciduous_tree": "๐ณ",
    "palm_tree": "๐ด",
    "seedling": "๐ฑ",
    "herb": "๐ฟ",
    "shamrock": "โ",
    "four_leaf_clover": "๐",
    "bamboo": "๐",
    "tanabata_tree": "๐",
    "leaves": "๐",
    "fallen_leaf": "๐",
    "maple_leaf": "๐",
    "mushroom": "๐",
    "ear_of_rice": "๐พ",
    "bouquet": "๐",
    "tulip": "๐ท",
    "rose": "๐น",
    "wilted_rose": "๐ฅ",
    "wilted_flower": "๐ฅ",
    "hibiscus": "๐บ",
    "cherry_blossom": "๐ธ",
    "blossom": "๐ผ",
    "sunflower": "๐ป",
    "sun_with_face": "๐",
    "full_moon_with_face": "๐",
    "first_quarter_moon_with_face": "๐",
    "last_quarter_moon_with_face": "๐",
    "new_moon_with_face": "๐",
    "full_moon": "๐",
    "waning_gibbous_moon": "๐",
    "last_quarter_moon": "๐",
    "waning_crescent_moon": "๐",
    "new_moon": "๐",
    "waxing_crescent_moon": "๐",
    "first_quarter_moon": "๐",
    "waxing_gibbous_moon": "๐",
    "crescent_moon": "๐",
    "earth_americas": "๐",
    "earth_africa": "๐",
    "earth_asia": "๐",
    "ringed_planet": "๐ช",
    "dizzy": "๐ซ",
    "star": "โญ",
    "star2": "๐",
    "sparkles": "โจ",
    "zap": "โก",
    "comet": "โ",
    "boom": "๐ฅ",
    "fire": "๐ฅ",
    "flame": "๐ฅ",
    "cloud_tornado": "๐ช",
    "cloud_with_tornado": "๐ช",
    "rainbow": "๐",
    "sunny": "โ",
    "white_sun_small_cloud": "๐ค",
    "white_sun_with_small_cloud": "๐ค",
    "partly_sunny": "โ",
    "white_sun_cloud": "๐ฅ",
    "white_sun_behind_cloud": "๐ฅ",
    "cloud": "โ",
    "white_sun_rain_cloud": "๐ฆ",
    "white_sun_behind_cloud_with_rain": "๐ฆ",
    "cloud_rain": "๐ง",
    "cloud_with_rain": "๐ง",
    "thunder_cloud_rain": "โ",
    "thunder_cloud_and_rain": "โ",
    "cloud_lightning": "๐ฉ",
    "cloud_with_lightning": "๐ฉ",
    "cloud_snow": "๐จ",
    "cloud_with_snow": "๐จ",
    "snowflake": "โ",
    "snowman2": "โ",
    "snowman": "โ",
    "wind_blowing_face": "๐ฌ",
    "dash": "๐จ",
    "droplet": "๐ง",
    "sweat_drops": "๐ฆ",
    "umbrella": "โ",
    "umbrella2": "โ",
    "ocean": "๐",
    "fog": "๐ซ",
    "green_apple": "๐",
    "apple": "๐",
    "pear": "๐",
    "tangerine": "๐",
    "lemon": "๐",
    "banana": "๐",
    "watermelon": "๐",
    "grapes": "๐",
    "strawberry": "๐",
    "melon": "๐",
    "cherries": "๐",
    "peach": "๐",
    "mango": "๐ฅญ",
    "pineapple": "๐",
    "coconut": "๐ฅฅ",
    "kiwi": "๐ฅ",
    "kiwifruit": "๐ฅ",
    "tomato": "๐",
    "eggplant": "๐",
    "avocado": "๐ฅ",
    "broccoli": "๐ฅฆ",
    "leafy_green": "๐ฅฌ",
    "cucumber": "๐ฅ",
    "hot_pepper": "๐ถ",
    "corn": "๐ฝ",
    "carrot": "๐ฅ",
    "onion": "๐ง",
    "garlic": "๐ง",
    "potato": "๐ฅ",
    "sweet_potato": "๐ ",
    "croissant": "๐ฅ",
    "bagel": "๐ฅฏ",
    "bread": "๐",
    "french_bread": "๐ฅ",
    "baguette_bread": "๐ฅ",
    "pretzel": "๐ฅจ",
    "cheese": "๐ง",
    "cheese_wedge": "๐ง",
    "egg": "๐ฅ",
    "cooking": "๐ณ",
    "pancakes": "๐ฅ",
    "waffle": "๐ง",
    "bacon": "๐ฅ",
    "cut_of_meat": "๐ฅฉ",
    "poultry_leg": "๐",
    "meat_on_bone": "๐",
    "hotdog": "๐ญ",
    "hot_dog": "๐ญ",
    "hamburger": "๐",
    "fries": "๐",
    "pizza": "๐",
    "sandwich": "๐ฅช",
    "falafel": "๐ง",
    "stuffed_flatbread": "๐ฅ",
    "stuffed_pita": "๐ฅ",
    "taco": "๐ฎ",
    "burrito": "๐ฏ",
    "salad": "๐ฅ",
    "green_salad": "๐ฅ",
    "shallow_pan_of_food": "๐ฅ",
    "paella": "๐ฅ",
    "canned_food": "๐ฅซ",
    "spaghetti": "๐",
    "ramen": "๐",
    "stew": "๐ฒ",
    "curry": "๐",
    "sushi": "๐ฃ",
    "bento": "๐ฑ",
    "dumpling": "๐ฅ",
    "fried_shrimp": "๐ค",
    "rice_ball": "๐",
    "rice": "๐",
    "rice_cracker": "๐",
    "fish_cake": "๐ฅ",
    "fortune_cookie": "๐ฅ ",
    "moon_cake": "๐ฅฎ",
    "oden": "๐ข",
    "dango": "๐ก",
    "shaved_ice": "๐ง",
    "ice_cream": "๐จ",
    "icecream": "๐ฆ",
    "pie": "๐ฅง",
    "cupcake": "๐ง",
    "cake": "๐ฐ",
    "birthday": "๐",
    "custard": "๐ฎ",
    "pudding": "๐ฎ",
    "flan": "๐ฎ",
    "lollipop": "๐ญ",
    "candy": "๐ฌ",
    "chocolate_bar": "๐ซ",
    "popcorn": "๐ฟ",
    "doughnut": "๐ฉ",
    "cookie": "๐ช",
    "chestnut": "๐ฐ",
    "peanuts": "๐ฅ",
    "shelled_peanut": "๐ฅ",
    "honey_pot": "๐ฏ",
    "butter": "๐ง",
    "milk": "๐ฅ",
    "glass_of_milk": "๐ฅ",
    "baby_bottle": "๐ผ",
    "coffee": "โ",
    "tea": "๐ต",
    "mate": "๐ง",
    "cup_with_straw": "๐ฅค",
    "beverage_box": "๐ง",
    "ice_cube": "๐ง",
    "sake": "๐ถ",
    "beer": "๐บ",
    "beers": "๐ป",
    "champagne_glass": "๐ฅ",
    "clinking_glass": "๐ฅ",
    "wine_glass": "๐ท",
    "tumbler_glass": "๐ฅ",
    "whisky": "๐ฅ",
    "cocktail": "๐ธ",
    "tropical_drink": "๐น",
    "champagne": "๐พ",
    "bottle_with_popping_cork": "๐พ",
    "spoon": "๐ฅ",
    "fork_and_knife": "๐ด",
    "fork_knife_plate": "๐ฝ",
    "fork_and_knife_with_plate": "๐ฝ",
    "bowl_with_spoon": "๐ฅฃ",
    "takeout_box": "๐ฅก",
    "chopsticks": "๐ฅข",
    "salt": "๐ง",
    "soccer": "โฝ",
    "basketball": "๐",
    "football": "๐",
    "baseball": "โพ",
    "softball": "๐ฅ",
    "tennis": "๐พ",
    "volleyball": "๐",
    "rugby_football": "๐",
    "flying_disc": "๐ฅ",
    "8ball": "๐ฑ",
    "ping_pong": "๐",
    "table_tennis": "๐",
    "badminton": "๐ธ",
    "hockey": "๐",
    "field_hockey": "๐",
    "lacrosse": "๐ฅ",
    "cricket_game": "๐",
    "cricket_bat_ball": "๐",
    "goal": "๐ฅ",
    "goal_net": "๐ฅ",
    "golf": "โณ",
    "bow_and_arrow": "๐น",
    "archery": "๐น",
    "fishing_pole_and_fish": "๐ฃ",
    "boxing_glove": "๐ฅ",
    "boxing_gloves": "๐ฅ",
    "martial_arts_uniform": "๐ฅ",
    "karate_uniform": "๐ฅ",
    "running_shirt_with_sash": "๐ฝ",
    "skateboard": "๐น",
    "sled": "๐ท",
    "parachute": "๐ช",
    "ice_skate": "โธ",
    "curling_stone": "๐ฅ",
    "ski": "๐ฟ",
    "skier": "โท",
    "snowboarder": "๐",
    "snowboarder_tone1": "๐๐ป",
    "snowboarder_light_skin_tone": "๐๐ป",
    "snowboarder_tone2": "๐๐ผ",
    "snowboarder_medium_light_skin_tone": "๐๐ผ",
    "snowboarder_tone3": "๐๐ฝ",
    "snowboarder_medium_skin_tone": "๐๐ฝ",
    "snowboarder_tone4": "๐๐พ",
    "snowboarder_medium_dark_skin_tone": "๐๐พ",
    "snowboarder_tone5": "๐๐ฟ",
    "snowboarder_dark_skin_tone": "๐๐ฟ",
    "person_lifting_weights": "๐",
    "lifter": "๐",
    "weight_lifter": "๐",
    "person_lifting_weights_tone1": "๐๐ป",
    "lifter_tone1": "๐๐ป",
    "weight_lifter_tone1": "๐๐ป",
    "person_lifting_weights_tone2": "๐๐ผ",
    "lifter_tone2": "๐๐ผ",
    "weight_lifter_tone2": "๐๐ผ",
    "person_lifting_weights_tone3": "๐๐ฝ",
    "lifter_tone3": "๐๐ฝ",
    "weight_lifter_tone3": "๐๐ฝ",
    "person_lifting_weights_tone4": "๐๐พ",
    "lifter_tone4": "๐๐พ",
    "weight_lifter_tone4": "๐๐พ",
    "person_lifting_weights_tone5": "๐๐ฟ",
    "lifter_tone5": "๐๐ฟ",
    "weight_lifter_tone5": "๐๐ฟ",
    "woman_lifting_weights": "๐โ",
    "woman_lifting_weights_tone1": "๐๐ปโ",
    "woman_lifting_weights_light_skin_tone": "๐๐ปโ",
    "woman_lifting_weights_tone2": "๐๐ผโ",
    "woman_lifting_weights_medium_light_skin_tone": "๐๐ผโ",
    "woman_lifting_weights_tone3": "๐๐ฝโ",
    "woman_lifting_weights_medium_skin_tone": "๐๐ฝโ",
    "woman_lifting_weights_tone4": "๐๐พโ",
    "woman_lifting_weights_medium_dark_skin_tone": "๐๐พโ",
    "woman_lifting_weights_tone5": "๐๐ฟโ",
    "woman_lifting_weights_dark_skin_tone": "๐๐ฟโ",
    "man_lifting_weights": "๐โ",
    "man_lifting_weights_tone1": "๐๐ปโ",
    "man_lifting_weights_light_skin_tone": "๐๐ปโ",
    "man_lifting_weights_tone2": "๐๐ผโ",
    "man_lifting_weights_medium_light_skin_tone": "๐๐ผโ",
    "man_lifting_weights_tone3": "๐๐ฝโ",
    "man_lifting_weights_medium_skin_tone": "๐๐ฝโ",
    "man_lifting_weights_tone4": "๐๐พโ",
    "man_lifting_weights_medium_dark_skin_tone": "๐๐พโ",
    "man_lifting_weights_tone5": "๐๐ฟโ",
    "man_lifting_weights_dark_skin_tone": "๐๐ฟโ",
    "people_wrestling": "๐คผ",
    "wrestlers": "๐คผ",
    "wrestling": "๐คผ",
    "women_wrestling": "๐คผโ",
    "men_wrestling": "๐คผโ",
    "person_doing_cartwheel": "๐คธ",
    "cartwheel": "๐คธ",
    "person_doing_cartwheel_tone1": "๐คธ๐ป",
    "cartwheel_tone1": "๐คธ๐ป",
    "person_doing_cartwheel_tone2": "๐คธ๐ผ",
    "cartwheel_tone2": "๐คธ๐ผ",
    "person_doing_cartwheel_tone3": "๐คธ๐ฝ",
    "cartwheel_tone3": "๐คธ๐ฝ",
    "person_doing_cartwheel_tone4": "๐คธ๐พ",
    "cartwheel_tone4": "๐คธ๐พ",
    "person_doing_cartwheel_tone5": "๐คธ๐ฟ",
    "cartwheel_tone5": "๐คธ๐ฟ",
    "woman_cartwheeling": "๐คธโ",
    "woman_cartwheeling_tone1": "๐คธ๐ปโ",
    "woman_cartwheeling_light_skin_tone": "๐คธ๐ปโ",
    "woman_cartwheeling_tone2": "๐คธ๐ผโ",
    "woman_cartwheeling_medium_light_skin_tone": "๐คธ๐ผโ",
    "woman_cartwheeling_tone3": "๐คธ๐ฝโ",
    "woman_cartwheeling_medium_skin_tone": "๐คธ๐ฝโ",
    "woman_cartwheeling_tone4": "๐คธ๐พโ",
    "woman_cartwheeling_medium_dark_skin_tone": "๐คธ๐พโ",
    "woman_cartwheeling_tone5": "๐คธ๐ฟโ",
    "woman_cartwheeling_dark_skin_tone": "๐คธ๐ฟโ",
    "man_cartwheeling": "๐คธโ",
    "man_cartwheeling_tone1": "๐คธ๐ปโ",
    "man_cartwheeling_light_skin_tone": "๐คธ๐ปโ",
    "man_cartwheeling_tone2": "๐คธ๐ผโ",
    "man_cartwheeling_medium_light_skin_tone": "๐คธ๐ผโ",
    "man_cartwheeling_tone3": "๐คธ๐ฝโ",
    "man_cartwheeling_medium_skin_tone": "๐คธ๐ฝโ",
    "man_cartwheeling_tone4": "๐คธ๐พโ",
    "man_cartwheeling_medium_dark_skin_tone": "๐คธ๐พโ",
    "man_cartwheeling_tone5": "๐คธ๐ฟโ",
    "man_cartwheeling_dark_skin_tone": "๐คธ๐ฟโ",
    "person_bouncing_ball": "โน",
    "basketball_player": "โน",
    "person_with_ball": "โน",
    "person_bouncing_ball_tone1": "โน๐ป",
    "basketball_player_tone1": "โน๐ป",
    "person_with_ball_tone1": "โน๐ป",
    "person_bouncing_ball_tone2": "โน๐ผ",
    "basketball_player_tone2": "โน๐ผ",
    "person_with_ball_tone2": "โน๐ผ",
    "person_bouncing_ball_tone3": "โน๐ฝ",
    "basketball_player_tone3": "โน๐ฝ",
    "person_with_ball_tone3": "โน๐ฝ",
    "person_bouncing_ball_tone4": "โน๐พ",
    "basketball_player_tone4": "โน๐พ",
    "person_with_ball_tone4": "โน๐พ",
    "person_bouncing_ball_tone5": "โน๐ฟ",
    "basketball_player_tone5": "โน๐ฟ",
    "person_with_ball_tone5": "โน๐ฟ",
    "woman_bouncing_ball": "โนโ",
    "woman_bouncing_ball_tone1": "โน๐ปโ",
    "woman_bouncing_ball_light_skin_tone": "โน๐ปโ",
    "woman_bouncing_ball_tone2": "โน๐ผโ",
    "woman_bouncing_ball_medium_light_skin_tone": "โน๐ผโ",
    "woman_bouncing_ball_tone3": "โน๐ฝโ",
    "woman_bouncing_ball_medium_skin_tone": "โน๐ฝโ",
    "woman_bouncing_ball_tone4": "โน๐พโ",
    "woman_bouncing_ball_medium_dark_skin_tone": "โน๐พโ",
    "woman_bouncing_ball_tone5": "โน๐ฟโ",
    "woman_bouncing_ball_dark_skin_tone": "โน๐ฟโ",
    "man_bouncing_ball": "โนโ",
    "man_bouncing_ball_tone1": "โน๐ปโ",
    "man_bouncing_ball_light_skin_tone": "โน๐ปโ",
    "man_bouncing_ball_tone2": "โน๐ผโ",
    "man_bouncing_ball_medium_light_skin_tone": "โน๐ผโ",
    "man_bouncing_ball_tone3": "โน๐ฝโ",
    "man_bouncing_ball_medium_skin_tone": "โน๐ฝโ",
    "man_bouncing_ball_tone4": "โน๐พโ",
    "man_bouncing_ball_medium_dark_skin_tone": "โน๐พโ",
    "man_bouncing_ball_tone5": "โน๐ฟโ",
    "man_bouncing_ball_dark_skin_tone": "โน๐ฟโ",
    "person_fencing": "๐คบ",
    "fencer": "๐คบ",
    "fencing": "๐คบ",
    "person_playing_handball": "๐คพ",
    "handball": "๐คพ",
    "person_playing_handball_tone1": "๐คพ๐ป",
    "handball_tone1": "๐คพ๐ป",
    "person_playing_handball_tone2": "๐คพ๐ผ",
    "handball_tone2": "๐คพ๐ผ",
    "person_playing_handball_tone3": "๐คพ๐ฝ",
    "handball_tone3": "๐คพ๐ฝ",
    "person_playing_handball_tone4": "๐คพ๐พ",
    "handball_tone4": "๐คพ๐พ",
    "person_playing_handball_tone5": "๐คพ๐ฟ",
    "handball_tone5": "๐คพ๐ฟ",
    "woman_playing_handball": "๐คพโ",
    "woman_playing_handball_tone1": "๐คพ๐ปโ",
    "woman_playing_handball_light_skin_tone": "๐คพ๐ปโ",
    "woman_playing_handball_tone2": "๐คพ๐ผโ",
    "woman_playing_handball_medium_light_skin_tone": "๐คพ๐ผโ",
    "woman_playing_handball_tone3": "๐คพ๐ฝโ",
    "woman_playing_handball_medium_skin_tone": "๐คพ๐ฝโ",
    "woman_playing_handball_tone4": "๐คพ๐พโ",
    "woman_playing_handball_medium_dark_skin_tone": "๐คพ๐พโ",
    "woman_playing_handball_tone5": "๐คพ๐ฟโ",
    "woman_playing_handball_dark_skin_tone": "๐คพ๐ฟโ",
    "man_playing_handball": "๐คพโ",
    "man_playing_handball_tone1": "๐คพ๐ปโ",
    "man_playing_handball_light_skin_tone": "๐คพ๐ปโ",
    "man_playing_handball_tone2": "๐คพ๐ผโ",
    "man_playing_handball_medium_light_skin_tone": "๐คพ๐ผโ",
    "man_playing_handball_tone3": "๐คพ๐ฝโ",
    "man_playing_handball_medium_skin_tone": "๐คพ๐ฝโ",
    "man_playing_handball_tone4": "๐คพ๐พโ",
    "man_playing_handball_medium_dark_skin_tone": "๐คพ๐พโ",
    "man_playing_handball_tone5": "๐คพ๐ฟโ",
    "man_playing_handball_dark_skin_tone": "๐คพ๐ฟโ",
    "person_golfing": "๐",
    "golfer": "๐",
    "person_golfing_tone1": "๐๐ป",
    "person_golfing_light_skin_tone": "๐๐ป",
    "person_golfing_tone2": "๐๐ผ",
    "person_golfing_medium_light_skin_tone": "๐๐ผ",
    "person_golfing_tone3": "๐๐ฝ",
    "person_golfing_medium_skin_tone": "๐๐ฝ",
    "person_golfing_tone4": "๐๐พ",
    "person_golfing_medium_dark_skin_tone": "๐๐พ",
    "person_golfing_tone5": "๐๐ฟ",
    "person_golfing_dark_skin_tone": "๐๐ฟ",
    "woman_golfing": "๐โ",
    "woman_golfing_tone1": "๐๐ปโ",
    "woman_golfing_light_skin_tone": "๐๐ปโ",
    "woman_golfing_tone2": "๐๐ผโ",
    "woman_golfing_medium_light_skin_tone": "๐๐ผโ",
    "woman_golfing_tone3": "๐๐ฝโ",
    "woman_golfing_medium_skin_tone": "๐๐ฝโ",
    "woman_golfing_tone4": "๐๐พโ",
    "woman_golfing_medium_dark_skin_tone": "๐๐พโ",
    "woman_golfing_tone5": "๐๐ฟโ",
    "woman_golfing_dark_skin_tone": "๐๐ฟโ",
    "man_golfing": "๐โ",
    "man_golfing_tone1": "๐๐ปโ",
    "man_golfing_light_skin_tone": "๐๐ปโ",
    "man_golfing_tone2": "๐๐ผโ",
    "man_golfing_medium_light_skin_tone": "๐๐ผโ",
    "man_golfing_tone3": "๐๐ฝโ",
    "man_golfing_medium_skin_tone": "๐๐ฝโ",
    "man_golfing_tone4": "๐๐พโ",
    "man_golfing_medium_dark_skin_tone": "๐๐พโ",
    "man_golfing_tone5": "๐๐ฟโ",
    "man_golfing_dark_skin_tone": "๐๐ฟโ",
    "horse_racing": "๐",
    "horse_racing_tone1": "๐๐ป",
    "horse_racing_tone2": "๐๐ผ",
    "horse_racing_tone3": "๐๐ฝ",
    "horse_racing_tone4": "๐๐พ",
    "horse_racing_tone5": "๐๐ฟ",
    "person_in_lotus_position": "๐ง",
    "person_in_lotus_position_tone1": "๐ง๐ป",
    "person_in_lotus_position_light_skin_tone": "๐ง๐ป",
    "person_in_lotus_position_tone2": "๐ง๐ผ",
    "person_in_lotus_position_medium_light_skin_tone": "๐ง๐ผ",
    "person_in_lotus_position_tone3": "๐ง๐ฝ",
    "person_in_lotus_position_medium_skin_tone": "๐ง๐ฝ",
    "person_in_lotus_position_tone4": "๐ง๐พ",
    "person_in_lotus_position_medium_dark_skin_tone": "๐ง๐พ",
    "person_in_lotus_position_tone5": "๐ง๐ฟ",
    "person_in_lotus_position_dark_skin_tone": "๐ง๐ฟ",
    "woman_in_lotus_position": "๐งโ",
    "woman_in_lotus_position_tone1": "๐ง๐ปโ",
    "woman_in_lotus_position_light_skin_tone": "๐ง๐ปโ",
    "woman_in_lotus_position_tone2": "๐ง๐ผโ",
    "woman_in_lotus_position_medium_light_skin_tone": "๐ง๐ผโ",
    "woman_in_lotus_position_tone3": "๐ง๐ฝโ",
    "woman_in_lotus_position_medium_skin_tone": "๐ง๐ฝโ",
    "woman_in_lotus_position_tone4": "๐ง๐พโ",
    "woman_in_lotus_position_medium_dark_skin_tone": "๐ง๐พโ",
    "woman_in_lotus_position_tone5": "๐ง๐ฟโ",
    "woman_in_lotus_position_dark_skin_tone": "๐ง๐ฟโ",
    "man_in_lotus_position": "๐งโ",
    "man_in_lotus_position_tone1": "๐ง๐ปโ",
    "man_in_lotus_position_light_skin_tone": "๐ง๐ปโ",
    "man_in_lotus_position_tone2": "๐ง๐ผโ",
    "man_in_lotus_position_medium_light_skin_tone": "๐ง๐ผโ",
    "man_in_lotus_position_tone3": "๐ง๐ฝโ",
    "man_in_lotus_position_medium_skin_tone": "๐ง๐ฝโ",
    "man_in_lotus_position_tone4": "๐ง๐พโ",
    "man_in_lotus_position_medium_dark_skin_tone": "๐ง๐พโ",
    "man_in_lotus_position_tone5": "๐ง๐ฟโ",
    "man_in_lotus_position_dark_skin_tone": "๐ง๐ฟโ",
    "person_surfing": "๐",
    "surfer": "๐",
    "person_surfing_tone1": "๐๐ป",
    "surfer_tone1": "๐๐ป",
    "person_surfing_tone2": "๐๐ผ",
    "surfer_tone2": "๐๐ผ",
    "person_surfing_tone3": "๐๐ฝ",
    "surfer_tone3": "๐๐ฝ",
    "person_surfing_tone4": "๐๐พ",
    "surfer_tone4": "๐๐พ",
    "person_surfing_tone5": "๐๐ฟ",
    "surfer_tone5": "๐๐ฟ",
    "woman_surfing": "๐โ",
    "woman_surfing_tone1": "๐๐ปโ",
    "woman_surfing_light_skin_tone": "๐๐ปโ",
    "woman_surfing_tone2": "๐๐ผโ",
    "woman_surfing_medium_light_skin_tone": "๐๐ผโ",
    "woman_surfing_tone3": "๐๐ฝโ",
    "woman_surfing_medium_skin_tone": "๐๐ฝโ",
    "woman_surfing_tone4": "๐๐พโ",
    "woman_surfing_medium_dark_skin_tone": "๐๐พโ",
    "woman_surfing_tone5": "๐๐ฟโ",
    "woman_surfing_dark_skin_tone": "๐๐ฟโ",
    "man_surfing": "๐โ",
    "man_surfing_tone1": "๐๐ปโ",
    "man_surfing_light_skin_tone": "๐๐ปโ",
    "man_surfing_tone2": "๐๐ผโ",
    "man_surfing_medium_light_skin_tone": "๐๐ผโ",
    "man_surfing_tone3": "๐๐ฝโ",
    "man_surfing_medium_skin_tone": "๐๐ฝโ",
    "man_surfing_tone4": "๐๐พโ",
    "man_surfing_medium_dark_skin_tone": "๐๐พโ",
    "man_surfing_tone5": "๐๐ฟโ",
    "man_surfing_dark_skin_tone": "๐๐ฟโ",
    "person_swimming": "๐",
    "swimmer": "๐",
    "person_swimming_tone1": "๐๐ป",
    "swimmer_tone1": "๐๐ป",
    "person_swimming_tone2": "๐๐ผ",
    "swimmer_tone2": "๐๐ผ",
    "person_swimming_tone3": "๐๐ฝ",
    "swimmer_tone3": "๐๐ฝ",
    "person_swimming_tone4": "๐๐พ",
    "swimmer_tone4": "๐๐พ",
    "person_swimming_tone5": "๐๐ฟ",
    "swimmer_tone5": "๐๐ฟ",
    "woman_swimming": "๐โ",
    "woman_swimming_tone1": "๐๐ปโ",
    "woman_swimming_light_skin_tone": "๐๐ปโ",
    "woman_swimming_tone2": "๐๐ผโ",
    "woman_swimming_medium_light_skin_tone": "๐๐ผโ",
    "woman_swimming_tone3": "๐๐ฝโ",
    "woman_swimming_medium_skin_tone": "๐๐ฝโ",
    "woman_swimming_tone4": "๐๐พโ",
    "woman_swimming_medium_dark_skin_tone": "๐๐พโ",
    "woman_swimming_tone5": "๐๐ฟโ",
    "woman_swimming_dark_skin_tone": "๐๐ฟโ",
    "man_swimming": "๐โ",
    "man_swimming_tone1": "๐๐ปโ",
    "man_swimming_light_skin_tone": "๐๐ปโ",
    "man_swimming_tone2": "๐๐ผโ",
    "man_swimming_medium_light_skin_tone": "๐๐ผโ",
    "man_swimming_tone3": "๐๐ฝโ",
    "man_swimming_medium_skin_tone": "๐๐ฝโ",
    "man_swimming_tone4": "๐๐พโ",
    "man_swimming_medium_dark_skin_tone": "๐๐พโ",
    "man_swimming_tone5": "๐๐ฟโ",
    "man_swimming_dark_skin_tone": "๐๐ฟโ",
    "person_playing_water_polo": "๐คฝ",
    "water_polo": "๐คฝ",
    "person_playing_water_polo_tone1": "๐คฝ๐ป",
    "water_polo_tone1": "๐คฝ๐ป",
    "person_playing_water_polo_tone2": "๐คฝ๐ผ",
    "water_polo_tone2": "๐คฝ๐ผ",
    "person_playing_water_polo_tone3": "๐คฝ๐ฝ",
    "water_polo_tone3": "๐คฝ๐ฝ",
    "person_playing_water_polo_tone4": "๐คฝ๐พ",
    "water_polo_tone4": "๐คฝ๐พ",
    "person_playing_water_polo_tone5": "๐คฝ๐ฟ",
    "water_polo_tone5": "๐คฝ๐ฟ",
    "woman_playing_water_polo": "๐คฝโ",
    "woman_playing_water_polo_tone1": "๐คฝ๐ปโ",
    "woman_playing_water_polo_light_skin_tone": "๐คฝ๐ปโ",
    "woman_playing_water_polo_tone2": "๐คฝ๐ผโ",
    "woman_playing_water_polo_medium_light_skin_tone": "๐คฝ๐ผโ",
    "woman_playing_water_polo_tone3": "๐คฝ๐ฝโ",
    "woman_playing_water_polo_medium_skin_tone": "๐คฝ๐ฝโ",
    "woman_playing_water_polo_tone4": "๐คฝ๐พโ",
    "woman_playing_water_polo_medium_dark_skin_tone": "๐คฝ๐พโ",
    "woman_playing_water_polo_tone5": "๐คฝ๐ฟโ",
    "woman_playing_water_polo_dark_skin_tone": "๐คฝ๐ฟโ",
    "man_playing_water_polo": "๐คฝโ",
    "man_playing_water_polo_tone1": "๐คฝ๐ปโ",
    "man_playing_water_polo_light_skin_tone": "๐คฝ๐ปโ",
    "man_playing_water_polo_tone2": "๐คฝ๐ผโ",
    "man_playing_water_polo_medium_light_skin_tone": "๐คฝ๐ผโ",
    "man_playing_water_polo_tone3": "๐คฝ๐ฝโ",
    "man_playing_water_polo_medium_skin_tone": "๐คฝ๐ฝโ",
    "man_playing_water_polo_tone4": "๐คฝ๐พโ",
    "man_playing_water_polo_medium_dark_skin_tone": "๐คฝ๐พโ",
    "man_playing_water_polo_tone5": "๐คฝ๐ฟโ",
    "man_playing_water_polo_dark_skin_tone": "๐คฝ๐ฟโ",
    "person_rowing_boat": "๐ฃ",
    "rowboat": "๐ฃ",
    "person_rowing_boat_tone1": "๐ฃ๐ป",
    "rowboat_tone1": "๐ฃ๐ป",
    "person_rowing_boat_tone2": "๐ฃ๐ผ",
    "rowboat_tone2": "๐ฃ๐ผ",
    "person_rowing_boat_tone3": "๐ฃ๐ฝ",
    "rowboat_tone3": "๐ฃ๐ฝ",
    "person_rowing_boat_tone4": "๐ฃ๐พ",
    "rowboat_tone4": "๐ฃ๐พ",
    "person_rowing_boat_tone5": "๐ฃ๐ฟ",
    "rowboat_tone5": "๐ฃ๐ฟ",
    "woman_rowing_boat": "๐ฃโ",
    "woman_rowing_boat_tone1": "๐ฃ๐ปโ",
    "woman_rowing_boat_light_skin_tone": "๐ฃ๐ปโ",
    "woman_rowing_boat_tone2": "๐ฃ๐ผโ",
    "woman_rowing_boat_medium_light_skin_tone": "๐ฃ๐ผโ",
    "woman_rowing_boat_tone3": "๐ฃ๐ฝโ",
    "woman_rowing_boat_medium_skin_tone": "๐ฃ๐ฝโ",
    "woman_rowing_boat_tone4": "๐ฃ๐พโ",
    "woman_rowing_boat_medium_dark_skin_tone": "๐ฃ๐พโ",
    "woman_rowing_boat_tone5": "๐ฃ๐ฟโ",
    "woman_rowing_boat_dark_skin_tone": "๐ฃ๐ฟโ",
    "man_rowing_boat": "๐ฃโ",
    "man_rowing_boat_tone1": "๐ฃ๐ปโ",
    "man_rowing_boat_light_skin_tone": "๐ฃ๐ปโ",
    "man_rowing_boat_tone2": "๐ฃ๐ผโ",
    "man_rowing_boat_medium_light_skin_tone": "๐ฃ๐ผโ",
    "man_rowing_boat_tone3": "๐ฃ๐ฝโ",
    "man_rowing_boat_medium_skin_tone": "๐ฃ๐ฝโ",
    "man_rowing_boat_tone4": "๐ฃ๐พโ",
    "man_rowing_boat_medium_dark_skin_tone": "๐ฃ๐พโ",
    "man_rowing_boat_tone5": "๐ฃ๐ฟโ",
    "man_rowing_boat_dark_skin_tone": "๐ฃ๐ฟโ",
    "person_climbing": "๐ง",
    "person_climbing_tone1": "๐ง๐ป",
    "person_climbing_light_skin_tone": "๐ง๐ป",
    "person_climbing_tone2": "๐ง๐ผ",
    "person_climbing_medium_light_skin_tone": "๐ง๐ผ",
    "person_climbing_tone3": "๐ง๐ฝ",
    "person_climbing_medium_skin_tone": "๐ง๐ฝ",
    "person_climbing_tone4": "๐ง๐พ",
    "person_climbing_medium_dark_skin_tone": "๐ง๐พ",
    "person_climbing_tone5": "๐ง๐ฟ",
    "person_climbing_dark_skin_tone": "๐ง๐ฟ",
    "woman_climbing": "๐งโ",
    "woman_climbing_tone1": "๐ง๐ปโ",
    "woman_climbing_light_skin_tone": "๐ง๐ปโ",
    "woman_climbing_tone2": "๐ง๐ผโ",
    "woman_climbing_medium_light_skin_tone": "๐ง๐ผโ",
    "woman_climbing_tone3": "๐ง๐ฝโ",
    "woman_climbing_medium_skin_tone": "๐ง๐ฝโ",
    "woman_climbing_tone4": "๐ง๐พโ",
    "woman_climbing_medium_dark_skin_tone": "๐ง๐พโ",
    "woman_climbing_tone5": "๐ง๐ฟโ",
    "woman_climbing_dark_skin_tone": "๐ง๐ฟโ",
    "man_climbing": "๐งโ",
    "man_climbing_tone1": "๐ง๐ปโ",
    "man_climbing_light_skin_tone": "๐ง๐ปโ",
    "man_climbing_tone2": "๐ง๐ผโ",
    "man_climbing_medium_light_skin_tone": "๐ง๐ผโ",
    "man_climbing_tone3": "๐ง๐ฝโ",
    "man_climbing_medium_skin_tone": "๐ง๐ฝโ",
    "man_climbing_tone4": "๐ง๐พโ",
    "man_climbing_medium_dark_skin_tone": "๐ง๐พโ",
    "man_climbing_tone5": "๐ง๐ฟโ",
    "man_climbing_dark_skin_tone": "๐ง๐ฟโ",
    "person_mountain_biking": "๐ต",
    "mountain_bicyclist": "๐ต",
    "person_mountain_biking_tone1": "๐ต๐ป",
    "mountain_bicyclist_tone1": "๐ต๐ป",
    "person_mountain_biking_tone2": "๐ต๐ผ",
    "mountain_bicyclist_tone2": "๐ต๐ผ",
    "person_mountain_biking_tone3": "๐ต๐ฝ",
    "mountain_bicyclist_tone3": "๐ต๐ฝ",
    "person_mountain_biking_tone4": "๐ต๐พ",
    "mountain_bicyclist_tone4": "๐ต๐พ",
    "person_mountain_biking_tone5": "๐ต๐ฟ",
    "mountain_bicyclist_tone5": "๐ต๐ฟ",
    "woman_mountain_biking": "๐ตโ",
    "woman_mountain_biking_tone1": "๐ต๐ปโ",
    "woman_mountain_biking_light_skin_tone": "๐ต๐ปโ",
    "woman_mountain_biking_tone2": "๐ต๐ผโ",
    "woman_mountain_biking_medium_light_skin_tone": "๐ต๐ผโ",
    "woman_mountain_biking_tone3": "๐ต๐ฝโ",
    "woman_mountain_biking_medium_skin_tone": "๐ต๐ฝโ",
    "woman_mountain_biking_tone4": "๐ต๐พโ",
    "woman_mountain_biking_medium_dark_skin_tone": "๐ต๐พโ",
    "woman_mountain_biking_tone5": "๐ต๐ฟโ",
    "woman_mountain_biking_dark_skin_tone": "๐ต๐ฟโ",
    "man_mountain_biking": "๐ตโ",
    "man_mountain_biking_tone1": "๐ต๐ปโ",
    "man_mountain_biking_light_skin_tone": "๐ต๐ปโ",
    "man_mountain_biking_tone2": "๐ต๐ผโ",
    "man_mountain_biking_medium_light_skin_tone": "๐ต๐ผโ",
    "man_mountain_biking_tone3": "๐ต๐ฝโ",
    "man_mountain_biking_medium_skin_tone": "๐ต๐ฝโ",
    "man_mountain_biking_tone4": "๐ต๐พโ",
    "man_mountain_biking_medium_dark_skin_tone": "๐ต๐พโ",
    "man_mountain_biking_tone5": "๐ต๐ฟโ",
    "man_mountain_biking_dark_skin_tone": "๐ต๐ฟโ",
    "person_biking": "๐ด",
    "bicyclist": "๐ด",
    "person_biking_tone1": "๐ด๐ป",
    "bicyclist_tone1": "๐ด๐ป",
    "person_biking_tone2": "๐ด๐ผ",
    "bicyclist_tone2": "๐ด๐ผ",
    "person_biking_tone3": "๐ด๐ฝ",
    "bicyclist_tone3": "๐ด๐ฝ",
    "person_biking_tone4": "๐ด๐พ",
    "bicyclist_tone4": "๐ด๐พ",
    "person_biking_tone5": "๐ด๐ฟ",
    "bicyclist_tone5": "๐ด๐ฟ",
    "woman_biking": "๐ดโ",
    "woman_biking_tone1": "๐ด๐ปโ",
    "woman_biking_light_skin_tone": "๐ด๐ปโ",
    "woman_biking_tone2": "๐ด๐ผโ",
    "woman_biking_medium_light_skin_tone": "๐ด๐ผโ",
    "woman_biking_tone3": "๐ด๐ฝโ",
    "woman_biking_medium_skin_tone": "๐ด๐ฝโ",
    "woman_biking_tone4": "๐ด๐พโ",
    "woman_biking_medium_dark_skin_tone": "๐ด๐พโ",
    "woman_biking_tone5": "๐ด๐ฟโ",
    "woman_biking_dark_skin_tone": "๐ด๐ฟโ",
    "man_biking": "๐ดโ",
    "man_biking_tone1": "๐ด๐ปโ",
    "man_biking_light_skin_tone": "๐ด๐ปโ",
    "man_biking_tone2": "๐ด๐ผโ",
    "man_biking_medium_light_skin_tone": "๐ด๐ผโ",
    "man_biking_tone3": "๐ด๐ฝโ",
    "man_biking_medium_skin_tone": "๐ด๐ฝโ",
    "man_biking_tone4": "๐ด๐พโ",
    "man_biking_medium_dark_skin_tone": "๐ด๐พโ",
    "man_biking_tone5": "๐ด๐ฟโ",
    "man_biking_dark_skin_tone": "๐ด๐ฟโ",
    "trophy": "๐",
    "first_place": "๐ฅ",
    "first_place_medal": "๐ฅ",
    "second_place": "๐ฅ",
    "second_place_medal": "๐ฅ",
    "third_place": "๐ฅ",
    "third_place_medal": "๐ฅ",
    "medal": "๐",
    "sports_medal": "๐",
    "military_medal": "๐",
    "rosette": "๐ต",
    "reminder_ribbon": "๐",
    "ticket": "๐ซ",
    "tickets": "๐",
    "admission_tickets": "๐",
    "circus_tent": "๐ช",
    "person_juggling": "๐คน",
    "juggling": "๐คน",
    "juggler": "๐คน",
    "person_juggling_tone1": "๐คน๐ป",
    "juggling_tone1": "๐คน๐ป",
    "juggler_tone1": "๐คน๐ป",
    "person_juggling_tone2": "๐คน๐ผ",
    "juggling_tone2": "๐คน๐ผ",
    "juggler_tone2": "๐คน๐ผ",
    "person_juggling_tone3": "๐คน๐ฝ",
    "juggling_tone3": "๐คน๐ฝ",
    "juggler_tone3": "๐คน๐ฝ",
    "person_juggling_tone4": "๐คน๐พ",
    "juggling_tone4": "๐คน๐พ",
    "juggler_tone4": "๐คน๐พ",
    "person_juggling_tone5": "๐คน๐ฟ",
    "juggling_tone5": "๐คน๐ฟ",
    "juggler_tone5": "๐คน๐ฟ",
    "woman_juggling": "๐คนโ",
    "woman_juggling_tone1": "๐คน๐ปโ",
    "woman_juggling_light_skin_tone": "๐คน๐ปโ",
    "woman_juggling_tone2": "๐คน๐ผโ",
    "woman_juggling_medium_light_skin_tone": "๐คน๐ผโ",
    "woman_juggling_tone3": "๐คน๐ฝโ",
    "woman_juggling_medium_skin_tone": "๐คน๐ฝโ",
    "woman_juggling_tone4": "๐คน๐พโ",
    "woman_juggling_medium_dark_skin_tone": "๐คน๐พโ",
    "woman_juggling_tone5": "๐คน๐ฟโ",
    "woman_juggling_dark_skin_tone": "๐คน๐ฟโ",
    "man_juggling": "๐คนโ",
    "man_juggling_tone1": "๐คน๐ปโ",
    "man_juggling_light_skin_tone": "๐คน๐ปโ",
    "man_juggling_tone2": "๐คน๐ผโ",
    "man_juggling_medium_light_skin_tone": "๐คน๐ผโ",
    "man_juggling_tone3": "๐คน๐ฝโ",
    "man_juggling_medium_skin_tone": "๐คน๐ฝโ",
    "man_juggling_tone4": "๐คน๐พโ",
    "man_juggling_medium_dark_skin_tone": "๐คน๐พโ",
    "man_juggling_tone5": "๐คน๐ฟโ",
    "man_juggling_dark_skin_tone": "๐คน๐ฟโ",
    "performing_arts": "๐ญ",
    "art": "๐จ",
    "clapper": "๐ฌ",
    "microphone": "๐ค",
    "headphones": "๐ง",
    "musical_score": "๐ผ",
    "musical_keyboard": "๐น",
    "drum": "๐ฅ",
    "drum_with_drumsticks": "๐ฅ",
    "saxophone": "๐ท",
    "trumpet": "๐บ",
    "banjo": "๐ช",
    "guitar": "๐ธ",
    "violin": "๐ป",
    "game_die": "๐ฒ",
    "chess_pawn": "โ",
    "dart": "๐ฏ",
    "kite": "๐ช",
    "yo_yo": "๐ช",
    "bowling": "๐ณ",
    "video_game": "๐ฎ",
    "slot_machine": "๐ฐ",
    "jigsaw": "๐งฉ",
    "red_car": "๐",
    "taxi": "๐",
    "blue_car": "๐",
    "bus": "๐",
    "trolleybus": "๐",
    "race_car": "๐",
    "racing_car": "๐",
    "police_car": "๐",
    "ambulance": "๐",
    "fire_engine": "๐",
    "minibus": "๐",
    "truck": "๐",
    "articulated_lorry": "๐",
    "tractor": "๐",
    "auto_rickshaw": "๐บ",
    "motor_scooter": "๐ต",
    "motorbike": "๐ต",
    "motorcycle": "๐",
    "racing_motorcycle": "๐",
    "scooter": "๐ด",
    "bike": "๐ฒ",
    "motorized_wheelchair": "๐ฆผ",
    "manual_wheelchair": "๐ฆฝ",
    "rotating_light": "๐จ",
    "oncoming_police_car": "๐",
    "oncoming_bus": "๐",
    "oncoming_automobile": "๐",
    "oncoming_taxi": "๐",
    "aerial_tramway": "๐ก",
    "mountain_cableway": "๐ ",
    "suspension_railway": "๐",
    "railway_car": "๐",
    "train": "๐",
    "mountain_railway": "๐",
    "monorail": "๐",
    "bullettrain_side": "๐",
    "bullettrain_front": "๐",
    "light_rail": "๐",
    "steam_locomotive": "๐",
    "train2": "๐",
    "metro": "๐",
    "tram": "๐",
    "station": "๐",
    "airplane": "โ",
    "airplane_departure": "๐ซ",
    "airplane_arriving": "๐ฌ",
    "airplane_small": "๐ฉ",
    "small_airplane": "๐ฉ",
    "seat": "๐บ",
    "satellite_orbital": "๐ฐ",
    "rocket": "๐",
    "flying_saucer": "๐ธ",
    "helicopter": "๐",
    "canoe": "๐ถ",
    "kayak": "๐ถ",
    "sailboat": "โต",
    "speedboat": "๐ค",
    "motorboat": "๐ฅ",
    "cruise_ship": "๐ณ",
    "passenger_ship": "๐ณ",
    "ferry": "โด",
    "ship": "๐ข",
    "anchor": "โ",
    "fuelpump": "โฝ",
    "construction": "๐ง",
    "vertical_traffic_light": "๐ฆ",
    "traffic_light": "๐ฅ",
    "busstop": "๐",
    "map": "๐บ",
    "world_map": "๐บ",
    "moyai": "๐ฟ",
    "statue_of_liberty": "๐ฝ",
    "tokyo_tower": "๐ผ",
    "european_castle": "๐ฐ",
    "japanese_castle": "๐ฏ",
    "stadium": "๐",
    "ferris_wheel": "๐ก",
    "roller_coaster": "๐ข",
    "carousel_horse": "๐ ",
    "fountain": "โฒ",
    "beach_umbrella": "โฑ",
    "umbrella_on_ground": "โฑ",
    "beach": "๐",
    "beach_with_umbrella": "๐",
    "island": "๐",
    "desert_island": "๐",
    "desert": "๐",
    "volcano": "๐",
    "mountain": "โฐ",
    "mountain_snow": "๐",
    "snow_capped_mountain": "๐",
    "mount_fuji": "๐ป",
    "camping": "๐",
    "tent": "โบ",
    "house": "๐ ",
    "house_with_garden": "๐ก",
    "homes": "๐",
    "house_buildings": "๐",
    "house_abandoned": "๐",
    "derelict_house_building": "๐",
    "construction_site": "๐",
    "building_construction": "๐",
    "factory": "๐ญ",
    "office": "๐ข",
    "department_store": "๐ฌ",
    "post_office": "๐ฃ",
    "european_post_office": "๐ค",
    "hospital": "๐ฅ",
    "bank": "๐ฆ",
    "hotel": "๐จ",
    "convenience_store": "๐ช",
    "school": "๐ซ",
    "love_hotel": "๐ฉ",
    "wedding": "๐",
    "classical_building": "๐",
    "church": "โช",
    "mosque": "๐",
    "hindu_temple": "๐",
    "synagogue": "๐",
    "kaaba": "๐",
    "shinto_shrine": "โฉ",
    "railway_track": "๐ค",
    "railroad_track": "๐ค",
    "motorway": "๐ฃ",
    "japan": "๐พ",
    "rice_scene": "๐",
    "park": "๐",
    "national_park": "๐",
    "sunrise": "๐",
    "sunrise_over_mountains": "๐",
    "stars": "๐ ",
    "sparkler": "๐",
    "fireworks": "๐",
    "city_sunset": "๐",
    "city_sunrise": "๐",
    "city_dusk": "๐",
    "cityscape": "๐",
    "night_with_stars": "๐",
    "milky_way": "๐",
    "bridge_at_night": "๐",
    "foggy": "๐",
    "watch": "โ",
    "iphone": "๐ฑ",
    "calling": "๐ฒ",
    "computer": "๐ป",
    "keyboard": "โจ",
    "desktop": "๐ฅ",
    "desktop_computer": "๐ฅ",
    "printer": "๐จ",
    "mouse_three_button": "๐ฑ",
    "three_button_mouse": "๐ฑ",
    "trackball": "๐ฒ",
    "joystick": "๐น",
    "compression": "๐",
    "minidisc": "๐ฝ",
    "floppy_disk": "๐พ",
    "cd": "๐ฟ",
    "dvd": "๐",
    "vhs": "๐ผ",
    "camera": "๐ท",
    "camera_with_flash": "๐ธ",
    "video_camera": "๐น",
    "movie_camera": "๐ฅ",
    "projector": "๐ฝ",
    "film_projector": "๐ฝ",
    "film_frames": "๐",
    "telephone_receiver": "๐",
    "telephone": "โ",
    "pager": "๐",
    "fax": "๐ ",
    "tv": "๐บ",
    "radio": "๐ป",
    "microphone2": "๐",
    "studio_microphone": "๐",
    "level_slider": "๐",
    "control_knobs": "๐",
    "compass": "๐งญ",
    "stopwatch": "โฑ",
    "timer": "โฒ",
    "timer_clock": "โฒ",
    "alarm_clock": "โฐ",
    "clock": "๐ฐ",
    "mantlepiece_clock": "๐ฐ",
    "hourglass": "โ",
    "hourglass_flowing_sand": "โณ",
    "satellite": "๐ก",
    "battery": "๐",
    "electric_plug": "๐",
    "bulb": "๐ก",
    "flashlight": "๐ฆ",
    "candle": "๐ฏ",
    "fire_extinguisher": "๐งฏ",
    "oil": "๐ข",
    "oil_drum": "๐ข",
    "money_with_wings": "๐ธ",
    "dollar": "๐ต",
    "yen": "๐ด",
    "euro": "๐ถ",
    "pound": "๐ท",
    "moneybag": "๐ฐ",
    "credit_card": "๐ณ",
    "gem": "๐",
    "scales": "โ",
    "toolbox": "๐งฐ",
    "wrench": "๐ง",
    "hammer": "๐จ",
    "hammer_pick": "โ",
    "hammer_and_pick": "โ",
    "tools": "๐ ",
    "hammer_and_wrench": "๐ ",
    "pick": "โ",
    "nut_and_bolt": "๐ฉ",
    "gear": "โ",
    "bricks": "๐งฑ",
    "chains": "โ",
    "magnet": "๐งฒ",
    "gun": "๐ซ",
    "bomb": "๐ฃ",
    "firecracker": "๐งจ",
    "axe": "๐ช",
    "razor": "๐ช",
    "knife": "๐ช",
    "dagger": "๐ก",
    "dagger_knife": "๐ก",
    "crossed_swords": "โ",
    "shield": "๐ก",
    "smoking": "๐ฌ",
    "coffin": "โฐ",
    "urn": "โฑ",
    "funeral_urn": "โฑ",
    "amphora": "๐บ",
    "diya_lamp": "๐ช",
    "crystal_ball": "๐ฎ",
    "prayer_beads": "๐ฟ",
    "nazar_amulet": "๐งฟ",
    "barber": "๐",
    "alembic": "โ",
    "telescope": "๐ญ",
    "microscope": "๐ฌ",
    "hole": "๐ณ",
    "probing_cane": "๐ฆฏ",
    "stethoscope": "๐ฉบ",
    "adhesive_bandage": "๐ฉน",
    "pill": "๐",
    "syringe": "๐",
    "drop_of_blood": "๐ฉธ",
    "dna": "๐งฌ",
    "microbe": "๐ฆ ",
    "petri_dish": "๐งซ",
    "test_tube": "๐งช",
    "thermometer": "๐ก",
    "chair": "๐ช",
    "broom": "๐งน",
    "basket": "๐งบ",
    "roll_of_paper": "๐งป",
    "toilet": "๐ฝ",
    "potable_water": "๐ฐ",
    "shower": "๐ฟ",
    "bathtub": "๐",
    "bath": "๐",
    "bath_tone1": "๐๐ป",
    "bath_tone2": "๐๐ผ",
    "bath_tone3": "๐๐ฝ",
    "bath_tone4": "๐๐พ",
    "bath_tone5": "๐๐ฟ",
    "soap": "๐งผ",
    "sponge": "๐งฝ",
    "squeeze_bottle": "๐งด",
    "bellhop": "๐",
    "bellhop_bell": "๐",
    "key": "๐",
    "key2": "๐",
    "old_key": "๐",
    "door": "๐ช",
    "couch": "๐",
    "couch_and_lamp": "๐",
    "bed": "๐",
    "sleeping_accommodation": "๐",
    "person_in_bed_tone1": "๐๐ป",
    "person_in_bed_light_skin_tone": "๐๐ป",
    "person_in_bed_tone2": "๐๐ผ",
    "person_in_bed_medium_light_skin_tone": "๐๐ผ",
    "person_in_bed_tone3": "๐๐ฝ",
    "person_in_bed_medium_skin_tone": "๐๐ฝ",
    "person_in_bed_tone4": "๐๐พ",
    "person_in_bed_medium_dark_skin_tone": "๐๐พ",
    "person_in_bed_tone5": "๐๐ฟ",
    "person_in_bed_dark_skin_tone": "๐๐ฟ",
    "teddy_bear": "๐งธ",
    "frame_photo": "๐ผ",
    "frame_with_picture": "๐ผ",
    "shopping_bags": "๐",
    "shopping_cart": "๐",
    "shopping_trolley": "๐",
    "gift": "๐",
    "balloon": "๐",
    "flags": "๐",
    "ribbon": "๐",
    "confetti_ball": "๐",
    "tada": "๐",
    "dolls": "๐",
    "izakaya_lantern": "๐ฎ",
    "wind_chime": "๐",
    "red_envelope": "๐งง",
    "envelope": "โ",
    "envelope_with_arrow": "๐ฉ",
    "incoming_envelope": "๐จ",
    "e_mail": "๐ง",
    "email": "๐ง",
    "love_letter": "๐",
    "inbox_tray": "๐ฅ",
    "outbox_tray": "๐ค",
    "package": "๐ฆ",
    "label": "๐ท",
    "mailbox_closed": "๐ช",
    "mailbox": "๐ซ",
    "mailbox_with_mail": "๐ฌ",
    "mailbox_with_no_mail": "๐ญ",
    "postbox": "๐ฎ",
    "postal_horn": "๐ฏ",
    "scroll": "๐",
    "page_with_curl": "๐",
    "page_facing_up": "๐",
    "bookmark_tabs": "๐",
    "receipt": "๐งพ",
    "bar_chart": "๐",
    "chart_with_upwards_trend": "๐",
    "chart_with_downwards_trend": "๐",
    "notepad_spiral": "๐",
    "spiral_note_pad": "๐",
    "calendar_spiral": "๐",
    "spiral_calendar_pad": "๐",
    "calendar": "๐",
    "date": "๐",
    "wastebasket": "๐",
    "card_index": "๐",
    "card_box": "๐",
    "card_file_box": "๐",
    "ballot_box": "๐ณ",
    "ballot_box_with_ballot": "๐ณ",
    "file_cabinet": "๐",
    "clipboard": "๐",
    "file_folder": "๐",
    "open_file_folder": "๐",
    "dividers": "๐",
    "card_index_dividers": "๐",
    "newspaper2": "๐",
    "rolled_up_newspaper": "๐",
    "newspaper": "๐ฐ",
    "notebook": "๐",
    "notebook_with_decorative_cover": "๐",
    "ledger": "๐",
    "closed_book": "๐",
    "green_book": "๐",
    "blue_book": "๐",
    "orange_book": "๐",
    "books": "๐",
    "book": "๐",
    "bookmark": "๐",
    "safety_pin": "๐งท",
    "link": "๐",
    "paperclip": "๐",
    "paperclips": "๐",
    "linked_paperclips": "๐",
    "triangular_ruler": "๐",
    "straight_ruler": "๐",
    "abacus": "๐งฎ",
    "pushpin": "๐",
    "round_pushpin": "๐",
    "scissors": "โ",
    "pen_ballpoint": "๐",
    "lower_left_ballpoint_pen": "๐",
    "pen_fountain": "๐",
    "lower_left_fountain_pen": "๐",
    "black_nib": "โ",
    "paintbrush": "๐",
    "lower_left_paintbrush": "๐",
    "crayon": "๐",
    "lower_left_crayon": "๐",
    "pencil": "๐",
    "memo": "๐",
    "pencil2": "โ",
    "mag": "๐",
    "mag_right": "๐",
    "lock_with_ink_pen": "๐",
    "closed_lock_with_key": "๐",
    "lock": "๐",
    "unlock": "๐",
    "heart": "โค",
    "orange_heart": "๐งก",
    "yellow_heart": "๐",
    "green_heart": "๐",
    "blue_heart": "๐",
    "purple_heart": "๐",
    "black_heart": "๐ค",
    "brown_heart": "๐ค",
    "white_heart": "๐ค",
    "broken_heart": "๐",
    "heart_exclamation": "โฃ",
    "heavy_heart_exclamation_mark_ornament": "โฃ",
    "two_hearts": "๐",
    "revolving_hearts": "๐",
    "heartbeat": "๐",
    "heartpulse": "๐",
    "sparkling_heart": "๐",
    "cupid": "๐",
    "gift_heart": "๐",
    "heart_decoration": "๐",
    "peace": "โฎ",
    "peace_symbol": "โฎ",
    "cross": "โ",
    "latin_cross": "โ",
    "star_and_crescent": "โช",
    "om_symbol": "๐",
    "wheel_of_dharma": "โธ",
    "star_of_david": "โก",
    "six_pointed_star": "๐ฏ",
    "menorah": "๐",
    "yin_yang": "โฏ",
    "orthodox_cross": "โฆ",
    "place_of_worship": "๐",
    "worship_symbol": "๐",
    "ophiuchus": "โ",
    "aries": "โ",
    "taurus": "โ",
    "gemini": "โ",
    "cancer": "โ",
    "leo": "โ",
    "virgo": "โ",
    "libra": "โ",
    "scorpius": "โ",
    "sagittarius": "โ",
    "capricorn": "โ",
    "aquarius": "โ",
    "pisces": "โ",
    "id": "๐",
    "atom": "โ",
    "atom_symbol": "โ",
    "accept": "๐",
    "radioactive": "โข",
    "radioactive_sign": "โข",
    "biohazard": "โฃ",
    "biohazard_sign": "โฃ",
    "mobile_phone_off": "๐ด",
    "vibration_mode": "๐ณ",
    "u6709": "๐ถ",
    "u7121": "๐",
    "u7533": "๐ธ",
    "u55b6": "๐บ",
    "u6708": "๐ท",
    "eight_pointed_black_star": "โด",
    "vs": "๐",
    "white_flower": "๐ฎ",
    "ideograph_advantage": "๐",
    "secret": "ใ",
    "congratulations": "ใ",
    "u6e80": "๐ต",
    "u5272": "๐น",
    "u7981": "๐ฒ",
    "a": "๐ฐ",
    "b": "๐ฑ",
    "ab": "๐",
    "cl": "๐",
    "o2": "๐พ",
    "sos": "๐",
    "x": "โ",
    "o": "โญ",
    "octagonal_sign": "๐",
    "stop_sign": "๐",
    "no_entry": "โ",
    "name_badge": "๐",
    "no_entry_sign": "๐ซ",
    "anger": "๐ข",
    "hotsprings": "โจ",
    "no_pedestrians": "๐ท",
    "do_not_litter": "๐ฏ",
    "no_bicycles": "๐ณ",
    "non_potable_water": "๐ฑ",
    "underage": "๐",
    "no_mobile_phones": "๐ต",
    "no_smoking": "๐ญ",
    "exclamation": "โ",
    "grey_exclamation": "โ",
    "question": "โ",
    "grey_question": "โ",
    "bangbang": "โผ",
    "interrobang": "โ",
    "low_brightness": "๐",
    "high_brightness": "๐",
    "part_alternation_mark": "ใฝ",
    "warning": "โ ",
    "children_crossing": "๐ธ",
    "trident": "๐ฑ",
    "fleur_de_lis": "โ",
    "beginner": "๐ฐ",
    "recycle": "โป",
    "white_check_mark": "โ",
    "u6307": "๐ฏ",
    "chart": "๐น",
    "sparkle": "โ",
    "eight_spoked_asterisk": "โณ",
    "negative_squared_cross_mark": "โ",
    "globe_with_meridians": "๐",
    "diamond_shape_with_a_dot_inside": "๐ ",
    "m": "โ",
    "cyclone": "๐",
    "zzz": "๐ค",
    "atm": "๐ง",
    "wc": "๐พ",
    "wheelchair": "โฟ",
    "parking": "๐ฟ",
    "u7a7a": "๐ณ",
    "sa": "๐",
    "customs": "๐",
    "baggage_claim": "๐",
    "left_luggage": "๐",
    "mens": "๐น",
    "womens": "๐บ",
    "baby_symbol": "๐ผ",
    "restroom": "๐ป",
    "put_litter_in_its_place": "๐ฎ",
    "cinema": "๐ฆ",
    "signal_strength": "๐ถ",
    "koko": "๐",
    "symbols": "๐ฃ",
    "information_source": "โน",
    "abc": "๐ค",
    "abcd": "๐ก",
    "capital_abcd": "๐ ",
    "ng": "๐",
    "ok": "๐",
    "up": "๐",
    "cool": "๐",
    "new": "๐",
    "free": "๐",
    "zero": "0๏ธโฃ",
    "one": "1๏ธโฃ",
    "two": "2๏ธโฃ",
    "three": "3๏ธโฃ",
    "four": "4๏ธโฃ",
    "five": "5๏ธโฃ",
    "six": "6๏ธโฃ",
    "seven": "7๏ธโฃ",
    "eight": "8๏ธโฃ",
    "nine": "9๏ธโฃ",
    "keycap_ten": "๐",
    "hash": "#๏ธโฃ",
    "keycap_asterisk": "*๏ธโฃ",
    "eject": "โ",
    "eject_symbol": "โ",
    "arrow_forward": "โถ",
    "pause_button": "โธ",
    "double_vertical_bar": "โธ",
    "play_pause": "โฏ",
    "stop_button": "โน",
    "record_button": "โบ",
    "track_next": "โญ",
    "next_track": "โญ",
    "track_previous": "โฎ",
    "previous_track": "โฎ",
    "fast_forward": "โฉ",
    "rewind": "โช",
    "arrow_double_up": "โซ",
    "arrow_double_down": "โฌ",
    "arrow_backward": "โ",
    "arrow_up_small": "๐ผ",
    "arrow_down_small": "๐ฝ",
    "arrow_right": "โก",
    "arrow_left": "โฌ",
    "arrow_up": "โฌ",
    "arrow_down": "โฌ",
    "arrow_upper_right": "โ",
    "arrow_lower_right": "โ",
    "arrow_lower_left": "โ",
    "arrow_upper_left": "โ",
    "arrow_up_down": "โ",
    "left_right_arrow": "โ",
    "arrow_right_hook": "โช",
    "leftwards_arrow_with_hook": "โฉ",
    "arrow_heading_up": "โคด",
    "arrow_heading_down": "โคต",
    "twisted_rightwards_arrows": "๐",
    "repeat": "๐",
    "repeat_one": "๐",
    "arrows_counterclockwise": "๐",
    "arrows_clockwise": "๐",
    "musical_note": "๐ต",
    "notes": "๐ถ",
    "heavy_plus_sign": "โ",
    "heavy_minus_sign": "โ",
    "heavy_division_sign": "โ",
    "heavy_multiplication_x": "โ",
    "infinity": "โพ",
    "heavy_dollar_sign": "๐ฒ",
    "currency_exchange": "๐ฑ",
    "tm": "โข",
    "copyright": "ยฉ",
    "registered": "ยฎ",
    "wavy_dash": "ใฐ",
    "curly_loop": "โฐ",
    "loop": "โฟ",
    "end": "๐",
    "back": "๐",
    "on": "๐",
    "top": "๐",
    "soon": "๐",
    "heavy_check_mark": "โ",
    "ballot_box_with_check": "โ",
    "radio_button": "๐",
    "white_circle": "โช",
    "black_circle": "โซ",
    "red_circle": "๐ด",
    "blue_circle": "๐ต",
    "brown_circle": "๐ค",
    "purple_circle": "๐ฃ",
    "green_circle": "๐ข",
    "yellow_circle": "๐ก",
    "orange_circle": "๐ ",
    "small_red_triangle": "๐บ",
    "small_red_triangle_down": "๐ป",
    "small_orange_diamond": "๐ธ",
    "small_blue_diamond": "๐น",
    "large_orange_diamond": "๐ถ",
    "large_blue_diamond": "๐ท",
    "white_square_button": "๐ณ",
    "black_square_button": "๐ฒ",
    "black_small_square": "โช",
    "white_small_square": "โซ",
    "black_medium_small_square": "โพ",
    "white_medium_small_square": "โฝ",
    "black_medium_square": "โผ",
    "white_medium_square": "โป",
    "black_large_square": "โฌ",
    "white_large_square": "โฌ",
    "orange_square": "๐ง",
    "blue_square": "๐ฆ",
    "red_square": "๐ฅ",
    "brown_square": "๐ซ",
    "purple_square": "๐ช",
    "green_square": "๐ฉ",
    "yellow_square": "๐จ",
    "speaker": "๐",
    "mute": "๐",
    "sound": "๐",
    "loud_sound": "๐",
    "bell": "๐",
    "no_bell": "๐",
    "mega": "๐ฃ",
    "loudspeaker": "๐ข",
    "speech_left": "๐จ",
    "left_speech_bubble": "๐จ",
    "eye_in_speech_bubble": "๐๐จ",
    "speech_balloon": "๐ฌ",
    "thought_balloon": "๐ญ",
    "anger_right": "๐ฏ",
    "right_anger_bubble": "๐ฏ",
    "spades": "โ ",
    "clubs": "โฃ",
    "hearts": "โฅ",
    "diamonds": "โฆ",
    "black_joker": "๐",
    "flower_playing_cards": "๐ด",
    "mahjong": "๐",
    "clock1": "๐",
    "clock2": "๐",
    "clock3": "๐",
    "clock4": "๐",
    "clock5": "๐",
    "clock6": "๐",
    "clock7": "๐",
    "clock8": "๐",
    "clock9": "๐",
    "clock10": "๐",
    "clock11": "๐",
    "clock12": "๐",
    "clock130": "๐",
    "clock230": "๐",
    "clock330": "๐",
    "clock430": "๐",
    "clock530": "๐ ",
    "clock630": "๐ก",
    "clock730": "๐ข",
    "clock830": "๐ฃ",
    "clock930": "๐ค",
    "clock1030": "๐ฅ",
    "clock1130": "๐ฆ",
    "clock1230": "๐ง",
    "female_sign": "โ",
    "male_sign": "โ",
    "medical_symbol": "โ",
    "regional_indicator_z": "๐ฟ",
    "regional_indicator_y": "๐พ",
    "regional_indicator_x": "๐ฝ",
    "regional_indicator_w": "๐ผ",
    "regional_indicator_v": "๐ป",
    "regional_indicator_u": "๐บ",
    "regional_indicator_t": "๐น",
    "regional_indicator_s": "๐ธ",
    "regional_indicator_r": "๐ท",
    "regional_indicator_q": "๐ถ",
    "regional_indicator_p": "๐ต",
    "regional_indicator_o": "๐ด",
    "regional_indicator_n": "๐ณ",
    "regional_indicator_m": "๐ฒ",
    "regional_indicator_l": "๐ฑ",
    "regional_indicator_k": "๐ฐ",
    "regional_indicator_j": "๐ฏ",
    "regional_indicator_i": "๐ฎ",
    "regional_indicator_h": "๐ญ",
    "regional_indicator_g": "๐ฌ",
    "regional_indicator_f": "๐ซ",
    "regional_indicator_e": "๐ช",
    "regional_indicator_d": "๐ฉ",
    "regional_indicator_c": "๐จ",
    "regional_indicator_b": "๐ง",
    "regional_indicator_a": "๐ฆ",
    "flag_white": "๐ณ",
    "flag_black": "๐ด",
    "checkered_flag": "๐",
    "triangular_flag_on_post": "๐ฉ",
    "rainbow_flag": "๐ณ๐",
    "gay_pride_flag": "๐ณ๐",
    "pirate_flag": "๐ดโ ",
    "flag_af": "๐ฆ๐ซ",
    "flag_ax": "๐ฆ๐ฝ",
    "flag_al": "๐ฆ๐ฑ",
    "flag_dz": "๐ฉ๐ฟ",
    "flag_as": "๐ฆ๐ธ",
    "flag_ad": "๐ฆ๐ฉ",
    "flag_ao": "๐ฆ๐ด",
    "flag_ai": "๐ฆ๐ฎ",
    "flag_aq": "๐ฆ๐ถ",
    "flag_ag": "๐ฆ๐ฌ",
    "flag_ar": "๐ฆ๐ท",
    "flag_am": "๐ฆ๐ฒ",
    "flag_aw": "๐ฆ๐ผ",
    "flag_au": "๐ฆ๐บ",
    "flag_at": "๐ฆ๐น",
    "flag_az": "๐ฆ๐ฟ",
    "flag_bs": "๐ง๐ธ",
    "flag_bh": "๐ง๐ญ",
    "flag_bd": "๐ง๐ฉ",
    "flag_bb": "๐ง๐ง",
    "flag_by": "๐ง๐พ",
    "flag_be": "๐ง๐ช",
    "flag_bz": "๐ง๐ฟ",
    "flag_bj": "๐ง๐ฏ",
    "flag_bm": "๐ง๐ฒ",
    "flag_bt": "๐ง๐น",
    "flag_bo": "๐ง๐ด",
    "flag_ba": "๐ง๐ฆ",
    "flag_bw": "๐ง๐ผ",
    "flag_br": "๐ง๐ท",
    "flag_io": "๐ฎ๐ด",
    "flag_vg": "๐ป๐ฌ",
    "flag_bn": "๐ง๐ณ",
    "flag_bg": "๐ง๐ฌ",
    "flag_bf": "๐ง๐ซ",
    "flag_bi": "๐ง๐ฎ",
    "flag_kh": "๐ฐ๐ญ",
    "flag_cm": "๐จ๐ฒ",
    "flag_ca": "๐จ๐ฆ",
    "flag_ic": "๐ฎ๐จ",
    "flag_cv": "๐จ๐ป",
    "flag_bq": "๐ง๐ถ",
    "flag_ky": "๐ฐ๐พ",
    "flag_cf": "๐จ๐ซ",
    "flag_td": "๐น๐ฉ",
    "flag_cl": "๐จ๐ฑ",
    "flag_cn": "๐จ๐ณ",
    "flag_cx": "๐จ๐ฝ",
    "flag_cc": "๐จ๐จ",
    "flag_co": "๐จ๐ด",
    "flag_km": "๐ฐ๐ฒ",
    "flag_cg": "๐จ๐ฌ",
    "flag_cd": "๐จ๐ฉ",
    "flag_ck": "๐จ๐ฐ",
    "flag_cr": "๐จ๐ท",
    "flag_ci": "๐จ๐ฎ",
    "flag_hr": "๐ญ๐ท",
    "flag_cu": "๐จ๐บ",
    "flag_cw": "๐จ๐ผ",
    "flag_cy": "๐จ๐พ",
    "flag_cz": "๐จ๐ฟ",
    "flag_dk": "๐ฉ๐ฐ",
    "flag_dj": "๐ฉ๐ฏ",
    "flag_dm": "๐ฉ๐ฒ",
    "flag_do": "๐ฉ๐ด",
    "flag_ec": "๐ช๐จ",
    "flag_eg": "๐ช๐ฌ",
    "flag_sv": "๐ธ๐ป",
    "flag_gq": "๐ฌ๐ถ",
    "flag_er": "๐ช๐ท",
    "flag_ee": "๐ช๐ช",
    "flag_et": "๐ช๐น",
    "flag_eu": "๐ช๐บ",
    "flag_fk": "๐ซ๐ฐ",
    "flag_fo": "๐ซ๐ด",
    "flag_fj": "๐ซ๐ฏ",
    "flag_fi": "๐ซ๐ฎ",
    "flag_fr": "๐ซ๐ท",
    "flag_gf": "๐ฌ๐ซ",
    "flag_pf": "๐ต๐ซ",
    "flag_tf": "๐น๐ซ",
    "flag_ga": "๐ฌ๐ฆ",
    "flag_gm": "๐ฌ๐ฒ",
    "flag_ge": "๐ฌ๐ช",
    "flag_de": "๐ฉ๐ช",
    "flag_gh": "๐ฌ๐ญ",
    "flag_gi": "๐ฌ๐ฎ",
    "flag_gr": "๐ฌ๐ท",
    "flag_gl": "๐ฌ๐ฑ",
    "flag_gd": "๐ฌ๐ฉ",
    "flag_gp": "๐ฌ๐ต",
    "flag_gu": "๐ฌ๐บ",
    "flag_gt": "๐ฌ๐น",
    "flag_gg": "๐ฌ๐ฌ",
    "flag_gn": "๐ฌ๐ณ",
    "flag_gw": "๐ฌ๐ผ",
    "flag_gy": "๐ฌ๐พ",
    "flag_ht": "๐ญ๐น",
    "flag_hn": "๐ญ๐ณ",
    "flag_hk": "๐ญ๐ฐ",
    "flag_hu": "๐ญ๐บ",
    "flag_is": "๐ฎ๐ธ",
    "flag_in": "๐ฎ๐ณ",
    "flag_id": "๐ฎ๐ฉ",
    "flag_ir": "๐ฎ๐ท",
    "flag_iq": "๐ฎ๐ถ",
    "flag_ie": "๐ฎ๐ช",
    "flag_im": "๐ฎ๐ฒ",
    "flag_il": "๐ฎ๐ฑ",
    "flag_it": "๐ฎ๐น",
    "flag_jm": "๐ฏ๐ฒ",
    "flag_jp": "๐ฏ๐ต",
    "crossed_flags": "๐",
    "flag_je": "๐ฏ๐ช",
    "flag_jo": "๐ฏ๐ด",
    "flag_kz": "๐ฐ๐ฟ",
    "flag_ke": "๐ฐ๐ช",
    "flag_ki": "๐ฐ๐ฎ",
    "flag_xk": "๐ฝ๐ฐ",
    "flag_kw": "๐ฐ๐ผ",
    "flag_kg": "๐ฐ๐ฌ",
    "flag_la": "๐ฑ๐ฆ",
    "flag_lv": "๐ฑ๐ป",
    "flag_lb": "๐ฑ๐ง",
    "flag_ls": "๐ฑ๐ธ",
    "flag_lr": "๐ฑ๐ท",
    "flag_ly": "๐ฑ๐พ",
    "flag_li": "๐ฑ๐ฎ",
    "flag_lt": "๐ฑ๐น",
    "flag_lu": "๐ฑ๐บ",
    "flag_mo": "๐ฒ๐ด",
    "flag_mk": "๐ฒ๐ฐ",
    "flag_mg": "๐ฒ๐ฌ",
    "flag_mw": "๐ฒ๐ผ",
    "flag_my": "๐ฒ๐พ",
    "flag_mv": "๐ฒ๐ป",
    "flag_ml": "๐ฒ๐ฑ",
    "flag_mt": "๐ฒ๐น",
    "flag_mh": "๐ฒ๐ญ",
    "flag_mq": "๐ฒ๐ถ",
    "flag_mr": "๐ฒ๐ท",
    "flag_mu": "๐ฒ๐บ",
    "flag_yt": "๐พ๐น",
    "flag_mx": "๐ฒ๐ฝ",
    "flag_fm": "๐ซ๐ฒ",
    "flag_md": "๐ฒ๐ฉ",
    "flag_mc": "๐ฒ๐จ",
    "flag_mn": "๐ฒ๐ณ",
    "flag_me": "๐ฒ๐ช",
    "flag_ms": "๐ฒ๐ธ",
    "flag_ma": "๐ฒ๐ฆ",
    "flag_mz": "๐ฒ๐ฟ",
    "flag_mm": "๐ฒ๐ฒ",
    "flag_na": "๐ณ๐ฆ",
    "flag_nr": "๐ณ๐ท",
    "flag_np": "๐ณ๐ต",
    "flag_nl": "๐ณ๐ฑ",
    "flag_nc": "๐ณ๐จ",
    "flag_nz": "๐ณ๐ฟ",
    "flag_ni": "๐ณ๐ฎ",
    "flag_ne": "๐ณ๐ช",
    "flag_ng": "๐ณ๐ฌ",
    "flag_nu": "๐ณ๐บ",
    "flag_nf": "๐ณ๐ซ",
    "flag_kp": "๐ฐ๐ต",
    "flag_mp": "๐ฒ๐ต",
    "flag_no": "๐ณ๐ด",
    "flag_om": "๐ด๐ฒ",
    "flag_pk": "๐ต๐ฐ",
    "flag_pw": "๐ต๐ผ",
    "flag_ps": "๐ต๐ธ",
    "flag_pa": "๐ต๐ฆ",
    "flag_pg": "๐ต๐ฌ",
    "flag_py": "๐ต๐พ",
    "flag_pe": "๐ต๐ช",
    "flag_ph": "๐ต๐ญ",
    "flag_pn": "๐ต๐ณ",
    "flag_pl": "๐ต๐ฑ",
    "flag_pt": "๐ต๐น",
    "flag_pr": "๐ต๐ท",
    "flag_qa": "๐ถ๐ฆ",
    "flag_re": "๐ท๐ช",
    "flag_ro": "๐ท๐ด",
    "flag_ru": "๐ท๐บ",
    "flag_rw": "๐ท๐ผ",
    "flag_ws": "๐ผ๐ธ",
    "flag_sm": "๐ธ๐ฒ",
    "flag_st": "๐ธ๐น",
    "flag_sa": "๐ธ๐ฆ",
    "flag_sn": "๐ธ๐ณ",
    "flag_rs": "๐ท๐ธ",
    "flag_sc": "๐ธ๐จ",
    "flag_sl": "๐ธ๐ฑ",
    "flag_sg": "๐ธ๐ฌ",
    "flag_sx": "๐ธ๐ฝ",
    "flag_sk": "๐ธ๐ฐ",
    "flag_si": "๐ธ๐ฎ",
    "flag_gs": "๐ฌ๐ธ",
    "flag_sb": "๐ธ๐ง",
    "flag_so": "๐ธ๐ด",
    "flag_za": "๐ฟ๐ฆ",
    "flag_kr": "๐ฐ๐ท",
    "flag_ss": "๐ธ๐ธ",
    "flag_es": "๐ช๐ธ",
    "flag_lk": "๐ฑ๐ฐ",
    "flag_bl": "๐ง๐ฑ",
    "flag_sh": "๐ธ๐ญ",
    "flag_kn": "๐ฐ๐ณ",
    "flag_lc": "๐ฑ๐จ",
    "flag_pm": "๐ต๐ฒ",
    "flag_vc": "๐ป๐จ",
    "flag_sd": "๐ธ๐ฉ",
    "flag_sr": "๐ธ๐ท",
    "flag_sz": "๐ธ๐ฟ",
    "flag_se": "๐ธ๐ช",
    "flag_ch": "๐จ๐ญ",
    "flag_sy": "๐ธ๐พ",
    "flag_tw": "๐น๐ผ",
    "flag_tj": "๐น๐ฏ",
    "flag_tz": "๐น๐ฟ",
    "flag_th": "๐น๐ญ",
    "flag_tl": "๐น๐ฑ",
    "flag_tg": "๐น๐ฌ",
    "flag_tk": "๐น๐ฐ",
    "flag_to": "๐น๐ด",
    "flag_tt": "๐น๐น",
    "flag_tn": "๐น๐ณ",
    "flag_tr": "๐น๐ท",
    "flag_tm": "๐น๐ฒ",
    "flag_tc": "๐น๐จ",
    "flag_vi": "๐ป๐ฎ",
    "flag_tv": "๐น๐ป",
    "flag_ug": "๐บ๐ฌ",
    "flag_ua": "๐บ๐ฆ",
    "flag_ae": "๐ฆ๐ช",
    "flag_gb": "๐ฌ๐ง",
    "england": "๐ด",
    "scotland": "๐ด",
    "wales": "๐ด",
    "flag_us": "๐บ๐ธ",
    "flag_uy": "๐บ๐พ",
    "flag_uz": "๐บ๐ฟ",
    "flag_vu": "๐ป๐บ",
    "flag_va": "๐ป๐ฆ",
    "flag_ve": "๐ป๐ช",
    "flag_vn": "๐ป๐ณ",
    "flag_wf": "๐ผ๐ซ",
    "flag_eh": "๐ช๐ญ",
    "flag_ye": "๐พ๐ช",
    "flag_zm": "๐ฟ๐ฒ",
    "flag_zw": "๐ฟ๐ผ",
    "flag_ac": "๐ฆ๐จ",
    "flag_bv": "๐ง๐ป",
    "flag_cp": "๐จ๐ต",
    "flag_ea": "๐ช๐ฆ",
    "flag_dg": "๐ฉ๐ฌ",
    "flag_hm": "๐ญ๐ฒ",
    "flag_mf": "๐ฒ๐ซ",
    "flag_sj": "๐ธ๐ฏ",
    "flag_ta": "๐น๐ฆ",
    "flag_um": "๐บ๐ฒ",
    "united_nations": "๐บ๐ณ",
}


discord_emoji_converter_inverse = {value: key for key, value in discord_emoji_converter.items()}


class EmojiUnicodeType (str, Enum):
    hundred = "๐ฏ"
    one_two_three_four = "๐ข"
    grinning = "๐"
    smiley = "๐"
    smile = "๐"
    grin = "๐"
    laughing = "๐"
    satisfied = "๐"
    sweat_smile = "๐"
    joy = "๐"
    rofl = "๐คฃ"
    rolling_on_the_floor_laughing = "๐คฃ"
    relaxed = "โบ"
    blush = "๐"
    innocent = "๐"
    slight_smile = "๐"
    slightly_smiling_face = "๐"
    upside_down = "๐"
    upside_down_face = "๐"
    wink = "๐"
    relieved = "๐"
    heart_eyes = "๐"
    smiling_face_with_3_hearts = "๐ฅฐ"
    kissing_heart = "๐"
    kissing = "๐"
    kissing_smiling_eyes = "๐"
    kissing_closed_eyes = "๐"
    yum = "๐"
    stuck_out_tongue = "๐"
    stuck_out_tongue_closed_eyes = "๐"
    stuck_out_tongue_winking_eye = "๐"
    zany_face = "๐คช"
    face_with_raised_eyebrow = "๐คจ"
    face_with_monocle = "๐ง"
    nerd = "๐ค"
    nerd_face = "๐ค"
    sunglasses = "๐"
    star_struck = "๐คฉ"
    partying_face = "๐ฅณ"
    smirk = "๐"
    unamused = "๐"
    disappointed = "๐"
    pensive = "๐"
    worried = "๐"
    confused = "๐"
    slight_frown = "๐"
    slightly_frowning_face = "๐"
    frowning2 = "โน"
    white_frowning_face = "โน"
    persevere = "๐ฃ"
    confounded = "๐"
    tired_face = "๐ซ"
    weary = "๐ฉ"
    pleading_face = "๐ฅบ"
    cry = "๐ข"
    sob = "๐ญ"
    triumph = "๐ค"
    angry = "๐ "
    rage = "๐ก"
    face_with_symbols_over_mouth = "๐คฌ"
    exploding_head = "๐คฏ"
    flushed = "๐ณ"
    hot_face = "๐ฅต"
    cold_face = "๐ฅถ"
    scream = "๐ฑ"
    fearful = "๐จ"
    cold_sweat = "๐ฐ"
    disappointed_relieved = "๐ฅ"
    sweat = "๐"
    hugging = "๐ค"
    hugging_face = "๐ค"
    thinking = "๐ค"
    thinking_face = "๐ค"
    face_with_hand_over_mouth = "๐คญ"
    yawning_face = "๐ฅฑ"
    shushing_face = "๐คซ"
    lying_face = "๐คฅ"
    liar = "๐คฅ"
    no_mouth = "๐ถ"
    neutral_face = "๐"
    expressionless = "๐"
    grimacing = "๐ฌ"
    rolling_eyes = "๐"
    face_with_rolling_eyes = "๐"
    hushed = "๐ฏ"
    frowning = "๐ฆ"
    anguished = "๐ง"
    open_mouth = "๐ฎ"
    astonished = "๐ฒ"
    sleeping = "๐ด"
    drooling_face = "๐คค"
    drool = "๐คค"
    sleepy = "๐ช"
    dizzy_face = "๐ต"
    zipper_mouth = "๐ค"
    zipper_mouth_face = "๐ค"
    woozy_face = "๐ฅด"
    nauseated_face = "๐คข"
    sick = "๐คข"
    face_vomiting = "๐คฎ"
    sneezing_face = "๐คง"
    sneeze = "๐คง"
    mask = "๐ท"
    thermometer_face = "๐ค"
    face_with_thermometer = "๐ค"
    head_bandage = "๐ค"
    face_with_head_bandage = "๐ค"
    money_mouth = "๐ค"
    money_mouth_face = "๐ค"
    cowboy = "๐ค "
    face_with_cowboy_hat = "๐ค "
    smiling_imp = "๐"
    imp = "๐ฟ"
    japanese_ogre = "๐น"
    japanese_goblin = "๐บ"
    clown = "๐คก"
    clown_face = "๐คก"
    poop = "๐ฉ"
    shit = "๐ฉ"
    hankey = "๐ฉ"
    poo = "๐ฉ"
    ghost = "๐ป"
    skull = "๐"
    skeleton = "๐"
    skull_crossbones = "โ "
    skull_and_crossbones = "โ "
    alien = "๐ฝ"
    space_invader = "๐พ"
    robot = "๐ค"
    robot_face = "๐ค"
    jack_o_lantern = "๐"
    smiley_cat = "๐บ"
    smile_cat = "๐ธ"
    joy_cat = "๐น"
    heart_eyes_cat = "๐ป"
    smirk_cat = "๐ผ"
    kissing_cat = "๐ฝ"
    scream_cat = "๐"
    crying_cat_face = "๐ฟ"
    pouting_cat = "๐พ"
    palms_up_together = "๐คฒ"
    palms_up_together_tone1 = "๐คฒ๐ป"
    palms_up_together_light_skin_tone = "๐คฒ๐ป"
    palms_up_together_tone2 = "๐คฒ๐ผ"
    palms_up_together_medium_light_skin_tone = "๐คฒ๐ผ"
    palms_up_together_tone3 = "๐คฒ๐ฝ"
    palms_up_together_medium_skin_tone = "๐คฒ๐ฝ"
    palms_up_together_tone4 = "๐คฒ๐พ"
    palms_up_together_medium_dark_skin_tone = "๐คฒ๐พ"
    palms_up_together_tone5 = "๐คฒ๐ฟ"
    palms_up_together_dark_skin_tone = "๐คฒ๐ฟ"
    open_hands = "๐"
    open_hands_tone1 = "๐๐ป"
    open_hands_tone2 = "๐๐ผ"
    open_hands_tone3 = "๐๐ฝ"
    open_hands_tone4 = "๐๐พ"
    open_hands_tone5 = "๐๐ฟ"
    raised_hands = "๐"
    raised_hands_tone1 = "๐๐ป"
    raised_hands_tone2 = "๐๐ผ"
    raised_hands_tone3 = "๐๐ฝ"
    raised_hands_tone4 = "๐๐พ"
    raised_hands_tone5 = "๐๐ฟ"
    clap = "๐"
    clap_tone1 = "๐๐ป"
    clap_tone2 = "๐๐ผ"
    clap_tone3 = "๐๐ฝ"
    clap_tone4 = "๐๐พ"
    clap_tone5 = "๐๐ฟ"
    handshake = "๐ค"
    shaking_hands = "๐ค"
    thumbsup = "๐"
    plus_one = "๐"
    thumbup = "๐"
    thumbsup_tone1 = "๐๐ป"
    plus_one_tone1 = "๐๐ป"
    thumbup_tone1 = "๐๐ป"
    thumbsup_tone2 = "๐๐ผ"
    plus_one_tone2 = "๐๐ผ"
    thumbup_tone2 = "๐๐ผ"
    thumbsup_tone3 = "๐๐ฝ"
    plus_one_tone3 = "๐๐ฝ"
    thumbup_tone3 = "๐๐ฝ"
    thumbsup_tone4 = "๐๐พ"
    plus_one_tone4 = "๐๐พ"
    thumbup_tone4 = "๐๐พ"
    thumbsup_tone5 = "๐๐ฟ"
    plus_one_tone5 = "๐๐ฟ"
    thumbup_tone5 = "๐๐ฟ"
    thumbsdown = "๐"
    minus_one = "๐"
    thumbdown = "๐"
    thumbsdown_tone1 = "๐๐ป"
    minus_one_tone1 = "๐๐ป"
    thumbdown_tone1 = "๐๐ป"
    thumbsdown_tone2 = "๐๐ผ"
    minus_one_tone2 = "๐๐ผ"
    thumbdown_tone2 = "๐๐ผ"
    thumbsdown_tone3 = "๐๐ฝ"
    minus_one_tone3 = "๐๐ฝ"
    thumbdown_tone3 = "๐๐ฝ"
    thumbsdown_tone4 = "๐๐พ"
    minus_one_tone4 = "๐๐พ"
    thumbdown_tone4 = "๐๐พ"
    thumbsdown_tone5 = "๐๐ฟ"
    minus_one_tone5 = "๐๐ฟ"
    thumbdown_tone5 = "๐๐ฟ"
    punch = "๐"
    punch_tone1 = "๐๐ป"
    punch_tone2 = "๐๐ผ"
    punch_tone3 = "๐๐ฝ"
    punch_tone4 = "๐๐พ"
    punch_tone5 = "๐๐ฟ"
    fist = "โ"
    fist_tone1 = "โ๐ป"
    fist_tone2 = "โ๐ผ"
    fist_tone3 = "โ๐ฝ"
    fist_tone4 = "โ๐พ"
    fist_tone5 = "โ๐ฟ"
    left_facing_fist = "๐ค"
    left_fist = "๐ค"
    left_facing_fist_tone1 = "๐ค๐ป"
    left_fist_tone1 = "๐ค๐ป"
    left_facing_fist_tone2 = "๐ค๐ผ"
    left_fist_tone2 = "๐ค๐ผ"
    left_facing_fist_tone3 = "๐ค๐ฝ"
    left_fist_tone3 = "๐ค๐ฝ"
    left_facing_fist_tone4 = "๐ค๐พ"
    left_fist_tone4 = "๐ค๐พ"
    left_facing_fist_tone5 = "๐ค๐ฟ"
    left_fist_tone5 = "๐ค๐ฟ"
    right_facing_fist = "๐ค"
    right_fist = "๐ค"
    right_facing_fist_tone1 = "๐ค๐ป"
    right_fist_tone1 = "๐ค๐ป"
    right_facing_fist_tone2 = "๐ค๐ผ"
    right_fist_tone2 = "๐ค๐ผ"
    right_facing_fist_tone3 = "๐ค๐ฝ"
    right_fist_tone3 = "๐ค๐ฝ"
    right_facing_fist_tone4 = "๐ค๐พ"
    right_fist_tone4 = "๐ค๐พ"
    right_facing_fist_tone5 = "๐ค๐ฟ"
    right_fist_tone5 = "๐ค๐ฟ"
    fingers_crossed = "๐ค"
    hand_with_index_and_middle_finger_crossed = "๐ค"
    fingers_crossed_tone1 = "๐ค๐ป"
    hand_with_index_and_middle_fingers_crossed_tone1 = "๐ค๐ป"
    fingers_crossed_tone2 = "๐ค๐ผ"
    hand_with_index_and_middle_fingers_crossed_tone2 = "๐ค๐ผ"
    fingers_crossed_tone3 = "๐ค๐ฝ"
    hand_with_index_and_middle_fingers_crossed_tone3 = "๐ค๐ฝ"
    fingers_crossed_tone4 = "๐ค๐พ"
    hand_with_index_and_middle_fingers_crossed_tone4 = "๐ค๐พ"
    fingers_crossed_tone5 = "๐ค๐ฟ"
    hand_with_index_and_middle_fingers_crossed_tone5 = "๐ค๐ฟ"
    v = "โ"
    v_tone1 = "โ๐ป"
    v_tone2 = "โ๐ผ"
    v_tone3 = "โ๐ฝ"
    v_tone4 = "โ๐พ"
    v_tone5 = "โ๐ฟ"
    love_you_gesture = "๐ค"
    love_you_gesture_tone1 = "๐ค๐ป"
    love_you_gesture_light_skin_tone = "๐ค๐ป"
    love_you_gesture_tone2 = "๐ค๐ผ"
    love_you_gesture_medium_light_skin_tone = "๐ค๐ผ"
    love_you_gesture_tone3 = "๐ค๐ฝ"
    love_you_gesture_medium_skin_tone = "๐ค๐ฝ"
    love_you_gesture_tone4 = "๐ค๐พ"
    love_you_gesture_medium_dark_skin_tone = "๐ค๐พ"
    love_you_gesture_tone5 = "๐ค๐ฟ"
    love_you_gesture_dark_skin_tone = "๐ค๐ฟ"
    metal = "๐ค"
    sign_of_the_horns = "๐ค"
    metal_tone1 = "๐ค๐ป"
    sign_of_the_horns_tone1 = "๐ค๐ป"
    metal_tone2 = "๐ค๐ผ"
    sign_of_the_horns_tone2 = "๐ค๐ผ"
    metal_tone3 = "๐ค๐ฝ"
    sign_of_the_horns_tone3 = "๐ค๐ฝ"
    metal_tone4 = "๐ค๐พ"
    sign_of_the_horns_tone4 = "๐ค๐พ"
    metal_tone5 = "๐ค๐ฟ"
    sign_of_the_horns_tone5 = "๐ค๐ฟ"
    ok_hand = "๐"
    ok_hand_tone1 = "๐๐ป"
    ok_hand_tone2 = "๐๐ผ"
    ok_hand_tone3 = "๐๐ฝ"
    ok_hand_tone4 = "๐๐พ"
    ok_hand_tone5 = "๐๐ฟ"
    pinching_hand = "๐ค"
    pinching_hand_tone1 = "๐ค๐ป"
    pinching_hand_light_skin_tone = "๐ค๐ป"
    pinching_hand_tone2 = "๐ค๐ผ"
    pinching_hand_medium_light_skin_tone = "๐ค๐ผ"
    pinching_hand_tone3 = "๐ค๐ฝ"
    pinching_hand_medium_skin_tone = "๐ค๐ฝ"
    pinching_hand_tone4 = "๐ค๐พ"
    pinching_hand_medium_dark_skin_tone = "๐ค๐พ"
    pinching_hand_tone5 = "๐ค๐ฟ"
    pinching_hand_dark_skin_tone = "๐ค๐ฟ"
    point_left = "๐"
    point_left_tone1 = "๐๐ป"
    point_left_tone2 = "๐๐ผ"
    point_left_tone3 = "๐๐ฝ"
    point_left_tone4 = "๐๐พ"
    point_left_tone5 = "๐๐ฟ"
    point_right = "๐"
    point_right_tone1 = "๐๐ป"
    point_right_tone2 = "๐๐ผ"
    point_right_tone3 = "๐๐ฝ"
    point_right_tone4 = "๐๐พ"
    point_right_tone5 = "๐๐ฟ"
    point_up_2 = "๐"
    point_up_2_tone1 = "๐๐ป"
    point_up_2_tone2 = "๐๐ผ"
    point_up_2_tone3 = "๐๐ฝ"
    point_up_2_tone4 = "๐๐พ"
    point_up_2_tone5 = "๐๐ฟ"
    point_down = "๐"
    point_down_tone1 = "๐๐ป"
    point_down_tone2 = "๐๐ผ"
    point_down_tone3 = "๐๐ฝ"
    point_down_tone4 = "๐๐พ"
    point_down_tone5 = "๐๐ฟ"
    point_up = "โ"
    point_up_tone1 = "โ๐ป"
    point_up_tone2 = "โ๐ผ"
    point_up_tone3 = "โ๐ฝ"
    point_up_tone4 = "โ๐พ"
    point_up_tone5 = "โ๐ฟ"
    raised_hand = "โ"
    raised_hand_tone1 = "โ๐ป"
    raised_hand_tone2 = "โ๐ผ"
    raised_hand_tone3 = "โ๐ฝ"
    raised_hand_tone4 = "โ๐พ"
    raised_hand_tone5 = "โ๐ฟ"
    raised_back_of_hand = "๐ค"
    back_of_hand = "๐ค"
    raised_back_of_hand_tone1 = "๐ค๐ป"
    back_of_hand_tone1 = "๐ค๐ป"
    raised_back_of_hand_tone2 = "๐ค๐ผ"
    back_of_hand_tone2 = "๐ค๐ผ"
    raised_back_of_hand_tone3 = "๐ค๐ฝ"
    back_of_hand_tone3 = "๐ค๐ฝ"
    raised_back_of_hand_tone4 = "๐ค๐พ"
    back_of_hand_tone4 = "๐ค๐พ"
    raised_back_of_hand_tone5 = "๐ค๐ฟ"
    back_of_hand_tone5 = "๐ค๐ฟ"
    hand_splayed = "๐"
    raised_hand_with_fingers_splayed = "๐"
    hand_splayed_tone1 = "๐๐ป"
    raised_hand_with_fingers_splayed_tone1 = "๐๐ป"
    hand_splayed_tone2 = "๐๐ผ"
    raised_hand_with_fingers_splayed_tone2 = "๐๐ผ"
    hand_splayed_tone3 = "๐๐ฝ"
    raised_hand_with_fingers_splayed_tone3 = "๐๐ฝ"
    hand_splayed_tone4 = "๐๐พ"
    raised_hand_with_fingers_splayed_tone4 = "๐๐พ"
    hand_splayed_tone5 = "๐๐ฟ"
    raised_hand_with_fingers_splayed_tone5 = "๐๐ฟ"
    vulcan = "๐"
    raised_hand_with_part_between_middle_and_ring_fingers = "๐"
    vulcan_tone1 = "๐๐ป"
    raised_hand_with_part_between_middle_and_ring_fingers_tone1 = "๐๐ป"
    vulcan_tone2 = "๐๐ผ"
    raised_hand_with_part_between_middle_and_ring_fingers_tone2 = "๐๐ผ"
    vulcan_tone3 = "๐๐ฝ"
    raised_hand_with_part_between_middle_and_ring_fingers_tone3 = "๐๐ฝ"
    vulcan_tone4 = "๐๐พ"
    raised_hand_with_part_between_middle_and_ring_fingers_tone4 = "๐๐พ"
    vulcan_tone5 = "๐๐ฟ"
    raised_hand_with_part_between_middle_and_ring_fingers_tone5 = "๐๐ฟ"
    wave = "๐"
    wave_tone1 = "๐๐ป"
    wave_tone2 = "๐๐ผ"
    wave_tone3 = "๐๐ฝ"
    wave_tone4 = "๐๐พ"
    wave_tone5 = "๐๐ฟ"
    call_me = "๐ค"
    call_me_hand = "๐ค"
    call_me_tone1 = "๐ค๐ป"
    call_me_hand_tone1 = "๐ค๐ป"
    call_me_tone2 = "๐ค๐ผ"
    call_me_hand_tone2 = "๐ค๐ผ"
    call_me_tone3 = "๐ค๐ฝ"
    call_me_hand_tone3 = "๐ค๐ฝ"
    call_me_tone4 = "๐ค๐พ"
    call_me_hand_tone4 = "๐ค๐พ"
    call_me_tone5 = "๐ค๐ฟ"
    call_me_hand_tone5 = "๐ค๐ฟ"
    muscle = "๐ช"
    muscle_tone1 = "๐ช๐ป"
    muscle_tone2 = "๐ช๐ผ"
    muscle_tone3 = "๐ช๐ฝ"
    muscle_tone4 = "๐ช๐พ"
    muscle_tone5 = "๐ช๐ฟ"
    mechanical_arm = "๐ฆพ"
    middle_finger = "๐"
    reversed_hand_with_middle_finger_extended = "๐"
    middle_finger_tone1 = "๐๐ป"
    reversed_hand_with_middle_finger_extended_tone1 = "๐๐ป"
    middle_finger_tone2 = "๐๐ผ"
    reversed_hand_with_middle_finger_extended_tone2 = "๐๐ผ"
    middle_finger_tone3 = "๐๐ฝ"
    reversed_hand_with_middle_finger_extended_tone3 = "๐๐ฝ"
    middle_finger_tone4 = "๐๐พ"
    reversed_hand_with_middle_finger_extended_tone4 = "๐๐พ"
    middle_finger_tone5 = "๐๐ฟ"
    reversed_hand_with_middle_finger_extended_tone5 = "๐๐ฟ"
    writing_hand = "โ"
    writing_hand_tone1 = "โ๐ป"
    writing_hand_tone2 = "โ๐ผ"
    writing_hand_tone3 = "โ๐ฝ"
    writing_hand_tone4 = "โ๐พ"
    writing_hand_tone5 = "โ๐ฟ"
    pray = "๐"
    pray_tone1 = "๐๐ป"
    pray_tone2 = "๐๐ผ"
    pray_tone3 = "๐๐ฝ"
    pray_tone4 = "๐๐พ"
    pray_tone5 = "๐๐ฟ"
    foot = "๐ฆถ"
    foot_tone1 = "๐ฆถ๐ป"
    foot_light_skin_tone = "๐ฆถ๐ป"
    foot_tone2 = "๐ฆถ๐ผ"
    foot_medium_light_skin_tone = "๐ฆถ๐ผ"
    foot_tone3 = "๐ฆถ๐ฝ"
    foot_medium_skin_tone = "๐ฆถ๐ฝ"
    foot_tone4 = "๐ฆถ๐พ"
    foot_medium_dark_skin_tone = "๐ฆถ๐พ"
    foot_tone5 = "๐ฆถ๐ฟ"
    foot_dark_skin_tone = "๐ฆถ๐ฟ"
    leg = "๐ฆต"
    leg_tone1 = "๐ฆต๐ป"
    leg_light_skin_tone = "๐ฆต๐ป"
    leg_tone2 = "๐ฆต๐ผ"
    leg_medium_light_skin_tone = "๐ฆต๐ผ"
    leg_tone3 = "๐ฆต๐ฝ"
    leg_medium_skin_tone = "๐ฆต๐ฝ"
    leg_tone4 = "๐ฆต๐พ"
    leg_medium_dark_skin_tone = "๐ฆต๐พ"
    leg_tone5 = "๐ฆต๐ฟ"
    leg_dark_skin_tone = "๐ฆต๐ฟ"
    mechanical_leg = "๐ฆฟ"
    lipstick = "๐"
    kiss = "๐"
    lips = "๐"
    tooth = "๐ฆท"
    bone = "๐ฆด"
    tongue = "๐"
    ear = "๐"
    ear_tone1 = "๐๐ป"
    ear_tone2 = "๐๐ผ"
    ear_tone3 = "๐๐ฝ"
    ear_tone4 = "๐๐พ"
    ear_tone5 = "๐๐ฟ"
    ear_with_hearing_aid = "๐ฆป"
    ear_with_hearing_aid_tone1 = "๐ฆป๐ป"
    ear_with_hearing_aid_light_skin_tone = "๐ฆป๐ป"
    ear_with_hearing_aid_tone2 = "๐ฆป๐ผ"
    ear_with_hearing_aid_medium_light_skin_tone = "๐ฆป๐ผ"
    ear_with_hearing_aid_tone3 = "๐ฆป๐ฝ"
    ear_with_hearing_aid_medium_skin_tone = "๐ฆป๐ฝ"
    ear_with_hearing_aid_tone4 = "๐ฆป๐พ"
    ear_with_hearing_aid_medium_dark_skin_tone = "๐ฆป๐พ"
    ear_with_hearing_aid_tone5 = "๐ฆป๐ฟ"
    ear_with_hearing_aid_dark_skin_tone = "๐ฆป๐ฟ"
    nose = "๐"
    nose_tone1 = "๐๐ป"
    nose_tone2 = "๐๐ผ"
    nose_tone3 = "๐๐ฝ"
    nose_tone4 = "๐๐พ"
    nose_tone5 = "๐๐ฟ"
    footprints = "๐ฃ"
    eye = "๐"
    eyes = "๐"
    brain = "๐ง "
    speaking_head = "๐ฃ"
    speaking_head_in_silhouette = "๐ฃ"
    bust_in_silhouette = "๐ค"
    busts_in_silhouette = "๐ฅ"
    baby = "๐ถ"
    baby_tone1 = "๐ถ๐ป"
    baby_tone2 = "๐ถ๐ผ"
    baby_tone3 = "๐ถ๐ฝ"
    baby_tone4 = "๐ถ๐พ"
    baby_tone5 = "๐ถ๐ฟ"
    girl = "๐ง"
    girl_tone1 = "๐ง๐ป"
    girl_tone2 = "๐ง๐ผ"
    girl_tone3 = "๐ง๐ฝ"
    girl_tone4 = "๐ง๐พ"
    girl_tone5 = "๐ง๐ฟ"
    child = "๐ง"
    child_tone1 = "๐ง๐ป"
    child_light_skin_tone = "๐ง๐ป"
    child_tone2 = "๐ง๐ผ"
    child_medium_light_skin_tone = "๐ง๐ผ"
    child_tone3 = "๐ง๐ฝ"
    child_medium_skin_tone = "๐ง๐ฝ"
    child_tone4 = "๐ง๐พ"
    child_medium_dark_skin_tone = "๐ง๐พ"
    child_tone5 = "๐ง๐ฟ"
    child_dark_skin_tone = "๐ง๐ฟ"
    boy = "๐ฆ"
    boy_tone1 = "๐ฆ๐ป"
    boy_tone2 = "๐ฆ๐ผ"
    boy_tone3 = "๐ฆ๐ฝ"
    boy_tone4 = "๐ฆ๐พ"
    boy_tone5 = "๐ฆ๐ฟ"
    woman = "๐ฉ"
    woman_tone1 = "๐ฉ๐ป"
    woman_tone2 = "๐ฉ๐ผ"
    woman_tone3 = "๐ฉ๐ฝ"
    woman_tone4 = "๐ฉ๐พ"
    woman_tone5 = "๐ฉ๐ฟ"
    adult = "๐ง"
    adult_tone1 = "๐ง๐ป"
    adult_light_skin_tone = "๐ง๐ป"
    adult_tone2 = "๐ง๐ผ"
    adult_medium_light_skin_tone = "๐ง๐ผ"
    adult_tone3 = "๐ง๐ฝ"
    adult_medium_skin_tone = "๐ง๐ฝ"
    adult_tone4 = "๐ง๐พ"
    adult_medium_dark_skin_tone = "๐ง๐พ"
    adult_tone5 = "๐ง๐ฟ"
    adult_dark_skin_tone = "๐ง๐ฟ"
    man = "๐จ"
    man_tone1 = "๐จ๐ป"
    man_tone2 = "๐จ๐ผ"
    man_tone3 = "๐จ๐ฝ"
    man_tone4 = "๐จ๐พ"
    man_tone5 = "๐จ๐ฟ"
    woman_curly_haired = "๐ฉ๐ฆฑ"
    woman_curly_haired_tone1 = "๐ฉ๐ป๐ฆฑ"
    woman_curly_haired_light_skin_tone = "๐ฉ๐ป๐ฆฑ"
    woman_curly_haired_tone2 = "๐ฉ๐ผ๐ฆฑ"
    woman_curly_haired_medium_light_skin_tone = "๐ฉ๐ผ๐ฆฑ"
    woman_curly_haired_tone3 = "๐ฉ๐ฝ๐ฆฑ"
    woman_curly_haired_medium_skin_tone = "๐ฉ๐ฝ๐ฆฑ"
    woman_curly_haired_tone4 = "๐ฉ๐พ๐ฆฑ"
    woman_curly_haired_medium_dark_skin_tone = "๐ฉ๐พ๐ฆฑ"
    woman_curly_haired_tone5 = "๐ฉ๐ฟ๐ฆฑ"
    woman_curly_haired_dark_skin_tone = "๐ฉ๐ฟ๐ฆฑ"
    man_curly_haired = "๐จ๐ฆฑ"
    man_curly_haired_tone1 = "๐จ๐ป๐ฆฑ"
    man_curly_haired_light_skin_tone = "๐จ๐ป๐ฆฑ"
    man_curly_haired_tone2 = "๐จ๐ผ๐ฆฑ"
    man_curly_haired_medium_light_skin_tone = "๐จ๐ผ๐ฆฑ"
    man_curly_haired_tone3 = "๐จ๐ฝ๐ฆฑ"
    man_curly_haired_medium_skin_tone = "๐จ๐ฝ๐ฆฑ"
    man_curly_haired_tone4 = "๐จ๐พ๐ฆฑ"
    man_curly_haired_medium_dark_skin_tone = "๐จ๐พ๐ฆฑ"
    man_curly_haired_tone5 = "๐จ๐ฟ๐ฆฑ"
    man_curly_haired_dark_skin_tone = "๐จ๐ฟ๐ฆฑ"
    woman_red_haired = "๐ฉ๐ฆฐ"
    woman_red_haired_tone1 = "๐ฉ๐ป๐ฆฐ"
    woman_red_haired_light_skin_tone = "๐ฉ๐ป๐ฆฐ"
    woman_red_haired_tone2 = "๐ฉ๐ผ๐ฆฐ"
    woman_red_haired_medium_light_skin_tone = "๐ฉ๐ผ๐ฆฐ"
    woman_red_haired_tone3 = "๐ฉ๐ฝ๐ฆฐ"
    woman_red_haired_medium_skin_tone = "๐ฉ๐ฝ๐ฆฐ"
    woman_red_haired_tone4 = "๐ฉ๐พ๐ฆฐ"
    woman_red_haired_medium_dark_skin_tone = "๐ฉ๐พ๐ฆฐ"
    woman_red_haired_tone5 = "๐ฉ๐ฟ๐ฆฐ"
    woman_red_haired_dark_skin_tone = "๐ฉ๐ฟ๐ฆฐ"
    man_red_haired = "๐จ๐ฆฐ"
    man_red_haired_tone1 = "๐จ๐ป๐ฆฐ"
    man_red_haired_light_skin_tone = "๐จ๐ป๐ฆฐ"
    man_red_haired_tone2 = "๐จ๐ผ๐ฆฐ"
    man_red_haired_medium_light_skin_tone = "๐จ๐ผ๐ฆฐ"
    man_red_haired_tone3 = "๐จ๐ฝ๐ฆฐ"
    man_red_haired_medium_skin_tone = "๐จ๐ฝ๐ฆฐ"
    man_red_haired_tone4 = "๐จ๐พ๐ฆฐ"
    man_red_haired_medium_dark_skin_tone = "๐จ๐พ๐ฆฐ"
    man_red_haired_tone5 = "๐จ๐ฟ๐ฆฐ"
    man_red_haired_dark_skin_tone = "๐จ๐ฟ๐ฆฐ"
    blond_haired_woman = "๐ฑโ"
    blond_haired_woman_tone1 = "๐ฑ๐ปโ"
    blond_haired_woman_light_skin_tone = "๐ฑ๐ปโ"
    blond_haired_woman_tone2 = "๐ฑ๐ผโ"
    blond_haired_woman_medium_light_skin_tone = "๐ฑ๐ผโ"
    blond_haired_woman_tone3 = "๐ฑ๐ฝโ"
    blond_haired_woman_medium_skin_tone = "๐ฑ๐ฝโ"
    blond_haired_woman_tone4 = "๐ฑ๐พโ"
    blond_haired_woman_medium_dark_skin_tone = "๐ฑ๐พโ"
    blond_haired_woman_tone5 = "๐ฑ๐ฟโ"
    blond_haired_woman_dark_skin_tone = "๐ฑ๐ฟโ"
    blond_haired_person = "๐ฑ"
    person_with_blond_hair = "๐ฑ"
    blond_haired_person_tone1 = "๐ฑ๐ป"
    person_with_blond_hair_tone1 = "๐ฑ๐ป"
    blond_haired_person_tone2 = "๐ฑ๐ผ"
    person_with_blond_hair_tone2 = "๐ฑ๐ผ"
    blond_haired_person_tone3 = "๐ฑ๐ฝ"
    person_with_blond_hair_tone3 = "๐ฑ๐ฝ"
    blond_haired_person_tone4 = "๐ฑ๐พ"
    person_with_blond_hair_tone4 = "๐ฑ๐พ"
    blond_haired_person_tone5 = "๐ฑ๐ฟ"
    person_with_blond_hair_tone5 = "๐ฑ๐ฟ"
    blond_haired_man = "๐ฑโ"
    blond_haired_man_tone1 = "๐ฑ๐ปโ"
    blond_haired_man_light_skin_tone = "๐ฑ๐ปโ"
    blond_haired_man_tone2 = "๐ฑ๐ผโ"
    blond_haired_man_medium_light_skin_tone = "๐ฑ๐ผโ"
    blond_haired_man_tone3 = "๐ฑ๐ฝโ"
    blond_haired_man_medium_skin_tone = "๐ฑ๐ฝโ"
    blond_haired_man_tone4 = "๐ฑ๐พโ"
    blond_haired_man_medium_dark_skin_tone = "๐ฑ๐พโ"
    blond_haired_man_tone5 = "๐ฑ๐ฟโ"
    blond_haired_man_dark_skin_tone = "๐ฑ๐ฟโ"
    woman_white_haired = "๐ฉ๐ฆณ"
    woman_white_haired_tone1 = "๐ฉ๐ป๐ฆณ"
    woman_white_haired_light_skin_tone = "๐ฉ๐ป๐ฆณ"
    woman_white_haired_tone2 = "๐ฉ๐ผ๐ฆณ"
    woman_white_haired_medium_light_skin_tone = "๐ฉ๐ผ๐ฆณ"
    woman_white_haired_tone3 = "๐ฉ๐ฝ๐ฆณ"
    woman_white_haired_medium_skin_tone = "๐ฉ๐ฝ๐ฆณ"
    woman_white_haired_tone4 = "๐ฉ๐พ๐ฆณ"
    woman_white_haired_medium_dark_skin_tone = "๐ฉ๐พ๐ฆณ"
    woman_white_haired_tone5 = "๐ฉ๐ฟ๐ฆณ"
    woman_white_haired_dark_skin_tone = "๐ฉ๐ฟ๐ฆณ"
    man_white_haired = "๐จ๐ฆณ"
    man_white_haired_tone1 = "๐จ๐ป๐ฆณ"
    man_white_haired_light_skin_tone = "๐จ๐ป๐ฆณ"
    man_white_haired_tone2 = "๐จ๐ผ๐ฆณ"
    man_white_haired_medium_light_skin_tone = "๐จ๐ผ๐ฆณ"
    man_white_haired_tone3 = "๐จ๐ฝ๐ฆณ"
    man_white_haired_medium_skin_tone = "๐จ๐ฝ๐ฆณ"
    man_white_haired_tone4 = "๐จ๐พ๐ฆณ"
    man_white_haired_medium_dark_skin_tone = "๐จ๐พ๐ฆณ"
    man_white_haired_tone5 = "๐จ๐ฟ๐ฆณ"
    man_white_haired_dark_skin_tone = "๐จ๐ฟ๐ฆณ"
    woman_bald = "๐ฉ๐ฆฒ"
    woman_bald_tone1 = "๐ฉ๐ป๐ฆฒ"
    woman_bald_light_skin_tone = "๐ฉ๐ป๐ฆฒ"
    woman_bald_tone2 = "๐ฉ๐ผ๐ฆฒ"
    woman_bald_medium_light_skin_tone = "๐ฉ๐ผ๐ฆฒ"
    woman_bald_tone3 = "๐ฉ๐ฝ๐ฆฒ"
    woman_bald_medium_skin_tone = "๐ฉ๐ฝ๐ฆฒ"
    woman_bald_tone4 = "๐ฉ๐พ๐ฆฒ"
    woman_bald_medium_dark_skin_tone = "๐ฉ๐พ๐ฆฒ"
    woman_bald_tone5 = "๐ฉ๐ฟ๐ฆฒ"
    woman_bald_dark_skin_tone = "๐ฉ๐ฟ๐ฆฒ"
    man_bald = "๐จ๐ฆฒ"
    man_bald_tone1 = "๐จ๐ป๐ฆฒ"
    man_bald_light_skin_tone = "๐จ๐ป๐ฆฒ"
    man_bald_tone2 = "๐จ๐ผ๐ฆฒ"
    man_bald_medium_light_skin_tone = "๐จ๐ผ๐ฆฒ"
    man_bald_tone3 = "๐จ๐ฝ๐ฆฒ"
    man_bald_medium_skin_tone = "๐จ๐ฝ๐ฆฒ"
    man_bald_tone4 = "๐จ๐พ๐ฆฒ"
    man_bald_medium_dark_skin_tone = "๐จ๐พ๐ฆฒ"
    man_bald_tone5 = "๐จ๐ฟ๐ฆฒ"
    man_bald_dark_skin_tone = "๐จ๐ฟ๐ฆฒ"
    bearded_person = "๐ง"
    bearded_person_tone1 = "๐ง๐ป"
    bearded_person_light_skin_tone = "๐ง๐ป"
    bearded_person_tone2 = "๐ง๐ผ"
    bearded_person_medium_light_skin_tone = "๐ง๐ผ"
    bearded_person_tone3 = "๐ง๐ฝ"
    bearded_person_medium_skin_tone = "๐ง๐ฝ"
    bearded_person_tone4 = "๐ง๐พ"
    bearded_person_medium_dark_skin_tone = "๐ง๐พ"
    bearded_person_tone5 = "๐ง๐ฟ"
    bearded_person_dark_skin_tone = "๐ง๐ฟ"
    older_woman = "๐ต"
    grandma = "๐ต"
    older_woman_tone1 = "๐ต๐ป"
    grandma_tone1 = "๐ต๐ป"
    older_woman_tone2 = "๐ต๐ผ"
    grandma_tone2 = "๐ต๐ผ"
    older_woman_tone3 = "๐ต๐ฝ"
    grandma_tone3 = "๐ต๐ฝ"
    older_woman_tone4 = "๐ต๐พ"
    grandma_tone4 = "๐ต๐พ"
    older_woman_tone5 = "๐ต๐ฟ"
    grandma_tone5 = "๐ต๐ฟ"
    older_adult = "๐ง"
    older_adult_tone1 = "๐ง๐ป"
    older_adult_light_skin_tone = "๐ง๐ป"
    older_adult_tone2 = "๐ง๐ผ"
    older_adult_medium_light_skin_tone = "๐ง๐ผ"
    older_adult_tone3 = "๐ง๐ฝ"
    older_adult_medium_skin_tone = "๐ง๐ฝ"
    older_adult_tone4 = "๐ง๐พ"
    older_adult_medium_dark_skin_tone = "๐ง๐พ"
    older_adult_tone5 = "๐ง๐ฟ"
    older_adult_dark_skin_tone = "๐ง๐ฟ"
    older_man = "๐ด"
    older_man_tone1 = "๐ด๐ป"
    older_man_tone2 = "๐ด๐ผ"
    older_man_tone3 = "๐ด๐ฝ"
    older_man_tone4 = "๐ด๐พ"
    older_man_tone5 = "๐ด๐ฟ"
    man_with_chinese_cap = "๐ฒ"
    man_with_gua_pi_mao = "๐ฒ"
    man_with_chinese_cap_tone1 = "๐ฒ๐ป"
    man_with_gua_pi_mao_tone1 = "๐ฒ๐ป"
    man_with_chinese_cap_tone2 = "๐ฒ๐ผ"
    man_with_gua_pi_mao_tone2 = "๐ฒ๐ผ"
    man_with_chinese_cap_tone3 = "๐ฒ๐ฝ"
    man_with_gua_pi_mao_tone3 = "๐ฒ๐ฝ"
    man_with_chinese_cap_tone4 = "๐ฒ๐พ"
    man_with_gua_pi_mao_tone4 = "๐ฒ๐พ"
    man_with_chinese_cap_tone5 = "๐ฒ๐ฟ"
    man_with_gua_pi_mao_tone5 = "๐ฒ๐ฟ"
    person_wearing_turban = "๐ณ"
    man_with_turban = "๐ณ"
    person_wearing_turban_tone1 = "๐ณ๐ป"
    man_with_turban_tone1 = "๐ณ๐ป"
    person_wearing_turban_tone2 = "๐ณ๐ผ"
    man_with_turban_tone2 = "๐ณ๐ผ"
    person_wearing_turban_tone3 = "๐ณ๐ฝ"
    man_with_turban_tone3 = "๐ณ๐ฝ"
    person_wearing_turban_tone4 = "๐ณ๐พ"
    man_with_turban_tone4 = "๐ณ๐พ"
    person_wearing_turban_tone5 = "๐ณ๐ฟ"
    man_with_turban_tone5 = "๐ณ๐ฟ"
    woman_wearing_turban = "๐ณโ"
    woman_wearing_turban_tone1 = "๐ณ๐ปโ"
    woman_wearing_turban_light_skin_tone = "๐ณ๐ปโ"
    woman_wearing_turban_tone2 = "๐ณ๐ผโ"
    woman_wearing_turban_medium_light_skin_tone = "๐ณ๐ผโ"
    woman_wearing_turban_tone3 = "๐ณ๐ฝโ"
    woman_wearing_turban_medium_skin_tone = "๐ณ๐ฝโ"
    woman_wearing_turban_tone4 = "๐ณ๐พโ"
    woman_wearing_turban_medium_dark_skin_tone = "๐ณ๐พโ"
    woman_wearing_turban_tone5 = "๐ณ๐ฟโ"
    woman_wearing_turban_dark_skin_tone = "๐ณ๐ฟโ"
    man_wearing_turban = "๐ณโ"
    man_wearing_turban_tone1 = "๐ณ๐ปโ"
    man_wearing_turban_light_skin_tone = "๐ณ๐ปโ"
    man_wearing_turban_tone2 = "๐ณ๐ผโ"
    man_wearing_turban_medium_light_skin_tone = "๐ณ๐ผโ"
    man_wearing_turban_tone3 = "๐ณ๐ฝโ"
    man_wearing_turban_medium_skin_tone = "๐ณ๐ฝโ"
    man_wearing_turban_tone4 = "๐ณ๐พโ"
    man_wearing_turban_medium_dark_skin_tone = "๐ณ๐พโ"
    man_wearing_turban_tone5 = "๐ณ๐ฟโ"
    man_wearing_turban_dark_skin_tone = "๐ณ๐ฟโ"
    woman_with_headscarf = "๐ง"
    woman_with_headscarf_tone1 = "๐ง๐ป"
    woman_with_headscarf_light_skin_tone = "๐ง๐ป"
    woman_with_headscarf_tone2 = "๐ง๐ผ"
    woman_with_headscarf_medium_light_skin_tone = "๐ง๐ผ"
    woman_with_headscarf_tone3 = "๐ง๐ฝ"
    woman_with_headscarf_medium_skin_tone = "๐ง๐ฝ"
    woman_with_headscarf_tone4 = "๐ง๐พ"
    woman_with_headscarf_medium_dark_skin_tone = "๐ง๐พ"
    woman_with_headscarf_tone5 = "๐ง๐ฟ"
    woman_with_headscarf_dark_skin_tone = "๐ง๐ฟ"
    police_officer = "๐ฎ"
    cop = "๐ฎ"
    police_officer_tone1 = "๐ฎ๐ป"
    cop_tone1 = "๐ฎ๐ป"
    police_officer_tone2 = "๐ฎ๐ผ"
    cop_tone2 = "๐ฎ๐ผ"
    police_officer_tone3 = "๐ฎ๐ฝ"
    cop_tone3 = "๐ฎ๐ฝ"
    police_officer_tone4 = "๐ฎ๐พ"
    cop_tone4 = "๐ฎ๐พ"
    police_officer_tone5 = "๐ฎ๐ฟ"
    cop_tone5 = "๐ฎ๐ฟ"
    woman_police_officer = "๐ฎโ"
    woman_police_officer_tone1 = "๐ฎ๐ปโ"
    woman_police_officer_light_skin_tone = "๐ฎ๐ปโ"
    woman_police_officer_tone2 = "๐ฎ๐ผโ"
    woman_police_officer_medium_light_skin_tone = "๐ฎ๐ผโ"
    woman_police_officer_tone3 = "๐ฎ๐ฝโ"
    woman_police_officer_medium_skin_tone = "๐ฎ๐ฝโ"
    woman_police_officer_tone4 = "๐ฎ๐พโ"
    woman_police_officer_medium_dark_skin_tone = "๐ฎ๐พโ"
    woman_police_officer_tone5 = "๐ฎ๐ฟโ"
    woman_police_officer_dark_skin_tone = "๐ฎ๐ฟโ"
    man_police_officer = "๐ฎโ"
    man_police_officer_tone1 = "๐ฎ๐ปโ"
    man_police_officer_light_skin_tone = "๐ฎ๐ปโ"
    man_police_officer_tone2 = "๐ฎ๐ผโ"
    man_police_officer_medium_light_skin_tone = "๐ฎ๐ผโ"
    man_police_officer_tone3 = "๐ฎ๐ฝโ"
    man_police_officer_medium_skin_tone = "๐ฎ๐ฝโ"
    man_police_officer_tone4 = "๐ฎ๐พโ"
    man_police_officer_medium_dark_skin_tone = "๐ฎ๐พโ"
    man_police_officer_tone5 = "๐ฎ๐ฟโ"
    man_police_officer_dark_skin_tone = "๐ฎ๐ฟโ"
    construction_worker = "๐ท"
    construction_worker_tone1 = "๐ท๐ป"
    construction_worker_tone2 = "๐ท๐ผ"
    construction_worker_tone3 = "๐ท๐ฝ"
    construction_worker_tone4 = "๐ท๐พ"
    construction_worker_tone5 = "๐ท๐ฟ"
    woman_construction_worker = "๐ทโ"
    woman_construction_worker_tone1 = "๐ท๐ปโ"
    woman_construction_worker_light_skin_tone = "๐ท๐ปโ"
    woman_construction_worker_tone2 = "๐ท๐ผโ"
    woman_construction_worker_medium_light_skin_tone = "๐ท๐ผโ"
    woman_construction_worker_tone3 = "๐ท๐ฝโ"
    woman_construction_worker_medium_skin_tone = "๐ท๐ฝโ"
    woman_construction_worker_tone4 = "๐ท๐พโ"
    woman_construction_worker_medium_dark_skin_tone = "๐ท๐พโ"
    woman_construction_worker_tone5 = "๐ท๐ฟโ"
    woman_construction_worker_dark_skin_tone = "๐ท๐ฟโ"
    man_construction_worker = "๐ทโ"
    man_construction_worker_tone1 = "๐ท๐ปโ"
    man_construction_worker_light_skin_tone = "๐ท๐ปโ"
    man_construction_worker_tone2 = "๐ท๐ผโ"
    man_construction_worker_medium_light_skin_tone = "๐ท๐ผโ"
    man_construction_worker_tone3 = "๐ท๐ฝโ"
    man_construction_worker_medium_skin_tone = "๐ท๐ฝโ"
    man_construction_worker_tone4 = "๐ท๐พโ"
    man_construction_worker_medium_dark_skin_tone = "๐ท๐พโ"
    man_construction_worker_tone5 = "๐ท๐ฟโ"
    man_construction_worker_dark_skin_tone = "๐ท๐ฟโ"
    guard = "๐"
    guardsman = "๐"
    guard_tone1 = "๐๐ป"
    guardsman_tone1 = "๐๐ป"
    guard_tone2 = "๐๐ผ"
    guardsman_tone2 = "๐๐ผ"
    guard_tone3 = "๐๐ฝ"
    guardsman_tone3 = "๐๐ฝ"
    guard_tone4 = "๐๐พ"
    guardsman_tone4 = "๐๐พ"
    guard_tone5 = "๐๐ฟ"
    guardsman_tone5 = "๐๐ฟ"
    woman_guard = "๐โ"
    woman_guard_tone1 = "๐๐ปโ"
    woman_guard_light_skin_tone = "๐๐ปโ"
    woman_guard_tone2 = "๐๐ผโ"
    woman_guard_medium_light_skin_tone = "๐๐ผโ"
    woman_guard_tone3 = "๐๐ฝโ"
    woman_guard_medium_skin_tone = "๐๐ฝโ"
    woman_guard_tone4 = "๐๐พโ"
    woman_guard_medium_dark_skin_tone = "๐๐พโ"
    woman_guard_tone5 = "๐๐ฟโ"
    woman_guard_dark_skin_tone = "๐๐ฟโ"
    man_guard = "๐โ"
    man_guard_tone1 = "๐๐ปโ"
    man_guard_light_skin_tone = "๐๐ปโ"
    man_guard_tone2 = "๐๐ผโ"
    man_guard_medium_light_skin_tone = "๐๐ผโ"
    man_guard_tone3 = "๐๐ฝโ"
    man_guard_medium_skin_tone = "๐๐ฝโ"
    man_guard_tone4 = "๐๐พโ"
    man_guard_medium_dark_skin_tone = "๐๐พโ"
    man_guard_tone5 = "๐๐ฟโ"
    man_guard_dark_skin_tone = "๐๐ฟโ"
    detective = "๐ต"
    spy = "๐ต"
    sleuth_or_spy = "๐ต"
    detective_tone1 = "๐ต๐ป"
    spy_tone1 = "๐ต๐ป"
    sleuth_or_spy_tone1 = "๐ต๐ป"
    detective_tone2 = "๐ต๐ผ"
    spy_tone2 = "๐ต๐ผ"
    sleuth_or_spy_tone2 = "๐ต๐ผ"
    detective_tone3 = "๐ต๐ฝ"
    spy_tone3 = "๐ต๐ฝ"
    sleuth_or_spy_tone3 = "๐ต๐ฝ"
    detective_tone4 = "๐ต๐พ"
    spy_tone4 = "๐ต๐พ"
    sleuth_or_spy_tone4 = "๐ต๐พ"
    detective_tone5 = "๐ต๐ฟ"
    spy_tone5 = "๐ต๐ฟ"
    sleuth_or_spy_tone5 = "๐ต๐ฟ"
    woman_detective = "๐ตโ"
    woman_detective_tone1 = "๐ต๐ปโ"
    woman_detective_light_skin_tone = "๐ต๐ปโ"
    woman_detective_tone2 = "๐ต๐ผโ"
    woman_detective_medium_light_skin_tone = "๐ต๐ผโ"
    woman_detective_tone3 = "๐ต๐ฝโ"
    woman_detective_medium_skin_tone = "๐ต๐ฝโ"
    woman_detective_tone4 = "๐ต๐พโ"
    woman_detective_medium_dark_skin_tone = "๐ต๐พโ"
    woman_detective_tone5 = "๐ต๐ฟโ"
    woman_detective_dark_skin_tone = "๐ต๐ฟโ"
    man_detective = "๐ตโ"
    man_detective_tone1 = "๐ต๐ปโ"
    man_detective_light_skin_tone = "๐ต๐ปโ"
    man_detective_tone2 = "๐ต๐ผโ"
    man_detective_medium_light_skin_tone = "๐ต๐ผโ"
    man_detective_tone3 = "๐ต๐ฝโ"
    man_detective_medium_skin_tone = "๐ต๐ฝโ"
    man_detective_tone4 = "๐ต๐พโ"
    man_detective_medium_dark_skin_tone = "๐ต๐พโ"
    man_detective_tone5 = "๐ต๐ฟโ"
    man_detective_dark_skin_tone = "๐ต๐ฟโ"
    woman_health_worker = "๐ฉโ"
    woman_health_worker_tone1 = "๐ฉ๐ปโ"
    woman_health_worker_light_skin_tone = "๐ฉ๐ปโ"
    woman_health_worker_tone2 = "๐ฉ๐ผโ"
    woman_health_worker_medium_light_skin_tone = "๐ฉ๐ผโ"
    woman_health_worker_tone3 = "๐ฉ๐ฝโ"
    woman_health_worker_medium_skin_tone = "๐ฉ๐ฝโ"
    woman_health_worker_tone4 = "๐ฉ๐พโ"
    woman_health_worker_medium_dark_skin_tone = "๐ฉ๐พโ"
    woman_health_worker_tone5 = "๐ฉ๐ฟโ"
    woman_health_worker_dark_skin_tone = "๐ฉ๐ฟโ"
    man_health_worker = "๐จโ"
    man_health_worker_tone1 = "๐จ๐ปโ"
    man_health_worker_light_skin_tone = "๐จ๐ปโ"
    man_health_worker_tone2 = "๐จ๐ผโ"
    man_health_worker_medium_light_skin_tone = "๐จ๐ผโ"
    man_health_worker_tone3 = "๐จ๐ฝโ"
    man_health_worker_medium_skin_tone = "๐จ๐ฝโ"
    man_health_worker_tone4 = "๐จ๐พโ"
    man_health_worker_medium_dark_skin_tone = "๐จ๐พโ"
    man_health_worker_tone5 = "๐จ๐ฟโ"
    man_health_worker_dark_skin_tone = "๐จ๐ฟโ"
    woman_farmer = "๐ฉ๐พ"
    woman_farmer_tone1 = "๐ฉ๐ป๐พ"
    woman_farmer_light_skin_tone = "๐ฉ๐ป๐พ"
    woman_farmer_tone2 = "๐ฉ๐ผ๐พ"
    woman_farmer_medium_light_skin_tone = "๐ฉ๐ผ๐พ"
    woman_farmer_tone3 = "๐ฉ๐ฝ๐พ"
    woman_farmer_medium_skin_tone = "๐ฉ๐ฝ๐พ"
    woman_farmer_tone4 = "๐ฉ๐พ๐พ"
    woman_farmer_medium_dark_skin_tone = "๐ฉ๐พ๐พ"
    woman_farmer_tone5 = "๐ฉ๐ฟ๐พ"
    woman_farmer_dark_skin_tone = "๐ฉ๐ฟ๐พ"
    man_farmer = "๐จ๐พ"
    man_farmer_tone1 = "๐จ๐ป๐พ"
    man_farmer_light_skin_tone = "๐จ๐ป๐พ"
    man_farmer_tone2 = "๐จ๐ผ๐พ"
    man_farmer_medium_light_skin_tone = "๐จ๐ผ๐พ"
    man_farmer_tone3 = "๐จ๐ฝ๐พ"
    man_farmer_medium_skin_tone = "๐จ๐ฝ๐พ"
    man_farmer_tone4 = "๐จ๐พ๐พ"
    man_farmer_medium_dark_skin_tone = "๐จ๐พ๐พ"
    man_farmer_tone5 = "๐จ๐ฟ๐พ"
    man_farmer_dark_skin_tone = "๐จ๐ฟ๐พ"
    woman_cook = "๐ฉ๐ณ"
    woman_cook_tone1 = "๐ฉ๐ป๐ณ"
    woman_cook_light_skin_tone = "๐ฉ๐ป๐ณ"
    woman_cook_tone2 = "๐ฉ๐ผ๐ณ"
    woman_cook_medium_light_skin_tone = "๐ฉ๐ผ๐ณ"
    woman_cook_tone3 = "๐ฉ๐ฝ๐ณ"
    woman_cook_medium_skin_tone = "๐ฉ๐ฝ๐ณ"
    woman_cook_tone4 = "๐ฉ๐พ๐ณ"
    woman_cook_medium_dark_skin_tone = "๐ฉ๐พ๐ณ"
    woman_cook_tone5 = "๐ฉ๐ฟ๐ณ"
    woman_cook_dark_skin_tone = "๐ฉ๐ฟ๐ณ"
    man_cook = "๐จ๐ณ"
    man_cook_tone1 = "๐จ๐ป๐ณ"
    man_cook_light_skin_tone = "๐จ๐ป๐ณ"
    man_cook_tone2 = "๐จ๐ผ๐ณ"
    man_cook_medium_light_skin_tone = "๐จ๐ผ๐ณ"
    man_cook_tone3 = "๐จ๐ฝ๐ณ"
    man_cook_medium_skin_tone = "๐จ๐ฝ๐ณ"
    man_cook_tone4 = "๐จ๐พ๐ณ"
    man_cook_medium_dark_skin_tone = "๐จ๐พ๐ณ"
    man_cook_tone5 = "๐จ๐ฟ๐ณ"
    man_cook_dark_skin_tone = "๐จ๐ฟ๐ณ"
    woman_student = "๐ฉ๐"
    woman_student_tone1 = "๐ฉ๐ป๐"
    woman_student_light_skin_tone = "๐ฉ๐ป๐"
    woman_student_tone2 = "๐ฉ๐ผ๐"
    woman_student_medium_light_skin_tone = "๐ฉ๐ผ๐"
    woman_student_tone3 = "๐ฉ๐ฝ๐"
    woman_student_medium_skin_tone = "๐ฉ๐ฝ๐"
    woman_student_tone4 = "๐ฉ๐พ๐"
    woman_student_medium_dark_skin_tone = "๐ฉ๐พ๐"
    woman_student_tone5 = "๐ฉ๐ฟ๐"
    woman_student_dark_skin_tone = "๐ฉ๐ฟ๐"
    man_student = "๐จ๐"
    man_student_tone1 = "๐จ๐ป๐"
    man_student_light_skin_tone = "๐จ๐ป๐"
    man_student_tone2 = "๐จ๐ผ๐"
    man_student_medium_light_skin_tone = "๐จ๐ผ๐"
    man_student_tone3 = "๐จ๐ฝ๐"
    man_student_medium_skin_tone = "๐จ๐ฝ๐"
    man_student_tone4 = "๐จ๐พ๐"
    man_student_medium_dark_skin_tone = "๐จ๐พ๐"
    man_student_tone5 = "๐จ๐ฟ๐"
    man_student_dark_skin_tone = "๐จ๐ฟ๐"
    woman_singer = "๐ฉ๐ค"
    woman_singer_tone1 = "๐ฉ๐ป๐ค"
    woman_singer_light_skin_tone = "๐ฉ๐ป๐ค"
    woman_singer_tone2 = "๐ฉ๐ผ๐ค"
    woman_singer_medium_light_skin_tone = "๐ฉ๐ผ๐ค"
    woman_singer_tone3 = "๐ฉ๐ฝ๐ค"
    woman_singer_medium_skin_tone = "๐ฉ๐ฝ๐ค"
    woman_singer_tone4 = "๐ฉ๐พ๐ค"
    woman_singer_medium_dark_skin_tone = "๐ฉ๐พ๐ค"
    woman_singer_tone5 = "๐ฉ๐ฟ๐ค"
    woman_singer_dark_skin_tone = "๐ฉ๐ฟ๐ค"
    man_singer = "๐จ๐ค"
    man_singer_tone1 = "๐จ๐ป๐ค"
    man_singer_light_skin_tone = "๐จ๐ป๐ค"
    man_singer_tone2 = "๐จ๐ผ๐ค"
    man_singer_medium_light_skin_tone = "๐จ๐ผ๐ค"
    man_singer_tone3 = "๐จ๐ฝ๐ค"
    man_singer_medium_skin_tone = "๐จ๐ฝ๐ค"
    man_singer_tone4 = "๐จ๐พ๐ค"
    man_singer_medium_dark_skin_tone = "๐จ๐พ๐ค"
    man_singer_tone5 = "๐จ๐ฟ๐ค"
    man_singer_dark_skin_tone = "๐จ๐ฟ๐ค"
    woman_teacher = "๐ฉ๐ซ"
    woman_teacher_tone1 = "๐ฉ๐ป๐ซ"
    woman_teacher_light_skin_tone = "๐ฉ๐ป๐ซ"
    woman_teacher_tone2 = "๐ฉ๐ผ๐ซ"
    woman_teacher_medium_light_skin_tone = "๐ฉ๐ผ๐ซ"
    woman_teacher_tone3 = "๐ฉ๐ฝ๐ซ"
    woman_teacher_medium_skin_tone = "๐ฉ๐ฝ๐ซ"
    woman_teacher_tone4 = "๐ฉ๐พ๐ซ"
    woman_teacher_medium_dark_skin_tone = "๐ฉ๐พ๐ซ"
    woman_teacher_tone5 = "๐ฉ๐ฟ๐ซ"
    woman_teacher_dark_skin_tone = "๐ฉ๐ฟ๐ซ"
    man_teacher = "๐จ๐ซ"
    man_teacher_tone1 = "๐จ๐ป๐ซ"
    man_teacher_light_skin_tone = "๐จ๐ป๐ซ"
    man_teacher_tone2 = "๐จ๐ผ๐ซ"
    man_teacher_medium_light_skin_tone = "๐จ๐ผ๐ซ"
    man_teacher_tone3 = "๐จ๐ฝ๐ซ"
    man_teacher_medium_skin_tone = "๐จ๐ฝ๐ซ"
    man_teacher_tone4 = "๐จ๐พ๐ซ"
    man_teacher_medium_dark_skin_tone = "๐จ๐พ๐ซ"
    man_teacher_tone5 = "๐จ๐ฟ๐ซ"
    man_teacher_dark_skin_tone = "๐จ๐ฟ๐ซ"
    woman_factory_worker = "๐ฉ๐ญ"
    woman_factory_worker_tone1 = "๐ฉ๐ป๐ญ"
    woman_factory_worker_light_skin_tone = "๐ฉ๐ป๐ญ"
    woman_factory_worker_tone2 = "๐ฉ๐ผ๐ญ"
    woman_factory_worker_medium_light_skin_tone = "๐ฉ๐ผ๐ญ"
    woman_factory_worker_tone3 = "๐ฉ๐ฝ๐ญ"
    woman_factory_worker_medium_skin_tone = "๐ฉ๐ฝ๐ญ"
    woman_factory_worker_tone4 = "๐ฉ๐พ๐ญ"
    woman_factory_worker_medium_dark_skin_tone = "๐ฉ๐พ๐ญ"
    woman_factory_worker_tone5 = "๐ฉ๐ฟ๐ญ"
    woman_factory_worker_dark_skin_tone = "๐ฉ๐ฟ๐ญ"
    man_factory_worker = "๐จ๐ญ"
    man_factory_worker_tone1 = "๐จ๐ป๐ญ"
    man_factory_worker_light_skin_tone = "๐จ๐ป๐ญ"
    man_factory_worker_tone2 = "๐จ๐ผ๐ญ"
    man_factory_worker_medium_light_skin_tone = "๐จ๐ผ๐ญ"
    man_factory_worker_tone3 = "๐จ๐ฝ๐ญ"
    man_factory_worker_medium_skin_tone = "๐จ๐ฝ๐ญ"
    man_factory_worker_tone4 = "๐จ๐พ๐ญ"
    man_factory_worker_medium_dark_skin_tone = "๐จ๐พ๐ญ"
    man_factory_worker_tone5 = "๐จ๐ฟ๐ญ"
    man_factory_worker_dark_skin_tone = "๐จ๐ฟ๐ญ"
    woman_technologist = "๐ฉ๐ป"
    woman_technologist_tone1 = "๐ฉ๐ป๐ป"
    woman_technologist_light_skin_tone = "๐ฉ๐ป๐ป"
    woman_technologist_tone2 = "๐ฉ๐ผ๐ป"
    woman_technologist_medium_light_skin_tone = "๐ฉ๐ผ๐ป"
    woman_technologist_tone3 = "๐ฉ๐ฝ๐ป"
    woman_technologist_medium_skin_tone = "๐ฉ๐ฝ๐ป"
    woman_technologist_tone4 = "๐ฉ๐พ๐ป"
    woman_technologist_medium_dark_skin_tone = "๐ฉ๐พ๐ป"
    woman_technologist_tone5 = "๐ฉ๐ฟ๐ป"
    woman_technologist_dark_skin_tone = "๐ฉ๐ฟ๐ป"
    man_technologist = "๐จ๐ป"
    man_technologist_tone1 = "๐จ๐ป๐ป"
    man_technologist_light_skin_tone = "๐จ๐ป๐ป"
    man_technologist_tone2 = "๐จ๐ผ๐ป"
    man_technologist_medium_light_skin_tone = "๐จ๐ผ๐ป"
    man_technologist_tone3 = "๐จ๐ฝ๐ป"
    man_technologist_medium_skin_tone = "๐จ๐ฝ๐ป"
    man_technologist_tone4 = "๐จ๐พ๐ป"
    man_technologist_medium_dark_skin_tone = "๐จ๐พ๐ป"
    man_technologist_tone5 = "๐จ๐ฟ๐ป"
    man_technologist_dark_skin_tone = "๐จ๐ฟ๐ป"
    woman_office_worker = "๐ฉ๐ผ"
    woman_office_worker_tone1 = "๐ฉ๐ป๐ผ"
    woman_office_worker_light_skin_tone = "๐ฉ๐ป๐ผ"
    woman_office_worker_tone2 = "๐ฉ๐ผ๐ผ"
    woman_office_worker_medium_light_skin_tone = "๐ฉ๐ผ๐ผ"
    woman_office_worker_tone3 = "๐ฉ๐ฝ๐ผ"
    woman_office_worker_medium_skin_tone = "๐ฉ๐ฝ๐ผ"
    woman_office_worker_tone4 = "๐ฉ๐พ๐ผ"
    woman_office_worker_medium_dark_skin_tone = "๐ฉ๐พ๐ผ"
    woman_office_worker_tone5 = "๐ฉ๐ฟ๐ผ"
    woman_office_worker_dark_skin_tone = "๐ฉ๐ฟ๐ผ"
    man_office_worker = "๐จ๐ผ"
    man_office_worker_tone1 = "๐จ๐ป๐ผ"
    man_office_worker_light_skin_tone = "๐จ๐ป๐ผ"
    man_office_worker_tone2 = "๐จ๐ผ๐ผ"
    man_office_worker_medium_light_skin_tone = "๐จ๐ผ๐ผ"
    man_office_worker_tone3 = "๐จ๐ฝ๐ผ"
    man_office_worker_medium_skin_tone = "๐จ๐ฝ๐ผ"
    man_office_worker_tone4 = "๐จ๐พ๐ผ"
    man_office_worker_medium_dark_skin_tone = "๐จ๐พ๐ผ"
    man_office_worker_tone5 = "๐จ๐ฟ๐ผ"
    man_office_worker_dark_skin_tone = "๐จ๐ฟ๐ผ"
    woman_mechanic = "๐ฉ๐ง"
    woman_mechanic_tone1 = "๐ฉ๐ป๐ง"
    woman_mechanic_light_skin_tone = "๐ฉ๐ป๐ง"
    woman_mechanic_tone2 = "๐ฉ๐ผ๐ง"
    woman_mechanic_medium_light_skin_tone = "๐ฉ๐ผ๐ง"
    woman_mechanic_tone3 = "๐ฉ๐ฝ๐ง"
    woman_mechanic_medium_skin_tone = "๐ฉ๐ฝ๐ง"
    woman_mechanic_tone4 = "๐ฉ๐พ๐ง"
    woman_mechanic_medium_dark_skin_tone = "๐ฉ๐พ๐ง"
    woman_mechanic_tone5 = "๐ฉ๐ฟ๐ง"
    woman_mechanic_dark_skin_tone = "๐ฉ๐ฟ๐ง"
    man_mechanic = "๐จ๐ง"
    man_mechanic_tone1 = "๐จ๐ป๐ง"
    man_mechanic_light_skin_tone = "๐จ๐ป๐ง"
    man_mechanic_tone2 = "๐จ๐ผ๐ง"
    man_mechanic_medium_light_skin_tone = "๐จ๐ผ๐ง"
    man_mechanic_tone3 = "๐จ๐ฝ๐ง"
    man_mechanic_medium_skin_tone = "๐จ๐ฝ๐ง"
    man_mechanic_tone4 = "๐จ๐พ๐ง"
    man_mechanic_medium_dark_skin_tone = "๐จ๐พ๐ง"
    man_mechanic_tone5 = "๐จ๐ฟ๐ง"
    man_mechanic_dark_skin_tone = "๐จ๐ฟ๐ง"
    woman_scientist = "๐ฉ๐ฌ"
    woman_scientist_tone1 = "๐ฉ๐ป๐ฌ"
    woman_scientist_light_skin_tone = "๐ฉ๐ป๐ฌ"
    woman_scientist_tone2 = "๐ฉ๐ผ๐ฌ"
    woman_scientist_medium_light_skin_tone = "๐ฉ๐ผ๐ฌ"
    woman_scientist_tone3 = "๐ฉ๐ฝ๐ฌ"
    woman_scientist_medium_skin_tone = "๐ฉ๐ฝ๐ฌ"
    woman_scientist_tone4 = "๐ฉ๐พ๐ฌ"
    woman_scientist_medium_dark_skin_tone = "๐ฉ๐พ๐ฌ"
    woman_scientist_tone5 = "๐ฉ๐ฟ๐ฌ"
    woman_scientist_dark_skin_tone = "๐ฉ๐ฟ๐ฌ"
    man_scientist = "๐จ๐ฌ"
    man_scientist_tone1 = "๐จ๐ป๐ฌ"
    man_scientist_light_skin_tone = "๐จ๐ป๐ฌ"
    man_scientist_tone2 = "๐จ๐ผ๐ฌ"
    man_scientist_medium_light_skin_tone = "๐จ๐ผ๐ฌ"
    man_scientist_tone3 = "๐จ๐ฝ๐ฌ"
    man_scientist_medium_skin_tone = "๐จ๐ฝ๐ฌ"
    man_scientist_tone4 = "๐จ๐พ๐ฌ"
    man_scientist_medium_dark_skin_tone = "๐จ๐พ๐ฌ"
    man_scientist_tone5 = "๐จ๐ฟ๐ฌ"
    man_scientist_dark_skin_tone = "๐จ๐ฟ๐ฌ"
    woman_artist = "๐ฉ๐จ"
    woman_artist_tone1 = "๐ฉ๐ป๐จ"
    woman_artist_light_skin_tone = "๐ฉ๐ป๐จ"
    woman_artist_tone2 = "๐ฉ๐ผ๐จ"
    woman_artist_medium_light_skin_tone = "๐ฉ๐ผ๐จ"
    woman_artist_tone3 = "๐ฉ๐ฝ๐จ"
    woman_artist_medium_skin_tone = "๐ฉ๐ฝ๐จ"
    woman_artist_tone4 = "๐ฉ๐พ๐จ"
    woman_artist_medium_dark_skin_tone = "๐ฉ๐พ๐จ"
    woman_artist_tone5 = "๐ฉ๐ฟ๐จ"
    woman_artist_dark_skin_tone = "๐ฉ๐ฟ๐จ"
    man_artist = "๐จ๐จ"
    man_artist_tone1 = "๐จ๐ป๐จ"
    man_artist_light_skin_tone = "๐จ๐ป๐จ"
    man_artist_tone2 = "๐จ๐ผ๐จ"
    man_artist_medium_light_skin_tone = "๐จ๐ผ๐จ"
    man_artist_tone3 = "๐จ๐ฝ๐จ"
    man_artist_medium_skin_tone = "๐จ๐ฝ๐จ"
    man_artist_tone4 = "๐จ๐พ๐จ"
    man_artist_medium_dark_skin_tone = "๐จ๐พ๐จ"
    man_artist_tone5 = "๐จ๐ฟ๐จ"
    man_artist_dark_skin_tone = "๐จ๐ฟ๐จ"
    woman_firefighter = "๐ฉ๐"
    woman_firefighter_tone1 = "๐ฉ๐ป๐"
    woman_firefighter_light_skin_tone = "๐ฉ๐ป๐"
    woman_firefighter_tone2 = "๐ฉ๐ผ๐"
    woman_firefighter_medium_light_skin_tone = "๐ฉ๐ผ๐"
    woman_firefighter_tone3 = "๐ฉ๐ฝ๐"
    woman_firefighter_medium_skin_tone = "๐ฉ๐ฝ๐"
    woman_firefighter_tone4 = "๐ฉ๐พ๐"
    woman_firefighter_medium_dark_skin_tone = "๐ฉ๐พ๐"
    woman_firefighter_tone5 = "๐ฉ๐ฟ๐"
    woman_firefighter_dark_skin_tone = "๐ฉ๐ฟ๐"
    man_firefighter = "๐จ๐"
    man_firefighter_tone1 = "๐จ๐ป๐"
    man_firefighter_light_skin_tone = "๐จ๐ป๐"
    man_firefighter_tone2 = "๐จ๐ผ๐"
    man_firefighter_medium_light_skin_tone = "๐จ๐ผ๐"
    man_firefighter_tone3 = "๐จ๐ฝ๐"
    man_firefighter_medium_skin_tone = "๐จ๐ฝ๐"
    man_firefighter_tone4 = "๐จ๐พ๐"
    man_firefighter_medium_dark_skin_tone = "๐จ๐พ๐"
    man_firefighter_tone5 = "๐จ๐ฟ๐"
    man_firefighter_dark_skin_tone = "๐จ๐ฟ๐"
    woman_pilot = "๐ฉโ"
    woman_pilot_tone1 = "๐ฉ๐ปโ"
    woman_pilot_light_skin_tone = "๐ฉ๐ปโ"
    woman_pilot_tone2 = "๐ฉ๐ผโ"
    woman_pilot_medium_light_skin_tone = "๐ฉ๐ผโ"
    woman_pilot_tone3 = "๐ฉ๐ฝโ"
    woman_pilot_medium_skin_tone = "๐ฉ๐ฝโ"
    woman_pilot_tone4 = "๐ฉ๐พโ"
    woman_pilot_medium_dark_skin_tone = "๐ฉ๐พโ"
    woman_pilot_tone5 = "๐ฉ๐ฟโ"
    woman_pilot_dark_skin_tone = "๐ฉ๐ฟโ"
    man_pilot = "๐จโ"
    man_pilot_tone1 = "๐จ๐ปโ"
    man_pilot_light_skin_tone = "๐จ๐ปโ"
    man_pilot_tone2 = "๐จ๐ผโ"
    man_pilot_medium_light_skin_tone = "๐จ๐ผโ"
    man_pilot_tone3 = "๐จ๐ฝโ"
    man_pilot_medium_skin_tone = "๐จ๐ฝโ"
    man_pilot_tone4 = "๐จ๐พโ"
    man_pilot_medium_dark_skin_tone = "๐จ๐พโ"
    man_pilot_tone5 = "๐จ๐ฟโ"
    man_pilot_dark_skin_tone = "๐จ๐ฟโ"
    woman_astronaut = "๐ฉ๐"
    woman_astronaut_tone1 = "๐ฉ๐ป๐"
    woman_astronaut_light_skin_tone = "๐ฉ๐ป๐"
    woman_astronaut_tone2 = "๐ฉ๐ผ๐"
    woman_astronaut_medium_light_skin_tone = "๐ฉ๐ผ๐"
    woman_astronaut_tone3 = "๐ฉ๐ฝ๐"
    woman_astronaut_medium_skin_tone = "๐ฉ๐ฝ๐"
    woman_astronaut_tone4 = "๐ฉ๐พ๐"
    woman_astronaut_medium_dark_skin_tone = "๐ฉ๐พ๐"
    woman_astronaut_tone5 = "๐ฉ๐ฟ๐"
    woman_astronaut_dark_skin_tone = "๐ฉ๐ฟ๐"
    man_astronaut = "๐จ๐"
    man_astronaut_tone1 = "๐จ๐ป๐"
    man_astronaut_light_skin_tone = "๐จ๐ป๐"
    man_astronaut_tone2 = "๐จ๐ผ๐"
    man_astronaut_medium_light_skin_tone = "๐จ๐ผ๐"
    man_astronaut_tone3 = "๐จ๐ฝ๐"
    man_astronaut_medium_skin_tone = "๐จ๐ฝ๐"
    man_astronaut_tone4 = "๐จ๐พ๐"
    man_astronaut_medium_dark_skin_tone = "๐จ๐พ๐"
    man_astronaut_tone5 = "๐จ๐ฟ๐"
    man_astronaut_dark_skin_tone = "๐จ๐ฟ๐"
    woman_judge = "๐ฉโ"
    woman_judge_tone1 = "๐ฉ๐ปโ"
    woman_judge_light_skin_tone = "๐ฉ๐ปโ"
    woman_judge_tone2 = "๐ฉ๐ผโ"
    woman_judge_medium_light_skin_tone = "๐ฉ๐ผโ"
    woman_judge_tone3 = "๐ฉ๐ฝโ"
    woman_judge_medium_skin_tone = "๐ฉ๐ฝโ"
    woman_judge_tone4 = "๐ฉ๐พโ"
    woman_judge_medium_dark_skin_tone = "๐ฉ๐พโ"
    woman_judge_tone5 = "๐ฉ๐ฟโ"
    woman_judge_dark_skin_tone = "๐ฉ๐ฟโ"
    man_judge = "๐จโ"
    man_judge_tone1 = "๐จ๐ปโ"
    man_judge_light_skin_tone = "๐จ๐ปโ"
    man_judge_tone2 = "๐จ๐ผโ"
    man_judge_medium_light_skin_tone = "๐จ๐ผโ"
    man_judge_tone3 = "๐จ๐ฝโ"
    man_judge_medium_skin_tone = "๐จ๐ฝโ"
    man_judge_tone4 = "๐จ๐พโ"
    man_judge_medium_dark_skin_tone = "๐จ๐พโ"
    man_judge_tone5 = "๐จ๐ฟโ"
    man_judge_dark_skin_tone = "๐จ๐ฟโ"
    bride_with_veil = "๐ฐ"
    bride_with_veil_tone1 = "๐ฐ๐ป"
    bride_with_veil_tone2 = "๐ฐ๐ผ"
    bride_with_veil_tone3 = "๐ฐ๐ฝ"
    bride_with_veil_tone4 = "๐ฐ๐พ"
    bride_with_veil_tone5 = "๐ฐ๐ฟ"
    man_in_tuxedo = "๐คต"
    man_in_tuxedo_tone1 = "๐คต๐ป"
    tuxedo_tone1 = "๐คต๐ป"
    man_in_tuxedo_tone2 = "๐คต๐ผ"
    tuxedo_tone2 = "๐คต๐ผ"
    man_in_tuxedo_tone3 = "๐คต๐ฝ"
    tuxedo_tone3 = "๐คต๐ฝ"
    man_in_tuxedo_tone4 = "๐คต๐พ"
    tuxedo_tone4 = "๐คต๐พ"
    man_in_tuxedo_tone5 = "๐คต๐ฟ"
    tuxedo_tone5 = "๐คต๐ฟ"
    princess = "๐ธ"
    princess_tone1 = "๐ธ๐ป"
    princess_tone2 = "๐ธ๐ผ"
    princess_tone3 = "๐ธ๐ฝ"
    princess_tone4 = "๐ธ๐พ"
    princess_tone5 = "๐ธ๐ฟ"
    prince = "๐คด"
    prince_tone1 = "๐คด๐ป"
    prince_tone2 = "๐คด๐ผ"
    prince_tone3 = "๐คด๐ฝ"
    prince_tone4 = "๐คด๐พ"
    prince_tone5 = "๐คด๐ฟ"
    superhero = "๐ฆธ"
    superhero_tone1 = "๐ฆธ๐ป"
    superhero_light_skin_tone = "๐ฆธ๐ป"
    superhero_tone2 = "๐ฆธ๐ผ"
    superhero_medium_light_skin_tone = "๐ฆธ๐ผ"
    superhero_tone3 = "๐ฆธ๐ฝ"
    superhero_medium_skin_tone = "๐ฆธ๐ฝ"
    superhero_tone4 = "๐ฆธ๐พ"
    superhero_medium_dark_skin_tone = "๐ฆธ๐พ"
    superhero_tone5 = "๐ฆธ๐ฟ"
    superhero_dark_skin_tone = "๐ฆธ๐ฟ"
    woman_superhero = "๐ฆธโ"
    woman_superhero_tone1 = "๐ฆธ๐ปโ"
    woman_superhero_light_skin_tone = "๐ฆธ๐ปโ"
    woman_superhero_tone2 = "๐ฆธ๐ผโ"
    woman_superhero_medium_light_skin_tone = "๐ฆธ๐ผโ"
    woman_superhero_tone3 = "๐ฆธ๐ฝโ"
    woman_superhero_medium_skin_tone = "๐ฆธ๐ฝโ"
    woman_superhero_tone4 = "๐ฆธ๐พโ"
    woman_superhero_medium_dark_skin_tone = "๐ฆธ๐พโ"
    woman_superhero_tone5 = "๐ฆธ๐ฟโ"
    woman_superhero_dark_skin_tone = "๐ฆธ๐ฟโ"
    man_superhero = "๐ฆธโ"
    man_superhero_tone1 = "๐ฆธ๐ปโ"
    man_superhero_light_skin_tone = "๐ฆธ๐ปโ"
    man_superhero_tone2 = "๐ฆธ๐ผโ"
    man_superhero_medium_light_skin_tone = "๐ฆธ๐ผโ"
    man_superhero_tone3 = "๐ฆธ๐ฝโ"
    man_superhero_medium_skin_tone = "๐ฆธ๐ฝโ"
    man_superhero_tone4 = "๐ฆธ๐พโ"
    man_superhero_medium_dark_skin_tone = "๐ฆธ๐พโ"
    man_superhero_tone5 = "๐ฆธ๐ฟโ"
    man_superhero_dark_skin_tone = "๐ฆธ๐ฟโ"
    supervillain = "๐ฆน"
    supervillain_tone1 = "๐ฆน๐ป"
    supervillain_light_skin_tone = "๐ฆน๐ป"
    supervillain_tone2 = "๐ฆน๐ผ"
    supervillain_medium_light_skin_tone = "๐ฆน๐ผ"
    supervillain_tone3 = "๐ฆน๐ฝ"
    supervillain_medium_skin_tone = "๐ฆน๐ฝ"
    supervillain_tone4 = "๐ฆน๐พ"
    supervillain_medium_dark_skin_tone = "๐ฆน๐พ"
    supervillain_tone5 = "๐ฆน๐ฟ"
    supervillain_dark_skin_tone = "๐ฆน๐ฟ"
    woman_supervillain = "๐ฆนโ"
    woman_supervillain_tone1 = "๐ฆน๐ปโ"
    woman_supervillain_light_skin_tone = "๐ฆน๐ปโ"
    woman_supervillain_tone2 = "๐ฆน๐ผโ"
    woman_supervillain_medium_light_skin_tone = "๐ฆน๐ผโ"
    woman_supervillain_tone3 = "๐ฆน๐ฝโ"
    woman_supervillain_medium_skin_tone = "๐ฆน๐ฝโ"
    woman_supervillain_tone4 = "๐ฆน๐พโ"
    woman_supervillain_medium_dark_skin_tone = "๐ฆน๐พโ"
    woman_supervillain_tone5 = "๐ฆน๐ฟโ"
    woman_supervillain_dark_skin_tone = "๐ฆน๐ฟโ"
    man_supervillain = "๐ฆนโ"
    man_supervillain_tone1 = "๐ฆน๐ปโ"
    man_supervillain_light_skin_tone = "๐ฆน๐ปโ"
    man_supervillain_tone2 = "๐ฆน๐ผโ"
    man_supervillain_medium_light_skin_tone = "๐ฆน๐ผโ"
    man_supervillain_tone3 = "๐ฆน๐ฝโ"
    man_supervillain_medium_skin_tone = "๐ฆน๐ฝโ"
    man_supervillain_tone4 = "๐ฆน๐พโ"
    man_supervillain_medium_dark_skin_tone = "๐ฆน๐พโ"
    man_supervillain_tone5 = "๐ฆน๐ฟโ"
    man_supervillain_dark_skin_tone = "๐ฆน๐ฟโ"
    mrs_claus = "๐คถ"
    mother_christmas = "๐คถ"
    mrs_claus_tone1 = "๐คถ๐ป"
    mother_christmas_tone1 = "๐คถ๐ป"
    mrs_claus_tone2 = "๐คถ๐ผ"
    mother_christmas_tone2 = "๐คถ๐ผ"
    mrs_claus_tone3 = "๐คถ๐ฝ"
    mother_christmas_tone3 = "๐คถ๐ฝ"
    mrs_claus_tone4 = "๐คถ๐พ"
    mother_christmas_tone4 = "๐คถ๐พ"
    mrs_claus_tone5 = "๐คถ๐ฟ"
    mother_christmas_tone5 = "๐คถ๐ฟ"
    santa = "๐"
    santa_tone1 = "๐๐ป"
    santa_tone2 = "๐๐ผ"
    santa_tone3 = "๐๐ฝ"
    santa_tone4 = "๐๐พ"
    santa_tone5 = "๐๐ฟ"
    mage = "๐ง"
    mage_tone1 = "๐ง๐ป"
    mage_light_skin_tone = "๐ง๐ป"
    mage_tone2 = "๐ง๐ผ"
    mage_medium_light_skin_tone = "๐ง๐ผ"
    mage_tone3 = "๐ง๐ฝ"
    mage_medium_skin_tone = "๐ง๐ฝ"
    mage_tone4 = "๐ง๐พ"
    mage_medium_dark_skin_tone = "๐ง๐พ"
    mage_tone5 = "๐ง๐ฟ"
    mage_dark_skin_tone = "๐ง๐ฟ"
    woman_mage = "๐งโ"
    woman_mage_tone1 = "๐ง๐ปโ"
    woman_mage_light_skin_tone = "๐ง๐ปโ"
    woman_mage_tone2 = "๐ง๐ผโ"
    woman_mage_medium_light_skin_tone = "๐ง๐ผโ"
    woman_mage_tone3 = "๐ง๐ฝโ"
    woman_mage_medium_skin_tone = "๐ง๐ฝโ"
    woman_mage_tone4 = "๐ง๐พโ"
    woman_mage_medium_dark_skin_tone = "๐ง๐พโ"
    woman_mage_tone5 = "๐ง๐ฟโ"
    woman_mage_dark_skin_tone = "๐ง๐ฟโ"
    man_mage = "๐งโ"
    man_mage_tone1 = "๐ง๐ปโ"
    man_mage_light_skin_tone = "๐ง๐ปโ"
    man_mage_tone2 = "๐ง๐ผโ"
    man_mage_medium_light_skin_tone = "๐ง๐ผโ"
    man_mage_tone3 = "๐ง๐ฝโ"
    man_mage_medium_skin_tone = "๐ง๐ฝโ"
    man_mage_tone4 = "๐ง๐พโ"
    man_mage_medium_dark_skin_tone = "๐ง๐พโ"
    man_mage_tone5 = "๐ง๐ฟโ"
    man_mage_dark_skin_tone = "๐ง๐ฟโ"
    elf = "๐ง"
    elf_tone1 = "๐ง๐ป"
    elf_light_skin_tone = "๐ง๐ป"
    elf_tone2 = "๐ง๐ผ"
    elf_medium_light_skin_tone = "๐ง๐ผ"
    elf_tone3 = "๐ง๐ฝ"
    elf_medium_skin_tone = "๐ง๐ฝ"
    elf_tone4 = "๐ง๐พ"
    elf_medium_dark_skin_tone = "๐ง๐พ"
    elf_tone5 = "๐ง๐ฟ"
    elf_dark_skin_tone = "๐ง๐ฟ"
    woman_elf = "๐งโ"
    woman_elf_tone1 = "๐ง๐ปโ"
    woman_elf_light_skin_tone = "๐ง๐ปโ"
    woman_elf_tone2 = "๐ง๐ผโ"
    woman_elf_medium_light_skin_tone = "๐ง๐ผโ"
    woman_elf_tone3 = "๐ง๐ฝโ"
    woman_elf_medium_skin_tone = "๐ง๐ฝโ"
    woman_elf_tone4 = "๐ง๐พโ"
    woman_elf_medium_dark_skin_tone = "๐ง๐พโ"
    woman_elf_tone5 = "๐ง๐ฟโ"
    woman_elf_dark_skin_tone = "๐ง๐ฟโ"
    man_elf = "๐งโ"
    man_elf_tone1 = "๐ง๐ปโ"
    man_elf_light_skin_tone = "๐ง๐ปโ"
    man_elf_tone2 = "๐ง๐ผโ"
    man_elf_medium_light_skin_tone = "๐ง๐ผโ"
    man_elf_tone3 = "๐ง๐ฝโ"
    man_elf_medium_skin_tone = "๐ง๐ฝโ"
    man_elf_tone4 = "๐ง๐พโ"
    man_elf_medium_dark_skin_tone = "๐ง๐พโ"
    man_elf_tone5 = "๐ง๐ฟโ"
    man_elf_dark_skin_tone = "๐ง๐ฟโ"
    vampire = "๐ง"
    vampire_tone1 = "๐ง๐ป"
    vampire_light_skin_tone = "๐ง๐ป"
    vampire_tone2 = "๐ง๐ผ"
    vampire_medium_light_skin_tone = "๐ง๐ผ"
    vampire_tone3 = "๐ง๐ฝ"
    vampire_medium_skin_tone = "๐ง๐ฝ"
    vampire_tone4 = "๐ง๐พ"
    vampire_medium_dark_skin_tone = "๐ง๐พ"
    vampire_tone5 = "๐ง๐ฟ"
    vampire_dark_skin_tone = "๐ง๐ฟ"
    woman_vampire = "๐งโ"
    woman_vampire_tone1 = "๐ง๐ปโ"
    woman_vampire_light_skin_tone = "๐ง๐ปโ"
    woman_vampire_tone2 = "๐ง๐ผโ"
    woman_vampire_medium_light_skin_tone = "๐ง๐ผโ"
    woman_vampire_tone3 = "๐ง๐ฝโ"
    woman_vampire_medium_skin_tone = "๐ง๐ฝโ"
    woman_vampire_tone4 = "๐ง๐พโ"
    woman_vampire_medium_dark_skin_tone = "๐ง๐พโ"
    woman_vampire_tone5 = "๐ง๐ฟโ"
    woman_vampire_dark_skin_tone = "๐ง๐ฟโ"
    man_vampire = "๐งโ"
    man_vampire_tone1 = "๐ง๐ปโ"
    man_vampire_light_skin_tone = "๐ง๐ปโ"
    man_vampire_tone2 = "๐ง๐ผโ"
    man_vampire_medium_light_skin_tone = "๐ง๐ผโ"
    man_vampire_tone3 = "๐ง๐ฝโ"
    man_vampire_medium_skin_tone = "๐ง๐ฝโ"
    man_vampire_tone4 = "๐ง๐พโ"
    man_vampire_medium_dark_skin_tone = "๐ง๐พโ"
    man_vampire_tone5 = "๐ง๐ฟโ"
    man_vampire_dark_skin_tone = "๐ง๐ฟโ"
    zombie = "๐ง"
    woman_zombie = "๐งโ"
    man_zombie = "๐งโ"
    genie = "๐ง"
    woman_genie = "๐งโ"
    man_genie = "๐งโ"
    merperson = "๐ง"
    merperson_tone1 = "๐ง๐ป"
    merperson_light_skin_tone = "๐ง๐ป"
    merperson_tone2 = "๐ง๐ผ"
    merperson_medium_light_skin_tone = "๐ง๐ผ"
    merperson_tone3 = "๐ง๐ฝ"
    merperson_medium_skin_tone = "๐ง๐ฝ"
    merperson_tone4 = "๐ง๐พ"
    merperson_medium_dark_skin_tone = "๐ง๐พ"
    merperson_tone5 = "๐ง๐ฟ"
    merperson_dark_skin_tone = "๐ง๐ฟ"
    mermaid = "๐งโ"
    mermaid_tone1 = "๐ง๐ปโ"
    mermaid_light_skin_tone = "๐ง๐ปโ"
    mermaid_tone2 = "๐ง๐ผโ"
    mermaid_medium_light_skin_tone = "๐ง๐ผโ"
    mermaid_tone3 = "๐ง๐ฝโ"
    mermaid_medium_skin_tone = "๐ง๐ฝโ"
    mermaid_tone4 = "๐ง๐พโ"
    mermaid_medium_dark_skin_tone = "๐ง๐พโ"
    mermaid_tone5 = "๐ง๐ฟโ"
    mermaid_dark_skin_tone = "๐ง๐ฟโ"
    merman = "๐งโ"
    merman_tone1 = "๐ง๐ปโ"
    merman_light_skin_tone = "๐ง๐ปโ"
    merman_tone2 = "๐ง๐ผโ"
    merman_medium_light_skin_tone = "๐ง๐ผโ"
    merman_tone3 = "๐ง๐ฝโ"
    merman_medium_skin_tone = "๐ง๐ฝโ"
    merman_tone4 = "๐ง๐พโ"
    merman_medium_dark_skin_tone = "๐ง๐พโ"
    merman_tone5 = "๐ง๐ฟโ"
    merman_dark_skin_tone = "๐ง๐ฟโ"
    fairy = "๐ง"
    fairy_tone1 = "๐ง๐ป"
    fairy_light_skin_tone = "๐ง๐ป"
    fairy_tone2 = "๐ง๐ผ"
    fairy_medium_light_skin_tone = "๐ง๐ผ"
    fairy_tone3 = "๐ง๐ฝ"
    fairy_medium_skin_tone = "๐ง๐ฝ"
    fairy_tone4 = "๐ง๐พ"
    fairy_medium_dark_skin_tone = "๐ง๐พ"
    fairy_tone5 = "๐ง๐ฟ"
    fairy_dark_skin_tone = "๐ง๐ฟ"
    woman_fairy = "๐งโ"
    woman_fairy_tone1 = "๐ง๐ปโ"
    woman_fairy_light_skin_tone = "๐ง๐ปโ"
    woman_fairy_tone2 = "๐ง๐ผโ"
    woman_fairy_medium_light_skin_tone = "๐ง๐ผโ"
    woman_fairy_tone3 = "๐ง๐ฝโ"
    woman_fairy_medium_skin_tone = "๐ง๐ฝโ"
    woman_fairy_tone4 = "๐ง๐พโ"
    woman_fairy_medium_dark_skin_tone = "๐ง๐พโ"
    woman_fairy_tone5 = "๐ง๐ฟโ"
    woman_fairy_dark_skin_tone = "๐ง๐ฟโ"
    man_fairy = "๐งโ"
    man_fairy_tone1 = "๐ง๐ปโ"
    man_fairy_light_skin_tone = "๐ง๐ปโ"
    man_fairy_tone2 = "๐ง๐ผโ"
    man_fairy_medium_light_skin_tone = "๐ง๐ผโ"
    man_fairy_tone3 = "๐ง๐ฝโ"
    man_fairy_medium_skin_tone = "๐ง๐ฝโ"
    man_fairy_tone4 = "๐ง๐พโ"
    man_fairy_medium_dark_skin_tone = "๐ง๐พโ"
    man_fairy_tone5 = "๐ง๐ฟโ"
    man_fairy_dark_skin_tone = "๐ง๐ฟโ"
    angel = "๐ผ"
    angel_tone1 = "๐ผ๐ป"
    angel_tone2 = "๐ผ๐ผ"
    angel_tone3 = "๐ผ๐ฝ"
    angel_tone4 = "๐ผ๐พ"
    angel_tone5 = "๐ผ๐ฟ"
    pregnant_woman = "๐คฐ"
    expecting_woman = "๐คฐ"
    pregnant_woman_tone1 = "๐คฐ๐ป"
    expecting_woman_tone1 = "๐คฐ๐ป"
    pregnant_woman_tone2 = "๐คฐ๐ผ"
    expecting_woman_tone2 = "๐คฐ๐ผ"
    pregnant_woman_tone3 = "๐คฐ๐ฝ"
    expecting_woman_tone3 = "๐คฐ๐ฝ"
    pregnant_woman_tone4 = "๐คฐ๐พ"
    expecting_woman_tone4 = "๐คฐ๐พ"
    pregnant_woman_tone5 = "๐คฐ๐ฟ"
    expecting_woman_tone5 = "๐คฐ๐ฟ"
    breast_feeding = "๐คฑ"
    breast_feeding_tone1 = "๐คฑ๐ป"
    breast_feeding_light_skin_tone = "๐คฑ๐ป"
    breast_feeding_tone2 = "๐คฑ๐ผ"
    breast_feeding_medium_light_skin_tone = "๐คฑ๐ผ"
    breast_feeding_tone3 = "๐คฑ๐ฝ"
    breast_feeding_medium_skin_tone = "๐คฑ๐ฝ"
    breast_feeding_tone4 = "๐คฑ๐พ"
    breast_feeding_medium_dark_skin_tone = "๐คฑ๐พ"
    breast_feeding_tone5 = "๐คฑ๐ฟ"
    breast_feeding_dark_skin_tone = "๐คฑ๐ฟ"
    person_bowing = "๐"
    bow = "๐"
    person_bowing_tone1 = "๐๐ป"
    bow_tone1 = "๐๐ป"
    person_bowing_tone2 = "๐๐ผ"
    bow_tone2 = "๐๐ผ"
    person_bowing_tone3 = "๐๐ฝ"
    bow_tone3 = "๐๐ฝ"
    person_bowing_tone4 = "๐๐พ"
    bow_tone4 = "๐๐พ"
    person_bowing_tone5 = "๐๐ฟ"
    bow_tone5 = "๐๐ฟ"
    woman_bowing = "๐โ"
    woman_bowing_tone1 = "๐๐ปโ"
    woman_bowing_light_skin_tone = "๐๐ปโ"
    woman_bowing_tone2 = "๐๐ผโ"
    woman_bowing_medium_light_skin_tone = "๐๐ผโ"
    woman_bowing_tone3 = "๐๐ฝโ"
    woman_bowing_medium_skin_tone = "๐๐ฝโ"
    woman_bowing_tone4 = "๐๐พโ"
    woman_bowing_medium_dark_skin_tone = "๐๐พโ"
    woman_bowing_tone5 = "๐๐ฟโ"
    woman_bowing_dark_skin_tone = "๐๐ฟโ"
    man_bowing = "๐โ"
    man_bowing_tone1 = "๐๐ปโ"
    man_bowing_light_skin_tone = "๐๐ปโ"
    man_bowing_tone2 = "๐๐ผโ"
    man_bowing_medium_light_skin_tone = "๐๐ผโ"
    man_bowing_tone3 = "๐๐ฝโ"
    man_bowing_medium_skin_tone = "๐๐ฝโ"
    man_bowing_tone4 = "๐๐พโ"
    man_bowing_medium_dark_skin_tone = "๐๐พโ"
    man_bowing_tone5 = "๐๐ฟโ"
    man_bowing_dark_skin_tone = "๐๐ฟโ"
    person_tipping_hand = "๐"
    information_desk_person = "๐"
    person_tipping_hand_tone1 = "๐๐ป"
    information_desk_person_tone1 = "๐๐ป"
    person_tipping_hand_tone2 = "๐๐ผ"
    information_desk_person_tone2 = "๐๐ผ"
    person_tipping_hand_tone3 = "๐๐ฝ"
    information_desk_person_tone3 = "๐๐ฝ"
    person_tipping_hand_tone4 = "๐๐พ"
    information_desk_person_tone4 = "๐๐พ"
    person_tipping_hand_tone5 = "๐๐ฟ"
    information_desk_person_tone5 = "๐๐ฟ"
    woman_tipping_hand = "๐โ"
    woman_tipping_hand_tone1 = "๐๐ปโ"
    woman_tipping_hand_light_skin_tone = "๐๐ปโ"
    woman_tipping_hand_tone2 = "๐๐ผโ"
    woman_tipping_hand_medium_light_skin_tone = "๐๐ผโ"
    woman_tipping_hand_tone3 = "๐๐ฝโ"
    woman_tipping_hand_medium_skin_tone = "๐๐ฝโ"
    woman_tipping_hand_tone4 = "๐๐พโ"
    woman_tipping_hand_medium_dark_skin_tone = "๐๐พโ"
    woman_tipping_hand_tone5 = "๐๐ฟโ"
    woman_tipping_hand_dark_skin_tone = "๐๐ฟโ"
    man_tipping_hand = "๐โ"
    man_tipping_hand_tone1 = "๐๐ปโ"
    man_tipping_hand_light_skin_tone = "๐๐ปโ"
    man_tipping_hand_tone2 = "๐๐ผโ"
    man_tipping_hand_medium_light_skin_tone = "๐๐ผโ"
    man_tipping_hand_tone3 = "๐๐ฝโ"
    man_tipping_hand_medium_skin_tone = "๐๐ฝโ"
    man_tipping_hand_tone4 = "๐๐พโ"
    man_tipping_hand_medium_dark_skin_tone = "๐๐พโ"
    man_tipping_hand_tone5 = "๐๐ฟโ"
    man_tipping_hand_dark_skin_tone = "๐๐ฟโ"
    person_gesturing_no = "๐"
    no_good = "๐"
    person_gesturing_no_tone1 = "๐๐ป"
    no_good_tone1 = "๐๐ป"
    person_gesturing_no_tone2 = "๐๐ผ"
    no_good_tone2 = "๐๐ผ"
    person_gesturing_no_tone3 = "๐๐ฝ"
    no_good_tone3 = "๐๐ฝ"
    person_gesturing_no_tone4 = "๐๐พ"
    no_good_tone4 = "๐๐พ"
    person_gesturing_no_tone5 = "๐๐ฟ"
    no_good_tone5 = "๐๐ฟ"
    woman_gesturing_no = "๐โ"
    woman_gesturing_no_tone1 = "๐๐ปโ"
    woman_gesturing_no_light_skin_tone = "๐๐ปโ"
    woman_gesturing_no_tone2 = "๐๐ผโ"
    woman_gesturing_no_medium_light_skin_tone = "๐๐ผโ"
    woman_gesturing_no_tone3 = "๐๐ฝโ"
    woman_gesturing_no_medium_skin_tone = "๐๐ฝโ"
    woman_gesturing_no_tone4 = "๐๐พโ"
    woman_gesturing_no_medium_dark_skin_tone = "๐๐พโ"
    woman_gesturing_no_tone5 = "๐๐ฟโ"
    woman_gesturing_no_dark_skin_tone = "๐๐ฟโ"
    man_gesturing_no = "๐โ"
    man_gesturing_no_tone1 = "๐๐ปโ"
    man_gesturing_no_light_skin_tone = "๐๐ปโ"
    man_gesturing_no_tone2 = "๐๐ผโ"
    man_gesturing_no_medium_light_skin_tone = "๐๐ผโ"
    man_gesturing_no_tone3 = "๐๐ฝโ"
    man_gesturing_no_medium_skin_tone = "๐๐ฝโ"
    man_gesturing_no_tone4 = "๐๐พโ"
    man_gesturing_no_medium_dark_skin_tone = "๐๐พโ"
    man_gesturing_no_tone5 = "๐๐ฟโ"
    man_gesturing_no_dark_skin_tone = "๐๐ฟโ"
    person_gesturing_ok = "๐"
    ok_woman = "๐"
    person_gesturing_ok_tone1 = "๐๐ป"
    ok_woman_tone1 = "๐๐ป"
    person_gesturing_ok_tone2 = "๐๐ผ"
    ok_woman_tone2 = "๐๐ผ"
    person_gesturing_ok_tone3 = "๐๐ฝ"
    ok_woman_tone3 = "๐๐ฝ"
    person_gesturing_ok_tone4 = "๐๐พ"
    ok_woman_tone4 = "๐๐พ"
    person_gesturing_ok_tone5 = "๐๐ฟ"
    ok_woman_tone5 = "๐๐ฟ"
    woman_gesturing_ok = "๐โ"
    woman_gesturing_ok_tone1 = "๐๐ปโ"
    woman_gesturing_ok_light_skin_tone = "๐๐ปโ"
    woman_gesturing_ok_tone2 = "๐๐ผโ"
    woman_gesturing_ok_medium_light_skin_tone = "๐๐ผโ"
    woman_gesturing_ok_tone3 = "๐๐ฝโ"
    woman_gesturing_ok_medium_skin_tone = "๐๐ฝโ"
    woman_gesturing_ok_tone4 = "๐๐พโ"
    woman_gesturing_ok_medium_dark_skin_tone = "๐๐พโ"
    woman_gesturing_ok_tone5 = "๐๐ฟโ"
    woman_gesturing_ok_dark_skin_tone = "๐๐ฟโ"
    man_gesturing_ok = "๐โ"
    man_gesturing_ok_tone1 = "๐๐ปโ"
    man_gesturing_ok_light_skin_tone = "๐๐ปโ"
    man_gesturing_ok_tone2 = "๐๐ผโ"
    man_gesturing_ok_medium_light_skin_tone = "๐๐ผโ"
    man_gesturing_ok_tone3 = "๐๐ฝโ"
    man_gesturing_ok_medium_skin_tone = "๐๐ฝโ"
    man_gesturing_ok_tone4 = "๐๐พโ"
    man_gesturing_ok_medium_dark_skin_tone = "๐๐พโ"
    man_gesturing_ok_tone5 = "๐๐ฟโ"
    man_gesturing_ok_dark_skin_tone = "๐๐ฟโ"
    person_raising_hand = "๐"
    raising_hand = "๐"
    person_raising_hand_tone1 = "๐๐ป"
    raising_hand_tone1 = "๐๐ป"
    person_raising_hand_tone2 = "๐๐ผ"
    raising_hand_tone2 = "๐๐ผ"
    person_raising_hand_tone3 = "๐๐ฝ"
    raising_hand_tone3 = "๐๐ฝ"
    person_raising_hand_tone4 = "๐๐พ"
    raising_hand_tone4 = "๐๐พ"
    person_raising_hand_tone5 = "๐๐ฟ"
    raising_hand_tone5 = "๐๐ฟ"
    woman_raising_hand = "๐โ"
    woman_raising_hand_tone1 = "๐๐ปโ"
    woman_raising_hand_light_skin_tone = "๐๐ปโ"
    woman_raising_hand_tone2 = "๐๐ผโ"
    woman_raising_hand_medium_light_skin_tone = "๐๐ผโ"
    woman_raising_hand_tone3 = "๐๐ฝโ"
    woman_raising_hand_medium_skin_tone = "๐๐ฝโ"
    woman_raising_hand_tone4 = "๐๐พโ"
    woman_raising_hand_medium_dark_skin_tone = "๐๐พโ"
    woman_raising_hand_tone5 = "๐๐ฟโ"
    woman_raising_hand_dark_skin_tone = "๐๐ฟโ"
    man_raising_hand = "๐โ"
    man_raising_hand_tone1 = "๐๐ปโ"
    man_raising_hand_light_skin_tone = "๐๐ปโ"
    man_raising_hand_tone2 = "๐๐ผโ"
    man_raising_hand_medium_light_skin_tone = "๐๐ผโ"
    man_raising_hand_tone3 = "๐๐ฝโ"
    man_raising_hand_medium_skin_tone = "๐๐ฝโ"
    man_raising_hand_tone4 = "๐๐พโ"
    man_raising_hand_medium_dark_skin_tone = "๐๐พโ"
    man_raising_hand_tone5 = "๐๐ฟโ"
    man_raising_hand_dark_skin_tone = "๐๐ฟโ"
    deaf_person = "๐ง"
    deaf_person_tone1 = "๐ง๐ป"
    deaf_person_light_skin_tone = "๐ง๐ป"
    deaf_person_tone2 = "๐ง๐ผ"
    deaf_person_medium_light_skin_tone = "๐ง๐ผ"
    deaf_person_tone3 = "๐ง๐ฝ"
    deaf_person_medium_skin_tone = "๐ง๐ฝ"
    deaf_person_tone4 = "๐ง๐พ"
    deaf_person_medium_dark_skin_tone = "๐ง๐พ"
    deaf_person_tone5 = "๐ง๐ฟ"
    deaf_person_dark_skin_tone = "๐ง๐ฟ"
    deaf_woman = "๐งโ"
    deaf_woman_tone1 = "๐ง๐ปโ"
    deaf_woman_light_skin_tone = "๐ง๐ปโ"
    deaf_woman_tone2 = "๐ง๐ผโ"
    deaf_woman_medium_light_skin_tone = "๐ง๐ผโ"
    deaf_woman_tone3 = "๐ง๐ฝโ"
    deaf_woman_medium_skin_tone = "๐ง๐ฝโ"
    deaf_woman_tone4 = "๐ง๐พโ"
    deaf_woman_medium_dark_skin_tone = "๐ง๐พโ"
    deaf_woman_tone5 = "๐ง๐ฟโ"
    deaf_woman_dark_skin_tone = "๐ง๐ฟโ"
    deaf_man = "๐งโ"
    deaf_man_tone1 = "๐ง๐ปโ"
    deaf_man_light_skin_tone = "๐ง๐ปโ"
    deaf_man_tone2 = "๐ง๐ผโ"
    deaf_man_medium_light_skin_tone = "๐ง๐ผโ"
    deaf_man_tone3 = "๐ง๐ฝโ"
    deaf_man_medium_skin_tone = "๐ง๐ฝโ"
    deaf_man_tone4 = "๐ง๐พโ"
    deaf_man_medium_dark_skin_tone = "๐ง๐พโ"
    deaf_man_tone5 = "๐ง๐ฟโ"
    deaf_man_dark_skin_tone = "๐ง๐ฟโ"
    person_facepalming = "๐คฆ"
    face_palm = "๐คฆ"
    facepalm = "๐คฆ"
    person_facepalming_tone1 = "๐คฆ๐ป"
    face_palm_tone1 = "๐คฆ๐ป"
    facepalm_tone1 = "๐คฆ๐ป"
    person_facepalming_tone2 = "๐คฆ๐ผ"
    face_palm_tone2 = "๐คฆ๐ผ"
    facepalm_tone2 = "๐คฆ๐ผ"
    person_facepalming_tone3 = "๐คฆ๐ฝ"
    face_palm_tone3 = "๐คฆ๐ฝ"
    facepalm_tone3 = "๐คฆ๐ฝ"
    person_facepalming_tone4 = "๐คฆ๐พ"
    face_palm_tone4 = "๐คฆ๐พ"
    facepalm_tone4 = "๐คฆ๐พ"
    person_facepalming_tone5 = "๐คฆ๐ฟ"
    face_palm_tone5 = "๐คฆ๐ฟ"
    facepalm_tone5 = "๐คฆ๐ฟ"
    woman_facepalming = "๐คฆโ"
    woman_facepalming_tone1 = "๐คฆ๐ปโ"
    woman_facepalming_light_skin_tone = "๐คฆ๐ปโ"
    woman_facepalming_tone2 = "๐คฆ๐ผโ"
    woman_facepalming_medium_light_skin_tone = "๐คฆ๐ผโ"
    woman_facepalming_tone3 = "๐คฆ๐ฝโ"
    woman_facepalming_medium_skin_tone = "๐คฆ๐ฝโ"
    woman_facepalming_tone4 = "๐คฆ๐พโ"
    woman_facepalming_medium_dark_skin_tone = "๐คฆ๐พโ"
    woman_facepalming_tone5 = "๐คฆ๐ฟโ"
    woman_facepalming_dark_skin_tone = "๐คฆ๐ฟโ"
    man_facepalming = "๐คฆโ"
    man_facepalming_tone1 = "๐คฆ๐ปโ"
    man_facepalming_light_skin_tone = "๐คฆ๐ปโ"
    man_facepalming_tone2 = "๐คฆ๐ผโ"
    man_facepalming_medium_light_skin_tone = "๐คฆ๐ผโ"
    man_facepalming_tone3 = "๐คฆ๐ฝโ"
    man_facepalming_medium_skin_tone = "๐คฆ๐ฝโ"
    man_facepalming_tone4 = "๐คฆ๐พโ"
    man_facepalming_medium_dark_skin_tone = "๐คฆ๐พโ"
    man_facepalming_tone5 = "๐คฆ๐ฟโ"
    man_facepalming_dark_skin_tone = "๐คฆ๐ฟโ"
    person_shrugging = "๐คท"
    shrug = "๐คท"
    person_shrugging_tone1 = "๐คท๐ป"
    shrug_tone1 = "๐คท๐ป"
    person_shrugging_tone2 = "๐คท๐ผ"
    shrug_tone2 = "๐คท๐ผ"
    person_shrugging_tone3 = "๐คท๐ฝ"
    shrug_tone3 = "๐คท๐ฝ"
    person_shrugging_tone4 = "๐คท๐พ"
    shrug_tone4 = "๐คท๐พ"
    person_shrugging_tone5 = "๐คท๐ฟ"
    shrug_tone5 = "๐คท๐ฟ"
    woman_shrugging = "๐คทโ"
    woman_shrugging_tone1 = "๐คท๐ปโ"
    woman_shrugging_light_skin_tone = "๐คท๐ปโ"
    woman_shrugging_tone2 = "๐คท๐ผโ"
    woman_shrugging_medium_light_skin_tone = "๐คท๐ผโ"
    woman_shrugging_tone3 = "๐คท๐ฝโ"
    woman_shrugging_medium_skin_tone = "๐คท๐ฝโ"
    woman_shrugging_tone4 = "๐คท๐พโ"
    woman_shrugging_medium_dark_skin_tone = "๐คท๐พโ"
    woman_shrugging_tone5 = "๐คท๐ฟโ"
    woman_shrugging_dark_skin_tone = "๐คท๐ฟโ"
    man_shrugging = "๐คทโ"
    man_shrugging_tone1 = "๐คท๐ปโ"
    man_shrugging_light_skin_tone = "๐คท๐ปโ"
    man_shrugging_tone2 = "๐คท๐ผโ"
    man_shrugging_medium_light_skin_tone = "๐คท๐ผโ"
    man_shrugging_tone3 = "๐คท๐ฝโ"
    man_shrugging_medium_skin_tone = "๐คท๐ฝโ"
    man_shrugging_tone4 = "๐คท๐พโ"
    man_shrugging_medium_dark_skin_tone = "๐คท๐พโ"
    man_shrugging_tone5 = "๐คท๐ฟโ"
    man_shrugging_dark_skin_tone = "๐คท๐ฟโ"
    person_pouting = "๐"
    person_with_pouting_face = "๐"
    person_pouting_tone1 = "๐๐ป"
    person_with_pouting_face_tone1 = "๐๐ป"
    person_pouting_tone2 = "๐๐ผ"
    person_with_pouting_face_tone2 = "๐๐ผ"
    person_pouting_tone3 = "๐๐ฝ"
    person_with_pouting_face_tone3 = "๐๐ฝ"
    person_pouting_tone4 = "๐๐พ"
    person_with_pouting_face_tone4 = "๐๐พ"
    person_pouting_tone5 = "๐๐ฟ"
    person_with_pouting_face_tone5 = "๐๐ฟ"
    woman_pouting = "๐โ"
    woman_pouting_tone1 = "๐๐ปโ"
    woman_pouting_light_skin_tone = "๐๐ปโ"
    woman_pouting_tone2 = "๐๐ผโ"
    woman_pouting_medium_light_skin_tone = "๐๐ผโ"
    woman_pouting_tone3 = "๐๐ฝโ"
    woman_pouting_medium_skin_tone = "๐๐ฝโ"
    woman_pouting_tone4 = "๐๐พโ"
    woman_pouting_medium_dark_skin_tone = "๐๐พโ"
    woman_pouting_tone5 = "๐๐ฟโ"
    woman_pouting_dark_skin_tone = "๐๐ฟโ"
    man_pouting = "๐โ"
    man_pouting_tone1 = "๐๐ปโ"
    man_pouting_light_skin_tone = "๐๐ปโ"
    man_pouting_tone2 = "๐๐ผโ"
    man_pouting_medium_light_skin_tone = "๐๐ผโ"
    man_pouting_tone3 = "๐๐ฝโ"
    man_pouting_medium_skin_tone = "๐๐ฝโ"
    man_pouting_tone4 = "๐๐พโ"
    man_pouting_medium_dark_skin_tone = "๐๐พโ"
    man_pouting_tone5 = "๐๐ฟโ"
    man_pouting_dark_skin_tone = "๐๐ฟโ"
    person_frowning = "๐"
    person_frowning_tone1 = "๐๐ป"
    person_frowning_tone2 = "๐๐ผ"
    person_frowning_tone3 = "๐๐ฝ"
    person_frowning_tone4 = "๐๐พ"
    person_frowning_tone5 = "๐๐ฟ"
    woman_frowning = "๐โ"
    woman_frowning_tone1 = "๐๐ปโ"
    woman_frowning_light_skin_tone = "๐๐ปโ"
    woman_frowning_tone2 = "๐๐ผโ"
    woman_frowning_medium_light_skin_tone = "๐๐ผโ"
    woman_frowning_tone3 = "๐๐ฝโ"
    woman_frowning_medium_skin_tone = "๐๐ฝโ"
    woman_frowning_tone4 = "๐๐พโ"
    woman_frowning_medium_dark_skin_tone = "๐๐พโ"
    woman_frowning_tone5 = "๐๐ฟโ"
    woman_frowning_dark_skin_tone = "๐๐ฟโ"
    man_frowning = "๐โ"
    man_frowning_tone1 = "๐๐ปโ"
    man_frowning_light_skin_tone = "๐๐ปโ"
    man_frowning_tone2 = "๐๐ผโ"
    man_frowning_medium_light_skin_tone = "๐๐ผโ"
    man_frowning_tone3 = "๐๐ฝโ"
    man_frowning_medium_skin_tone = "๐๐ฝโ"
    man_frowning_tone4 = "๐๐พโ"
    man_frowning_medium_dark_skin_tone = "๐๐พโ"
    man_frowning_tone5 = "๐๐ฟโ"
    man_frowning_dark_skin_tone = "๐๐ฟโ"
    person_getting_haircut = "๐"
    haircut = "๐"
    person_getting_haircut_tone1 = "๐๐ป"
    haircut_tone1 = "๐๐ป"
    person_getting_haircut_tone2 = "๐๐ผ"
    haircut_tone2 = "๐๐ผ"
    person_getting_haircut_tone3 = "๐๐ฝ"
    haircut_tone3 = "๐๐ฝ"
    person_getting_haircut_tone4 = "๐๐พ"
    haircut_tone4 = "๐๐พ"
    person_getting_haircut_tone5 = "๐๐ฟ"
    haircut_tone5 = "๐๐ฟ"
    woman_getting_haircut = "๐โ"
    woman_getting_haircut_tone1 = "๐๐ปโ"
    woman_getting_haircut_light_skin_tone = "๐๐ปโ"
    woman_getting_haircut_tone2 = "๐๐ผโ"
    woman_getting_haircut_medium_light_skin_tone = "๐๐ผโ"
    woman_getting_haircut_tone3 = "๐๐ฝโ"
    woman_getting_haircut_medium_skin_tone = "๐๐ฝโ"
    woman_getting_haircut_tone4 = "๐๐พโ"
    woman_getting_haircut_medium_dark_skin_tone = "๐๐พโ"
    woman_getting_haircut_tone5 = "๐๐ฟโ"
    woman_getting_haircut_dark_skin_tone = "๐๐ฟโ"
    man_getting_haircut = "๐โ"
    man_getting_haircut_tone1 = "๐๐ปโ"
    man_getting_haircut_light_skin_tone = "๐๐ปโ"
    man_getting_haircut_tone2 = "๐๐ผโ"
    man_getting_haircut_medium_light_skin_tone = "๐๐ผโ"
    man_getting_haircut_tone3 = "๐๐ฝโ"
    man_getting_haircut_medium_skin_tone = "๐๐ฝโ"
    man_getting_haircut_tone4 = "๐๐พโ"
    man_getting_haircut_medium_dark_skin_tone = "๐๐พโ"
    man_getting_haircut_tone5 = "๐๐ฟโ"
    man_getting_haircut_dark_skin_tone = "๐๐ฟโ"
    person_getting_massage = "๐"
    massage = "๐"
    person_getting_massage_tone1 = "๐๐ป"
    massage_tone1 = "๐๐ป"
    person_getting_massage_tone2 = "๐๐ผ"
    massage_tone2 = "๐๐ผ"
    person_getting_massage_tone3 = "๐๐ฝ"
    massage_tone3 = "๐๐ฝ"
    person_getting_massage_tone4 = "๐๐พ"
    massage_tone4 = "๐๐พ"
    person_getting_massage_tone5 = "๐๐ฟ"
    massage_tone5 = "๐๐ฟ"
    woman_getting_face_massage = "๐โ"
    woman_getting_face_massage_tone1 = "๐๐ปโ"
    woman_getting_face_massage_light_skin_tone = "๐๐ปโ"
    woman_getting_face_massage_tone2 = "๐๐ผโ"
    woman_getting_face_massage_medium_light_skin_tone = "๐๐ผโ"
    woman_getting_face_massage_tone3 = "๐๐ฝโ"
    woman_getting_face_massage_medium_skin_tone = "๐๐ฝโ"
    woman_getting_face_massage_tone4 = "๐๐พโ"
    woman_getting_face_massage_medium_dark_skin_tone = "๐๐พโ"
    woman_getting_face_massage_tone5 = "๐๐ฟโ"
    woman_getting_face_massage_dark_skin_tone = "๐๐ฟโ"
    man_getting_face_massage = "๐โ"
    man_getting_face_massage_tone1 = "๐๐ปโ"
    man_getting_face_massage_light_skin_tone = "๐๐ปโ"
    man_getting_face_massage_tone2 = "๐๐ผโ"
    man_getting_face_massage_medium_light_skin_tone = "๐๐ผโ"
    man_getting_face_massage_tone3 = "๐๐ฝโ"
    man_getting_face_massage_medium_skin_tone = "๐๐ฝโ"
    man_getting_face_massage_tone4 = "๐๐พโ"
    man_getting_face_massage_medium_dark_skin_tone = "๐๐พโ"
    man_getting_face_massage_tone5 = "๐๐ฟโ"
    man_getting_face_massage_dark_skin_tone = "๐๐ฟโ"
    person_in_steamy_room = "๐ง"
    person_in_steamy_room_tone1 = "๐ง๐ป"
    person_in_steamy_room_light_skin_tone = "๐ง๐ป"
    person_in_steamy_room_tone2 = "๐ง๐ผ"
    person_in_steamy_room_medium_light_skin_tone = "๐ง๐ผ"
    person_in_steamy_room_tone3 = "๐ง๐ฝ"
    person_in_steamy_room_medium_skin_tone = "๐ง๐ฝ"
    person_in_steamy_room_tone4 = "๐ง๐พ"
    person_in_steamy_room_medium_dark_skin_tone = "๐ง๐พ"
    person_in_steamy_room_tone5 = "๐ง๐ฟ"
    person_in_steamy_room_dark_skin_tone = "๐ง๐ฟ"
    woman_in_steamy_room = "๐งโ"
    woman_in_steamy_room_tone1 = "๐ง๐ปโ"
    woman_in_steamy_room_light_skin_tone = "๐ง๐ปโ"
    woman_in_steamy_room_tone2 = "๐ง๐ผโ"
    woman_in_steamy_room_medium_light_skin_tone = "๐ง๐ผโ"
    woman_in_steamy_room_tone3 = "๐ง๐ฝโ"
    woman_in_steamy_room_medium_skin_tone = "๐ง๐ฝโ"
    woman_in_steamy_room_tone4 = "๐ง๐พโ"
    woman_in_steamy_room_medium_dark_skin_tone = "๐ง๐พโ"
    woman_in_steamy_room_tone5 = "๐ง๐ฟโ"
    woman_in_steamy_room_dark_skin_tone = "๐ง๐ฟโ"
    man_in_steamy_room = "๐งโ"
    man_in_steamy_room_tone1 = "๐ง๐ปโ"
    man_in_steamy_room_light_skin_tone = "๐ง๐ปโ"
    man_in_steamy_room_tone2 = "๐ง๐ผโ"
    man_in_steamy_room_medium_light_skin_tone = "๐ง๐ผโ"
    man_in_steamy_room_tone3 = "๐ง๐ฝโ"
    man_in_steamy_room_medium_skin_tone = "๐ง๐ฝโ"
    man_in_steamy_room_tone4 = "๐ง๐พโ"
    man_in_steamy_room_medium_dark_skin_tone = "๐ง๐พโ"
    man_in_steamy_room_tone5 = "๐ง๐ฟโ"
    man_in_steamy_room_dark_skin_tone = "๐ง๐ฟโ"
    nail_care = "๐"
    nail_care_tone1 = "๐๐ป"
    nail_care_tone2 = "๐๐ผ"
    nail_care_tone3 = "๐๐ฝ"
    nail_care_tone4 = "๐๐พ"
    nail_care_tone5 = "๐๐ฟ"
    selfie = "๐คณ"
    selfie_tone1 = "๐คณ๐ป"
    selfie_tone2 = "๐คณ๐ผ"
    selfie_tone3 = "๐คณ๐ฝ"
    selfie_tone4 = "๐คณ๐พ"
    selfie_tone5 = "๐คณ๐ฟ"
    dancer = "๐"
    dancer_tone1 = "๐๐ป"
    dancer_tone2 = "๐๐ผ"
    dancer_tone3 = "๐๐ฝ"
    dancer_tone4 = "๐๐พ"
    dancer_tone5 = "๐๐ฟ"
    man_dancing = "๐บ"
    male_dancer = "๐บ"
    man_dancing_tone1 = "๐บ๐ป"
    male_dancer_tone1 = "๐บ๐ป"
    man_dancing_tone2 = "๐บ๐ผ"
    male_dancer_tone2 = "๐บ๐ผ"
    man_dancing_tone3 = "๐บ๐ฝ"
    male_dancer_tone3 = "๐บ๐ฝ"
    man_dancing_tone5 = "๐บ๐ฟ"
    male_dancer_tone5 = "๐บ๐ฟ"
    man_dancing_tone4 = "๐บ๐พ"
    male_dancer_tone4 = "๐บ๐พ"
    people_with_bunny_ears_partying = "๐ฏ"
    dancers = "๐ฏ"
    women_with_bunny_ears_partying = "๐ฏโ"
    men_with_bunny_ears_partying = "๐ฏโ"
    levitate = "๐ด"
    man_in_business_suit_levitating = "๐ด"
    levitate_tone1 = "๐ด๐ป"
    man_in_business_suit_levitating_tone1 = "๐ด๐ป"
    man_in_business_suit_levitating_light_skin_tone = "๐ด๐ป"
    levitate_tone2 = "๐ด๐ผ"
    man_in_business_suit_levitating_tone2 = "๐ด๐ผ"
    man_in_business_suit_levitating_medium_light_skin_tone = "๐ด๐ผ"
    levitate_tone3 = "๐ด๐ฝ"
    man_in_business_suit_levitating_tone3 = "๐ด๐ฝ"
    man_in_business_suit_levitating_medium_skin_tone = "๐ด๐ฝ"
    levitate_tone4 = "๐ด๐พ"
    man_in_business_suit_levitating_tone4 = "๐ด๐พ"
    man_in_business_suit_levitating_medium_dark_skin_tone = "๐ด๐พ"
    levitate_tone5 = "๐ด๐ฟ"
    man_in_business_suit_levitating_tone5 = "๐ด๐ฟ"
    man_in_business_suit_levitating_dark_skin_tone = "๐ด๐ฟ"
    person_walking = "๐ถ"
    walking = "๐ถ"
    person_walking_tone1 = "๐ถ๐ป"
    walking_tone1 = "๐ถ๐ป"
    person_walking_tone2 = "๐ถ๐ผ"
    walking_tone2 = "๐ถ๐ผ"
    person_walking_tone3 = "๐ถ๐ฝ"
    walking_tone3 = "๐ถ๐ฝ"
    person_walking_tone4 = "๐ถ๐พ"
    walking_tone4 = "๐ถ๐พ"
    person_walking_tone5 = "๐ถ๐ฟ"
    walking_tone5 = "๐ถ๐ฟ"
    woman_walking = "๐ถโ"
    woman_walking_tone1 = "๐ถ๐ปโ"
    woman_walking_light_skin_tone = "๐ถ๐ปโ"
    woman_walking_tone2 = "๐ถ๐ผโ"
    woman_walking_medium_light_skin_tone = "๐ถ๐ผโ"
    woman_walking_tone3 = "๐ถ๐ฝโ"
    woman_walking_medium_skin_tone = "๐ถ๐ฝโ"
    woman_walking_tone4 = "๐ถ๐พโ"
    woman_walking_medium_dark_skin_tone = "๐ถ๐พโ"
    woman_walking_tone5 = "๐ถ๐ฟโ"
    woman_walking_dark_skin_tone = "๐ถ๐ฟโ"
    man_walking = "๐ถโ"
    man_walking_tone1 = "๐ถ๐ปโ"
    man_walking_light_skin_tone = "๐ถ๐ปโ"
    man_walking_tone2 = "๐ถ๐ผโ"
    man_walking_medium_light_skin_tone = "๐ถ๐ผโ"
    man_walking_tone3 = "๐ถ๐ฝโ"
    man_walking_medium_skin_tone = "๐ถ๐ฝโ"
    man_walking_tone4 = "๐ถ๐พโ"
    man_walking_medium_dark_skin_tone = "๐ถ๐พโ"
    man_walking_tone5 = "๐ถ๐ฟโ"
    man_walking_dark_skin_tone = "๐ถ๐ฟโ"
    person_running = "๐"
    runner = "๐"
    person_running_tone1 = "๐๐ป"
    runner_tone1 = "๐๐ป"
    person_running_tone2 = "๐๐ผ"
    runner_tone2 = "๐๐ผ"
    person_running_tone3 = "๐๐ฝ"
    runner_tone3 = "๐๐ฝ"
    person_running_tone4 = "๐๐พ"
    runner_tone4 = "๐๐พ"
    person_running_tone5 = "๐๐ฟ"
    runner_tone5 = "๐๐ฟ"
    woman_running = "๐โ"
    woman_running_tone1 = "๐๐ปโ"
    woman_running_light_skin_tone = "๐๐ปโ"
    woman_running_tone2 = "๐๐ผโ"
    woman_running_medium_light_skin_tone = "๐๐ผโ"
    woman_running_tone3 = "๐๐ฝโ"
    woman_running_medium_skin_tone = "๐๐ฝโ"
    woman_running_tone4 = "๐๐พโ"
    woman_running_medium_dark_skin_tone = "๐๐พโ"
    woman_running_tone5 = "๐๐ฟโ"
    woman_running_dark_skin_tone = "๐๐ฟโ"
    man_running = "๐โ"
    man_running_tone1 = "๐๐ปโ"
    man_running_light_skin_tone = "๐๐ปโ"
    man_running_tone2 = "๐๐ผโ"
    man_running_medium_light_skin_tone = "๐๐ผโ"
    man_running_tone3 = "๐๐ฝโ"
    man_running_medium_skin_tone = "๐๐ฝโ"
    man_running_tone4 = "๐๐พโ"
    man_running_medium_dark_skin_tone = "๐๐พโ"
    man_running_tone5 = "๐๐ฟโ"
    man_running_dark_skin_tone = "๐๐ฟโ"
    person_standing = "๐ง"
    person_standing_tone1 = "๐ง๐ป"
    person_standing_light_skin_tone = "๐ง๐ป"
    person_standing_tone2 = "๐ง๐ผ"
    person_standing_medium_light_skin_tone = "๐ง๐ผ"
    person_standing_tone3 = "๐ง๐ฝ"
    person_standing_medium_skin_tone = "๐ง๐ฝ"
    person_standing_tone4 = "๐ง๐พ"
    person_standing_medium_dark_skin_tone = "๐ง๐พ"
    person_standing_tone5 = "๐ง๐ฟ"
    person_standing_dark_skin_tone = "๐ง๐ฟ"
    woman_standing = "๐งโ"
    woman_standing_tone1 = "๐ง๐ปโ"
    woman_standing_light_skin_tone = "๐ง๐ปโ"
    woman_standing_tone2 = "๐ง๐ผโ"
    woman_standing_medium_light_skin_tone = "๐ง๐ผโ"
    woman_standing_tone3 = "๐ง๐ฝโ"
    woman_standing_medium_skin_tone = "๐ง๐ฝโ"
    woman_standing_tone4 = "๐ง๐พโ"
    woman_standing_medium_dark_skin_tone = "๐ง๐พโ"
    woman_standing_tone5 = "๐ง๐ฟโ"
    woman_standing_dark_skin_tone = "๐ง๐ฟโ"
    man_standing = "๐งโ"
    man_standing_tone1 = "๐ง๐ปโ"
    man_standing_light_skin_tone = "๐ง๐ปโ"
    man_standing_tone2 = "๐ง๐ผโ"
    man_standing_medium_light_skin_tone = "๐ง๐ผโ"
    man_standing_tone3 = "๐ง๐ฝโ"
    man_standing_medium_skin_tone = "๐ง๐ฝโ"
    man_standing_tone4 = "๐ง๐พโ"
    man_standing_medium_dark_skin_tone = "๐ง๐พโ"
    man_standing_tone5 = "๐ง๐ฟโ"
    man_standing_dark_skin_tone = "๐ง๐ฟโ"
    person_kneeling = "๐ง"
    person_kneeling_tone1 = "๐ง๐ป"
    person_kneeling_light_skin_tone = "๐ง๐ป"
    person_kneeling_tone2 = "๐ง๐ผ"
    person_kneeling_medium_light_skin_tone = "๐ง๐ผ"
    person_kneeling_tone3 = "๐ง๐ฝ"
    person_kneeling_medium_skin_tone = "๐ง๐ฝ"
    person_kneeling_tone4 = "๐ง๐พ"
    person_kneeling_medium_dark_skin_tone = "๐ง๐พ"
    person_kneeling_tone5 = "๐ง๐ฟ"
    person_kneeling_dark_skin_tone = "๐ง๐ฟ"
    woman_kneeling = "๐งโ"
    woman_kneeling_tone1 = "๐ง๐ปโ"
    woman_kneeling_light_skin_tone = "๐ง๐ปโ"
    woman_kneeling_tone2 = "๐ง๐ผโ"
    woman_kneeling_medium_light_skin_tone = "๐ง๐ผโ"
    woman_kneeling_tone3 = "๐ง๐ฝโ"
    woman_kneeling_medium_skin_tone = "๐ง๐ฝโ"
    woman_kneeling_tone4 = "๐ง๐พโ"
    woman_kneeling_medium_dark_skin_tone = "๐ง๐พโ"
    woman_kneeling_tone5 = "๐ง๐ฟโ"
    woman_kneeling_dark_skin_tone = "๐ง๐ฟโ"
    man_kneeling = "๐งโ"
    man_kneeling_tone1 = "๐ง๐ปโ"
    man_kneeling_light_skin_tone = "๐ง๐ปโ"
    man_kneeling_tone2 = "๐ง๐ผโ"
    man_kneeling_medium_light_skin_tone = "๐ง๐ผโ"
    man_kneeling_tone3 = "๐ง๐ฝโ"
    man_kneeling_medium_skin_tone = "๐ง๐ฝโ"
    man_kneeling_tone4 = "๐ง๐พโ"
    man_kneeling_medium_dark_skin_tone = "๐ง๐พโ"
    man_kneeling_tone5 = "๐ง๐ฟโ"
    man_kneeling_dark_skin_tone = "๐ง๐ฟโ"
    woman_with_probing_cane = "๐ฉ๐ฆฏ"
    woman_with_probing_cane_tone1 = "๐ฉ๐ป๐ฆฏ"
    woman_with_probing_cane_light_skin_tone = "๐ฉ๐ป๐ฆฏ"
    woman_with_probing_cane_tone2 = "๐ฉ๐ผ๐ฆฏ"
    woman_with_probing_cane_medium_light_skin_tone = "๐ฉ๐ผ๐ฆฏ"
    woman_with_probing_cane_tone3 = "๐ฉ๐ฝ๐ฆฏ"
    woman_with_probing_cane_medium_skin_tone = "๐ฉ๐ฝ๐ฆฏ"
    woman_with_probing_cane_tone4 = "๐ฉ๐พ๐ฆฏ"
    woman_with_probing_cane_medium_dark_skin_tone = "๐ฉ๐พ๐ฆฏ"
    woman_with_probing_cane_tone5 = "๐ฉ๐ฟ๐ฆฏ"
    woman_with_probing_cane_dark_skin_tone = "๐ฉ๐ฟ๐ฆฏ"
    man_with_probing_cane = "๐จ๐ฆฏ"
    man_with_probing_cane_tone1 = "๐จ๐ป๐ฆฏ"
    man_with_probing_cane_light_skin_tone = "๐จ๐ป๐ฆฏ"
    man_with_probing_cane_tone2 = "๐จ๐ผ๐ฆฏ"
    man_with_probing_cane_medium_light_skin_tone = "๐จ๐ผ๐ฆฏ"
    man_with_probing_cane_tone3 = "๐จ๐ฝ๐ฆฏ"
    man_with_probing_cane_medium_skin_tone = "๐จ๐ฝ๐ฆฏ"
    man_with_probing_cane_tone4 = "๐จ๐พ๐ฆฏ"
    man_with_probing_cane_medium_dark_skin_tone = "๐จ๐พ๐ฆฏ"
    man_with_probing_cane_tone5 = "๐จ๐ฟ๐ฆฏ"
    man_with_probing_cane_dark_skin_tone = "๐จ๐ฟ๐ฆฏ"
    woman_in_motorized_wheelchair = "๐ฉ๐ฆผ"
    woman_in_motorized_wheelchair_tone1 = "๐ฉ๐ป๐ฆผ"
    woman_in_motorized_wheelchair_light_skin_tone = "๐ฉ๐ป๐ฆผ"
    woman_in_motorized_wheelchair_tone2 = "๐ฉ๐ผ๐ฆผ"
    woman_in_motorized_wheelchair_medium_light_skin_tone = "๐ฉ๐ผ๐ฆผ"
    woman_in_motorized_wheelchair_tone3 = "๐ฉ๐ฝ๐ฆผ"
    woman_in_motorized_wheelchair_medium_skin_tone = "๐ฉ๐ฝ๐ฆผ"
    woman_in_motorized_wheelchair_tone4 = "๐ฉ๐พ๐ฆผ"
    woman_in_motorized_wheelchair_medium_dark_skin_tone = "๐ฉ๐พ๐ฆผ"
    woman_in_motorized_wheelchair_tone5 = "๐ฉ๐ฟ๐ฆผ"
    woman_in_motorized_wheelchair_dark_skin_tone = "๐ฉ๐ฟ๐ฆผ"
    man_in_motorized_wheelchair = "๐จ๐ฆผ"
    man_in_motorized_wheelchair_tone1 = "๐จ๐ป๐ฆผ"
    man_in_motorized_wheelchair_light_skin_tone = "๐จ๐ป๐ฆผ"
    man_in_motorized_wheelchair_tone2 = "๐จ๐ผ๐ฆผ"
    man_in_motorized_wheelchair_medium_light_skin_tone = "๐จ๐ผ๐ฆผ"
    man_in_motorized_wheelchair_tone3 = "๐จ๐ฝ๐ฆผ"
    man_in_motorized_wheelchair_medium_skin_tone = "๐จ๐ฝ๐ฆผ"
    man_in_motorized_wheelchair_tone4 = "๐จ๐พ๐ฆผ"
    man_in_motorized_wheelchair_medium_dark_skin_tone = "๐จ๐พ๐ฆผ"
    man_in_motorized_wheelchair_tone5 = "๐จ๐ฟ๐ฆผ"
    man_in_motorized_wheelchair_dark_skin_tone = "๐จ๐ฟ๐ฆผ"
    woman_in_manual_wheelchair = "๐ฉ๐ฆฝ"
    woman_in_manual_wheelchair_tone1 = "๐ฉ๐ป๐ฆฝ"
    woman_in_manual_wheelchair_light_skin_tone = "๐ฉ๐ป๐ฆฝ"
    woman_in_manual_wheelchair_tone2 = "๐ฉ๐ผ๐ฆฝ"
    woman_in_manual_wheelchair_medium_light_skin_tone = "๐ฉ๐ผ๐ฆฝ"
    woman_in_manual_wheelchair_tone3 = "๐ฉ๐ฝ๐ฆฝ"
    woman_in_manual_wheelchair_medium_skin_tone = "๐ฉ๐ฝ๐ฆฝ"
    woman_in_manual_wheelchair_tone4 = "๐ฉ๐พ๐ฆฝ"
    woman_in_manual_wheelchair_medium_dark_skin_tone = "๐ฉ๐พ๐ฆฝ"
    woman_in_manual_wheelchair_tone5 = "๐ฉ๐ฟ๐ฆฝ"
    woman_in_manual_wheelchair_dark_skin_tone = "๐ฉ๐ฟ๐ฆฝ"
    man_in_manual_wheelchair = "๐จ๐ฆฝ"
    man_in_manual_wheelchair_tone1 = "๐จ๐ป๐ฆฝ"
    man_in_manual_wheelchair_light_skin_tone = "๐จ๐ป๐ฆฝ"
    man_in_manual_wheelchair_tone2 = "๐จ๐ผ๐ฆฝ"
    man_in_manual_wheelchair_medium_light_skin_tone = "๐จ๐ผ๐ฆฝ"
    man_in_manual_wheelchair_tone3 = "๐จ๐ฝ๐ฆฝ"
    man_in_manual_wheelchair_medium_skin_tone = "๐จ๐ฝ๐ฆฝ"
    man_in_manual_wheelchair_tone4 = "๐จ๐พ๐ฆฝ"
    man_in_manual_wheelchair_medium_dark_skin_tone = "๐จ๐พ๐ฆฝ"
    man_in_manual_wheelchair_tone5 = "๐จ๐ฟ๐ฆฝ"
    man_in_manual_wheelchair_dark_skin_tone = "๐จ๐ฟ๐ฆฝ"
    people_holding_hands = "๐ง๐ค๐ง"
    couple = "๐ซ"
    two_women_holding_hands = "๐ญ"
    two_men_holding_hands = "๐ฌ"
    couple_with_heart = "๐"
    couple_with_heart_woman_man = "๐ฉโค๐จ"
    couple_ww = "๐ฉโค๐ฉ"
    couple_with_heart_ww = "๐ฉโค๐ฉ"
    couple_mm = "๐จโค๐จ"
    couple_with_heart_mm = "๐จโค๐จ"
    couplekiss = "๐"
    kiss_woman_man = "๐ฉโค๐๐จ"
    kiss_ww = "๐ฉโค๐๐ฉ"
    couplekiss_ww = "๐ฉโค๐๐ฉ"
    kiss_mm = "๐จโค๐๐จ"
    couplekiss_mm = "๐จโค๐๐จ"
    family = "๐ช"
    family_man_woman_boy = "๐จ๐ฉ๐ฆ"
    family_mwg = "๐จ๐ฉ๐ง"
    family_mwgb = "๐จ๐ฉ๐ง๐ฆ"
    family_mwbb = "๐จ๐ฉ๐ฆ๐ฆ"
    family_mwgg = "๐จ๐ฉ๐ง๐ง"
    family_wwb = "๐ฉ๐ฉ๐ฆ"
    family_wwg = "๐ฉ๐ฉ๐ง"
    family_wwgb = "๐ฉ๐ฉ๐ง๐ฆ"
    family_wwbb = "๐ฉ๐ฉ๐ฆ๐ฆ"
    family_wwgg = "๐ฉ๐ฉ๐ง๐ง"
    family_mmb = "๐จ๐จ๐ฆ"
    family_mmg = "๐จ๐จ๐ง"
    family_mmgb = "๐จ๐จ๐ง๐ฆ"
    family_mmbb = "๐จ๐จ๐ฆ๐ฆ"
    family_mmgg = "๐จ๐จ๐ง๐ง"
    family_woman_boy = "๐ฉ๐ฆ"
    family_woman_girl = "๐ฉ๐ง"
    family_woman_girl_boy = "๐ฉ๐ง๐ฆ"
    family_woman_boy_boy = "๐ฉ๐ฆ๐ฆ"
    family_woman_girl_girl = "๐ฉ๐ง๐ง"
    family_man_boy = "๐จ๐ฆ"
    family_man_girl = "๐จ๐ง"
    family_man_girl_boy = "๐จ๐ง๐ฆ"
    family_man_boy_boy = "๐จ๐ฆ๐ฆ"
    family_man_girl_girl = "๐จ๐ง๐ง"
    yarn = "๐งถ"
    thread = "๐งต"
    coat = "๐งฅ"
    lab_coat = "๐ฅผ"
    safety_vest = "๐ฆบ"
    womans_clothes = "๐"
    shirt = "๐"
    jeans = "๐"
    shorts = "๐ฉณ"
    necktie = "๐"
    dress = "๐"
    bikini = "๐"
    one_piece_swimsuit = "๐ฉฑ"
    kimono = "๐"
    sari = "๐ฅป"
    womans_flat_shoe = "๐ฅฟ"
    high_heel = "๐ "
    sandal = "๐ก"
    boot = "๐ข"
    ballet_shoes = "๐ฉฐ"
    mans_shoe = "๐"
    athletic_shoe = "๐"
    hiking_boot = "๐ฅพ"
    briefs = "๐ฉฒ"
    socks = "๐งฆ"
    gloves = "๐งค"
    scarf = "๐งฃ"
    tophat = "๐ฉ"
    billed_cap = "๐งข"
    womans_hat = "๐"
    mortar_board = "๐"
    helmet_with_cross = "โ"
    helmet_with_white_cross = "โ"
    crown = "๐"
    ring = "๐"
    pouch = "๐"
    purse = "๐"
    handbag = "๐"
    briefcase = "๐ผ"
    school_satchel = "๐"
    luggage = "๐งณ"
    eyeglasses = "๐"
    dark_sunglasses = "๐ถ"
    goggles = "๐ฅฝ"
    diving_mask = "๐คฟ"
    closed_umbrella = "๐"
    dog = "๐ถ"
    cat = "๐ฑ"
    mouse = "๐ญ"
    hamster = "๐น"
    rabbit = "๐ฐ"
    fox = "๐ฆ"
    fox_face = "๐ฆ"
    bear = "๐ป"
    panda_face = "๐ผ"
    koala = "๐จ"
    tiger = "๐ฏ"
    lion_face = "๐ฆ"
    lion = "๐ฆ"
    cow = "๐ฎ"
    pig = "๐ท"
    pig_nose = "๐ฝ"
    frog = "๐ธ"
    monkey_face = "๐ต"
    see_no_evil = "๐"
    hear_no_evil = "๐"
    speak_no_evil = "๐"
    monkey = "๐"
    chicken = "๐"
    penguin = "๐ง"
    bird = "๐ฆ"
    baby_chick = "๐ค"
    hatching_chick = "๐ฃ"
    hatched_chick = "๐ฅ"
    duck = "๐ฆ"
    eagle = "๐ฆ"
    owl = "๐ฆ"
    bat = "๐ฆ"
    wolf = "๐บ"
    boar = "๐"
    horse = "๐ด"
    unicorn = "๐ฆ"
    unicorn_face = "๐ฆ"
    bee = "๐"
    bug = "๐"
    butterfly = "๐ฆ"
    snail = "๐"
    shell = "๐"
    beetle = "๐"
    ant = "๐"
    mosquito = "๐ฆ"
    cricket = "๐ฆ"
    spider = "๐ท"
    spider_web = "๐ธ"
    scorpion = "๐ฆ"
    turtle = "๐ข"
    snake = "๐"
    lizard = "๐ฆ"
    t_rex = "๐ฆ"
    sauropod = "๐ฆ"
    octopus = "๐"
    squid = "๐ฆ"
    shrimp = "๐ฆ"
    lobster = "๐ฆ"
    oyster = "๐ฆช"
    crab = "๐ฆ"
    blowfish = "๐ก"
    tropical_fish = "๐ "
    fish = "๐"
    dolphin = "๐ฌ"
    whale = "๐ณ"
    whale2 = "๐"
    shark = "๐ฆ"
    crocodile = "๐"
    tiger2 = "๐"
    leopard = "๐"
    zebra = "๐ฆ"
    gorilla = "๐ฆ"
    orangutan = "๐ฆง"
    elephant = "๐"
    hippopotamus = "๐ฆ"
    rhino = "๐ฆ"
    rhinoceros = "๐ฆ"
    dromedary_camel = "๐ช"
    camel = "๐ซ"
    giraffe = "๐ฆ"
    kangaroo = "๐ฆ"
    water_buffalo = "๐"
    ox = "๐"
    cow2 = "๐"
    racehorse = "๐"
    pig2 = "๐"
    ram = "๐"
    llama = "๐ฆ"
    sheep = "๐"
    goat = "๐"
    deer = "๐ฆ"
    dog2 = "๐"
    guide_dog = "๐ฆฎ"
    service_dog = "๐๐ฆบ"
    poodle = "๐ฉ"
    cat2 = "๐"
    rooster = "๐"
    turkey = "๐ฆ"
    peacock = "๐ฆ"
    parrot = "๐ฆ"
    swan = "๐ฆข"
    flamingo = "๐ฆฉ"
    dove = "๐"
    dove_of_peace = "๐"
    rabbit2 = "๐"
    sloth = "๐ฆฅ"
    otter = "๐ฆฆ"
    skunk = "๐ฆจ"
    raccoon = "๐ฆ"
    badger = "๐ฆก"
    mouse2 = "๐"
    rat = "๐"
    chipmunk = "๐ฟ"
    hedgehog = "๐ฆ"
    feet = "๐พ"
    paw_prints = "๐พ"
    dragon = "๐"
    dragon_face = "๐ฒ"
    cactus = "๐ต"
    christmas_tree = "๐"
    evergreen_tree = "๐ฒ"
    deciduous_tree = "๐ณ"
    palm_tree = "๐ด"
    seedling = "๐ฑ"
    herb = "๐ฟ"
    shamrock = "โ"
    four_leaf_clover = "๐"
    bamboo = "๐"
    tanabata_tree = "๐"
    leaves = "๐"
    fallen_leaf = "๐"
    maple_leaf = "๐"
    mushroom = "๐"
    ear_of_rice = "๐พ"
    bouquet = "๐"
    tulip = "๐ท"
    rose = "๐น"
    wilted_rose = "๐ฅ"
    wilted_flower = "๐ฅ"
    hibiscus = "๐บ"
    cherry_blossom = "๐ธ"
    blossom = "๐ผ"
    sunflower = "๐ป"
    sun_with_face = "๐"
    full_moon_with_face = "๐"
    first_quarter_moon_with_face = "๐"
    last_quarter_moon_with_face = "๐"
    new_moon_with_face = "๐"
    full_moon = "๐"
    waning_gibbous_moon = "๐"
    last_quarter_moon = "๐"
    waning_crescent_moon = "๐"
    new_moon = "๐"
    waxing_crescent_moon = "๐"
    first_quarter_moon = "๐"
    waxing_gibbous_moon = "๐"
    crescent_moon = "๐"
    earth_americas = "๐"
    earth_africa = "๐"
    earth_asia = "๐"
    ringed_planet = "๐ช"
    dizzy = "๐ซ"
    star = "โญ"
    star2 = "๐"
    sparkles = "โจ"
    zap = "โก"
    comet = "โ"
    boom = "๐ฅ"
    fire = "๐ฅ"
    flame = "๐ฅ"
    cloud_tornado = "๐ช"
    cloud_with_tornado = "๐ช"
    rainbow = "๐"
    sunny = "โ"
    white_sun_small_cloud = "๐ค"
    white_sun_with_small_cloud = "๐ค"
    partly_sunny = "โ"
    white_sun_cloud = "๐ฅ"
    white_sun_behind_cloud = "๐ฅ"
    cloud = "โ"
    white_sun_rain_cloud = "๐ฆ"
    white_sun_behind_cloud_with_rain = "๐ฆ"
    cloud_rain = "๐ง"
    cloud_with_rain = "๐ง"
    thunder_cloud_rain = "โ"
    thunder_cloud_and_rain = "โ"
    cloud_lightning = "๐ฉ"
    cloud_with_lightning = "๐ฉ"
    cloud_snow = "๐จ"
    cloud_with_snow = "๐จ"
    snowflake = "โ"
    snowman2 = "โ"
    snowman = "โ"
    wind_blowing_face = "๐ฌ"
    dash = "๐จ"
    droplet = "๐ง"
    sweat_drops = "๐ฆ"
    umbrella = "โ"
    umbrella2 = "โ"
    ocean = "๐"
    fog = "๐ซ"
    green_apple = "๐"
    apple = "๐"
    pear = "๐"
    tangerine = "๐"
    lemon = "๐"
    banana = "๐"
    watermelon = "๐"
    grapes = "๐"
    strawberry = "๐"
    melon = "๐"
    cherries = "๐"
    peach = "๐"
    mango = "๐ฅญ"
    pineapple = "๐"
    coconut = "๐ฅฅ"
    kiwi = "๐ฅ"
    kiwifruit = "๐ฅ"
    tomato = "๐"
    eggplant = "๐"
    avocado = "๐ฅ"
    broccoli = "๐ฅฆ"
    leafy_green = "๐ฅฌ"
    cucumber = "๐ฅ"
    hot_pepper = "๐ถ"
    corn = "๐ฝ"
    carrot = "๐ฅ"
    onion = "๐ง"
    garlic = "๐ง"
    potato = "๐ฅ"
    sweet_potato = "๐ "
    croissant = "๐ฅ"
    bagel = "๐ฅฏ"
    bread = "๐"
    french_bread = "๐ฅ"
    baguette_bread = "๐ฅ"
    pretzel = "๐ฅจ"
    cheese = "๐ง"
    cheese_wedge = "๐ง"
    egg = "๐ฅ"
    cooking = "๐ณ"
    pancakes = "๐ฅ"
    waffle = "๐ง"
    bacon = "๐ฅ"
    cut_of_meat = "๐ฅฉ"
    poultry_leg = "๐"
    meat_on_bone = "๐"
    hotdog = "๐ญ"
    hot_dog = "๐ญ"
    hamburger = "๐"
    fries = "๐"
    pizza = "๐"
    sandwich = "๐ฅช"
    falafel = "๐ง"
    stuffed_flatbread = "๐ฅ"
    stuffed_pita = "๐ฅ"
    taco = "๐ฎ"
    burrito = "๐ฏ"
    salad = "๐ฅ"
    green_salad = "๐ฅ"
    shallow_pan_of_food = "๐ฅ"
    paella = "๐ฅ"
    canned_food = "๐ฅซ"
    spaghetti = "๐"
    ramen = "๐"
    stew = "๐ฒ"
    curry = "๐"
    sushi = "๐ฃ"
    bento = "๐ฑ"
    dumpling = "๐ฅ"
    fried_shrimp = "๐ค"
    rice_ball = "๐"
    rice = "๐"
    rice_cracker = "๐"
    fish_cake = "๐ฅ"
    fortune_cookie = "๐ฅ "
    moon_cake = "๐ฅฎ"
    oden = "๐ข"
    dango = "๐ก"
    shaved_ice = "๐ง"
    ice_cream = "๐จ"
    icecream = "๐ฆ"
    pie = "๐ฅง"
    cupcake = "๐ง"
    cake = "๐ฐ"
    birthday = "๐"
    custard = "๐ฎ"
    pudding = "๐ฎ"
    flan = "๐ฎ"
    lollipop = "๐ญ"
    candy = "๐ฌ"
    chocolate_bar = "๐ซ"
    popcorn = "๐ฟ"
    doughnut = "๐ฉ"
    cookie = "๐ช"
    chestnut = "๐ฐ"
    peanuts = "๐ฅ"
    shelled_peanut = "๐ฅ"
    honey_pot = "๐ฏ"
    butter = "๐ง"
    milk = "๐ฅ"
    glass_of_milk = "๐ฅ"
    baby_bottle = "๐ผ"
    coffee = "โ"
    tea = "๐ต"
    mate = "๐ง"
    cup_with_straw = "๐ฅค"
    beverage_box = "๐ง"
    ice_cube = "๐ง"
    sake = "๐ถ"
    beer = "๐บ"
    beers = "๐ป"
    champagne_glass = "๐ฅ"
    clinking_glass = "๐ฅ"
    wine_glass = "๐ท"
    tumbler_glass = "๐ฅ"
    whisky = "๐ฅ"
    cocktail = "๐ธ"
    tropical_drink = "๐น"
    champagne = "๐พ"
    bottle_with_popping_cork = "๐พ"
    spoon = "๐ฅ"
    fork_and_knife = "๐ด"
    fork_knife_plate = "๐ฝ"
    fork_and_knife_with_plate = "๐ฝ"
    bowl_with_spoon = "๐ฅฃ"
    takeout_box = "๐ฅก"
    chopsticks = "๐ฅข"
    salt = "๐ง"
    soccer = "โฝ"
    basketball = "๐"
    football = "๐"
    baseball = "โพ"
    softball = "๐ฅ"
    tennis = "๐พ"
    volleyball = "๐"
    rugby_football = "๐"
    flying_disc = "๐ฅ"
    eight_ball = "๐ฑ"
    ping_pong = "๐"
    table_tennis = "๐"
    badminton = "๐ธ"
    hockey = "๐"
    field_hockey = "๐"
    lacrosse = "๐ฅ"
    cricket_game = "๐"
    cricket_bat_ball = "๐"
    goal = "๐ฅ"
    goal_net = "๐ฅ"
    golf = "โณ"
    bow_and_arrow = "๐น"
    archery = "๐น"
    fishing_pole_and_fish = "๐ฃ"
    boxing_glove = "๐ฅ"
    boxing_gloves = "๐ฅ"
    martial_arts_uniform = "๐ฅ"
    karate_uniform = "๐ฅ"
    running_shirt_with_sash = "๐ฝ"
    skateboard = "๐น"
    sled = "๐ท"
    parachute = "๐ช"
    ice_skate = "โธ"
    curling_stone = "๐ฅ"
    ski = "๐ฟ"
    skier = "โท"
    snowboarder = "๐"
    snowboarder_tone1 = "๐๐ป"
    snowboarder_light_skin_tone = "๐๐ป"
    snowboarder_tone2 = "๐๐ผ"
    snowboarder_medium_light_skin_tone = "๐๐ผ"
    snowboarder_tone3 = "๐๐ฝ"
    snowboarder_medium_skin_tone = "๐๐ฝ"
    snowboarder_tone4 = "๐๐พ"
    snowboarder_medium_dark_skin_tone = "๐๐พ"
    snowboarder_tone5 = "๐๐ฟ"
    snowboarder_dark_skin_tone = "๐๐ฟ"
    person_lifting_weights = "๐"
    lifter = "๐"
    weight_lifter = "๐"
    person_lifting_weights_tone1 = "๐๐ป"
    lifter_tone1 = "๐๐ป"
    weight_lifter_tone1 = "๐๐ป"
    person_lifting_weights_tone2 = "๐๐ผ"
    lifter_tone2 = "๐๐ผ"
    weight_lifter_tone2 = "๐๐ผ"
    person_lifting_weights_tone3 = "๐๐ฝ"
    lifter_tone3 = "๐๐ฝ"
    weight_lifter_tone3 = "๐๐ฝ"
    person_lifting_weights_tone4 = "๐๐พ"
    lifter_tone4 = "๐๐พ"
    weight_lifter_tone4 = "๐๐พ"
    person_lifting_weights_tone5 = "๐๐ฟ"
    lifter_tone5 = "๐๐ฟ"
    weight_lifter_tone5 = "๐๐ฟ"
    woman_lifting_weights = "๐โ"
    woman_lifting_weights_tone1 = "๐๐ปโ"
    woman_lifting_weights_light_skin_tone = "๐๐ปโ"
    woman_lifting_weights_tone2 = "๐๐ผโ"
    woman_lifting_weights_medium_light_skin_tone = "๐๐ผโ"
    woman_lifting_weights_tone3 = "๐๐ฝโ"
    woman_lifting_weights_medium_skin_tone = "๐๐ฝโ"
    woman_lifting_weights_tone4 = "๐๐พโ"
    woman_lifting_weights_medium_dark_skin_tone = "๐๐พโ"
    woman_lifting_weights_tone5 = "๐๐ฟโ"
    woman_lifting_weights_dark_skin_tone = "๐๐ฟโ"
    man_lifting_weights = "๐โ"
    man_lifting_weights_tone1 = "๐๐ปโ"
    man_lifting_weights_light_skin_tone = "๐๐ปโ"
    man_lifting_weights_tone2 = "๐๐ผโ"
    man_lifting_weights_medium_light_skin_tone = "๐๐ผโ"
    man_lifting_weights_tone3 = "๐๐ฝโ"
    man_lifting_weights_medium_skin_tone = "๐๐ฝโ"
    man_lifting_weights_tone4 = "๐๐พโ"
    man_lifting_weights_medium_dark_skin_tone = "๐๐พโ"
    man_lifting_weights_tone5 = "๐๐ฟโ"
    man_lifting_weights_dark_skin_tone = "๐๐ฟโ"
    people_wrestling = "๐คผ"
    wrestlers = "๐คผ"
    wrestling = "๐คผ"
    women_wrestling = "๐คผโ"
    men_wrestling = "๐คผโ"
    person_doing_cartwheel = "๐คธ"
    cartwheel = "๐คธ"
    person_doing_cartwheel_tone1 = "๐คธ๐ป"
    cartwheel_tone1 = "๐คธ๐ป"
    person_doing_cartwheel_tone2 = "๐คธ๐ผ"
    cartwheel_tone2 = "๐คธ๐ผ"
    person_doing_cartwheel_tone3 = "๐คธ๐ฝ"
    cartwheel_tone3 = "๐คธ๐ฝ"
    person_doing_cartwheel_tone4 = "๐คธ๐พ"
    cartwheel_tone4 = "๐คธ๐พ"
    person_doing_cartwheel_tone5 = "๐คธ๐ฟ"
    cartwheel_tone5 = "๐คธ๐ฟ"
    woman_cartwheeling = "๐คธโ"
    woman_cartwheeling_tone1 = "๐คธ๐ปโ"
    woman_cartwheeling_light_skin_tone = "๐คธ๐ปโ"
    woman_cartwheeling_tone2 = "๐คธ๐ผโ"
    woman_cartwheeling_medium_light_skin_tone = "๐คธ๐ผโ"
    woman_cartwheeling_tone3 = "๐คธ๐ฝโ"
    woman_cartwheeling_medium_skin_tone = "๐คธ๐ฝโ"
    woman_cartwheeling_tone4 = "๐คธ๐พโ"
    woman_cartwheeling_medium_dark_skin_tone = "๐คธ๐พโ"
    woman_cartwheeling_tone5 = "๐คธ๐ฟโ"
    woman_cartwheeling_dark_skin_tone = "๐คธ๐ฟโ"
    man_cartwheeling = "๐คธโ"
    man_cartwheeling_tone1 = "๐คธ๐ปโ"
    man_cartwheeling_light_skin_tone = "๐คธ๐ปโ"
    man_cartwheeling_tone2 = "๐คธ๐ผโ"
    man_cartwheeling_medium_light_skin_tone = "๐คธ๐ผโ"
    man_cartwheeling_tone3 = "๐คธ๐ฝโ"
    man_cartwheeling_medium_skin_tone = "๐คธ๐ฝโ"
    man_cartwheeling_tone4 = "๐คธ๐พโ"
    man_cartwheeling_medium_dark_skin_tone = "๐คธ๐พโ"
    man_cartwheeling_tone5 = "๐คธ๐ฟโ"
    man_cartwheeling_dark_skin_tone = "๐คธ๐ฟโ"
    person_bouncing_ball = "โน"
    basketball_player = "โน"
    person_with_ball = "โน"
    person_bouncing_ball_tone1 = "โน๐ป"
    basketball_player_tone1 = "โน๐ป"
    person_with_ball_tone1 = "โน๐ป"
    person_bouncing_ball_tone2 = "โน๐ผ"
    basketball_player_tone2 = "โน๐ผ"
    person_with_ball_tone2 = "โน๐ผ"
    person_bouncing_ball_tone3 = "โน๐ฝ"
    basketball_player_tone3 = "โน๐ฝ"
    person_with_ball_tone3 = "โน๐ฝ"
    person_bouncing_ball_tone4 = "โน๐พ"
    basketball_player_tone4 = "โน๐พ"
    person_with_ball_tone4 = "โน๐พ"
    person_bouncing_ball_tone5 = "โน๐ฟ"
    basketball_player_tone5 = "โน๐ฟ"
    person_with_ball_tone5 = "โน๐ฟ"
    woman_bouncing_ball = "โนโ"
    woman_bouncing_ball_tone1 = "โน๐ปโ"
    woman_bouncing_ball_light_skin_tone = "โน๐ปโ"
    woman_bouncing_ball_tone2 = "โน๐ผโ"
    woman_bouncing_ball_medium_light_skin_tone = "โน๐ผโ"
    woman_bouncing_ball_tone3 = "โน๐ฝโ"
    woman_bouncing_ball_medium_skin_tone = "โน๐ฝโ"
    woman_bouncing_ball_tone4 = "โน๐พโ"
    woman_bouncing_ball_medium_dark_skin_tone = "โน๐พโ"
    woman_bouncing_ball_tone5 = "โน๐ฟโ"
    woman_bouncing_ball_dark_skin_tone = "โน๐ฟโ"
    man_bouncing_ball = "โนโ"
    man_bouncing_ball_tone1 = "โน๐ปโ"
    man_bouncing_ball_light_skin_tone = "โน๐ปโ"
    man_bouncing_ball_tone2 = "โน๐ผโ"
    man_bouncing_ball_medium_light_skin_tone = "โน๐ผโ"
    man_bouncing_ball_tone3 = "โน๐ฝโ"
    man_bouncing_ball_medium_skin_tone = "โน๐ฝโ"
    man_bouncing_ball_tone4 = "โน๐พโ"
    man_bouncing_ball_medium_dark_skin_tone = "โน๐พโ"
    man_bouncing_ball_tone5 = "โน๐ฟโ"
    man_bouncing_ball_dark_skin_tone = "โน๐ฟโ"
    person_fencing = "๐คบ"
    fencer = "๐คบ"
    fencing = "๐คบ"
    person_playing_handball = "๐คพ"
    handball = "๐คพ"
    person_playing_handball_tone1 = "๐คพ๐ป"
    handball_tone1 = "๐คพ๐ป"
    person_playing_handball_tone2 = "๐คพ๐ผ"
    handball_tone2 = "๐คพ๐ผ"
    person_playing_handball_tone3 = "๐คพ๐ฝ"
    handball_tone3 = "๐คพ๐ฝ"
    person_playing_handball_tone4 = "๐คพ๐พ"
    handball_tone4 = "๐คพ๐พ"
    person_playing_handball_tone5 = "๐คพ๐ฟ"
    handball_tone5 = "๐คพ๐ฟ"
    woman_playing_handball = "๐คพโ"
    woman_playing_handball_tone1 = "๐คพ๐ปโ"
    woman_playing_handball_light_skin_tone = "๐คพ๐ปโ"
    woman_playing_handball_tone2 = "๐คพ๐ผโ"
    woman_playing_handball_medium_light_skin_tone = "๐คพ๐ผโ"
    woman_playing_handball_tone3 = "๐คพ๐ฝโ"
    woman_playing_handball_medium_skin_tone = "๐คพ๐ฝโ"
    woman_playing_handball_tone4 = "๐คพ๐พโ"
    woman_playing_handball_medium_dark_skin_tone = "๐คพ๐พโ"
    woman_playing_handball_tone5 = "๐คพ๐ฟโ"
    woman_playing_handball_dark_skin_tone = "๐คพ๐ฟโ"
    man_playing_handball = "๐คพโ"
    man_playing_handball_tone1 = "๐คพ๐ปโ"
    man_playing_handball_light_skin_tone = "๐คพ๐ปโ"
    man_playing_handball_tone2 = "๐คพ๐ผโ"
    man_playing_handball_medium_light_skin_tone = "๐คพ๐ผโ"
    man_playing_handball_tone3 = "๐คพ๐ฝโ"
    man_playing_handball_medium_skin_tone = "๐คพ๐ฝโ"
    man_playing_handball_tone4 = "๐คพ๐พโ"
    man_playing_handball_medium_dark_skin_tone = "๐คพ๐พโ"
    man_playing_handball_tone5 = "๐คพ๐ฟโ"
    man_playing_handball_dark_skin_tone = "๐คพ๐ฟโ"
    person_golfing = "๐"
    golfer = "๐"
    person_golfing_tone1 = "๐๐ป"
    person_golfing_light_skin_tone = "๐๐ป"
    person_golfing_tone2 = "๐๐ผ"
    person_golfing_medium_light_skin_tone = "๐๐ผ"
    person_golfing_tone3 = "๐๐ฝ"
    person_golfing_medium_skin_tone = "๐๐ฝ"
    person_golfing_tone4 = "๐๐พ"
    person_golfing_medium_dark_skin_tone = "๐๐พ"
    person_golfing_tone5 = "๐๐ฟ"
    person_golfing_dark_skin_tone = "๐๐ฟ"
    woman_golfing = "๐โ"
    woman_golfing_tone1 = "๐๐ปโ"
    woman_golfing_light_skin_tone = "๐๐ปโ"
    woman_golfing_tone2 = "๐๐ผโ"
    woman_golfing_medium_light_skin_tone = "๐๐ผโ"
    woman_golfing_tone3 = "๐๐ฝโ"
    woman_golfing_medium_skin_tone = "๐๐ฝโ"
    woman_golfing_tone4 = "๐๐พโ"
    woman_golfing_medium_dark_skin_tone = "๐๐พโ"
    woman_golfing_tone5 = "๐๐ฟโ"
    woman_golfing_dark_skin_tone = "๐๐ฟโ"
    man_golfing = "๐โ"
    man_golfing_tone1 = "๐๐ปโ"
    man_golfing_light_skin_tone = "๐๐ปโ"
    man_golfing_tone2 = "๐๐ผโ"
    man_golfing_medium_light_skin_tone = "๐๐ผโ"
    man_golfing_tone3 = "๐๐ฝโ"
    man_golfing_medium_skin_tone = "๐๐ฝโ"
    man_golfing_tone4 = "๐๐พโ"
    man_golfing_medium_dark_skin_tone = "๐๐พโ"
    man_golfing_tone5 = "๐๐ฟโ"
    man_golfing_dark_skin_tone = "๐๐ฟโ"
    horse_racing = "๐"
    horse_racing_tone1 = "๐๐ป"
    horse_racing_tone2 = "๐๐ผ"
    horse_racing_tone3 = "๐๐ฝ"
    horse_racing_tone4 = "๐๐พ"
    horse_racing_tone5 = "๐๐ฟ"
    person_in_lotus_position = "๐ง"
    person_in_lotus_position_tone1 = "๐ง๐ป"
    person_in_lotus_position_light_skin_tone = "๐ง๐ป"
    person_in_lotus_position_tone2 = "๐ง๐ผ"
    person_in_lotus_position_medium_light_skin_tone = "๐ง๐ผ"
    person_in_lotus_position_tone3 = "๐ง๐ฝ"
    person_in_lotus_position_medium_skin_tone = "๐ง๐ฝ"
    person_in_lotus_position_tone4 = "๐ง๐พ"
    person_in_lotus_position_medium_dark_skin_tone = "๐ง๐พ"
    person_in_lotus_position_tone5 = "๐ง๐ฟ"
    person_in_lotus_position_dark_skin_tone = "๐ง๐ฟ"
    woman_in_lotus_position = "๐งโ"
    woman_in_lotus_position_tone1 = "๐ง๐ปโ"
    woman_in_lotus_position_light_skin_tone = "๐ง๐ปโ"
    woman_in_lotus_position_tone2 = "๐ง๐ผโ"
    woman_in_lotus_position_medium_light_skin_tone = "๐ง๐ผโ"
    woman_in_lotus_position_tone3 = "๐ง๐ฝโ"
    woman_in_lotus_position_medium_skin_tone = "๐ง๐ฝโ"
    woman_in_lotus_position_tone4 = "๐ง๐พโ"
    woman_in_lotus_position_medium_dark_skin_tone = "๐ง๐พโ"
    woman_in_lotus_position_tone5 = "๐ง๐ฟโ"
    woman_in_lotus_position_dark_skin_tone = "๐ง๐ฟโ"
    man_in_lotus_position = "๐งโ"
    man_in_lotus_position_tone1 = "๐ง๐ปโ"
    man_in_lotus_position_light_skin_tone = "๐ง๐ปโ"
    man_in_lotus_position_tone2 = "๐ง๐ผโ"
    man_in_lotus_position_medium_light_skin_tone = "๐ง๐ผโ"
    man_in_lotus_position_tone3 = "๐ง๐ฝโ"
    man_in_lotus_position_medium_skin_tone = "๐ง๐ฝโ"
    man_in_lotus_position_tone4 = "๐ง๐พโ"
    man_in_lotus_position_medium_dark_skin_tone = "๐ง๐พโ"
    man_in_lotus_position_tone5 = "๐ง๐ฟโ"
    man_in_lotus_position_dark_skin_tone = "๐ง๐ฟโ"
    person_surfing = "๐"
    surfer = "๐"
    person_surfing_tone1 = "๐๐ป"
    surfer_tone1 = "๐๐ป"
    person_surfing_tone2 = "๐๐ผ"
    surfer_tone2 = "๐๐ผ"
    person_surfing_tone3 = "๐๐ฝ"
    surfer_tone3 = "๐๐ฝ"
    person_surfing_tone4 = "๐๐พ"
    surfer_tone4 = "๐๐พ"
    person_surfing_tone5 = "๐๐ฟ"
    surfer_tone5 = "๐๐ฟ"
    woman_surfing = "๐โ"
    woman_surfing_tone1 = "๐๐ปโ"
    woman_surfing_light_skin_tone = "๐๐ปโ"
    woman_surfing_tone2 = "๐๐ผโ"
    woman_surfing_medium_light_skin_tone = "๐๐ผโ"
    woman_surfing_tone3 = "๐๐ฝโ"
    woman_surfing_medium_skin_tone = "๐๐ฝโ"
    woman_surfing_tone4 = "๐๐พโ"
    woman_surfing_medium_dark_skin_tone = "๐๐พโ"
    woman_surfing_tone5 = "๐๐ฟโ"
    woman_surfing_dark_skin_tone = "๐๐ฟโ"
    man_surfing = "๐โ"
    man_surfing_tone1 = "๐๐ปโ"
    man_surfing_light_skin_tone = "๐๐ปโ"
    man_surfing_tone2 = "๐๐ผโ"
    man_surfing_medium_light_skin_tone = "๐๐ผโ"
    man_surfing_tone3 = "๐๐ฝโ"
    man_surfing_medium_skin_tone = "๐๐ฝโ"
    man_surfing_tone4 = "๐๐พโ"
    man_surfing_medium_dark_skin_tone = "๐๐พโ"
    man_surfing_tone5 = "๐๐ฟโ"
    man_surfing_dark_skin_tone = "๐๐ฟโ"
    person_swimming = "๐"
    swimmer = "๐"
    person_swimming_tone1 = "๐๐ป"
    swimmer_tone1 = "๐๐ป"
    person_swimming_tone2 = "๐๐ผ"
    swimmer_tone2 = "๐๐ผ"
    person_swimming_tone3 = "๐๐ฝ"
    swimmer_tone3 = "๐๐ฝ"
    person_swimming_tone4 = "๐๐พ"
    swimmer_tone4 = "๐๐พ"
    person_swimming_tone5 = "๐๐ฟ"
    swimmer_tone5 = "๐๐ฟ"
    woman_swimming = "๐โ"
    woman_swimming_tone1 = "๐๐ปโ"
    woman_swimming_light_skin_tone = "๐๐ปโ"
    woman_swimming_tone2 = "๐๐ผโ"
    woman_swimming_medium_light_skin_tone = "๐๐ผโ"
    woman_swimming_tone3 = "๐๐ฝโ"
    woman_swimming_medium_skin_tone = "๐๐ฝโ"
    woman_swimming_tone4 = "๐๐พโ"
    woman_swimming_medium_dark_skin_tone = "๐๐พโ"
    woman_swimming_tone5 = "๐๐ฟโ"
    woman_swimming_dark_skin_tone = "๐๐ฟโ"
    man_swimming = "๐โ"
    man_swimming_tone1 = "๐๐ปโ"
    man_swimming_light_skin_tone = "๐๐ปโ"
    man_swimming_tone2 = "๐๐ผโ"
    man_swimming_medium_light_skin_tone = "๐๐ผโ"
    man_swimming_tone3 = "๐๐ฝโ"
    man_swimming_medium_skin_tone = "๐๐ฝโ"
    man_swimming_tone4 = "๐๐พโ"
    man_swimming_medium_dark_skin_tone = "๐๐พโ"
    man_swimming_tone5 = "๐๐ฟโ"
    man_swimming_dark_skin_tone = "๐๐ฟโ"
    person_playing_water_polo = "๐คฝ"
    water_polo = "๐คฝ"
    person_playing_water_polo_tone1 = "๐คฝ๐ป"
    water_polo_tone1 = "๐คฝ๐ป"
    person_playing_water_polo_tone2 = "๐คฝ๐ผ"
    water_polo_tone2 = "๐คฝ๐ผ"
    person_playing_water_polo_tone3 = "๐คฝ๐ฝ"
    water_polo_tone3 = "๐คฝ๐ฝ"
    person_playing_water_polo_tone4 = "๐คฝ๐พ"
    water_polo_tone4 = "๐คฝ๐พ"
    person_playing_water_polo_tone5 = "๐คฝ๐ฟ"
    water_polo_tone5 = "๐คฝ๐ฟ"
    woman_playing_water_polo = "๐คฝโ"
    woman_playing_water_polo_tone1 = "๐คฝ๐ปโ"
    woman_playing_water_polo_light_skin_tone = "๐คฝ๐ปโ"
    woman_playing_water_polo_tone2 = "๐คฝ๐ผโ"
    woman_playing_water_polo_medium_light_skin_tone = "๐คฝ๐ผโ"
    woman_playing_water_polo_tone3 = "๐คฝ๐ฝโ"
    woman_playing_water_polo_medium_skin_tone = "๐คฝ๐ฝโ"
    woman_playing_water_polo_tone4 = "๐คฝ๐พโ"
    woman_playing_water_polo_medium_dark_skin_tone = "๐คฝ๐พโ"
    woman_playing_water_polo_tone5 = "๐คฝ๐ฟโ"
    woman_playing_water_polo_dark_skin_tone = "๐คฝ๐ฟโ"
    man_playing_water_polo = "๐คฝโ"
    man_playing_water_polo_tone1 = "๐คฝ๐ปโ"
    man_playing_water_polo_light_skin_tone = "๐คฝ๐ปโ"
    man_playing_water_polo_tone2 = "๐คฝ๐ผโ"
    man_playing_water_polo_medium_light_skin_tone = "๐คฝ๐ผโ"
    man_playing_water_polo_tone3 = "๐คฝ๐ฝโ"
    man_playing_water_polo_medium_skin_tone = "๐คฝ๐ฝโ"
    man_playing_water_polo_tone4 = "๐คฝ๐พโ"
    man_playing_water_polo_medium_dark_skin_tone = "๐คฝ๐พโ"
    man_playing_water_polo_tone5 = "๐คฝ๐ฟโ"
    man_playing_water_polo_dark_skin_tone = "๐คฝ๐ฟโ"
    person_rowing_boat = "๐ฃ"
    rowboat = "๐ฃ"
    person_rowing_boat_tone1 = "๐ฃ๐ป"
    rowboat_tone1 = "๐ฃ๐ป"
    person_rowing_boat_tone2 = "๐ฃ๐ผ"
    rowboat_tone2 = "๐ฃ๐ผ"
    person_rowing_boat_tone3 = "๐ฃ๐ฝ"
    rowboat_tone3 = "๐ฃ๐ฝ"
    person_rowing_boat_tone4 = "๐ฃ๐พ"
    rowboat_tone4 = "๐ฃ๐พ"
    person_rowing_boat_tone5 = "๐ฃ๐ฟ"
    rowboat_tone5 = "๐ฃ๐ฟ"
    woman_rowing_boat = "๐ฃโ"
    woman_rowing_boat_tone1 = "๐ฃ๐ปโ"
    woman_rowing_boat_light_skin_tone = "๐ฃ๐ปโ"
    woman_rowing_boat_tone2 = "๐ฃ๐ผโ"
    woman_rowing_boat_medium_light_skin_tone = "๐ฃ๐ผโ"
    woman_rowing_boat_tone3 = "๐ฃ๐ฝโ"
    woman_rowing_boat_medium_skin_tone = "๐ฃ๐ฝโ"
    woman_rowing_boat_tone4 = "๐ฃ๐พโ"
    woman_rowing_boat_medium_dark_skin_tone = "๐ฃ๐พโ"
    woman_rowing_boat_tone5 = "๐ฃ๐ฟโ"
    woman_rowing_boat_dark_skin_tone = "๐ฃ๐ฟโ"
    man_rowing_boat = "๐ฃโ"
    man_rowing_boat_tone1 = "๐ฃ๐ปโ"
    man_rowing_boat_light_skin_tone = "๐ฃ๐ปโ"
    man_rowing_boat_tone2 = "๐ฃ๐ผโ"
    man_rowing_boat_medium_light_skin_tone = "๐ฃ๐ผโ"
    man_rowing_boat_tone3 = "๐ฃ๐ฝโ"
    man_rowing_boat_medium_skin_tone = "๐ฃ๐ฝโ"
    man_rowing_boat_tone4 = "๐ฃ๐พโ"
    man_rowing_boat_medium_dark_skin_tone = "๐ฃ๐พโ"
    man_rowing_boat_tone5 = "๐ฃ๐ฟโ"
    man_rowing_boat_dark_skin_tone = "๐ฃ๐ฟโ"
    person_climbing = "๐ง"
    person_climbing_tone1 = "๐ง๐ป"
    person_climbing_light_skin_tone = "๐ง๐ป"
    person_climbing_tone2 = "๐ง๐ผ"
    person_climbing_medium_light_skin_tone = "๐ง๐ผ"
    person_climbing_tone3 = "๐ง๐ฝ"
    person_climbing_medium_skin_tone = "๐ง๐ฝ"
    person_climbing_tone4 = "๐ง๐พ"
    person_climbing_medium_dark_skin_tone = "๐ง๐พ"
    person_climbing_tone5 = "๐ง๐ฟ"
    person_climbing_dark_skin_tone = "๐ง๐ฟ"
    woman_climbing = "๐งโ"
    woman_climbing_tone1 = "๐ง๐ปโ"
    woman_climbing_light_skin_tone = "๐ง๐ปโ"
    woman_climbing_tone2 = "๐ง๐ผโ"
    woman_climbing_medium_light_skin_tone = "๐ง๐ผโ"
    woman_climbing_tone3 = "๐ง๐ฝโ"
    woman_climbing_medium_skin_tone = "๐ง๐ฝโ"
    woman_climbing_tone4 = "๐ง๐พโ"
    woman_climbing_medium_dark_skin_tone = "๐ง๐พโ"
    woman_climbing_tone5 = "๐ง๐ฟโ"
    woman_climbing_dark_skin_tone = "๐ง๐ฟโ"
    man_climbing = "๐งโ"
    man_climbing_tone1 = "๐ง๐ปโ"
    man_climbing_light_skin_tone = "๐ง๐ปโ"
    man_climbing_tone2 = "๐ง๐ผโ"
    man_climbing_medium_light_skin_tone = "๐ง๐ผโ"
    man_climbing_tone3 = "๐ง๐ฝโ"
    man_climbing_medium_skin_tone = "๐ง๐ฝโ"
    man_climbing_tone4 = "๐ง๐พโ"
    man_climbing_medium_dark_skin_tone = "๐ง๐พโ"
    man_climbing_tone5 = "๐ง๐ฟโ"
    man_climbing_dark_skin_tone = "๐ง๐ฟโ"
    person_mountain_biking = "๐ต"
    mountain_bicyclist = "๐ต"
    person_mountain_biking_tone1 = "๐ต๐ป"
    mountain_bicyclist_tone1 = "๐ต๐ป"
    person_mountain_biking_tone2 = "๐ต๐ผ"
    mountain_bicyclist_tone2 = "๐ต๐ผ"
    person_mountain_biking_tone3 = "๐ต๐ฝ"
    mountain_bicyclist_tone3 = "๐ต๐ฝ"
    person_mountain_biking_tone4 = "๐ต๐พ"
    mountain_bicyclist_tone4 = "๐ต๐พ"
    person_mountain_biking_tone5 = "๐ต๐ฟ"
    mountain_bicyclist_tone5 = "๐ต๐ฟ"
    woman_mountain_biking = "๐ตโ"
    woman_mountain_biking_tone1 = "๐ต๐ปโ"
    woman_mountain_biking_light_skin_tone = "๐ต๐ปโ"
    woman_mountain_biking_tone2 = "๐ต๐ผโ"
    woman_mountain_biking_medium_light_skin_tone = "๐ต๐ผโ"
    woman_mountain_biking_tone3 = "๐ต๐ฝโ"
    woman_mountain_biking_medium_skin_tone = "๐ต๐ฝโ"
    woman_mountain_biking_tone4 = "๐ต๐พโ"
    woman_mountain_biking_medium_dark_skin_tone = "๐ต๐พโ"
    woman_mountain_biking_tone5 = "๐ต๐ฟโ"
    woman_mountain_biking_dark_skin_tone = "๐ต๐ฟโ"
    man_mountain_biking = "๐ตโ"
    man_mountain_biking_tone1 = "๐ต๐ปโ"
    man_mountain_biking_light_skin_tone = "๐ต๐ปโ"
    man_mountain_biking_tone2 = "๐ต๐ผโ"
    man_mountain_biking_medium_light_skin_tone = "๐ต๐ผโ"
    man_mountain_biking_tone3 = "๐ต๐ฝโ"
    man_mountain_biking_medium_skin_tone = "๐ต๐ฝโ"
    man_mountain_biking_tone4 = "๐ต๐พโ"
    man_mountain_biking_medium_dark_skin_tone = "๐ต๐พโ"
    man_mountain_biking_tone5 = "๐ต๐ฟโ"
    man_mountain_biking_dark_skin_tone = "๐ต๐ฟโ"
    person_biking = "๐ด"
    bicyclist = "๐ด"
    person_biking_tone1 = "๐ด๐ป"
    bicyclist_tone1 = "๐ด๐ป"
    person_biking_tone2 = "๐ด๐ผ"
    bicyclist_tone2 = "๐ด๐ผ"
    person_biking_tone3 = "๐ด๐ฝ"
    bicyclist_tone3 = "๐ด๐ฝ"
    person_biking_tone4 = "๐ด๐พ"
    bicyclist_tone4 = "๐ด๐พ"
    person_biking_tone5 = "๐ด๐ฟ"
    bicyclist_tone5 = "๐ด๐ฟ"
    woman_biking = "๐ดโ"
    woman_biking_tone1 = "๐ด๐ปโ"
    woman_biking_light_skin_tone = "๐ด๐ปโ"
    woman_biking_tone2 = "๐ด๐ผโ"
    woman_biking_medium_light_skin_tone = "๐ด๐ผโ"
    woman_biking_tone3 = "๐ด๐ฝโ"
    woman_biking_medium_skin_tone = "๐ด๐ฝโ"
    woman_biking_tone4 = "๐ด๐พโ"
    woman_biking_medium_dark_skin_tone = "๐ด๐พโ"
    woman_biking_tone5 = "๐ด๐ฟโ"
    woman_biking_dark_skin_tone = "๐ด๐ฟโ"
    man_biking = "๐ดโ"
    man_biking_tone1 = "๐ด๐ปโ"
    man_biking_light_skin_tone = "๐ด๐ปโ"
    man_biking_tone2 = "๐ด๐ผโ"
    man_biking_medium_light_skin_tone = "๐ด๐ผโ"
    man_biking_tone3 = "๐ด๐ฝโ"
    man_biking_medium_skin_tone = "๐ด๐ฝโ"
    man_biking_tone4 = "๐ด๐พโ"
    man_biking_medium_dark_skin_tone = "๐ด๐พโ"
    man_biking_tone5 = "๐ด๐ฟโ"
    man_biking_dark_skin_tone = "๐ด๐ฟโ"
    trophy = "๐"
    first_place = "๐ฅ"
    first_place_medal = "๐ฅ"
    second_place = "๐ฅ"
    second_place_medal = "๐ฅ"
    third_place = "๐ฅ"
    third_place_medal = "๐ฅ"
    medal = "๐"
    sports_medal = "๐"
    military_medal = "๐"
    rosette = "๐ต"
    reminder_ribbon = "๐"
    ticket = "๐ซ"
    tickets = "๐"
    admission_tickets = "๐"
    circus_tent = "๐ช"
    person_juggling = "๐คน"
    juggling = "๐คน"
    juggler = "๐คน"
    person_juggling_tone1 = "๐คน๐ป"
    juggling_tone1 = "๐คน๐ป"
    juggler_tone1 = "๐คน๐ป"
    person_juggling_tone2 = "๐คน๐ผ"
    juggling_tone2 = "๐คน๐ผ"
    juggler_tone2 = "๐คน๐ผ"
    person_juggling_tone3 = "๐คน๐ฝ"
    juggling_tone3 = "๐คน๐ฝ"
    juggler_tone3 = "๐คน๐ฝ"
    person_juggling_tone4 = "๐คน๐พ"
    juggling_tone4 = "๐คน๐พ"
    juggler_tone4 = "๐คน๐พ"
    person_juggling_tone5 = "๐คน๐ฟ"
    juggling_tone5 = "๐คน๐ฟ"
    juggler_tone5 = "๐คน๐ฟ"
    woman_juggling = "๐คนโ"
    woman_juggling_tone1 = "๐คน๐ปโ"
    woman_juggling_light_skin_tone = "๐คน๐ปโ"
    woman_juggling_tone2 = "๐คน๐ผโ"
    woman_juggling_medium_light_skin_tone = "๐คน๐ผโ"
    woman_juggling_tone3 = "๐คน๐ฝโ"
    woman_juggling_medium_skin_tone = "๐คน๐ฝโ"
    woman_juggling_tone4 = "๐คน๐พโ"
    woman_juggling_medium_dark_skin_tone = "๐คน๐พโ"
    woman_juggling_tone5 = "๐คน๐ฟโ"
    woman_juggling_dark_skin_tone = "๐คน๐ฟโ"
    man_juggling = "๐คนโ"
    man_juggling_tone1 = "๐คน๐ปโ"
    man_juggling_light_skin_tone = "๐คน๐ปโ"
    man_juggling_tone2 = "๐คน๐ผโ"
    man_juggling_medium_light_skin_tone = "๐คน๐ผโ"
    man_juggling_tone3 = "๐คน๐ฝโ"
    man_juggling_medium_skin_tone = "๐คน๐ฝโ"
    man_juggling_tone4 = "๐คน๐พโ"
    man_juggling_medium_dark_skin_tone = "๐คน๐พโ"
    man_juggling_tone5 = "๐คน๐ฟโ"
    man_juggling_dark_skin_tone = "๐คน๐ฟโ"
    performing_arts = "๐ญ"
    art = "๐จ"
    clapper = "๐ฌ"
    microphone = "๐ค"
    headphones = "๐ง"
    musical_score = "๐ผ"
    musical_keyboard = "๐น"
    drum = "๐ฅ"
    drum_with_drumsticks = "๐ฅ"
    saxophone = "๐ท"
    trumpet = "๐บ"
    banjo = "๐ช"
    guitar = "๐ธ"
    violin = "๐ป"
    game_die = "๐ฒ"
    chess_pawn = "โ"
    dart = "๐ฏ"
    kite = "๐ช"
    yo_yo = "๐ช"
    bowling = "๐ณ"
    video_game = "๐ฎ"
    slot_machine = "๐ฐ"
    jigsaw = "๐งฉ"
    red_car = "๐"
    taxi = "๐"
    blue_car = "๐"
    bus = "๐"
    trolleybus = "๐"
    race_car = "๐"
    racing_car = "๐"
    police_car = "๐"
    ambulance = "๐"
    fire_engine = "๐"
    minibus = "๐"
    truck = "๐"
    articulated_lorry = "๐"
    tractor = "๐"
    auto_rickshaw = "๐บ"
    motor_scooter = "๐ต"
    motorbike = "๐ต"
    motorcycle = "๐"
    racing_motorcycle = "๐"
    scooter = "๐ด"
    bike = "๐ฒ"
    motorized_wheelchair = "๐ฆผ"
    manual_wheelchair = "๐ฆฝ"
    rotating_light = "๐จ"
    oncoming_police_car = "๐"
    oncoming_bus = "๐"
    oncoming_automobile = "๐"
    oncoming_taxi = "๐"
    aerial_tramway = "๐ก"
    mountain_cableway = "๐ "
    suspension_railway = "๐"
    railway_car = "๐"
    train = "๐"
    mountain_railway = "๐"
    monorail = "๐"
    bullettrain_side = "๐"
    bullettrain_front = "๐"
    light_rail = "๐"
    steam_locomotive = "๐"
    train2 = "๐"
    metro = "๐"
    tram = "๐"
    station = "๐"
    airplane = "โ"
    airplane_departure = "๐ซ"
    airplane_arriving = "๐ฌ"
    airplane_small = "๐ฉ"
    small_airplane = "๐ฉ"
    seat = "๐บ"
    satellite_orbital = "๐ฐ"
    rocket = "๐"
    flying_saucer = "๐ธ"
    helicopter = "๐"
    canoe = "๐ถ"
    kayak = "๐ถ"
    sailboat = "โต"
    speedboat = "๐ค"
    motorboat = "๐ฅ"
    cruise_ship = "๐ณ"
    passenger_ship = "๐ณ"
    ferry = "โด"
    ship = "๐ข"
    anchor = "โ"
    fuelpump = "โฝ"
    construction = "๐ง"
    vertical_traffic_light = "๐ฆ"
    traffic_light = "๐ฅ"
    busstop = "๐"
    map = "๐บ"
    world_map = "๐บ"
    moyai = "๐ฟ"
    statue_of_liberty = "๐ฝ"
    tokyo_tower = "๐ผ"
    european_castle = "๐ฐ"
    japanese_castle = "๐ฏ"
    stadium = "๐"
    ferris_wheel = "๐ก"
    roller_coaster = "๐ข"
    carousel_horse = "๐ "
    fountain = "โฒ"
    beach_umbrella = "โฑ"
    umbrella_on_ground = "โฑ"
    beach = "๐"
    beach_with_umbrella = "๐"
    island = "๐"
    desert_island = "๐"
    desert = "๐"
    volcano = "๐"
    mountain = "โฐ"
    mountain_snow = "๐"
    snow_capped_mountain = "๐"
    mount_fuji = "๐ป"
    camping = "๐"
    tent = "โบ"
    house = "๐ "
    house_with_garden = "๐ก"
    homes = "๐"
    house_buildings = "๐"
    house_abandoned = "๐"
    derelict_house_building = "๐"
    construction_site = "๐"
    building_construction = "๐"
    factory = "๐ญ"
    office = "๐ข"
    department_store = "๐ฌ"
    post_office = "๐ฃ"
    european_post_office = "๐ค"
    hospital = "๐ฅ"
    bank = "๐ฆ"
    hotel = "๐จ"
    convenience_store = "๐ช"
    school = "๐ซ"
    love_hotel = "๐ฉ"
    wedding = "๐"
    classical_building = "๐"
    church = "โช"
    mosque = "๐"
    hindu_temple = "๐"
    synagogue = "๐"
    kaaba = "๐"
    shinto_shrine = "โฉ"
    railway_track = "๐ค"
    railroad_track = "๐ค"
    motorway = "๐ฃ"
    japan = "๐พ"
    rice_scene = "๐"
    park = "๐"
    national_park = "๐"
    sunrise = "๐"
    sunrise_over_mountains = "๐"
    stars = "๐ "
    sparkler = "๐"
    fireworks = "๐"
    city_sunset = "๐"
    city_sunrise = "๐"
    city_dusk = "๐"
    cityscape = "๐"
    night_with_stars = "๐"
    milky_way = "๐"
    bridge_at_night = "๐"
    foggy = "๐"
    watch = "โ"
    iphone = "๐ฑ"
    calling = "๐ฒ"
    computer = "๐ป"
    keyboard = "โจ"
    desktop = "๐ฅ"
    desktop_computer = "๐ฅ"
    printer = "๐จ"
    mouse_three_button = "๐ฑ"
    three_button_mouse = "๐ฑ"
    trackball = "๐ฒ"
    joystick = "๐น"
    compression = "๐"
    minidisc = "๐ฝ"
    floppy_disk = "๐พ"
    cd = "๐ฟ"
    dvd = "๐"
    vhs = "๐ผ"
    camera = "๐ท"
    camera_with_flash = "๐ธ"
    video_camera = "๐น"
    movie_camera = "๐ฅ"
    projector = "๐ฝ"
    film_projector = "๐ฝ"
    film_frames = "๐"
    telephone_receiver = "๐"
    telephone = "โ"
    pager = "๐"
    fax = "๐ "
    tv = "๐บ"
    radio = "๐ป"
    microphone2 = "๐"
    studio_microphone = "๐"
    level_slider = "๐"
    control_knobs = "๐"
    compass = "๐งญ"
    stopwatch = "โฑ"
    timer = "โฒ"
    timer_clock = "โฒ"
    alarm_clock = "โฐ"
    clock = "๐ฐ"
    mantlepiece_clock = "๐ฐ"
    hourglass = "โ"
    hourglass_flowing_sand = "โณ"
    satellite = "๐ก"
    battery = "๐"
    electric_plug = "๐"
    bulb = "๐ก"
    flashlight = "๐ฆ"
    candle = "๐ฏ"
    fire_extinguisher = "๐งฏ"
    oil = "๐ข"
    oil_drum = "๐ข"
    money_with_wings = "๐ธ"
    dollar = "๐ต"
    yen = "๐ด"
    euro = "๐ถ"
    pound = "๐ท"
    moneybag = "๐ฐ"
    credit_card = "๐ณ"
    gem = "๐"
    scales = "โ"
    toolbox = "๐งฐ"
    wrench = "๐ง"
    hammer = "๐จ"
    hammer_pick = "โ"
    hammer_and_pick = "โ"
    tools = "๐ "
    hammer_and_wrench = "๐ "
    pick = "โ"
    nut_and_bolt = "๐ฉ"
    gear = "โ"
    bricks = "๐งฑ"
    chains = "โ"
    magnet = "๐งฒ"
    gun = "๐ซ"
    bomb = "๐ฃ"
    firecracker = "๐งจ"
    axe = "๐ช"
    razor = "๐ช"
    knife = "๐ช"
    dagger = "๐ก"
    dagger_knife = "๐ก"
    crossed_swords = "โ"
    shield = "๐ก"
    smoking = "๐ฌ"
    coffin = "โฐ"
    urn = "โฑ"
    funeral_urn = "โฑ"
    amphora = "๐บ"
    diya_lamp = "๐ช"
    crystal_ball = "๐ฎ"
    prayer_beads = "๐ฟ"
    nazar_amulet = "๐งฟ"
    barber = "๐"
    alembic = "โ"
    telescope = "๐ญ"
    microscope = "๐ฌ"
    hole = "๐ณ"
    probing_cane = "๐ฆฏ"
    stethoscope = "๐ฉบ"
    adhesive_bandage = "๐ฉน"
    pill = "๐"
    syringe = "๐"
    drop_of_blood = "๐ฉธ"
    dna = "๐งฌ"
    microbe = "๐ฆ "
    petri_dish = "๐งซ"
    test_tube = "๐งช"
    thermometer = "๐ก"
    chair = "๐ช"
    broom = "๐งน"
    basket = "๐งบ"
    roll_of_paper = "๐งป"
    toilet = "๐ฝ"
    potable_water = "๐ฐ"
    shower = "๐ฟ"
    bathtub = "๐"
    bath = "๐"
    bath_tone1 = "๐๐ป"
    bath_tone2 = "๐๐ผ"
    bath_tone3 = "๐๐ฝ"
    bath_tone4 = "๐๐พ"
    bath_tone5 = "๐๐ฟ"
    soap = "๐งผ"
    sponge = "๐งฝ"
    squeeze_bottle = "๐งด"
    bellhop = "๐"
    bellhop_bell = "๐"
    key = "๐"
    key2 = "๐"
    old_key = "๐"
    door = "๐ช"
    couch = "๐"
    couch_and_lamp = "๐"
    bed = "๐"
    sleeping_accommodation = "๐"
    person_in_bed_tone1 = "๐๐ป"
    person_in_bed_light_skin_tone = "๐๐ป"
    person_in_bed_tone2 = "๐๐ผ"
    person_in_bed_medium_light_skin_tone = "๐๐ผ"
    person_in_bed_tone3 = "๐๐ฝ"
    person_in_bed_medium_skin_tone = "๐๐ฝ"
    person_in_bed_tone4 = "๐๐พ"
    person_in_bed_medium_dark_skin_tone = "๐๐พ"
    person_in_bed_tone5 = "๐๐ฟ"
    person_in_bed_dark_skin_tone = "๐๐ฟ"
    teddy_bear = "๐งธ"
    frame_photo = "๐ผ"
    frame_with_picture = "๐ผ"
    shopping_bags = "๐"
    shopping_cart = "๐"
    shopping_trolley = "๐"
    gift = "๐"
    balloon = "๐"
    flags = "๐"
    ribbon = "๐"
    confetti_ball = "๐"
    tada = "๐"
    dolls = "๐"
    izakaya_lantern = "๐ฎ"
    wind_chime = "๐"
    red_envelope = "๐งง"
    envelope = "โ"
    envelope_with_arrow = "๐ฉ"
    incoming_envelope = "๐จ"
    e_mail = "๐ง"
    email = "๐ง"
    love_letter = "๐"
    inbox_tray = "๐ฅ"
    outbox_tray = "๐ค"
    package = "๐ฆ"
    label = "๐ท"
    mailbox_closed = "๐ช"
    mailbox = "๐ซ"
    mailbox_with_mail = "๐ฌ"
    mailbox_with_no_mail = "๐ญ"
    postbox = "๐ฎ"
    postal_horn = "๐ฏ"
    scroll = "๐"
    page_with_curl = "๐"
    page_facing_up = "๐"
    bookmark_tabs = "๐"
    receipt = "๐งพ"
    bar_chart = "๐"
    chart_with_upwards_trend = "๐"
    chart_with_downwards_trend = "๐"
    notepad_spiral = "๐"
    spiral_note_pad = "๐"
    calendar_spiral = "๐"
    spiral_calendar_pad = "๐"
    calendar = "๐"
    date = "๐"
    wastebasket = "๐"
    card_index = "๐"
    card_box = "๐"
    card_file_box = "๐"
    ballot_box = "๐ณ"
    ballot_box_with_ballot = "๐ณ"
    file_cabinet = "๐"
    clipboard = "๐"
    file_folder = "๐"
    open_file_folder = "๐"
    dividers = "๐"
    card_index_dividers = "๐"
    newspaper2 = "๐"
    rolled_up_newspaper = "๐"
    newspaper = "๐ฐ"
    notebook = "๐"
    notebook_with_decorative_cover = "๐"
    ledger = "๐"
    closed_book = "๐"
    green_book = "๐"
    blue_book = "๐"
    orange_book = "๐"
    books = "๐"
    book = "๐"
    bookmark = "๐"
    safety_pin = "๐งท"
    link = "๐"
    paperclip = "๐"
    paperclips = "๐"
    linked_paperclips = "๐"
    triangular_ruler = "๐"
    straight_ruler = "๐"
    abacus = "๐งฎ"
    pushpin = "๐"
    round_pushpin = "๐"
    scissors = "โ"
    pen_ballpoint = "๐"
    lower_left_ballpoint_pen = "๐"
    pen_fountain = "๐"
    lower_left_fountain_pen = "๐"
    black_nib = "โ"
    paintbrush = "๐"
    lower_left_paintbrush = "๐"
    crayon = "๐"
    lower_left_crayon = "๐"
    pencil = "๐"
    memo = "๐"
    pencil2 = "โ"
    mag = "๐"
    mag_right = "๐"
    lock_with_ink_pen = "๐"
    closed_lock_with_key = "๐"
    lock = "๐"
    unlock = "๐"
    heart = "โค"
    orange_heart = "๐งก"
    yellow_heart = "๐"
    green_heart = "๐"
    blue_heart = "๐"
    purple_heart = "๐"
    black_heart = "๐ค"
    brown_heart = "๐ค"
    white_heart = "๐ค"
    broken_heart = "๐"
    heart_exclamation = "โฃ"
    heavy_heart_exclamation_mark_ornament = "โฃ"
    two_hearts = "๐"
    revolving_hearts = "๐"
    heartbeat = "๐"
    heartpulse = "๐"
    sparkling_heart = "๐"
    cupid = "๐"
    gift_heart = "๐"
    heart_decoration = "๐"
    peace = "โฎ"
    peace_symbol = "โฎ"
    cross = "โ"
    latin_cross = "โ"
    star_and_crescent = "โช"
    om_symbol = "๐"
    wheel_of_dharma = "โธ"
    star_of_david = "โก"
    six_pointed_star = "๐ฏ"
    menorah = "๐"
    yin_yang = "โฏ"
    orthodox_cross = "โฆ"
    place_of_worship = "๐"
    worship_symbol = "๐"
    ophiuchus = "โ"
    aries = "โ"
    taurus = "โ"
    gemini = "โ"
    cancer = "โ"
    leo = "โ"
    virgo = "โ"
    libra = "โ"
    scorpius = "โ"
    sagittarius = "โ"
    capricorn = "โ"
    aquarius = "โ"
    pisces = "โ"
    id = "๐"
    atom = "โ"
    atom_symbol = "โ"
    accept = "๐"
    radioactive = "โข"
    radioactive_sign = "โข"
    biohazard = "โฃ"
    biohazard_sign = "โฃ"
    mobile_phone_off = "๐ด"
    vibration_mode = "๐ณ"
    u6709 = "๐ถ"
    u7121 = "๐"
    u7533 = "๐ธ"
    u55b6 = "๐บ"
    u6708 = "๐ท"
    eight_pointed_black_star = "โด"
    vs = "๐"
    white_flower = "๐ฎ"
    ideograph_advantage = "๐"
    secret = "ใ"
    congratulations = "ใ"
    u6e80 = "๐ต"
    u5272 = "๐น"
    u7981 = "๐ฒ"
    a = "๐ฐ"
    b = "๐ฑ"
    ab = "๐"
    cl = "๐"
    o2 = "๐พ"
    sos = "๐"
    x = "โ"
    o = "โญ"
    octagonal_sign = "๐"
    stop_sign = "๐"
    no_entry = "โ"
    name_badge = "๐"
    no_entry_sign = "๐ซ"
    anger = "๐ข"
    hotsprings = "โจ"
    no_pedestrians = "๐ท"
    do_not_litter = "๐ฏ"
    no_bicycles = "๐ณ"
    non_potable_water = "๐ฑ"
    underage = "๐"
    no_mobile_phones = "๐ต"
    no_smoking = "๐ญ"
    exclamation = "โ"
    grey_exclamation = "โ"
    question = "โ"
    grey_question = "โ"
    bangbang = "โผ"
    interrobang = "โ"
    low_brightness = "๐"
    high_brightness = "๐"
    part_alternation_mark = "ใฝ"
    warning = "โ "
    children_crossing = "๐ธ"
    trident = "๐ฑ"
    fleur_de_lis = "โ"
    beginner = "๐ฐ"
    recycle = "โป"
    white_check_mark = "โ"
    u6307 = "๐ฏ"
    chart = "๐น"
    sparkle = "โ"
    eight_spoked_asterisk = "โณ"
    negative_squared_cross_mark = "โ"
    globe_with_meridians = "๐"
    diamond_shape_with_a_dot_inside = "๐ "
    m = "โ"
    cyclone = "๐"
    zzz = "๐ค"
    atm = "๐ง"
    wc = "๐พ"
    wheelchair = "โฟ"
    parking = "๐ฟ"
    u7a7a = "๐ณ"
    sa = "๐"
    customs = "๐"
    baggage_claim = "๐"
    left_luggage = "๐"
    mens = "๐น"
    womens = "๐บ"
    baby_symbol = "๐ผ"
    restroom = "๐ป"
    put_litter_in_its_place = "๐ฎ"
    cinema = "๐ฆ"
    signal_strength = "๐ถ"
    koko = "๐"
    symbols = "๐ฃ"
    information_source = "โน"
    abc = "๐ค"
    abcd = "๐ก"
    capital_abcd = "๐ "
    ng = "๐"
    ok = "๐"
    up = "๐"
    cool = "๐"
    new = "๐"
    free = "๐"
    zero = "0๏ธโฃ"
    one = "1๏ธโฃ"
    two = "2๏ธโฃ"
    three = "3๏ธโฃ"
    four = "4๏ธโฃ"
    five = "5๏ธโฃ"
    six = "6๏ธโฃ"
    seven = "7๏ธโฃ"
    eight = "8๏ธโฃ"
    nine = "9๏ธโฃ"
    keycap_ten = "๐"
    hash = "#๏ธโฃ"
    keycap_asterisk = "*๏ธโฃ"
    eject = "โ"
    eject_symbol = "โ"
    arrow_forward = "โถ"
    pause_button = "โธ"
    double_vertical_bar = "โธ"
    play_pause = "โฏ"
    stop_button = "โน"
    record_button = "โบ"
    track_next = "โญ"
    next_track = "โญ"
    track_previous = "โฎ"
    previous_track = "โฎ"
    fast_forward = "โฉ"
    rewind = "โช"
    arrow_double_up = "โซ"
    arrow_double_down = "โฌ"
    arrow_backward = "โ"
    arrow_up_small = "๐ผ"
    arrow_down_small = "๐ฝ"
    arrow_right = "โก"
    arrow_left = "โฌ"
    arrow_up = "โฌ"
    arrow_down = "โฌ"
    arrow_upper_right = "โ"
    arrow_lower_right = "โ"
    arrow_lower_left = "โ"
    arrow_upper_left = "โ"
    arrow_up_down = "โ"
    left_right_arrow = "โ"
    arrow_right_hook = "โช"
    leftwards_arrow_with_hook = "โฉ"
    arrow_heading_up = "โคด"
    arrow_heading_down = "โคต"
    twisted_rightwards_arrows = "๐"
    repeat = "๐"
    repeat_one = "๐"
    arrows_counterclockwise = "๐"
    arrows_clockwise = "๐"
    musical_note = "๐ต"
    notes = "๐ถ"
    heavy_plus_sign = "โ"
    heavy_minus_sign = "โ"
    heavy_division_sign = "โ"
    heavy_multiplication_x = "โ"
    infinity = "โพ"
    heavy_dollar_sign = "๐ฒ"
    currency_exchange = "๐ฑ"
    tm = "โข"
    copyright = "ยฉ"
    registered = "ยฎ"
    wavy_dash = "ใฐ"
    curly_loop = "โฐ"
    loop = "โฟ"
    end = "๐"
    back = "๐"
    on = "๐"
    top = "๐"
    soon = "๐"
    heavy_check_mark = "โ"
    ballot_box_with_check = "โ"
    radio_button = "๐"
    white_circle = "โช"
    black_circle = "โซ"
    red_circle = "๐ด"
    blue_circle = "๐ต"
    brown_circle = "๐ค"
    purple_circle = "๐ฃ"
    green_circle = "๐ข"
    yellow_circle = "๐ก"
    orange_circle = "๐ "
    small_red_triangle = "๐บ"
    small_red_triangle_down = "๐ป"
    small_orange_diamond = "๐ธ"
    small_blue_diamond = "๐น"
    large_orange_diamond = "๐ถ"
    large_blue_diamond = "๐ท"
    white_square_button = "๐ณ"
    black_square_button = "๐ฒ"
    black_small_square = "โช"
    white_small_square = "โซ"
    black_medium_small_square = "โพ"
    white_medium_small_square = "โฝ"
    black_medium_square = "โผ"
    white_medium_square = "โป"
    black_large_square = "โฌ"
    white_large_square = "โฌ"
    orange_square = "๐ง"
    blue_square = "๐ฆ"
    red_square = "๐ฅ"
    brown_square = "๐ซ"
    purple_square = "๐ช"
    green_square = "๐ฉ"
    yellow_square = "๐จ"
    speaker = "๐"
    mute = "๐"
    sound = "๐"
    loud_sound = "๐"
    bell = "๐"
    no_bell = "๐"
    mega = "๐ฃ"
    loudspeaker = "๐ข"
    speech_left = "๐จ"
    left_speech_bubble = "๐จ"
    eye_in_speech_bubble = "๐๐จ"
    speech_balloon = "๐ฌ"
    thought_balloon = "๐ญ"
    anger_right = "๐ฏ"
    right_anger_bubble = "๐ฏ"
    spades = "โ "
    clubs = "โฃ"
    hearts = "โฅ"
    diamonds = "โฆ"
    black_joker = "๐"
    flower_playing_cards = "๐ด"
    mahjong = "๐"
    clock1 = "๐"
    clock2 = "๐"
    clock3 = "๐"
    clock4 = "๐"
    clock5 = "๐"
    clock6 = "๐"
    clock7 = "๐"
    clock8 = "๐"
    clock9 = "๐"
    clock10 = "๐"
    clock11 = "๐"
    clock12 = "๐"
    clock130 = "๐"
    clock230 = "๐"
    clock330 = "๐"
    clock430 = "๐"
    clock530 = "๐ "
    clock630 = "๐ก"
    clock730 = "๐ข"
    clock830 = "๐ฃ"
    clock930 = "๐ค"
    clock1030 = "๐ฅ"
    clock1130 = "๐ฆ"
    clock1230 = "๐ง"
    female_sign = "โ"
    male_sign = "โ"
    medical_symbol = "โ"
    regional_indicator_z = "๐ฟ"
    regional_indicator_y = "๐พ"
    regional_indicator_x = "๐ฝ"
    regional_indicator_w = "๐ผ"
    regional_indicator_v = "๐ป"
    regional_indicator_u = "๐บ"
    regional_indicator_t = "๐น"
    regional_indicator_s = "๐ธ"
    regional_indicator_r = "๐ท"
    regional_indicator_q = "๐ถ"
    regional_indicator_p = "๐ต"
    regional_indicator_o = "๐ด"
    regional_indicator_n = "๐ณ"
    regional_indicator_m = "๐ฒ"
    regional_indicator_l = "๐ฑ"
    regional_indicator_k = "๐ฐ"
    regional_indicator_j = "๐ฏ"
    regional_indicator_i = "๐ฎ"
    regional_indicator_h = "๐ญ"
    regional_indicator_g = "๐ฌ"
    regional_indicator_f = "๐ซ"
    regional_indicator_e = "๐ช"
    regional_indicator_d = "๐ฉ"
    regional_indicator_c = "๐จ"
    regional_indicator_b = "๐ง"
    regional_indicator_a = "๐ฆ"
    flag_white = "๐ณ"
    flag_black = "๐ด"
    checkered_flag = "๐"
    triangular_flag_on_post = "๐ฉ"
    rainbow_flag = "๐ณ๐"
    gay_pride_flag = "๐ณ๐"
    pirate_flag = "๐ดโ "
    flag_af = "๐ฆ๐ซ"
    flag_ax = "๐ฆ๐ฝ"
    flag_al = "๐ฆ๐ฑ"
    flag_dz = "๐ฉ๐ฟ"
    flag_as = "๐ฆ๐ธ"
    flag_ad = "๐ฆ๐ฉ"
    flag_ao = "๐ฆ๐ด"
    flag_ai = "๐ฆ๐ฎ"
    flag_aq = "๐ฆ๐ถ"
    flag_ag = "๐ฆ๐ฌ"
    flag_ar = "๐ฆ๐ท"
    flag_am = "๐ฆ๐ฒ"
    flag_aw = "๐ฆ๐ผ"
    flag_au = "๐ฆ๐บ"
    flag_at = "๐ฆ๐น"
    flag_az = "๐ฆ๐ฟ"
    flag_bs = "๐ง๐ธ"
    flag_bh = "๐ง๐ญ"
    flag_bd = "๐ง๐ฉ"
    flag_bb = "๐ง๐ง"
    flag_by = "๐ง๐พ"
    flag_be = "๐ง๐ช"
    flag_bz = "๐ง๐ฟ"
    flag_bj = "๐ง๐ฏ"
    flag_bm = "๐ง๐ฒ"
    flag_bt = "๐ง๐น"
    flag_bo = "๐ง๐ด"
    flag_ba = "๐ง๐ฆ"
    flag_bw = "๐ง๐ผ"
    flag_br = "๐ง๐ท"
    flag_io = "๐ฎ๐ด"
    flag_vg = "๐ป๐ฌ"
    flag_bn = "๐ง๐ณ"
    flag_bg = "๐ง๐ฌ"
    flag_bf = "๐ง๐ซ"
    flag_bi = "๐ง๐ฎ"
    flag_kh = "๐ฐ๐ญ"
    flag_cm = "๐จ๐ฒ"
    flag_ca = "๐จ๐ฆ"
    flag_ic = "๐ฎ๐จ"
    flag_cv = "๐จ๐ป"
    flag_bq = "๐ง๐ถ"
    flag_ky = "๐ฐ๐พ"
    flag_cf = "๐จ๐ซ"
    flag_td = "๐น๐ฉ"
    flag_cl = "๐จ๐ฑ"
    flag_cn = "๐จ๐ณ"
    flag_cx = "๐จ๐ฝ"
    flag_cc = "๐จ๐จ"
    flag_co = "๐จ๐ด"
    flag_km = "๐ฐ๐ฒ"
    flag_cg = "๐จ๐ฌ"
    flag_cd = "๐จ๐ฉ"
    flag_ck = "๐จ๐ฐ"
    flag_cr = "๐จ๐ท"
    flag_ci = "๐จ๐ฎ"
    flag_hr = "๐ญ๐ท"
    flag_cu = "๐จ๐บ"
    flag_cw = "๐จ๐ผ"
    flag_cy = "๐จ๐พ"
    flag_cz = "๐จ๐ฟ"
    flag_dk = "๐ฉ๐ฐ"
    flag_dj = "๐ฉ๐ฏ"
    flag_dm = "๐ฉ๐ฒ"
    flag_do = "๐ฉ๐ด"
    flag_ec = "๐ช๐จ"
    flag_eg = "๐ช๐ฌ"
    flag_sv = "๐ธ๐ป"
    flag_gq = "๐ฌ๐ถ"
    flag_er = "๐ช๐ท"
    flag_ee = "๐ช๐ช"
    flag_et = "๐ช๐น"
    flag_eu = "๐ช๐บ"
    flag_fk = "๐ซ๐ฐ"
    flag_fo = "๐ซ๐ด"
    flag_fj = "๐ซ๐ฏ"
    flag_fi = "๐ซ๐ฎ"
    flag_fr = "๐ซ๐ท"
    flag_gf = "๐ฌ๐ซ"
    flag_pf = "๐ต๐ซ"
    flag_tf = "๐น๐ซ"
    flag_ga = "๐ฌ๐ฆ"
    flag_gm = "๐ฌ๐ฒ"
    flag_ge = "๐ฌ๐ช"
    flag_de = "๐ฉ๐ช"
    flag_gh = "๐ฌ๐ญ"
    flag_gi = "๐ฌ๐ฎ"
    flag_gr = "๐ฌ๐ท"
    flag_gl = "๐ฌ๐ฑ"
    flag_gd = "๐ฌ๐ฉ"
    flag_gp = "๐ฌ๐ต"
    flag_gu = "๐ฌ๐บ"
    flag_gt = "๐ฌ๐น"
    flag_gg = "๐ฌ๐ฌ"
    flag_gn = "๐ฌ๐ณ"
    flag_gw = "๐ฌ๐ผ"
    flag_gy = "๐ฌ๐พ"
    flag_ht = "๐ญ๐น"
    flag_hn = "๐ญ๐ณ"
    flag_hk = "๐ญ๐ฐ"
    flag_hu = "๐ญ๐บ"
    flag_is = "๐ฎ๐ธ"
    flag_in = "๐ฎ๐ณ"
    flag_id = "๐ฎ๐ฉ"
    flag_ir = "๐ฎ๐ท"
    flag_iq = "๐ฎ๐ถ"
    flag_ie = "๐ฎ๐ช"
    flag_im = "๐ฎ๐ฒ"
    flag_il = "๐ฎ๐ฑ"
    flag_it = "๐ฎ๐น"
    flag_jm = "๐ฏ๐ฒ"
    flag_jp = "๐ฏ๐ต"
    crossed_flags = "๐"
    flag_je = "๐ฏ๐ช"
    flag_jo = "๐ฏ๐ด"
    flag_kz = "๐ฐ๐ฟ"
    flag_ke = "๐ฐ๐ช"
    flag_ki = "๐ฐ๐ฎ"
    flag_xk = "๐ฝ๐ฐ"
    flag_kw = "๐ฐ๐ผ"
    flag_kg = "๐ฐ๐ฌ"
    flag_la = "๐ฑ๐ฆ"
    flag_lv = "๐ฑ๐ป"
    flag_lb = "๐ฑ๐ง"
    flag_ls = "๐ฑ๐ธ"
    flag_lr = "๐ฑ๐ท"
    flag_ly = "๐ฑ๐พ"
    flag_li = "๐ฑ๐ฎ"
    flag_lt = "๐ฑ๐น"
    flag_lu = "๐ฑ๐บ"
    flag_mo = "๐ฒ๐ด"
    flag_mk = "๐ฒ๐ฐ"
    flag_mg = "๐ฒ๐ฌ"
    flag_mw = "๐ฒ๐ผ"
    flag_my = "๐ฒ๐พ"
    flag_mv = "๐ฒ๐ป"
    flag_ml = "๐ฒ๐ฑ"
    flag_mt = "๐ฒ๐น"
    flag_mh = "๐ฒ๐ญ"
    flag_mq = "๐ฒ๐ถ"
    flag_mr = "๐ฒ๐ท"
    flag_mu = "๐ฒ๐บ"
    flag_yt = "๐พ๐น"
    flag_mx = "๐ฒ๐ฝ"
    flag_fm = "๐ซ๐ฒ"
    flag_md = "๐ฒ๐ฉ"
    flag_mc = "๐ฒ๐จ"
    flag_mn = "๐ฒ๐ณ"
    flag_me = "๐ฒ๐ช"
    flag_ms = "๐ฒ๐ธ"
    flag_ma = "๐ฒ๐ฆ"
    flag_mz = "๐ฒ๐ฟ"
    flag_mm = "๐ฒ๐ฒ"
    flag_na = "๐ณ๐ฆ"
    flag_nr = "๐ณ๐ท"
    flag_np = "๐ณ๐ต"
    flag_nl = "๐ณ๐ฑ"
    flag_nc = "๐ณ๐จ"
    flag_nz = "๐ณ๐ฟ"
    flag_ni = "๐ณ๐ฎ"
    flag_ne = "๐ณ๐ช"
    flag_ng = "๐ณ๐ฌ"
    flag_nu = "๐ณ๐บ"
    flag_nf = "๐ณ๐ซ"
    flag_kp = "๐ฐ๐ต"
    flag_mp = "๐ฒ๐ต"
    flag_no = "๐ณ๐ด"
    flag_om = "๐ด๐ฒ"
    flag_pk = "๐ต๐ฐ"
    flag_pw = "๐ต๐ผ"
    flag_ps = "๐ต๐ธ"
    flag_pa = "๐ต๐ฆ"
    flag_pg = "๐ต๐ฌ"
    flag_py = "๐ต๐พ"
    flag_pe = "๐ต๐ช"
    flag_ph = "๐ต๐ญ"
    flag_pn = "๐ต๐ณ"
    flag_pl = "๐ต๐ฑ"
    flag_pt = "๐ต๐น"
    flag_pr = "๐ต๐ท"
    flag_qa = "๐ถ๐ฆ"
    flag_re = "๐ท๐ช"
    flag_ro = "๐ท๐ด"
    flag_ru = "๐ท๐บ"
    flag_rw = "๐ท๐ผ"
    flag_ws = "๐ผ๐ธ"
    flag_sm = "๐ธ๐ฒ"
    flag_st = "๐ธ๐น"
    flag_sa = "๐ธ๐ฆ"
    flag_sn = "๐ธ๐ณ"
    flag_rs = "๐ท๐ธ"
    flag_sc = "๐ธ๐จ"
    flag_sl = "๐ธ๐ฑ"
    flag_sg = "๐ธ๐ฌ"
    flag_sx = "๐ธ๐ฝ"
    flag_sk = "๐ธ๐ฐ"
    flag_si = "๐ธ๐ฎ"
    flag_gs = "๐ฌ๐ธ"
    flag_sb = "๐ธ๐ง"
    flag_so = "๐ธ๐ด"
    flag_za = "๐ฟ๐ฆ"
    flag_kr = "๐ฐ๐ท"
    flag_ss = "๐ธ๐ธ"
    flag_es = "๐ช๐ธ"
    flag_lk = "๐ฑ๐ฐ"
    flag_bl = "๐ง๐ฑ"
    flag_sh = "๐ธ๐ญ"
    flag_kn = "๐ฐ๐ณ"
    flag_lc = "๐ฑ๐จ"
    flag_pm = "๐ต๐ฒ"
    flag_vc = "๐ป๐จ"
    flag_sd = "๐ธ๐ฉ"
    flag_sr = "๐ธ๐ท"
    flag_sz = "๐ธ๐ฟ"
    flag_se = "๐ธ๐ช"
    flag_ch = "๐จ๐ญ"
    flag_sy = "๐ธ๐พ"
    flag_tw = "๐น๐ผ"
    flag_tj = "๐น๐ฏ"
    flag_tz = "๐น๐ฟ"
    flag_th = "๐น๐ญ"
    flag_tl = "๐น๐ฑ"
    flag_tg = "๐น๐ฌ"
    flag_tk = "๐น๐ฐ"
    flag_to = "๐น๐ด"
    flag_tt = "๐น๐น"
    flag_tn = "๐น๐ณ"
    flag_tr = "๐น๐ท"
    flag_tm = "๐น๐ฒ"
    flag_tc = "๐น๐จ"
    flag_vi = "๐ป๐ฎ"
    flag_tv = "๐น๐ป"
    flag_ug = "๐บ๐ฌ"
    flag_ua = "๐บ๐ฆ"
    flag_ae = "๐ฆ๐ช"
    flag_gb = "๐ฌ๐ง"
    england = "๐ด"
    scotland = "๐ด"
    wales = "๐ด"
    flag_us = "๐บ๐ธ"
    flag_uy = "๐บ๐พ"
    flag_uz = "๐บ๐ฟ"
    flag_vu = "๐ป๐บ"
    flag_va = "๐ป๐ฆ"
    flag_ve = "๐ป๐ช"
    flag_vn = "๐ป๐ณ"
    flag_wf = "๐ผ๐ซ"
    flag_eh = "๐ช๐ญ"
    flag_ye = "๐พ๐ช"
    flag_zm = "๐ฟ๐ฒ"
    flag_zw = "๐ฟ๐ผ"
    flag_ac = "๐ฆ๐จ"
    flag_bv = "๐ง๐ป"
    flag_cp = "๐จ๐ต"
    flag_ea = "๐ช๐ฆ"
    flag_dg = "๐ฉ๐ฌ"
    flag_hm = "๐ญ๐ฒ"
    flag_mf = "๐ฒ๐ซ"
    flag_sj = "๐ธ๐ฏ"
    flag_ta = "๐น๐ฆ"
    flag_um = "๐บ๐ฒ"
    united_nations = "๐บ๐ณ"


class EmojiNameType (str, Enum):
    hundred = "100"
    one_two_three_four = "1234"
    grinning = "grinning"
    smiley = "smiley"
    smile = "smile"
    grin = "grin"
    laughing = "laughing"
    satisfied = "satisfied"
    sweat_smile = "sweat_smile"
    joy = "joy"
    rofl = "rofl"
    rolling_on_the_floor_laughing = "rolling_on_the_floor_laughing"
    relaxed = "relaxed"
    blush = "blush"
    innocent = "innocent"
    slight_smile = "slight_smile"
    slightly_smiling_face = "slightly_smiling_face"
    upside_down = "upside_down"
    upside_down_face = "upside_down_face"
    wink = "wink"
    relieved = "relieved"
    heart_eyes = "heart_eyes"
    smiling_face_with_3_hearts = "smiling_face_with_3_hearts"
    kissing_heart = "kissing_heart"
    kissing = "kissing"
    kissing_smiling_eyes = "kissing_smiling_eyes"
    kissing_closed_eyes = "kissing_closed_eyes"
    yum = "yum"
    stuck_out_tongue = "stuck_out_tongue"
    stuck_out_tongue_closed_eyes = "stuck_out_tongue_closed_eyes"
    stuck_out_tongue_winking_eye = "stuck_out_tongue_winking_eye"
    zany_face = "zany_face"
    face_with_raised_eyebrow = "face_with_raised_eyebrow"
    face_with_monocle = "face_with_monocle"
    nerd = "nerd"
    nerd_face = "nerd_face"
    sunglasses = "sunglasses"
    star_struck = "star_struck"
    partying_face = "partying_face"
    smirk = "smirk"
    unamused = "unamused"
    disappointed = "disappointed"
    pensive = "pensive"
    worried = "worried"
    confused = "confused"
    slight_frown = "slight_frown"
    slightly_frowning_face = "slightly_frowning_face"
    frowning2 = "frowning2"
    white_frowning_face = "white_frowning_face"
    persevere = "persevere"
    confounded = "confounded"
    tired_face = "tired_face"
    weary = "weary"
    pleading_face = "pleading_face"
    cry = "cry"
    sob = "sob"
    triumph = "triumph"
    angry = "angry"
    rage = "rage"
    face_with_symbols_over_mouth = "face_with_symbols_over_mouth"
    exploding_head = "exploding_head"
    flushed = "flushed"
    hot_face = "hot_face"
    cold_face = "cold_face"
    scream = "scream"
    fearful = "fearful"
    cold_sweat = "cold_sweat"
    disappointed_relieved = "disappointed_relieved"
    sweat = "sweat"
    hugging = "hugging"
    hugging_face = "hugging_face"
    thinking = "thinking"
    thinking_face = "thinking_face"
    face_with_hand_over_mouth = "face_with_hand_over_mouth"
    yawning_face = "yawning_face"
    shushing_face = "shushing_face"
    lying_face = "lying_face"
    liar = "liar"
    no_mouth = "no_mouth"
    neutral_face = "neutral_face"
    expressionless = "expressionless"
    grimacing = "grimacing"
    rolling_eyes = "rolling_eyes"
    face_with_rolling_eyes = "face_with_rolling_eyes"
    hushed = "hushed"
    frowning = "frowning"
    anguished = "anguished"
    open_mouth = "open_mouth"
    astonished = "astonished"
    sleeping = "sleeping"
    drooling_face = "drooling_face"
    drool = "drool"
    sleepy = "sleepy"
    dizzy_face = "dizzy_face"
    zipper_mouth = "zipper_mouth"
    zipper_mouth_face = "zipper_mouth_face"
    woozy_face = "woozy_face"
    nauseated_face = "nauseated_face"
    sick = "sick"
    face_vomiting = "face_vomiting"
    sneezing_face = "sneezing_face"
    sneeze = "sneeze"
    mask = "mask"
    thermometer_face = "thermometer_face"
    face_with_thermometer = "face_with_thermometer"
    head_bandage = "head_bandage"
    face_with_head_bandage = "face_with_head_bandage"
    money_mouth = "money_mouth"
    money_mouth_face = "money_mouth_face"
    cowboy = "cowboy"
    face_with_cowboy_hat = "face_with_cowboy_hat"
    smiling_imp = "smiling_imp"
    imp = "imp"
    japanese_ogre = "japanese_ogre"
    japanese_goblin = "japanese_goblin"
    clown = "clown"
    clown_face = "clown_face"
    poop = "poop"
    shit = "shit"
    hankey = "hankey"
    poo = "poo"
    ghost = "ghost"
    skull = "skull"
    skeleton = "skeleton"
    skull_crossbones = "skull_crossbones"
    skull_and_crossbones = "skull_and_crossbones"
    alien = "alien"
    space_invader = "space_invader"
    robot = "robot"
    robot_face = "robot_face"
    jack_o_lantern = "jack_o_lantern"
    smiley_cat = "smiley_cat"
    smile_cat = "smile_cat"
    joy_cat = "joy_cat"
    heart_eyes_cat = "heart_eyes_cat"
    smirk_cat = "smirk_cat"
    kissing_cat = "kissing_cat"
    scream_cat = "scream_cat"
    crying_cat_face = "crying_cat_face"
    pouting_cat = "pouting_cat"
    palms_up_together = "palms_up_together"
    palms_up_together_tone1 = "palms_up_together_tone1"
    palms_up_together_light_skin_tone = "palms_up_together_light_skin_tone"
    palms_up_together_tone2 = "palms_up_together_tone2"
    palms_up_together_medium_light_skin_tone = "palms_up_together_medium_light_skin_tone"
    palms_up_together_tone3 = "palms_up_together_tone3"
    palms_up_together_medium_skin_tone = "palms_up_together_medium_skin_tone"
    palms_up_together_tone4 = "palms_up_together_tone4"
    palms_up_together_medium_dark_skin_tone = "palms_up_together_medium_dark_skin_tone"
    palms_up_together_tone5 = "palms_up_together_tone5"
    palms_up_together_dark_skin_tone = "palms_up_together_dark_skin_tone"
    open_hands = "open_hands"
    open_hands_tone1 = "open_hands_tone1"
    open_hands_tone2 = "open_hands_tone2"
    open_hands_tone3 = "open_hands_tone3"
    open_hands_tone4 = "open_hands_tone4"
    open_hands_tone5 = "open_hands_tone5"
    raised_hands = "raised_hands"
    raised_hands_tone1 = "raised_hands_tone1"
    raised_hands_tone2 = "raised_hands_tone2"
    raised_hands_tone3 = "raised_hands_tone3"
    raised_hands_tone4 = "raised_hands_tone4"
    raised_hands_tone5 = "raised_hands_tone5"
    clap = "clap"
    clap_tone1 = "clap_tone1"
    clap_tone2 = "clap_tone2"
    clap_tone3 = "clap_tone3"
    clap_tone4 = "clap_tone4"
    clap_tone5 = "clap_tone5"
    handshake = "handshake"
    shaking_hands = "shaking_hands"
    thumbsup = "thumbsup"
    plus_one = "+1"
    thumbup = "thumbup"
    thumbsup_tone1 = "thumbsup_tone1"
    plus_one_tone1 = "+1_tone1"
    thumbup_tone1 = "thumbup_tone1"
    thumbsup_tone2 = "thumbsup_tone2"
    plus_one_tone2 = "+1_tone2"
    thumbup_tone2 = "thumbup_tone2"
    thumbsup_tone3 = "thumbsup_tone3"
    plus_one_tone3 = "+1_tone3"
    thumbup_tone3 = "thumbup_tone3"
    thumbsup_tone4 = "thumbsup_tone4"
    plus_one_tone4 = "+1_tone4"
    thumbup_tone4 = "thumbup_tone4"
    thumbsup_tone5 = "thumbsup_tone5"
    plus_one_tone5 = "+1_tone5"
    thumbup_tone5 = "thumbup_tone5"
    thumbsdown = "thumbsdown"
    minus_one = "-1"
    thumbdown = "thumbdown"
    thumbsdown_tone1 = "thumbsdown_tone1"
    minus_one_tone1 = "_1_tone1"
    thumbdown_tone1 = "thumbdown_tone1"
    thumbsdown_tone2 = "thumbsdown_tone2"
    minus_one_tone2 = "_1_tone2"
    thumbdown_tone2 = "thumbdown_tone2"
    thumbsdown_tone3 = "thumbsdown_tone3"
    minus_one_tone3 = "_1_tone3"
    thumbdown_tone3 = "thumbdown_tone3"
    thumbsdown_tone4 = "thumbsdown_tone4"
    minus_one_tone4 = "_1_tone4"
    thumbdown_tone4 = "thumbdown_tone4"
    thumbsdown_tone5 = "thumbsdown_tone5"
    minus_one_tone5 = "_1_tone5"
    thumbdown_tone5 = "thumbdown_tone5"
    punch = "punch"
    punch_tone1 = "punch_tone1"
    punch_tone2 = "punch_tone2"
    punch_tone3 = "punch_tone3"
    punch_tone4 = "punch_tone4"
    punch_tone5 = "punch_tone5"
    fist = "fist"
    fist_tone1 = "fist_tone1"
    fist_tone2 = "fist_tone2"
    fist_tone3 = "fist_tone3"
    fist_tone4 = "fist_tone4"
    fist_tone5 = "fist_tone5"
    left_facing_fist = "left_facing_fist"
    left_fist = "left_fist"
    left_facing_fist_tone1 = "left_facing_fist_tone1"
    left_fist_tone1 = "left_fist_tone1"
    left_facing_fist_tone2 = "left_facing_fist_tone2"
    left_fist_tone2 = "left_fist_tone2"
    left_facing_fist_tone3 = "left_facing_fist_tone3"
    left_fist_tone3 = "left_fist_tone3"
    left_facing_fist_tone4 = "left_facing_fist_tone4"
    left_fist_tone4 = "left_fist_tone4"
    left_facing_fist_tone5 = "left_facing_fist_tone5"
    left_fist_tone5 = "left_fist_tone5"
    right_facing_fist = "right_facing_fist"
    right_fist = "right_fist"
    right_facing_fist_tone1 = "right_facing_fist_tone1"
    right_fist_tone1 = "right_fist_tone1"
    right_facing_fist_tone2 = "right_facing_fist_tone2"
    right_fist_tone2 = "right_fist_tone2"
    right_facing_fist_tone3 = "right_facing_fist_tone3"
    right_fist_tone3 = "right_fist_tone3"
    right_facing_fist_tone4 = "right_facing_fist_tone4"
    right_fist_tone4 = "right_fist_tone4"
    right_facing_fist_tone5 = "right_facing_fist_tone5"
    right_fist_tone5 = "right_fist_tone5"
    fingers_crossed = "fingers_crossed"
    hand_with_index_and_middle_finger_crossed = "hand_with_index_and_middle_finger_crossed"
    fingers_crossed_tone1 = "fingers_crossed_tone1"
    hand_with_index_and_middle_fingers_crossed_tone1 = "hand_with_index_and_middle_fingers_crossed_tone1"
    fingers_crossed_tone2 = "fingers_crossed_tone2"
    hand_with_index_and_middle_fingers_crossed_tone2 = "hand_with_index_and_middle_fingers_crossed_tone2"
    fingers_crossed_tone3 = "fingers_crossed_tone3"
    hand_with_index_and_middle_fingers_crossed_tone3 = "hand_with_index_and_middle_fingers_crossed_tone3"
    fingers_crossed_tone4 = "fingers_crossed_tone4"
    hand_with_index_and_middle_fingers_crossed_tone4 = "hand_with_index_and_middle_fingers_crossed_tone4"
    fingers_crossed_tone5 = "fingers_crossed_tone5"
    hand_with_index_and_middle_fingers_crossed_tone5 = "hand_with_index_and_middle_fingers_crossed_tone5"
    v = "v"
    v_tone1 = "v_tone1"
    v_tone2 = "v_tone2"
    v_tone3 = "v_tone3"
    v_tone4 = "v_tone4"
    v_tone5 = "v_tone5"
    love_you_gesture = "love_you_gesture"
    love_you_gesture_tone1 = "love_you_gesture_tone1"
    love_you_gesture_light_skin_tone = "love_you_gesture_light_skin_tone"
    love_you_gesture_tone2 = "love_you_gesture_tone2"
    love_you_gesture_medium_light_skin_tone = "love_you_gesture_medium_light_skin_tone"
    love_you_gesture_tone3 = "love_you_gesture_tone3"
    love_you_gesture_medium_skin_tone = "love_you_gesture_medium_skin_tone"
    love_you_gesture_tone4 = "love_you_gesture_tone4"
    love_you_gesture_medium_dark_skin_tone = "love_you_gesture_medium_dark_skin_tone"
    love_you_gesture_tone5 = "love_you_gesture_tone5"
    love_you_gesture_dark_skin_tone = "love_you_gesture_dark_skin_tone"
    metal = "metal"
    sign_of_the_horns = "sign_of_the_horns"
    metal_tone1 = "metal_tone1"
    sign_of_the_horns_tone1 = "sign_of_the_horns_tone1"
    metal_tone2 = "metal_tone2"
    sign_of_the_horns_tone2 = "sign_of_the_horns_tone2"
    metal_tone3 = "metal_tone3"
    sign_of_the_horns_tone3 = "sign_of_the_horns_tone3"
    metal_tone4 = "metal_tone4"
    sign_of_the_horns_tone4 = "sign_of_the_horns_tone4"
    metal_tone5 = "metal_tone5"
    sign_of_the_horns_tone5 = "sign_of_the_horns_tone5"
    ok_hand = "ok_hand"
    ok_hand_tone1 = "ok_hand_tone1"
    ok_hand_tone2 = "ok_hand_tone2"
    ok_hand_tone3 = "ok_hand_tone3"
    ok_hand_tone4 = "ok_hand_tone4"
    ok_hand_tone5 = "ok_hand_tone5"
    pinching_hand = "pinching_hand"
    pinching_hand_tone1 = "pinching_hand_tone1"
    pinching_hand_light_skin_tone = "pinching_hand_light_skin_tone"
    pinching_hand_tone2 = "pinching_hand_tone2"
    pinching_hand_medium_light_skin_tone = "pinching_hand_medium_light_skin_tone"
    pinching_hand_tone3 = "pinching_hand_tone3"
    pinching_hand_medium_skin_tone = "pinching_hand_medium_skin_tone"
    pinching_hand_tone4 = "pinching_hand_tone4"
    pinching_hand_medium_dark_skin_tone = "pinching_hand_medium_dark_skin_tone"
    pinching_hand_tone5 = "pinching_hand_tone5"
    pinching_hand_dark_skin_tone = "pinching_hand_dark_skin_tone"
    point_left = "point_left"
    point_left_tone1 = "point_left_tone1"
    point_left_tone2 = "point_left_tone2"
    point_left_tone3 = "point_left_tone3"
    point_left_tone4 = "point_left_tone4"
    point_left_tone5 = "point_left_tone5"
    point_right = "point_right"
    point_right_tone1 = "point_right_tone1"
    point_right_tone2 = "point_right_tone2"
    point_right_tone3 = "point_right_tone3"
    point_right_tone4 = "point_right_tone4"
    point_right_tone5 = "point_right_tone5"
    point_up_2 = "point_up_2"
    point_up_2_tone1 = "point_up_2_tone1"
    point_up_2_tone2 = "point_up_2_tone2"
    point_up_2_tone3 = "point_up_2_tone3"
    point_up_2_tone4 = "point_up_2_tone4"
    point_up_2_tone5 = "point_up_2_tone5"
    point_down = "point_down"
    point_down_tone1 = "point_down_tone1"
    point_down_tone2 = "point_down_tone2"
    point_down_tone3 = "point_down_tone3"
    point_down_tone4 = "point_down_tone4"
    point_down_tone5 = "point_down_tone5"
    point_up = "point_up"
    point_up_tone1 = "point_up_tone1"
    point_up_tone2 = "point_up_tone2"
    point_up_tone3 = "point_up_tone3"
    point_up_tone4 = "point_up_tone4"
    point_up_tone5 = "point_up_tone5"
    raised_hand = "raised_hand"
    raised_hand_tone1 = "raised_hand_tone1"
    raised_hand_tone2 = "raised_hand_tone2"
    raised_hand_tone3 = "raised_hand_tone3"
    raised_hand_tone4 = "raised_hand_tone4"
    raised_hand_tone5 = "raised_hand_tone5"
    raised_back_of_hand = "raised_back_of_hand"
    back_of_hand = "back_of_hand"
    raised_back_of_hand_tone1 = "raised_back_of_hand_tone1"
    back_of_hand_tone1 = "back_of_hand_tone1"
    raised_back_of_hand_tone2 = "raised_back_of_hand_tone2"
    back_of_hand_tone2 = "back_of_hand_tone2"
    raised_back_of_hand_tone3 = "raised_back_of_hand_tone3"
    back_of_hand_tone3 = "back_of_hand_tone3"
    raised_back_of_hand_tone4 = "raised_back_of_hand_tone4"
    back_of_hand_tone4 = "back_of_hand_tone4"
    raised_back_of_hand_tone5 = "raised_back_of_hand_tone5"
    back_of_hand_tone5 = "back_of_hand_tone5"
    hand_splayed = "hand_splayed"
    raised_hand_with_fingers_splayed = "raised_hand_with_fingers_splayed"
    hand_splayed_tone1 = "hand_splayed_tone1"
    raised_hand_with_fingers_splayed_tone1 = "raised_hand_with_fingers_splayed_tone1"
    hand_splayed_tone2 = "hand_splayed_tone2"
    raised_hand_with_fingers_splayed_tone2 = "raised_hand_with_fingers_splayed_tone2"
    hand_splayed_tone3 = "hand_splayed_tone3"
    raised_hand_with_fingers_splayed_tone3 = "raised_hand_with_fingers_splayed_tone3"
    hand_splayed_tone4 = "hand_splayed_tone4"
    raised_hand_with_fingers_splayed_tone4 = "raised_hand_with_fingers_splayed_tone4"
    hand_splayed_tone5 = "hand_splayed_tone5"
    raised_hand_with_fingers_splayed_tone5 = "raised_hand_with_fingers_splayed_tone5"
    vulcan = "vulcan"
    raised_hand_with_part_between_middle_and_ring_fingers = "raised_hand_with_part_between_middle_and_ring_fingers"
    vulcan_tone1 = "vulcan_tone1"
    raised_hand_with_part_between_middle_and_ring_fingers_tone1 = "raised_hand_with_part_between_middle_and_ring_fingers_tone1"
    vulcan_tone2 = "vulcan_tone2"
    raised_hand_with_part_between_middle_and_ring_fingers_tone2 = "raised_hand_with_part_between_middle_and_ring_fingers_tone2"
    vulcan_tone3 = "vulcan_tone3"
    raised_hand_with_part_between_middle_and_ring_fingers_tone3 = "raised_hand_with_part_between_middle_and_ring_fingers_tone3"
    vulcan_tone4 = "vulcan_tone4"
    raised_hand_with_part_between_middle_and_ring_fingers_tone4 = "raised_hand_with_part_between_middle_and_ring_fingers_tone4"
    vulcan_tone5 = "vulcan_tone5"
    raised_hand_with_part_between_middle_and_ring_fingers_tone5 = "raised_hand_with_part_between_middle_and_ring_fingers_tone5"
    wave = "wave"
    wave_tone1 = "wave_tone1"
    wave_tone2 = "wave_tone2"
    wave_tone3 = "wave_tone3"
    wave_tone4 = "wave_tone4"
    wave_tone5 = "wave_tone5"
    call_me = "call_me"
    call_me_hand = "call_me_hand"
    call_me_tone1 = "call_me_tone1"
    call_me_hand_tone1 = "call_me_hand_tone1"
    call_me_tone2 = "call_me_tone2"
    call_me_hand_tone2 = "call_me_hand_tone2"
    call_me_tone3 = "call_me_tone3"
    call_me_hand_tone3 = "call_me_hand_tone3"
    call_me_tone4 = "call_me_tone4"
    call_me_hand_tone4 = "call_me_hand_tone4"
    call_me_tone5 = "call_me_tone5"
    call_me_hand_tone5 = "call_me_hand_tone5"
    muscle = "muscle"
    muscle_tone1 = "muscle_tone1"
    muscle_tone2 = "muscle_tone2"
    muscle_tone3 = "muscle_tone3"
    muscle_tone4 = "muscle_tone4"
    muscle_tone5 = "muscle_tone5"
    mechanical_arm = "mechanical_arm"
    middle_finger = "middle_finger"
    reversed_hand_with_middle_finger_extended = "reversed_hand_with_middle_finger_extended"
    middle_finger_tone1 = "middle_finger_tone1"
    reversed_hand_with_middle_finger_extended_tone1 = "reversed_hand_with_middle_finger_extended_tone1"
    middle_finger_tone2 = "middle_finger_tone2"
    reversed_hand_with_middle_finger_extended_tone2 = "reversed_hand_with_middle_finger_extended_tone2"
    middle_finger_tone3 = "middle_finger_tone3"
    reversed_hand_with_middle_finger_extended_tone3 = "reversed_hand_with_middle_finger_extended_tone3"
    middle_finger_tone4 = "middle_finger_tone4"
    reversed_hand_with_middle_finger_extended_tone4 = "reversed_hand_with_middle_finger_extended_tone4"
    middle_finger_tone5 = "middle_finger_tone5"
    reversed_hand_with_middle_finger_extended_tone5 = "reversed_hand_with_middle_finger_extended_tone5"
    writing_hand = "writing_hand"
    writing_hand_tone1 = "writing_hand_tone1"
    writing_hand_tone2 = "writing_hand_tone2"
    writing_hand_tone3 = "writing_hand_tone3"
    writing_hand_tone4 = "writing_hand_tone4"
    writing_hand_tone5 = "writing_hand_tone5"
    pray = "pray"
    pray_tone1 = "pray_tone1"
    pray_tone2 = "pray_tone2"
    pray_tone3 = "pray_tone3"
    pray_tone4 = "pray_tone4"
    pray_tone5 = "pray_tone5"
    foot = "foot"
    foot_tone1 = "foot_tone1"
    foot_light_skin_tone = "foot_light_skin_tone"
    foot_tone2 = "foot_tone2"
    foot_medium_light_skin_tone = "foot_medium_light_skin_tone"
    foot_tone3 = "foot_tone3"
    foot_medium_skin_tone = "foot_medium_skin_tone"
    foot_tone4 = "foot_tone4"
    foot_medium_dark_skin_tone = "foot_medium_dark_skin_tone"
    foot_tone5 = "foot_tone5"
    foot_dark_skin_tone = "foot_dark_skin_tone"
    leg = "leg"
    leg_tone1 = "leg_tone1"
    leg_light_skin_tone = "leg_light_skin_tone"
    leg_tone2 = "leg_tone2"
    leg_medium_light_skin_tone = "leg_medium_light_skin_tone"
    leg_tone3 = "leg_tone3"
    leg_medium_skin_tone = "leg_medium_skin_tone"
    leg_tone4 = "leg_tone4"
    leg_medium_dark_skin_tone = "leg_medium_dark_skin_tone"
    leg_tone5 = "leg_tone5"
    leg_dark_skin_tone = "leg_dark_skin_tone"
    mechanical_leg = "mechanical_leg"
    lipstick = "lipstick"
    kiss = "kiss"
    lips = "lips"
    tooth = "tooth"
    bone = "bone"
    tongue = "tongue"
    ear = "ear"
    ear_tone1 = "ear_tone1"
    ear_tone2 = "ear_tone2"
    ear_tone3 = "ear_tone3"
    ear_tone4 = "ear_tone4"
    ear_tone5 = "ear_tone5"
    ear_with_hearing_aid = "ear_with_hearing_aid"
    ear_with_hearing_aid_tone1 = "ear_with_hearing_aid_tone1"
    ear_with_hearing_aid_light_skin_tone = "ear_with_hearing_aid_light_skin_tone"
    ear_with_hearing_aid_tone2 = "ear_with_hearing_aid_tone2"
    ear_with_hearing_aid_medium_light_skin_tone = "ear_with_hearing_aid_medium_light_skin_tone"
    ear_with_hearing_aid_tone3 = "ear_with_hearing_aid_tone3"
    ear_with_hearing_aid_medium_skin_tone = "ear_with_hearing_aid_medium_skin_tone"
    ear_with_hearing_aid_tone4 = "ear_with_hearing_aid_tone4"
    ear_with_hearing_aid_medium_dark_skin_tone = "ear_with_hearing_aid_medium_dark_skin_tone"
    ear_with_hearing_aid_tone5 = "ear_with_hearing_aid_tone5"
    ear_with_hearing_aid_dark_skin_tone = "ear_with_hearing_aid_dark_skin_tone"
    nose = "nose"
    nose_tone1 = "nose_tone1"
    nose_tone2 = "nose_tone2"
    nose_tone3 = "nose_tone3"
    nose_tone4 = "nose_tone4"
    nose_tone5 = "nose_tone5"
    footprints = "footprints"
    eye = "eye"
    eyes = "eyes"
    brain = "brain"
    speaking_head = "speaking_head"
    speaking_head_in_silhouette = "speaking_head_in_silhouette"
    bust_in_silhouette = "bust_in_silhouette"
    busts_in_silhouette = "busts_in_silhouette"
    baby = "baby"
    baby_tone1 = "baby_tone1"
    baby_tone2 = "baby_tone2"
    baby_tone3 = "baby_tone3"
    baby_tone4 = "baby_tone4"
    baby_tone5 = "baby_tone5"
    girl = "girl"
    girl_tone1 = "girl_tone1"
    girl_tone2 = "girl_tone2"
    girl_tone3 = "girl_tone3"
    girl_tone4 = "girl_tone4"
    girl_tone5 = "girl_tone5"
    child = "child"
    child_tone1 = "child_tone1"
    child_light_skin_tone = "child_light_skin_tone"
    child_tone2 = "child_tone2"
    child_medium_light_skin_tone = "child_medium_light_skin_tone"
    child_tone3 = "child_tone3"
    child_medium_skin_tone = "child_medium_skin_tone"
    child_tone4 = "child_tone4"
    child_medium_dark_skin_tone = "child_medium_dark_skin_tone"
    child_tone5 = "child_tone5"
    child_dark_skin_tone = "child_dark_skin_tone"
    boy = "boy"
    boy_tone1 = "boy_tone1"
    boy_tone2 = "boy_tone2"
    boy_tone3 = "boy_tone3"
    boy_tone4 = "boy_tone4"
    boy_tone5 = "boy_tone5"
    woman = "woman"
    woman_tone1 = "woman_tone1"
    woman_tone2 = "woman_tone2"
    woman_tone3 = "woman_tone3"
    woman_tone4 = "woman_tone4"
    woman_tone5 = "woman_tone5"
    adult = "adult"
    adult_tone1 = "adult_tone1"
    adult_light_skin_tone = "adult_light_skin_tone"
    adult_tone2 = "adult_tone2"
    adult_medium_light_skin_tone = "adult_medium_light_skin_tone"
    adult_tone3 = "adult_tone3"
    adult_medium_skin_tone = "adult_medium_skin_tone"
    adult_tone4 = "adult_tone4"
    adult_medium_dark_skin_tone = "adult_medium_dark_skin_tone"
    adult_tone5 = "adult_tone5"
    adult_dark_skin_tone = "adult_dark_skin_tone"
    man = "man"
    man_tone1 = "man_tone1"
    man_tone2 = "man_tone2"
    man_tone3 = "man_tone3"
    man_tone4 = "man_tone4"
    man_tone5 = "man_tone5"
    woman_curly_haired = "woman_curly_haired"
    woman_curly_haired_tone1 = "woman_curly_haired_tone1"
    woman_curly_haired_light_skin_tone = "woman_curly_haired_light_skin_tone"
    woman_curly_haired_tone2 = "woman_curly_haired_tone2"
    woman_curly_haired_medium_light_skin_tone = "woman_curly_haired_medium_light_skin_tone"
    woman_curly_haired_tone3 = "woman_curly_haired_tone3"
    woman_curly_haired_medium_skin_tone = "woman_curly_haired_medium_skin_tone"
    woman_curly_haired_tone4 = "woman_curly_haired_tone4"
    woman_curly_haired_medium_dark_skin_tone = "woman_curly_haired_medium_dark_skin_tone"
    woman_curly_haired_tone5 = "woman_curly_haired_tone5"
    woman_curly_haired_dark_skin_tone = "woman_curly_haired_dark_skin_tone"
    man_curly_haired = "man_curly_haired"
    man_curly_haired_tone1 = "man_curly_haired_tone1"
    man_curly_haired_light_skin_tone = "man_curly_haired_light_skin_tone"
    man_curly_haired_tone2 = "man_curly_haired_tone2"
    man_curly_haired_medium_light_skin_tone = "man_curly_haired_medium_light_skin_tone"
    man_curly_haired_tone3 = "man_curly_haired_tone3"
    man_curly_haired_medium_skin_tone = "man_curly_haired_medium_skin_tone"
    man_curly_haired_tone4 = "man_curly_haired_tone4"
    man_curly_haired_medium_dark_skin_tone = "man_curly_haired_medium_dark_skin_tone"
    man_curly_haired_tone5 = "man_curly_haired_tone5"
    man_curly_haired_dark_skin_tone = "man_curly_haired_dark_skin_tone"
    woman_red_haired = "woman_red_haired"
    woman_red_haired_tone1 = "woman_red_haired_tone1"
    woman_red_haired_light_skin_tone = "woman_red_haired_light_skin_tone"
    woman_red_haired_tone2 = "woman_red_haired_tone2"
    woman_red_haired_medium_light_skin_tone = "woman_red_haired_medium_light_skin_tone"
    woman_red_haired_tone3 = "woman_red_haired_tone3"
    woman_red_haired_medium_skin_tone = "woman_red_haired_medium_skin_tone"
    woman_red_haired_tone4 = "woman_red_haired_tone4"
    woman_red_haired_medium_dark_skin_tone = "woman_red_haired_medium_dark_skin_tone"
    woman_red_haired_tone5 = "woman_red_haired_tone5"
    woman_red_haired_dark_skin_tone = "woman_red_haired_dark_skin_tone"
    man_red_haired = "man_red_haired"
    man_red_haired_tone1 = "man_red_haired_tone1"
    man_red_haired_light_skin_tone = "man_red_haired_light_skin_tone"
    man_red_haired_tone2 = "man_red_haired_tone2"
    man_red_haired_medium_light_skin_tone = "man_red_haired_medium_light_skin_tone"
    man_red_haired_tone3 = "man_red_haired_tone3"
    man_red_haired_medium_skin_tone = "man_red_haired_medium_skin_tone"
    man_red_haired_tone4 = "man_red_haired_tone4"
    man_red_haired_medium_dark_skin_tone = "man_red_haired_medium_dark_skin_tone"
    man_red_haired_tone5 = "man_red_haired_tone5"
    man_red_haired_dark_skin_tone = "man_red_haired_dark_skin_tone"
    blond_haired_woman = "blond_haired_woman"
    blond_haired_woman_tone1 = "blond_haired_woman_tone1"
    blond_haired_woman_light_skin_tone = "blond_haired_woman_light_skin_tone"
    blond_haired_woman_tone2 = "blond_haired_woman_tone2"
    blond_haired_woman_medium_light_skin_tone = "blond_haired_woman_medium_light_skin_tone"
    blond_haired_woman_tone3 = "blond_haired_woman_tone3"
    blond_haired_woman_medium_skin_tone = "blond_haired_woman_medium_skin_tone"
    blond_haired_woman_tone4 = "blond_haired_woman_tone4"
    blond_haired_woman_medium_dark_skin_tone = "blond_haired_woman_medium_dark_skin_tone"
    blond_haired_woman_tone5 = "blond_haired_woman_tone5"
    blond_haired_woman_dark_skin_tone = "blond_haired_woman_dark_skin_tone"
    blond_haired_person = "blond_haired_person"
    person_with_blond_hair = "person_with_blond_hair"
    blond_haired_person_tone1 = "blond_haired_person_tone1"
    person_with_blond_hair_tone1 = "person_with_blond_hair_tone1"
    blond_haired_person_tone2 = "blond_haired_person_tone2"
    person_with_blond_hair_tone2 = "person_with_blond_hair_tone2"
    blond_haired_person_tone3 = "blond_haired_person_tone3"
    person_with_blond_hair_tone3 = "person_with_blond_hair_tone3"
    blond_haired_person_tone4 = "blond_haired_person_tone4"
    person_with_blond_hair_tone4 = "person_with_blond_hair_tone4"
    blond_haired_person_tone5 = "blond_haired_person_tone5"
    person_with_blond_hair_tone5 = "person_with_blond_hair_tone5"
    blond_haired_man = "blond_haired_man"
    blond_haired_man_tone1 = "blond_haired_man_tone1"
    blond_haired_man_light_skin_tone = "blond_haired_man_light_skin_tone"
    blond_haired_man_tone2 = "blond_haired_man_tone2"
    blond_haired_man_medium_light_skin_tone = "blond_haired_man_medium_light_skin_tone"
    blond_haired_man_tone3 = "blond_haired_man_tone3"
    blond_haired_man_medium_skin_tone = "blond_haired_man_medium_skin_tone"
    blond_haired_man_tone4 = "blond_haired_man_tone4"
    blond_haired_man_medium_dark_skin_tone = "blond_haired_man_medium_dark_skin_tone"
    blond_haired_man_tone5 = "blond_haired_man_tone5"
    blond_haired_man_dark_skin_tone = "blond_haired_man_dark_skin_tone"
    woman_white_haired = "woman_white_haired"
    woman_white_haired_tone1 = "woman_white_haired_tone1"
    woman_white_haired_light_skin_tone = "woman_white_haired_light_skin_tone"
    woman_white_haired_tone2 = "woman_white_haired_tone2"
    woman_white_haired_medium_light_skin_tone = "woman_white_haired_medium_light_skin_tone"
    woman_white_haired_tone3 = "woman_white_haired_tone3"
    woman_white_haired_medium_skin_tone = "woman_white_haired_medium_skin_tone"
    woman_white_haired_tone4 = "woman_white_haired_tone4"
    woman_white_haired_medium_dark_skin_tone = "woman_white_haired_medium_dark_skin_tone"
    woman_white_haired_tone5 = "woman_white_haired_tone5"
    woman_white_haired_dark_skin_tone = "woman_white_haired_dark_skin_tone"
    man_white_haired = "man_white_haired"
    man_white_haired_tone1 = "man_white_haired_tone1"
    man_white_haired_light_skin_tone = "man_white_haired_light_skin_tone"
    man_white_haired_tone2 = "man_white_haired_tone2"
    man_white_haired_medium_light_skin_tone = "man_white_haired_medium_light_skin_tone"
    man_white_haired_tone3 = "man_white_haired_tone3"
    man_white_haired_medium_skin_tone = "man_white_haired_medium_skin_tone"
    man_white_haired_tone4 = "man_white_haired_tone4"
    man_white_haired_medium_dark_skin_tone = "man_white_haired_medium_dark_skin_tone"
    man_white_haired_tone5 = "man_white_haired_tone5"
    man_white_haired_dark_skin_tone = "man_white_haired_dark_skin_tone"
    woman_bald = "woman_bald"
    woman_bald_tone1 = "woman_bald_tone1"
    woman_bald_light_skin_tone = "woman_bald_light_skin_tone"
    woman_bald_tone2 = "woman_bald_tone2"
    woman_bald_medium_light_skin_tone = "woman_bald_medium_light_skin_tone"
    woman_bald_tone3 = "woman_bald_tone3"
    woman_bald_medium_skin_tone = "woman_bald_medium_skin_tone"
    woman_bald_tone4 = "woman_bald_tone4"
    woman_bald_medium_dark_skin_tone = "woman_bald_medium_dark_skin_tone"
    woman_bald_tone5 = "woman_bald_tone5"
    woman_bald_dark_skin_tone = "woman_bald_dark_skin_tone"
    man_bald = "man_bald"
    man_bald_tone1 = "man_bald_tone1"
    man_bald_light_skin_tone = "man_bald_light_skin_tone"
    man_bald_tone2 = "man_bald_tone2"
    man_bald_medium_light_skin_tone = "man_bald_medium_light_skin_tone"
    man_bald_tone3 = "man_bald_tone3"
    man_bald_medium_skin_tone = "man_bald_medium_skin_tone"
    man_bald_tone4 = "man_bald_tone4"
    man_bald_medium_dark_skin_tone = "man_bald_medium_dark_skin_tone"
    man_bald_tone5 = "man_bald_tone5"
    man_bald_dark_skin_tone = "man_bald_dark_skin_tone"
    bearded_person = "bearded_person"
    bearded_person_tone1 = "bearded_person_tone1"
    bearded_person_light_skin_tone = "bearded_person_light_skin_tone"
    bearded_person_tone2 = "bearded_person_tone2"
    bearded_person_medium_light_skin_tone = "bearded_person_medium_light_skin_tone"
    bearded_person_tone3 = "bearded_person_tone3"
    bearded_person_medium_skin_tone = "bearded_person_medium_skin_tone"
    bearded_person_tone4 = "bearded_person_tone4"
    bearded_person_medium_dark_skin_tone = "bearded_person_medium_dark_skin_tone"
    bearded_person_tone5 = "bearded_person_tone5"
    bearded_person_dark_skin_tone = "bearded_person_dark_skin_tone"
    older_woman = "older_woman"
    grandma = "grandma"
    older_woman_tone1 = "older_woman_tone1"
    grandma_tone1 = "grandma_tone1"
    older_woman_tone2 = "older_woman_tone2"
    grandma_tone2 = "grandma_tone2"
    older_woman_tone3 = "older_woman_tone3"
    grandma_tone3 = "grandma_tone3"
    older_woman_tone4 = "older_woman_tone4"
    grandma_tone4 = "grandma_tone4"
    older_woman_tone5 = "older_woman_tone5"
    grandma_tone5 = "grandma_tone5"
    older_adult = "older_adult"
    older_adult_tone1 = "older_adult_tone1"
    older_adult_light_skin_tone = "older_adult_light_skin_tone"
    older_adult_tone2 = "older_adult_tone2"
    older_adult_medium_light_skin_tone = "older_adult_medium_light_skin_tone"
    older_adult_tone3 = "older_adult_tone3"
    older_adult_medium_skin_tone = "older_adult_medium_skin_tone"
    older_adult_tone4 = "older_adult_tone4"
    older_adult_medium_dark_skin_tone = "older_adult_medium_dark_skin_tone"
    older_adult_tone5 = "older_adult_tone5"
    older_adult_dark_skin_tone = "older_adult_dark_skin_tone"
    older_man = "older_man"
    older_man_tone1 = "older_man_tone1"
    older_man_tone2 = "older_man_tone2"
    older_man_tone3 = "older_man_tone3"
    older_man_tone4 = "older_man_tone4"
    older_man_tone5 = "older_man_tone5"
    man_with_chinese_cap = "man_with_chinese_cap"
    man_with_gua_pi_mao = "man_with_gua_pi_mao"
    man_with_chinese_cap_tone1 = "man_with_chinese_cap_tone1"
    man_with_gua_pi_mao_tone1 = "man_with_gua_pi_mao_tone1"
    man_with_chinese_cap_tone2 = "man_with_chinese_cap_tone2"
    man_with_gua_pi_mao_tone2 = "man_with_gua_pi_mao_tone2"
    man_with_chinese_cap_tone3 = "man_with_chinese_cap_tone3"
    man_with_gua_pi_mao_tone3 = "man_with_gua_pi_mao_tone3"
    man_with_chinese_cap_tone4 = "man_with_chinese_cap_tone4"
    man_with_gua_pi_mao_tone4 = "man_with_gua_pi_mao_tone4"
    man_with_chinese_cap_tone5 = "man_with_chinese_cap_tone5"
    man_with_gua_pi_mao_tone5 = "man_with_gua_pi_mao_tone5"
    person_wearing_turban = "person_wearing_turban"
    man_with_turban = "man_with_turban"
    person_wearing_turban_tone1 = "person_wearing_turban_tone1"
    man_with_turban_tone1 = "man_with_turban_tone1"
    person_wearing_turban_tone2 = "person_wearing_turban_tone2"
    man_with_turban_tone2 = "man_with_turban_tone2"
    person_wearing_turban_tone3 = "person_wearing_turban_tone3"
    man_with_turban_tone3 = "man_with_turban_tone3"
    person_wearing_turban_tone4 = "person_wearing_turban_tone4"
    man_with_turban_tone4 = "man_with_turban_tone4"
    person_wearing_turban_tone5 = "person_wearing_turban_tone5"
    man_with_turban_tone5 = "man_with_turban_tone5"
    woman_wearing_turban = "woman_wearing_turban"
    woman_wearing_turban_tone1 = "woman_wearing_turban_tone1"
    woman_wearing_turban_light_skin_tone = "woman_wearing_turban_light_skin_tone"
    woman_wearing_turban_tone2 = "woman_wearing_turban_tone2"
    woman_wearing_turban_medium_light_skin_tone = "woman_wearing_turban_medium_light_skin_tone"
    woman_wearing_turban_tone3 = "woman_wearing_turban_tone3"
    woman_wearing_turban_medium_skin_tone = "woman_wearing_turban_medium_skin_tone"
    woman_wearing_turban_tone4 = "woman_wearing_turban_tone4"
    woman_wearing_turban_medium_dark_skin_tone = "woman_wearing_turban_medium_dark_skin_tone"
    woman_wearing_turban_tone5 = "woman_wearing_turban_tone5"
    woman_wearing_turban_dark_skin_tone = "woman_wearing_turban_dark_skin_tone"
    man_wearing_turban = "man_wearing_turban"
    man_wearing_turban_tone1 = "man_wearing_turban_tone1"
    man_wearing_turban_light_skin_tone = "man_wearing_turban_light_skin_tone"
    man_wearing_turban_tone2 = "man_wearing_turban_tone2"
    man_wearing_turban_medium_light_skin_tone = "man_wearing_turban_medium_light_skin_tone"
    man_wearing_turban_tone3 = "man_wearing_turban_tone3"
    man_wearing_turban_medium_skin_tone = "man_wearing_turban_medium_skin_tone"
    man_wearing_turban_tone4 = "man_wearing_turban_tone4"
    man_wearing_turban_medium_dark_skin_tone = "man_wearing_turban_medium_dark_skin_tone"
    man_wearing_turban_tone5 = "man_wearing_turban_tone5"
    man_wearing_turban_dark_skin_tone = "man_wearing_turban_dark_skin_tone"
    woman_with_headscarf = "woman_with_headscarf"
    woman_with_headscarf_tone1 = "woman_with_headscarf_tone1"
    woman_with_headscarf_light_skin_tone = "woman_with_headscarf_light_skin_tone"
    woman_with_headscarf_tone2 = "woman_with_headscarf_tone2"
    woman_with_headscarf_medium_light_skin_tone = "woman_with_headscarf_medium_light_skin_tone"
    woman_with_headscarf_tone3 = "woman_with_headscarf_tone3"
    woman_with_headscarf_medium_skin_tone = "woman_with_headscarf_medium_skin_tone"
    woman_with_headscarf_tone4 = "woman_with_headscarf_tone4"
    woman_with_headscarf_medium_dark_skin_tone = "woman_with_headscarf_medium_dark_skin_tone"
    woman_with_headscarf_tone5 = "woman_with_headscarf_tone5"
    woman_with_headscarf_dark_skin_tone = "woman_with_headscarf_dark_skin_tone"
    police_officer = "police_officer"
    cop = "cop"
    police_officer_tone1 = "police_officer_tone1"
    cop_tone1 = "cop_tone1"
    police_officer_tone2 = "police_officer_tone2"
    cop_tone2 = "cop_tone2"
    police_officer_tone3 = "police_officer_tone3"
    cop_tone3 = "cop_tone3"
    police_officer_tone4 = "police_officer_tone4"
    cop_tone4 = "cop_tone4"
    police_officer_tone5 = "police_officer_tone5"
    cop_tone5 = "cop_tone5"
    woman_police_officer = "woman_police_officer"
    woman_police_officer_tone1 = "woman_police_officer_tone1"
    woman_police_officer_light_skin_tone = "woman_police_officer_light_skin_tone"
    woman_police_officer_tone2 = "woman_police_officer_tone2"
    woman_police_officer_medium_light_skin_tone = "woman_police_officer_medium_light_skin_tone"
    woman_police_officer_tone3 = "woman_police_officer_tone3"
    woman_police_officer_medium_skin_tone = "woman_police_officer_medium_skin_tone"
    woman_police_officer_tone4 = "woman_police_officer_tone4"
    woman_police_officer_medium_dark_skin_tone = "woman_police_officer_medium_dark_skin_tone"
    woman_police_officer_tone5 = "woman_police_officer_tone5"
    woman_police_officer_dark_skin_tone = "woman_police_officer_dark_skin_tone"
    man_police_officer = "man_police_officer"
    man_police_officer_tone1 = "man_police_officer_tone1"
    man_police_officer_light_skin_tone = "man_police_officer_light_skin_tone"
    man_police_officer_tone2 = "man_police_officer_tone2"
    man_police_officer_medium_light_skin_tone = "man_police_officer_medium_light_skin_tone"
    man_police_officer_tone3 = "man_police_officer_tone3"
    man_police_officer_medium_skin_tone = "man_police_officer_medium_skin_tone"
    man_police_officer_tone4 = "man_police_officer_tone4"
    man_police_officer_medium_dark_skin_tone = "man_police_officer_medium_dark_skin_tone"
    man_police_officer_tone5 = "man_police_officer_tone5"
    man_police_officer_dark_skin_tone = "man_police_officer_dark_skin_tone"
    construction_worker = "construction_worker"
    construction_worker_tone1 = "construction_worker_tone1"
    construction_worker_tone2 = "construction_worker_tone2"
    construction_worker_tone3 = "construction_worker_tone3"
    construction_worker_tone4 = "construction_worker_tone4"
    construction_worker_tone5 = "construction_worker_tone5"
    woman_construction_worker = "woman_construction_worker"
    woman_construction_worker_tone1 = "woman_construction_worker_tone1"
    woman_construction_worker_light_skin_tone = "woman_construction_worker_light_skin_tone"
    woman_construction_worker_tone2 = "woman_construction_worker_tone2"
    woman_construction_worker_medium_light_skin_tone = "woman_construction_worker_medium_light_skin_tone"
    woman_construction_worker_tone3 = "woman_construction_worker_tone3"
    woman_construction_worker_medium_skin_tone = "woman_construction_worker_medium_skin_tone"
    woman_construction_worker_tone4 = "woman_construction_worker_tone4"
    woman_construction_worker_medium_dark_skin_tone = "woman_construction_worker_medium_dark_skin_tone"
    woman_construction_worker_tone5 = "woman_construction_worker_tone5"
    woman_construction_worker_dark_skin_tone = "woman_construction_worker_dark_skin_tone"
    man_construction_worker = "man_construction_worker"
    man_construction_worker_tone1 = "man_construction_worker_tone1"
    man_construction_worker_light_skin_tone = "man_construction_worker_light_skin_tone"
    man_construction_worker_tone2 = "man_construction_worker_tone2"
    man_construction_worker_medium_light_skin_tone = "man_construction_worker_medium_light_skin_tone"
    man_construction_worker_tone3 = "man_construction_worker_tone3"
    man_construction_worker_medium_skin_tone = "man_construction_worker_medium_skin_tone"
    man_construction_worker_tone4 = "man_construction_worker_tone4"
    man_construction_worker_medium_dark_skin_tone = "man_construction_worker_medium_dark_skin_tone"
    man_construction_worker_tone5 = "man_construction_worker_tone5"
    man_construction_worker_dark_skin_tone = "man_construction_worker_dark_skin_tone"
    guard = "guard"
    guardsman = "guardsman"
    guard_tone1 = "guard_tone1"
    guardsman_tone1 = "guardsman_tone1"
    guard_tone2 = "guard_tone2"
    guardsman_tone2 = "guardsman_tone2"
    guard_tone3 = "guard_tone3"
    guardsman_tone3 = "guardsman_tone3"
    guard_tone4 = "guard_tone4"
    guardsman_tone4 = "guardsman_tone4"
    guard_tone5 = "guard_tone5"
    guardsman_tone5 = "guardsman_tone5"
    woman_guard = "woman_guard"
    woman_guard_tone1 = "woman_guard_tone1"
    woman_guard_light_skin_tone = "woman_guard_light_skin_tone"
    woman_guard_tone2 = "woman_guard_tone2"
    woman_guard_medium_light_skin_tone = "woman_guard_medium_light_skin_tone"
    woman_guard_tone3 = "woman_guard_tone3"
    woman_guard_medium_skin_tone = "woman_guard_medium_skin_tone"
    woman_guard_tone4 = "woman_guard_tone4"
    woman_guard_medium_dark_skin_tone = "woman_guard_medium_dark_skin_tone"
    woman_guard_tone5 = "woman_guard_tone5"
    woman_guard_dark_skin_tone = "woman_guard_dark_skin_tone"
    man_guard = "man_guard"
    man_guard_tone1 = "man_guard_tone1"
    man_guard_light_skin_tone = "man_guard_light_skin_tone"
    man_guard_tone2 = "man_guard_tone2"
    man_guard_medium_light_skin_tone = "man_guard_medium_light_skin_tone"
    man_guard_tone3 = "man_guard_tone3"
    man_guard_medium_skin_tone = "man_guard_medium_skin_tone"
    man_guard_tone4 = "man_guard_tone4"
    man_guard_medium_dark_skin_tone = "man_guard_medium_dark_skin_tone"
    man_guard_tone5 = "man_guard_tone5"
    man_guard_dark_skin_tone = "man_guard_dark_skin_tone"
    detective = "detective"
    spy = "spy"
    sleuth_or_spy = "sleuth_or_spy"
    detective_tone1 = "detective_tone1"
    spy_tone1 = "spy_tone1"
    sleuth_or_spy_tone1 = "sleuth_or_spy_tone1"
    detective_tone2 = "detective_tone2"
    spy_tone2 = "spy_tone2"
    sleuth_or_spy_tone2 = "sleuth_or_spy_tone2"
    detective_tone3 = "detective_tone3"
    spy_tone3 = "spy_tone3"
    sleuth_or_spy_tone3 = "sleuth_or_spy_tone3"
    detective_tone4 = "detective_tone4"
    spy_tone4 = "spy_tone4"
    sleuth_or_spy_tone4 = "sleuth_or_spy_tone4"
    detective_tone5 = "detective_tone5"
    spy_tone5 = "spy_tone5"
    sleuth_or_spy_tone5 = "sleuth_or_spy_tone5"
    woman_detective = "woman_detective"
    woman_detective_tone1 = "woman_detective_tone1"
    woman_detective_light_skin_tone = "woman_detective_light_skin_tone"
    woman_detective_tone2 = "woman_detective_tone2"
    woman_detective_medium_light_skin_tone = "woman_detective_medium_light_skin_tone"
    woman_detective_tone3 = "woman_detective_tone3"
    woman_detective_medium_skin_tone = "woman_detective_medium_skin_tone"
    woman_detective_tone4 = "woman_detective_tone4"
    woman_detective_medium_dark_skin_tone = "woman_detective_medium_dark_skin_tone"
    woman_detective_tone5 = "woman_detective_tone5"
    woman_detective_dark_skin_tone = "woman_detective_dark_skin_tone"
    man_detective = "man_detective"
    man_detective_tone1 = "man_detective_tone1"
    man_detective_light_skin_tone = "man_detective_light_skin_tone"
    man_detective_tone2 = "man_detective_tone2"
    man_detective_medium_light_skin_tone = "man_detective_medium_light_skin_tone"
    man_detective_tone3 = "man_detective_tone3"
    man_detective_medium_skin_tone = "man_detective_medium_skin_tone"
    man_detective_tone4 = "man_detective_tone4"
    man_detective_medium_dark_skin_tone = "man_detective_medium_dark_skin_tone"
    man_detective_tone5 = "man_detective_tone5"
    man_detective_dark_skin_tone = "man_detective_dark_skin_tone"
    woman_health_worker = "woman_health_worker"
    woman_health_worker_tone1 = "woman_health_worker_tone1"
    woman_health_worker_light_skin_tone = "woman_health_worker_light_skin_tone"
    woman_health_worker_tone2 = "woman_health_worker_tone2"
    woman_health_worker_medium_light_skin_tone = "woman_health_worker_medium_light_skin_tone"
    woman_health_worker_tone3 = "woman_health_worker_tone3"
    woman_health_worker_medium_skin_tone = "woman_health_worker_medium_skin_tone"
    woman_health_worker_tone4 = "woman_health_worker_tone4"
    woman_health_worker_medium_dark_skin_tone = "woman_health_worker_medium_dark_skin_tone"
    woman_health_worker_tone5 = "woman_health_worker_tone5"
    woman_health_worker_dark_skin_tone = "woman_health_worker_dark_skin_tone"
    man_health_worker = "man_health_worker"
    man_health_worker_tone1 = "man_health_worker_tone1"
    man_health_worker_light_skin_tone = "man_health_worker_light_skin_tone"
    man_health_worker_tone2 = "man_health_worker_tone2"
    man_health_worker_medium_light_skin_tone = "man_health_worker_medium_light_skin_tone"
    man_health_worker_tone3 = "man_health_worker_tone3"
    man_health_worker_medium_skin_tone = "man_health_worker_medium_skin_tone"
    man_health_worker_tone4 = "man_health_worker_tone4"
    man_health_worker_medium_dark_skin_tone = "man_health_worker_medium_dark_skin_tone"
    man_health_worker_tone5 = "man_health_worker_tone5"
    man_health_worker_dark_skin_tone = "man_health_worker_dark_skin_tone"
    woman_farmer = "woman_farmer"
    woman_farmer_tone1 = "woman_farmer_tone1"
    woman_farmer_light_skin_tone = "woman_farmer_light_skin_tone"
    woman_farmer_tone2 = "woman_farmer_tone2"
    woman_farmer_medium_light_skin_tone = "woman_farmer_medium_light_skin_tone"
    woman_farmer_tone3 = "woman_farmer_tone3"
    woman_farmer_medium_skin_tone = "woman_farmer_medium_skin_tone"
    woman_farmer_tone4 = "woman_farmer_tone4"
    woman_farmer_medium_dark_skin_tone = "woman_farmer_medium_dark_skin_tone"
    woman_farmer_tone5 = "woman_farmer_tone5"
    woman_farmer_dark_skin_tone = "woman_farmer_dark_skin_tone"
    man_farmer = "man_farmer"
    man_farmer_tone1 = "man_farmer_tone1"
    man_farmer_light_skin_tone = "man_farmer_light_skin_tone"
    man_farmer_tone2 = "man_farmer_tone2"
    man_farmer_medium_light_skin_tone = "man_farmer_medium_light_skin_tone"
    man_farmer_tone3 = "man_farmer_tone3"
    man_farmer_medium_skin_tone = "man_farmer_medium_skin_tone"
    man_farmer_tone4 = "man_farmer_tone4"
    man_farmer_medium_dark_skin_tone = "man_farmer_medium_dark_skin_tone"
    man_farmer_tone5 = "man_farmer_tone5"
    man_farmer_dark_skin_tone = "man_farmer_dark_skin_tone"
    woman_cook = "woman_cook"
    woman_cook_tone1 = "woman_cook_tone1"
    woman_cook_light_skin_tone = "woman_cook_light_skin_tone"
    woman_cook_tone2 = "woman_cook_tone2"
    woman_cook_medium_light_skin_tone = "woman_cook_medium_light_skin_tone"
    woman_cook_tone3 = "woman_cook_tone3"
    woman_cook_medium_skin_tone = "woman_cook_medium_skin_tone"
    woman_cook_tone4 = "woman_cook_tone4"
    woman_cook_medium_dark_skin_tone = "woman_cook_medium_dark_skin_tone"
    woman_cook_tone5 = "woman_cook_tone5"
    woman_cook_dark_skin_tone = "woman_cook_dark_skin_tone"
    man_cook = "man_cook"
    man_cook_tone1 = "man_cook_tone1"
    man_cook_light_skin_tone = "man_cook_light_skin_tone"
    man_cook_tone2 = "man_cook_tone2"
    man_cook_medium_light_skin_tone = "man_cook_medium_light_skin_tone"
    man_cook_tone3 = "man_cook_tone3"
    man_cook_medium_skin_tone = "man_cook_medium_skin_tone"
    man_cook_tone4 = "man_cook_tone4"
    man_cook_medium_dark_skin_tone = "man_cook_medium_dark_skin_tone"
    man_cook_tone5 = "man_cook_tone5"
    man_cook_dark_skin_tone = "man_cook_dark_skin_tone"
    woman_student = "woman_student"
    woman_student_tone1 = "woman_student_tone1"
    woman_student_light_skin_tone = "woman_student_light_skin_tone"
    woman_student_tone2 = "woman_student_tone2"
    woman_student_medium_light_skin_tone = "woman_student_medium_light_skin_tone"
    woman_student_tone3 = "woman_student_tone3"
    woman_student_medium_skin_tone = "woman_student_medium_skin_tone"
    woman_student_tone4 = "woman_student_tone4"
    woman_student_medium_dark_skin_tone = "woman_student_medium_dark_skin_tone"
    woman_student_tone5 = "woman_student_tone5"
    woman_student_dark_skin_tone = "woman_student_dark_skin_tone"
    man_student = "man_student"
    man_student_tone1 = "man_student_tone1"
    man_student_light_skin_tone = "man_student_light_skin_tone"
    man_student_tone2 = "man_student_tone2"
    man_student_medium_light_skin_tone = "man_student_medium_light_skin_tone"
    man_student_tone3 = "man_student_tone3"
    man_student_medium_skin_tone = "man_student_medium_skin_tone"
    man_student_tone4 = "man_student_tone4"
    man_student_medium_dark_skin_tone = "man_student_medium_dark_skin_tone"
    man_student_tone5 = "man_student_tone5"
    man_student_dark_skin_tone = "man_student_dark_skin_tone"
    woman_singer = "woman_singer"
    woman_singer_tone1 = "woman_singer_tone1"
    woman_singer_light_skin_tone = "woman_singer_light_skin_tone"
    woman_singer_tone2 = "woman_singer_tone2"
    woman_singer_medium_light_skin_tone = "woman_singer_medium_light_skin_tone"
    woman_singer_tone3 = "woman_singer_tone3"
    woman_singer_medium_skin_tone = "woman_singer_medium_skin_tone"
    woman_singer_tone4 = "woman_singer_tone4"
    woman_singer_medium_dark_skin_tone = "woman_singer_medium_dark_skin_tone"
    woman_singer_tone5 = "woman_singer_tone5"
    woman_singer_dark_skin_tone = "woman_singer_dark_skin_tone"
    man_singer = "man_singer"
    man_singer_tone1 = "man_singer_tone1"
    man_singer_light_skin_tone = "man_singer_light_skin_tone"
    man_singer_tone2 = "man_singer_tone2"
    man_singer_medium_light_skin_tone = "man_singer_medium_light_skin_tone"
    man_singer_tone3 = "man_singer_tone3"
    man_singer_medium_skin_tone = "man_singer_medium_skin_tone"
    man_singer_tone4 = "man_singer_tone4"
    man_singer_medium_dark_skin_tone = "man_singer_medium_dark_skin_tone"
    man_singer_tone5 = "man_singer_tone5"
    man_singer_dark_skin_tone = "man_singer_dark_skin_tone"
    woman_teacher = "woman_teacher"
    woman_teacher_tone1 = "woman_teacher_tone1"
    woman_teacher_light_skin_tone = "woman_teacher_light_skin_tone"
    woman_teacher_tone2 = "woman_teacher_tone2"
    woman_teacher_medium_light_skin_tone = "woman_teacher_medium_light_skin_tone"
    woman_teacher_tone3 = "woman_teacher_tone3"
    woman_teacher_medium_skin_tone = "woman_teacher_medium_skin_tone"
    woman_teacher_tone4 = "woman_teacher_tone4"
    woman_teacher_medium_dark_skin_tone = "woman_teacher_medium_dark_skin_tone"
    woman_teacher_tone5 = "woman_teacher_tone5"
    woman_teacher_dark_skin_tone = "woman_teacher_dark_skin_tone"
    man_teacher = "man_teacher"
    man_teacher_tone1 = "man_teacher_tone1"
    man_teacher_light_skin_tone = "man_teacher_light_skin_tone"
    man_teacher_tone2 = "man_teacher_tone2"
    man_teacher_medium_light_skin_tone = "man_teacher_medium_light_skin_tone"
    man_teacher_tone3 = "man_teacher_tone3"
    man_teacher_medium_skin_tone = "man_teacher_medium_skin_tone"
    man_teacher_tone4 = "man_teacher_tone4"
    man_teacher_medium_dark_skin_tone = "man_teacher_medium_dark_skin_tone"
    man_teacher_tone5 = "man_teacher_tone5"
    man_teacher_dark_skin_tone = "man_teacher_dark_skin_tone"
    woman_factory_worker = "woman_factory_worker"
    woman_factory_worker_tone1 = "woman_factory_worker_tone1"
    woman_factory_worker_light_skin_tone = "woman_factory_worker_light_skin_tone"
    woman_factory_worker_tone2 = "woman_factory_worker_tone2"
    woman_factory_worker_medium_light_skin_tone = "woman_factory_worker_medium_light_skin_tone"
    woman_factory_worker_tone3 = "woman_factory_worker_tone3"
    woman_factory_worker_medium_skin_tone = "woman_factory_worker_medium_skin_tone"
    woman_factory_worker_tone4 = "woman_factory_worker_tone4"
    woman_factory_worker_medium_dark_skin_tone = "woman_factory_worker_medium_dark_skin_tone"
    woman_factory_worker_tone5 = "woman_factory_worker_tone5"
    woman_factory_worker_dark_skin_tone = "woman_factory_worker_dark_skin_tone"
    man_factory_worker = "man_factory_worker"
    man_factory_worker_tone1 = "man_factory_worker_tone1"
    man_factory_worker_light_skin_tone = "man_factory_worker_light_skin_tone"
    man_factory_worker_tone2 = "man_factory_worker_tone2"
    man_factory_worker_medium_light_skin_tone = "man_factory_worker_medium_light_skin_tone"
    man_factory_worker_tone3 = "man_factory_worker_tone3"
    man_factory_worker_medium_skin_tone = "man_factory_worker_medium_skin_tone"
    man_factory_worker_tone4 = "man_factory_worker_tone4"
    man_factory_worker_medium_dark_skin_tone = "man_factory_worker_medium_dark_skin_tone"
    man_factory_worker_tone5 = "man_factory_worker_tone5"
    man_factory_worker_dark_skin_tone = "man_factory_worker_dark_skin_tone"
    woman_technologist = "woman_technologist"
    woman_technologist_tone1 = "woman_technologist_tone1"
    woman_technologist_light_skin_tone = "woman_technologist_light_skin_tone"
    woman_technologist_tone2 = "woman_technologist_tone2"
    woman_technologist_medium_light_skin_tone = "woman_technologist_medium_light_skin_tone"
    woman_technologist_tone3 = "woman_technologist_tone3"
    woman_technologist_medium_skin_tone = "woman_technologist_medium_skin_tone"
    woman_technologist_tone4 = "woman_technologist_tone4"
    woman_technologist_medium_dark_skin_tone = "woman_technologist_medium_dark_skin_tone"
    woman_technologist_tone5 = "woman_technologist_tone5"
    woman_technologist_dark_skin_tone = "woman_technologist_dark_skin_tone"
    man_technologist = "man_technologist"
    man_technologist_tone1 = "man_technologist_tone1"
    man_technologist_light_skin_tone = "man_technologist_light_skin_tone"
    man_technologist_tone2 = "man_technologist_tone2"
    man_technologist_medium_light_skin_tone = "man_technologist_medium_light_skin_tone"
    man_technologist_tone3 = "man_technologist_tone3"
    man_technologist_medium_skin_tone = "man_technologist_medium_skin_tone"
    man_technologist_tone4 = "man_technologist_tone4"
    man_technologist_medium_dark_skin_tone = "man_technologist_medium_dark_skin_tone"
    man_technologist_tone5 = "man_technologist_tone5"
    man_technologist_dark_skin_tone = "man_technologist_dark_skin_tone"
    woman_office_worker = "woman_office_worker"
    woman_office_worker_tone1 = "woman_office_worker_tone1"
    woman_office_worker_light_skin_tone = "woman_office_worker_light_skin_tone"
    woman_office_worker_tone2 = "woman_office_worker_tone2"
    woman_office_worker_medium_light_skin_tone = "woman_office_worker_medium_light_skin_tone"
    woman_office_worker_tone3 = "woman_office_worker_tone3"
    woman_office_worker_medium_skin_tone = "woman_office_worker_medium_skin_tone"
    woman_office_worker_tone4 = "woman_office_worker_tone4"
    woman_office_worker_medium_dark_skin_tone = "woman_office_worker_medium_dark_skin_tone"
    woman_office_worker_tone5 = "woman_office_worker_tone5"
    woman_office_worker_dark_skin_tone = "woman_office_worker_dark_skin_tone"
    man_office_worker = "man_office_worker"
    man_office_worker_tone1 = "man_office_worker_tone1"
    man_office_worker_light_skin_tone = "man_office_worker_light_skin_tone"
    man_office_worker_tone2 = "man_office_worker_tone2"
    man_office_worker_medium_light_skin_tone = "man_office_worker_medium_light_skin_tone"
    man_office_worker_tone3 = "man_office_worker_tone3"
    man_office_worker_medium_skin_tone = "man_office_worker_medium_skin_tone"
    man_office_worker_tone4 = "man_office_worker_tone4"
    man_office_worker_medium_dark_skin_tone = "man_office_worker_medium_dark_skin_tone"
    man_office_worker_tone5 = "man_office_worker_tone5"
    man_office_worker_dark_skin_tone = "man_office_worker_dark_skin_tone"
    woman_mechanic = "woman_mechanic"
    woman_mechanic_tone1 = "woman_mechanic_tone1"
    woman_mechanic_light_skin_tone = "woman_mechanic_light_skin_tone"
    woman_mechanic_tone2 = "woman_mechanic_tone2"
    woman_mechanic_medium_light_skin_tone = "woman_mechanic_medium_light_skin_tone"
    woman_mechanic_tone3 = "woman_mechanic_tone3"
    woman_mechanic_medium_skin_tone = "woman_mechanic_medium_skin_tone"
    woman_mechanic_tone4 = "woman_mechanic_tone4"
    woman_mechanic_medium_dark_skin_tone = "woman_mechanic_medium_dark_skin_tone"
    woman_mechanic_tone5 = "woman_mechanic_tone5"
    woman_mechanic_dark_skin_tone = "woman_mechanic_dark_skin_tone"
    man_mechanic = "man_mechanic"
    man_mechanic_tone1 = "man_mechanic_tone1"
    man_mechanic_light_skin_tone = "man_mechanic_light_skin_tone"
    man_mechanic_tone2 = "man_mechanic_tone2"
    man_mechanic_medium_light_skin_tone = "man_mechanic_medium_light_skin_tone"
    man_mechanic_tone3 = "man_mechanic_tone3"
    man_mechanic_medium_skin_tone = "man_mechanic_medium_skin_tone"
    man_mechanic_tone4 = "man_mechanic_tone4"
    man_mechanic_medium_dark_skin_tone = "man_mechanic_medium_dark_skin_tone"
    man_mechanic_tone5 = "man_mechanic_tone5"
    man_mechanic_dark_skin_tone = "man_mechanic_dark_skin_tone"
    woman_scientist = "woman_scientist"
    woman_scientist_tone1 = "woman_scientist_tone1"
    woman_scientist_light_skin_tone = "woman_scientist_light_skin_tone"
    woman_scientist_tone2 = "woman_scientist_tone2"
    woman_scientist_medium_light_skin_tone = "woman_scientist_medium_light_skin_tone"
    woman_scientist_tone3 = "woman_scientist_tone3"
    woman_scientist_medium_skin_tone = "woman_scientist_medium_skin_tone"
    woman_scientist_tone4 = "woman_scientist_tone4"
    woman_scientist_medium_dark_skin_tone = "woman_scientist_medium_dark_skin_tone"
    woman_scientist_tone5 = "woman_scientist_tone5"
    woman_scientist_dark_skin_tone = "woman_scientist_dark_skin_tone"
    man_scientist = "man_scientist"
    man_scientist_tone1 = "man_scientist_tone1"
    man_scientist_light_skin_tone = "man_scientist_light_skin_tone"
    man_scientist_tone2 = "man_scientist_tone2"
    man_scientist_medium_light_skin_tone = "man_scientist_medium_light_skin_tone"
    man_scientist_tone3 = "man_scientist_tone3"
    man_scientist_medium_skin_tone = "man_scientist_medium_skin_tone"
    man_scientist_tone4 = "man_scientist_tone4"
    man_scientist_medium_dark_skin_tone = "man_scientist_medium_dark_skin_tone"
    man_scientist_tone5 = "man_scientist_tone5"
    man_scientist_dark_skin_tone = "man_scientist_dark_skin_tone"
    woman_artist = "woman_artist"
    woman_artist_tone1 = "woman_artist_tone1"
    woman_artist_light_skin_tone = "woman_artist_light_skin_tone"
    woman_artist_tone2 = "woman_artist_tone2"
    woman_artist_medium_light_skin_tone = "woman_artist_medium_light_skin_tone"
    woman_artist_tone3 = "woman_artist_tone3"
    woman_artist_medium_skin_tone = "woman_artist_medium_skin_tone"
    woman_artist_tone4 = "woman_artist_tone4"
    woman_artist_medium_dark_skin_tone = "woman_artist_medium_dark_skin_tone"
    woman_artist_tone5 = "woman_artist_tone5"
    woman_artist_dark_skin_tone = "woman_artist_dark_skin_tone"
    man_artist = "man_artist"
    man_artist_tone1 = "man_artist_tone1"
    man_artist_light_skin_tone = "man_artist_light_skin_tone"
    man_artist_tone2 = "man_artist_tone2"
    man_artist_medium_light_skin_tone = "man_artist_medium_light_skin_tone"
    man_artist_tone3 = "man_artist_tone3"
    man_artist_medium_skin_tone = "man_artist_medium_skin_tone"
    man_artist_tone4 = "man_artist_tone4"
    man_artist_medium_dark_skin_tone = "man_artist_medium_dark_skin_tone"
    man_artist_tone5 = "man_artist_tone5"
    man_artist_dark_skin_tone = "man_artist_dark_skin_tone"
    woman_firefighter = "woman_firefighter"
    woman_firefighter_tone1 = "woman_firefighter_tone1"
    woman_firefighter_light_skin_tone = "woman_firefighter_light_skin_tone"
    woman_firefighter_tone2 = "woman_firefighter_tone2"
    woman_firefighter_medium_light_skin_tone = "woman_firefighter_medium_light_skin_tone"
    woman_firefighter_tone3 = "woman_firefighter_tone3"
    woman_firefighter_medium_skin_tone = "woman_firefighter_medium_skin_tone"
    woman_firefighter_tone4 = "woman_firefighter_tone4"
    woman_firefighter_medium_dark_skin_tone = "woman_firefighter_medium_dark_skin_tone"
    woman_firefighter_tone5 = "woman_firefighter_tone5"
    woman_firefighter_dark_skin_tone = "woman_firefighter_dark_skin_tone"
    man_firefighter = "man_firefighter"
    man_firefighter_tone1 = "man_firefighter_tone1"
    man_firefighter_light_skin_tone = "man_firefighter_light_skin_tone"
    man_firefighter_tone2 = "man_firefighter_tone2"
    man_firefighter_medium_light_skin_tone = "man_firefighter_medium_light_skin_tone"
    man_firefighter_tone3 = "man_firefighter_tone3"
    man_firefighter_medium_skin_tone = "man_firefighter_medium_skin_tone"
    man_firefighter_tone4 = "man_firefighter_tone4"
    man_firefighter_medium_dark_skin_tone = "man_firefighter_medium_dark_skin_tone"
    man_firefighter_tone5 = "man_firefighter_tone5"
    man_firefighter_dark_skin_tone = "man_firefighter_dark_skin_tone"
    woman_pilot = "woman_pilot"
    woman_pilot_tone1 = "woman_pilot_tone1"
    woman_pilot_light_skin_tone = "woman_pilot_light_skin_tone"
    woman_pilot_tone2 = "woman_pilot_tone2"
    woman_pilot_medium_light_skin_tone = "woman_pilot_medium_light_skin_tone"
    woman_pilot_tone3 = "woman_pilot_tone3"
    woman_pilot_medium_skin_tone = "woman_pilot_medium_skin_tone"
    woman_pilot_tone4 = "woman_pilot_tone4"
    woman_pilot_medium_dark_skin_tone = "woman_pilot_medium_dark_skin_tone"
    woman_pilot_tone5 = "woman_pilot_tone5"
    woman_pilot_dark_skin_tone = "woman_pilot_dark_skin_tone"
    man_pilot = "man_pilot"
    man_pilot_tone1 = "man_pilot_tone1"
    man_pilot_light_skin_tone = "man_pilot_light_skin_tone"
    man_pilot_tone2 = "man_pilot_tone2"
    man_pilot_medium_light_skin_tone = "man_pilot_medium_light_skin_tone"
    man_pilot_tone3 = "man_pilot_tone3"
    man_pilot_medium_skin_tone = "man_pilot_medium_skin_tone"
    man_pilot_tone4 = "man_pilot_tone4"
    man_pilot_medium_dark_skin_tone = "man_pilot_medium_dark_skin_tone"
    man_pilot_tone5 = "man_pilot_tone5"
    man_pilot_dark_skin_tone = "man_pilot_dark_skin_tone"
    woman_astronaut = "woman_astronaut"
    woman_astronaut_tone1 = "woman_astronaut_tone1"
    woman_astronaut_light_skin_tone = "woman_astronaut_light_skin_tone"
    woman_astronaut_tone2 = "woman_astronaut_tone2"
    woman_astronaut_medium_light_skin_tone = "woman_astronaut_medium_light_skin_tone"
    woman_astronaut_tone3 = "woman_astronaut_tone3"
    woman_astronaut_medium_skin_tone = "woman_astronaut_medium_skin_tone"
    woman_astronaut_tone4 = "woman_astronaut_tone4"
    woman_astronaut_medium_dark_skin_tone = "woman_astronaut_medium_dark_skin_tone"
    woman_astronaut_tone5 = "woman_astronaut_tone5"
    woman_astronaut_dark_skin_tone = "woman_astronaut_dark_skin_tone"
    man_astronaut = "man_astronaut"
    man_astronaut_tone1 = "man_astronaut_tone1"
    man_astronaut_light_skin_tone = "man_astronaut_light_skin_tone"
    man_astronaut_tone2 = "man_astronaut_tone2"
    man_astronaut_medium_light_skin_tone = "man_astronaut_medium_light_skin_tone"
    man_astronaut_tone3 = "man_astronaut_tone3"
    man_astronaut_medium_skin_tone = "man_astronaut_medium_skin_tone"
    man_astronaut_tone4 = "man_astronaut_tone4"
    man_astronaut_medium_dark_skin_tone = "man_astronaut_medium_dark_skin_tone"
    man_astronaut_tone5 = "man_astronaut_tone5"
    man_astronaut_dark_skin_tone = "man_astronaut_dark_skin_tone"
    woman_judge = "woman_judge"
    woman_judge_tone1 = "woman_judge_tone1"
    woman_judge_light_skin_tone = "woman_judge_light_skin_tone"
    woman_judge_tone2 = "woman_judge_tone2"
    woman_judge_medium_light_skin_tone = "woman_judge_medium_light_skin_tone"
    woman_judge_tone3 = "woman_judge_tone3"
    woman_judge_medium_skin_tone = "woman_judge_medium_skin_tone"
    woman_judge_tone4 = "woman_judge_tone4"
    woman_judge_medium_dark_skin_tone = "woman_judge_medium_dark_skin_tone"
    woman_judge_tone5 = "woman_judge_tone5"
    woman_judge_dark_skin_tone = "woman_judge_dark_skin_tone"
    man_judge = "man_judge"
    man_judge_tone1 = "man_judge_tone1"
    man_judge_light_skin_tone = "man_judge_light_skin_tone"
    man_judge_tone2 = "man_judge_tone2"
    man_judge_medium_light_skin_tone = "man_judge_medium_light_skin_tone"
    man_judge_tone3 = "man_judge_tone3"
    man_judge_medium_skin_tone = "man_judge_medium_skin_tone"
    man_judge_tone4 = "man_judge_tone4"
    man_judge_medium_dark_skin_tone = "man_judge_medium_dark_skin_tone"
    man_judge_tone5 = "man_judge_tone5"
    man_judge_dark_skin_tone = "man_judge_dark_skin_tone"
    bride_with_veil = "bride_with_veil"
    bride_with_veil_tone1 = "bride_with_veil_tone1"
    bride_with_veil_tone2 = "bride_with_veil_tone2"
    bride_with_veil_tone3 = "bride_with_veil_tone3"
    bride_with_veil_tone4 = "bride_with_veil_tone4"
    bride_with_veil_tone5 = "bride_with_veil_tone5"
    man_in_tuxedo = "man_in_tuxedo"
    man_in_tuxedo_tone1 = "man_in_tuxedo_tone1"
    tuxedo_tone1 = "tuxedo_tone1"
    man_in_tuxedo_tone2 = "man_in_tuxedo_tone2"
    tuxedo_tone2 = "tuxedo_tone2"
    man_in_tuxedo_tone3 = "man_in_tuxedo_tone3"
    tuxedo_tone3 = "tuxedo_tone3"
    man_in_tuxedo_tone4 = "man_in_tuxedo_tone4"
    tuxedo_tone4 = "tuxedo_tone4"
    man_in_tuxedo_tone5 = "man_in_tuxedo_tone5"
    tuxedo_tone5 = "tuxedo_tone5"
    princess = "princess"
    princess_tone1 = "princess_tone1"
    princess_tone2 = "princess_tone2"
    princess_tone3 = "princess_tone3"
    princess_tone4 = "princess_tone4"
    princess_tone5 = "princess_tone5"
    prince = "prince"
    prince_tone1 = "prince_tone1"
    prince_tone2 = "prince_tone2"
    prince_tone3 = "prince_tone3"
    prince_tone4 = "prince_tone4"
    prince_tone5 = "prince_tone5"
    superhero = "superhero"
    superhero_tone1 = "superhero_tone1"
    superhero_light_skin_tone = "superhero_light_skin_tone"
    superhero_tone2 = "superhero_tone2"
    superhero_medium_light_skin_tone = "superhero_medium_light_skin_tone"
    superhero_tone3 = "superhero_tone3"
    superhero_medium_skin_tone = "superhero_medium_skin_tone"
    superhero_tone4 = "superhero_tone4"
    superhero_medium_dark_skin_tone = "superhero_medium_dark_skin_tone"
    superhero_tone5 = "superhero_tone5"
    superhero_dark_skin_tone = "superhero_dark_skin_tone"
    woman_superhero = "woman_superhero"
    woman_superhero_tone1 = "woman_superhero_tone1"
    woman_superhero_light_skin_tone = "woman_superhero_light_skin_tone"
    woman_superhero_tone2 = "woman_superhero_tone2"
    woman_superhero_medium_light_skin_tone = "woman_superhero_medium_light_skin_tone"
    woman_superhero_tone3 = "woman_superhero_tone3"
    woman_superhero_medium_skin_tone = "woman_superhero_medium_skin_tone"
    woman_superhero_tone4 = "woman_superhero_tone4"
    woman_superhero_medium_dark_skin_tone = "woman_superhero_medium_dark_skin_tone"
    woman_superhero_tone5 = "woman_superhero_tone5"
    woman_superhero_dark_skin_tone = "woman_superhero_dark_skin_tone"
    man_superhero = "man_superhero"
    man_superhero_tone1 = "man_superhero_tone1"
    man_superhero_light_skin_tone = "man_superhero_light_skin_tone"
    man_superhero_tone2 = "man_superhero_tone2"
    man_superhero_medium_light_skin_tone = "man_superhero_medium_light_skin_tone"
    man_superhero_tone3 = "man_superhero_tone3"
    man_superhero_medium_skin_tone = "man_superhero_medium_skin_tone"
    man_superhero_tone4 = "man_superhero_tone4"
    man_superhero_medium_dark_skin_tone = "man_superhero_medium_dark_skin_tone"
    man_superhero_tone5 = "man_superhero_tone5"
    man_superhero_dark_skin_tone = "man_superhero_dark_skin_tone"
    supervillain = "supervillain"
    supervillain_tone1 = "supervillain_tone1"
    supervillain_light_skin_tone = "supervillain_light_skin_tone"
    supervillain_tone2 = "supervillain_tone2"
    supervillain_medium_light_skin_tone = "supervillain_medium_light_skin_tone"
    supervillain_tone3 = "supervillain_tone3"
    supervillain_medium_skin_tone = "supervillain_medium_skin_tone"
    supervillain_tone4 = "supervillain_tone4"
    supervillain_medium_dark_skin_tone = "supervillain_medium_dark_skin_tone"
    supervillain_tone5 = "supervillain_tone5"
    supervillain_dark_skin_tone = "supervillain_dark_skin_tone"
    woman_supervillain = "woman_supervillain"
    woman_supervillain_tone1 = "woman_supervillain_tone1"
    woman_supervillain_light_skin_tone = "woman_supervillain_light_skin_tone"
    woman_supervillain_tone2 = "woman_supervillain_tone2"
    woman_supervillain_medium_light_skin_tone = "woman_supervillain_medium_light_skin_tone"
    woman_supervillain_tone3 = "woman_supervillain_tone3"
    woman_supervillain_medium_skin_tone = "woman_supervillain_medium_skin_tone"
    woman_supervillain_tone4 = "woman_supervillain_tone4"
    woman_supervillain_medium_dark_skin_tone = "woman_supervillain_medium_dark_skin_tone"
    woman_supervillain_tone5 = "woman_supervillain_tone5"
    woman_supervillain_dark_skin_tone = "woman_supervillain_dark_skin_tone"
    man_supervillain = "man_supervillain"
    man_supervillain_tone1 = "man_supervillain_tone1"
    man_supervillain_light_skin_tone = "man_supervillain_light_skin_tone"
    man_supervillain_tone2 = "man_supervillain_tone2"
    man_supervillain_medium_light_skin_tone = "man_supervillain_medium_light_skin_tone"
    man_supervillain_tone3 = "man_supervillain_tone3"
    man_supervillain_medium_skin_tone = "man_supervillain_medium_skin_tone"
    man_supervillain_tone4 = "man_supervillain_tone4"
    man_supervillain_medium_dark_skin_tone = "man_supervillain_medium_dark_skin_tone"
    man_supervillain_tone5 = "man_supervillain_tone5"
    man_supervillain_dark_skin_tone = "man_supervillain_dark_skin_tone"
    mrs_claus = "mrs_claus"
    mother_christmas = "mother_christmas"
    mrs_claus_tone1 = "mrs_claus_tone1"
    mother_christmas_tone1 = "mother_christmas_tone1"
    mrs_claus_tone2 = "mrs_claus_tone2"
    mother_christmas_tone2 = "mother_christmas_tone2"
    mrs_claus_tone3 = "mrs_claus_tone3"
    mother_christmas_tone3 = "mother_christmas_tone3"
    mrs_claus_tone4 = "mrs_claus_tone4"
    mother_christmas_tone4 = "mother_christmas_tone4"
    mrs_claus_tone5 = "mrs_claus_tone5"
    mother_christmas_tone5 = "mother_christmas_tone5"
    santa = "santa"
    santa_tone1 = "santa_tone1"
    santa_tone2 = "santa_tone2"
    santa_tone3 = "santa_tone3"
    santa_tone4 = "santa_tone4"
    santa_tone5 = "santa_tone5"
    mage = "mage"
    mage_tone1 = "mage_tone1"
    mage_light_skin_tone = "mage_light_skin_tone"
    mage_tone2 = "mage_tone2"
    mage_medium_light_skin_tone = "mage_medium_light_skin_tone"
    mage_tone3 = "mage_tone3"
    mage_medium_skin_tone = "mage_medium_skin_tone"
    mage_tone4 = "mage_tone4"
    mage_medium_dark_skin_tone = "mage_medium_dark_skin_tone"
    mage_tone5 = "mage_tone5"
    mage_dark_skin_tone = "mage_dark_skin_tone"
    woman_mage = "woman_mage"
    woman_mage_tone1 = "woman_mage_tone1"
    woman_mage_light_skin_tone = "woman_mage_light_skin_tone"
    woman_mage_tone2 = "woman_mage_tone2"
    woman_mage_medium_light_skin_tone = "woman_mage_medium_light_skin_tone"
    woman_mage_tone3 = "woman_mage_tone3"
    woman_mage_medium_skin_tone = "woman_mage_medium_skin_tone"
    woman_mage_tone4 = "woman_mage_tone4"
    woman_mage_medium_dark_skin_tone = "woman_mage_medium_dark_skin_tone"
    woman_mage_tone5 = "woman_mage_tone5"
    woman_mage_dark_skin_tone = "woman_mage_dark_skin_tone"
    man_mage = "man_mage"
    man_mage_tone1 = "man_mage_tone1"
    man_mage_light_skin_tone = "man_mage_light_skin_tone"
    man_mage_tone2 = "man_mage_tone2"
    man_mage_medium_light_skin_tone = "man_mage_medium_light_skin_tone"
    man_mage_tone3 = "man_mage_tone3"
    man_mage_medium_skin_tone = "man_mage_medium_skin_tone"
    man_mage_tone4 = "man_mage_tone4"
    man_mage_medium_dark_skin_tone = "man_mage_medium_dark_skin_tone"
    man_mage_tone5 = "man_mage_tone5"
    man_mage_dark_skin_tone = "man_mage_dark_skin_tone"
    elf = "elf"
    elf_tone1 = "elf_tone1"
    elf_light_skin_tone = "elf_light_skin_tone"
    elf_tone2 = "elf_tone2"
    elf_medium_light_skin_tone = "elf_medium_light_skin_tone"
    elf_tone3 = "elf_tone3"
    elf_medium_skin_tone = "elf_medium_skin_tone"
    elf_tone4 = "elf_tone4"
    elf_medium_dark_skin_tone = "elf_medium_dark_skin_tone"
    elf_tone5 = "elf_tone5"
    elf_dark_skin_tone = "elf_dark_skin_tone"
    woman_elf = "woman_elf"
    woman_elf_tone1 = "woman_elf_tone1"
    woman_elf_light_skin_tone = "woman_elf_light_skin_tone"
    woman_elf_tone2 = "woman_elf_tone2"
    woman_elf_medium_light_skin_tone = "woman_elf_medium_light_skin_tone"
    woman_elf_tone3 = "woman_elf_tone3"
    woman_elf_medium_skin_tone = "woman_elf_medium_skin_tone"
    woman_elf_tone4 = "woman_elf_tone4"
    woman_elf_medium_dark_skin_tone = "woman_elf_medium_dark_skin_tone"
    woman_elf_tone5 = "woman_elf_tone5"
    woman_elf_dark_skin_tone = "woman_elf_dark_skin_tone"
    man_elf = "man_elf"
    man_elf_tone1 = "man_elf_tone1"
    man_elf_light_skin_tone = "man_elf_light_skin_tone"
    man_elf_tone2 = "man_elf_tone2"
    man_elf_medium_light_skin_tone = "man_elf_medium_light_skin_tone"
    man_elf_tone3 = "man_elf_tone3"
    man_elf_medium_skin_tone = "man_elf_medium_skin_tone"
    man_elf_tone4 = "man_elf_tone4"
    man_elf_medium_dark_skin_tone = "man_elf_medium_dark_skin_tone"
    man_elf_tone5 = "man_elf_tone5"
    man_elf_dark_skin_tone = "man_elf_dark_skin_tone"
    vampire = "vampire"
    vampire_tone1 = "vampire_tone1"
    vampire_light_skin_tone = "vampire_light_skin_tone"
    vampire_tone2 = "vampire_tone2"
    vampire_medium_light_skin_tone = "vampire_medium_light_skin_tone"
    vampire_tone3 = "vampire_tone3"
    vampire_medium_skin_tone = "vampire_medium_skin_tone"
    vampire_tone4 = "vampire_tone4"
    vampire_medium_dark_skin_tone = "vampire_medium_dark_skin_tone"
    vampire_tone5 = "vampire_tone5"
    vampire_dark_skin_tone = "vampire_dark_skin_tone"
    woman_vampire = "woman_vampire"
    woman_vampire_tone1 = "woman_vampire_tone1"
    woman_vampire_light_skin_tone = "woman_vampire_light_skin_tone"
    woman_vampire_tone2 = "woman_vampire_tone2"
    woman_vampire_medium_light_skin_tone = "woman_vampire_medium_light_skin_tone"
    woman_vampire_tone3 = "woman_vampire_tone3"
    woman_vampire_medium_skin_tone = "woman_vampire_medium_skin_tone"
    woman_vampire_tone4 = "woman_vampire_tone4"
    woman_vampire_medium_dark_skin_tone = "woman_vampire_medium_dark_skin_tone"
    woman_vampire_tone5 = "woman_vampire_tone5"
    woman_vampire_dark_skin_tone = "woman_vampire_dark_skin_tone"
    man_vampire = "man_vampire"
    man_vampire_tone1 = "man_vampire_tone1"
    man_vampire_light_skin_tone = "man_vampire_light_skin_tone"
    man_vampire_tone2 = "man_vampire_tone2"
    man_vampire_medium_light_skin_tone = "man_vampire_medium_light_skin_tone"
    man_vampire_tone3 = "man_vampire_tone3"
    man_vampire_medium_skin_tone = "man_vampire_medium_skin_tone"
    man_vampire_tone4 = "man_vampire_tone4"
    man_vampire_medium_dark_skin_tone = "man_vampire_medium_dark_skin_tone"
    man_vampire_tone5 = "man_vampire_tone5"
    man_vampire_dark_skin_tone = "man_vampire_dark_skin_tone"
    zombie = "zombie"
    woman_zombie = "woman_zombie"
    man_zombie = "man_zombie"
    genie = "genie"
    woman_genie = "woman_genie"
    man_genie = "man_genie"
    merperson = "merperson"
    merperson_tone1 = "merperson_tone1"
    merperson_light_skin_tone = "merperson_light_skin_tone"
    merperson_tone2 = "merperson_tone2"
    merperson_medium_light_skin_tone = "merperson_medium_light_skin_tone"
    merperson_tone3 = "merperson_tone3"
    merperson_medium_skin_tone = "merperson_medium_skin_tone"
    merperson_tone4 = "merperson_tone4"
    merperson_medium_dark_skin_tone = "merperson_medium_dark_skin_tone"
    merperson_tone5 = "merperson_tone5"
    merperson_dark_skin_tone = "merperson_dark_skin_tone"
    mermaid = "mermaid"
    mermaid_tone1 = "mermaid_tone1"
    mermaid_light_skin_tone = "mermaid_light_skin_tone"
    mermaid_tone2 = "mermaid_tone2"
    mermaid_medium_light_skin_tone = "mermaid_medium_light_skin_tone"
    mermaid_tone3 = "mermaid_tone3"
    mermaid_medium_skin_tone = "mermaid_medium_skin_tone"
    mermaid_tone4 = "mermaid_tone4"
    mermaid_medium_dark_skin_tone = "mermaid_medium_dark_skin_tone"
    mermaid_tone5 = "mermaid_tone5"
    mermaid_dark_skin_tone = "mermaid_dark_skin_tone"
    merman = "merman"
    merman_tone1 = "merman_tone1"
    merman_light_skin_tone = "merman_light_skin_tone"
    merman_tone2 = "merman_tone2"
    merman_medium_light_skin_tone = "merman_medium_light_skin_tone"
    merman_tone3 = "merman_tone3"
    merman_medium_skin_tone = "merman_medium_skin_tone"
    merman_tone4 = "merman_tone4"
    merman_medium_dark_skin_tone = "merman_medium_dark_skin_tone"
    merman_tone5 = "merman_tone5"
    merman_dark_skin_tone = "merman_dark_skin_tone"
    fairy = "fairy"
    fairy_tone1 = "fairy_tone1"
    fairy_light_skin_tone = "fairy_light_skin_tone"
    fairy_tone2 = "fairy_tone2"
    fairy_medium_light_skin_tone = "fairy_medium_light_skin_tone"
    fairy_tone3 = "fairy_tone3"
    fairy_medium_skin_tone = "fairy_medium_skin_tone"
    fairy_tone4 = "fairy_tone4"
    fairy_medium_dark_skin_tone = "fairy_medium_dark_skin_tone"
    fairy_tone5 = "fairy_tone5"
    fairy_dark_skin_tone = "fairy_dark_skin_tone"
    woman_fairy = "woman_fairy"
    woman_fairy_tone1 = "woman_fairy_tone1"
    woman_fairy_light_skin_tone = "woman_fairy_light_skin_tone"
    woman_fairy_tone2 = "woman_fairy_tone2"
    woman_fairy_medium_light_skin_tone = "woman_fairy_medium_light_skin_tone"
    woman_fairy_tone3 = "woman_fairy_tone3"
    woman_fairy_medium_skin_tone = "woman_fairy_medium_skin_tone"
    woman_fairy_tone4 = "woman_fairy_tone4"
    woman_fairy_medium_dark_skin_tone = "woman_fairy_medium_dark_skin_tone"
    woman_fairy_tone5 = "woman_fairy_tone5"
    woman_fairy_dark_skin_tone = "woman_fairy_dark_skin_tone"
    man_fairy = "man_fairy"
    man_fairy_tone1 = "man_fairy_tone1"
    man_fairy_light_skin_tone = "man_fairy_light_skin_tone"
    man_fairy_tone2 = "man_fairy_tone2"
    man_fairy_medium_light_skin_tone = "man_fairy_medium_light_skin_tone"
    man_fairy_tone3 = "man_fairy_tone3"
    man_fairy_medium_skin_tone = "man_fairy_medium_skin_tone"
    man_fairy_tone4 = "man_fairy_tone4"
    man_fairy_medium_dark_skin_tone = "man_fairy_medium_dark_skin_tone"
    man_fairy_tone5 = "man_fairy_tone5"
    man_fairy_dark_skin_tone = "man_fairy_dark_skin_tone"
    angel = "angel"
    angel_tone1 = "angel_tone1"
    angel_tone2 = "angel_tone2"
    angel_tone3 = "angel_tone3"
    angel_tone4 = "angel_tone4"
    angel_tone5 = "angel_tone5"
    pregnant_woman = "pregnant_woman"
    expecting_woman = "expecting_woman"
    pregnant_woman_tone1 = "pregnant_woman_tone1"
    expecting_woman_tone1 = "expecting_woman_tone1"
    pregnant_woman_tone2 = "pregnant_woman_tone2"
    expecting_woman_tone2 = "expecting_woman_tone2"
    pregnant_woman_tone3 = "pregnant_woman_tone3"
    expecting_woman_tone3 = "expecting_woman_tone3"
    pregnant_woman_tone4 = "pregnant_woman_tone4"
    expecting_woman_tone4 = "expecting_woman_tone4"
    pregnant_woman_tone5 = "pregnant_woman_tone5"
    expecting_woman_tone5 = "expecting_woman_tone5"
    breast_feeding = "breast_feeding"
    breast_feeding_tone1 = "breast_feeding_tone1"
    breast_feeding_light_skin_tone = "breast_feeding_light_skin_tone"
    breast_feeding_tone2 = "breast_feeding_tone2"
    breast_feeding_medium_light_skin_tone = "breast_feeding_medium_light_skin_tone"
    breast_feeding_tone3 = "breast_feeding_tone3"
    breast_feeding_medium_skin_tone = "breast_feeding_medium_skin_tone"
    breast_feeding_tone4 = "breast_feeding_tone4"
    breast_feeding_medium_dark_skin_tone = "breast_feeding_medium_dark_skin_tone"
    breast_feeding_tone5 = "breast_feeding_tone5"
    breast_feeding_dark_skin_tone = "breast_feeding_dark_skin_tone"
    person_bowing = "person_bowing"
    bow = "bow"
    person_bowing_tone1 = "person_bowing_tone1"
    bow_tone1 = "bow_tone1"
    person_bowing_tone2 = "person_bowing_tone2"
    bow_tone2 = "bow_tone2"
    person_bowing_tone3 = "person_bowing_tone3"
    bow_tone3 = "bow_tone3"
    person_bowing_tone4 = "person_bowing_tone4"
    bow_tone4 = "bow_tone4"
    person_bowing_tone5 = "person_bowing_tone5"
    bow_tone5 = "bow_tone5"
    woman_bowing = "woman_bowing"
    woman_bowing_tone1 = "woman_bowing_tone1"
    woman_bowing_light_skin_tone = "woman_bowing_light_skin_tone"
    woman_bowing_tone2 = "woman_bowing_tone2"
    woman_bowing_medium_light_skin_tone = "woman_bowing_medium_light_skin_tone"
    woman_bowing_tone3 = "woman_bowing_tone3"
    woman_bowing_medium_skin_tone = "woman_bowing_medium_skin_tone"
    woman_bowing_tone4 = "woman_bowing_tone4"
    woman_bowing_medium_dark_skin_tone = "woman_bowing_medium_dark_skin_tone"
    woman_bowing_tone5 = "woman_bowing_tone5"
    woman_bowing_dark_skin_tone = "woman_bowing_dark_skin_tone"
    man_bowing = "man_bowing"
    man_bowing_tone1 = "man_bowing_tone1"
    man_bowing_light_skin_tone = "man_bowing_light_skin_tone"
    man_bowing_tone2 = "man_bowing_tone2"
    man_bowing_medium_light_skin_tone = "man_bowing_medium_light_skin_tone"
    man_bowing_tone3 = "man_bowing_tone3"
    man_bowing_medium_skin_tone = "man_bowing_medium_skin_tone"
    man_bowing_tone4 = "man_bowing_tone4"
    man_bowing_medium_dark_skin_tone = "man_bowing_medium_dark_skin_tone"
    man_bowing_tone5 = "man_bowing_tone5"
    man_bowing_dark_skin_tone = "man_bowing_dark_skin_tone"
    person_tipping_hand = "person_tipping_hand"
    information_desk_person = "information_desk_person"
    person_tipping_hand_tone1 = "person_tipping_hand_tone1"
    information_desk_person_tone1 = "information_desk_person_tone1"
    person_tipping_hand_tone2 = "person_tipping_hand_tone2"
    information_desk_person_tone2 = "information_desk_person_tone2"
    person_tipping_hand_tone3 = "person_tipping_hand_tone3"
    information_desk_person_tone3 = "information_desk_person_tone3"
    person_tipping_hand_tone4 = "person_tipping_hand_tone4"
    information_desk_person_tone4 = "information_desk_person_tone4"
    person_tipping_hand_tone5 = "person_tipping_hand_tone5"
    information_desk_person_tone5 = "information_desk_person_tone5"
    woman_tipping_hand = "woman_tipping_hand"
    woman_tipping_hand_tone1 = "woman_tipping_hand_tone1"
    woman_tipping_hand_light_skin_tone = "woman_tipping_hand_light_skin_tone"
    woman_tipping_hand_tone2 = "woman_tipping_hand_tone2"
    woman_tipping_hand_medium_light_skin_tone = "woman_tipping_hand_medium_light_skin_tone"
    woman_tipping_hand_tone3 = "woman_tipping_hand_tone3"
    woman_tipping_hand_medium_skin_tone = "woman_tipping_hand_medium_skin_tone"
    woman_tipping_hand_tone4 = "woman_tipping_hand_tone4"
    woman_tipping_hand_medium_dark_skin_tone = "woman_tipping_hand_medium_dark_skin_tone"
    woman_tipping_hand_tone5 = "woman_tipping_hand_tone5"
    woman_tipping_hand_dark_skin_tone = "woman_tipping_hand_dark_skin_tone"
    man_tipping_hand = "man_tipping_hand"
    man_tipping_hand_tone1 = "man_tipping_hand_tone1"
    man_tipping_hand_light_skin_tone = "man_tipping_hand_light_skin_tone"
    man_tipping_hand_tone2 = "man_tipping_hand_tone2"
    man_tipping_hand_medium_light_skin_tone = "man_tipping_hand_medium_light_skin_tone"
    man_tipping_hand_tone3 = "man_tipping_hand_tone3"
    man_tipping_hand_medium_skin_tone = "man_tipping_hand_medium_skin_tone"
    man_tipping_hand_tone4 = "man_tipping_hand_tone4"
    man_tipping_hand_medium_dark_skin_tone = "man_tipping_hand_medium_dark_skin_tone"
    man_tipping_hand_tone5 = "man_tipping_hand_tone5"
    man_tipping_hand_dark_skin_tone = "man_tipping_hand_dark_skin_tone"
    person_gesturing_no = "person_gesturing_no"
    no_good = "no_good"
    person_gesturing_no_tone1 = "person_gesturing_no_tone1"
    no_good_tone1 = "no_good_tone1"
    person_gesturing_no_tone2 = "person_gesturing_no_tone2"
    no_good_tone2 = "no_good_tone2"
    person_gesturing_no_tone3 = "person_gesturing_no_tone3"
    no_good_tone3 = "no_good_tone3"
    person_gesturing_no_tone4 = "person_gesturing_no_tone4"
    no_good_tone4 = "no_good_tone4"
    person_gesturing_no_tone5 = "person_gesturing_no_tone5"
    no_good_tone5 = "no_good_tone5"
    woman_gesturing_no = "woman_gesturing_no"
    woman_gesturing_no_tone1 = "woman_gesturing_no_tone1"
    woman_gesturing_no_light_skin_tone = "woman_gesturing_no_light_skin_tone"
    woman_gesturing_no_tone2 = "woman_gesturing_no_tone2"
    woman_gesturing_no_medium_light_skin_tone = "woman_gesturing_no_medium_light_skin_tone"
    woman_gesturing_no_tone3 = "woman_gesturing_no_tone3"
    woman_gesturing_no_medium_skin_tone = "woman_gesturing_no_medium_skin_tone"
    woman_gesturing_no_tone4 = "woman_gesturing_no_tone4"
    woman_gesturing_no_medium_dark_skin_tone = "woman_gesturing_no_medium_dark_skin_tone"
    woman_gesturing_no_tone5 = "woman_gesturing_no_tone5"
    woman_gesturing_no_dark_skin_tone = "woman_gesturing_no_dark_skin_tone"
    man_gesturing_no = "man_gesturing_no"
    man_gesturing_no_tone1 = "man_gesturing_no_tone1"
    man_gesturing_no_light_skin_tone = "man_gesturing_no_light_skin_tone"
    man_gesturing_no_tone2 = "man_gesturing_no_tone2"
    man_gesturing_no_medium_light_skin_tone = "man_gesturing_no_medium_light_skin_tone"
    man_gesturing_no_tone3 = "man_gesturing_no_tone3"
    man_gesturing_no_medium_skin_tone = "man_gesturing_no_medium_skin_tone"
    man_gesturing_no_tone4 = "man_gesturing_no_tone4"
    man_gesturing_no_medium_dark_skin_tone = "man_gesturing_no_medium_dark_skin_tone"
    man_gesturing_no_tone5 = "man_gesturing_no_tone5"
    man_gesturing_no_dark_skin_tone = "man_gesturing_no_dark_skin_tone"
    person_gesturing_ok = "person_gesturing_ok"
    ok_woman = "ok_woman"
    person_gesturing_ok_tone1 = "person_gesturing_ok_tone1"
    ok_woman_tone1 = "ok_woman_tone1"
    person_gesturing_ok_tone2 = "person_gesturing_ok_tone2"
    ok_woman_tone2 = "ok_woman_tone2"
    person_gesturing_ok_tone3 = "person_gesturing_ok_tone3"
    ok_woman_tone3 = "ok_woman_tone3"
    person_gesturing_ok_tone4 = "person_gesturing_ok_tone4"
    ok_woman_tone4 = "ok_woman_tone4"
    person_gesturing_ok_tone5 = "person_gesturing_ok_tone5"
    ok_woman_tone5 = "ok_woman_tone5"
    woman_gesturing_ok = "woman_gesturing_ok"
    woman_gesturing_ok_tone1 = "woman_gesturing_ok_tone1"
    woman_gesturing_ok_light_skin_tone = "woman_gesturing_ok_light_skin_tone"
    woman_gesturing_ok_tone2 = "woman_gesturing_ok_tone2"
    woman_gesturing_ok_medium_light_skin_tone = "woman_gesturing_ok_medium_light_skin_tone"
    woman_gesturing_ok_tone3 = "woman_gesturing_ok_tone3"
    woman_gesturing_ok_medium_skin_tone = "woman_gesturing_ok_medium_skin_tone"
    woman_gesturing_ok_tone4 = "woman_gesturing_ok_tone4"
    woman_gesturing_ok_medium_dark_skin_tone = "woman_gesturing_ok_medium_dark_skin_tone"
    woman_gesturing_ok_tone5 = "woman_gesturing_ok_tone5"
    woman_gesturing_ok_dark_skin_tone = "woman_gesturing_ok_dark_skin_tone"
    man_gesturing_ok = "man_gesturing_ok"
    man_gesturing_ok_tone1 = "man_gesturing_ok_tone1"
    man_gesturing_ok_light_skin_tone = "man_gesturing_ok_light_skin_tone"
    man_gesturing_ok_tone2 = "man_gesturing_ok_tone2"
    man_gesturing_ok_medium_light_skin_tone = "man_gesturing_ok_medium_light_skin_tone"
    man_gesturing_ok_tone3 = "man_gesturing_ok_tone3"
    man_gesturing_ok_medium_skin_tone = "man_gesturing_ok_medium_skin_tone"
    man_gesturing_ok_tone4 = "man_gesturing_ok_tone4"
    man_gesturing_ok_medium_dark_skin_tone = "man_gesturing_ok_medium_dark_skin_tone"
    man_gesturing_ok_tone5 = "man_gesturing_ok_tone5"
    man_gesturing_ok_dark_skin_tone = "man_gesturing_ok_dark_skin_tone"
    person_raising_hand = "person_raising_hand"
    raising_hand = "raising_hand"
    person_raising_hand_tone1 = "person_raising_hand_tone1"
    raising_hand_tone1 = "raising_hand_tone1"
    person_raising_hand_tone2 = "person_raising_hand_tone2"
    raising_hand_tone2 = "raising_hand_tone2"
    person_raising_hand_tone3 = "person_raising_hand_tone3"
    raising_hand_tone3 = "raising_hand_tone3"
    person_raising_hand_tone4 = "person_raising_hand_tone4"
    raising_hand_tone4 = "raising_hand_tone4"
    person_raising_hand_tone5 = "person_raising_hand_tone5"
    raising_hand_tone5 = "raising_hand_tone5"
    woman_raising_hand = "woman_raising_hand"
    woman_raising_hand_tone1 = "woman_raising_hand_tone1"
    woman_raising_hand_light_skin_tone = "woman_raising_hand_light_skin_tone"
    woman_raising_hand_tone2 = "woman_raising_hand_tone2"
    woman_raising_hand_medium_light_skin_tone = "woman_raising_hand_medium_light_skin_tone"
    woman_raising_hand_tone3 = "woman_raising_hand_tone3"
    woman_raising_hand_medium_skin_tone = "woman_raising_hand_medium_skin_tone"
    woman_raising_hand_tone4 = "woman_raising_hand_tone4"
    woman_raising_hand_medium_dark_skin_tone = "woman_raising_hand_medium_dark_skin_tone"
    woman_raising_hand_tone5 = "woman_raising_hand_tone5"
    woman_raising_hand_dark_skin_tone = "woman_raising_hand_dark_skin_tone"
    man_raising_hand = "man_raising_hand"
    man_raising_hand_tone1 = "man_raising_hand_tone1"
    man_raising_hand_light_skin_tone = "man_raising_hand_light_skin_tone"
    man_raising_hand_tone2 = "man_raising_hand_tone2"
    man_raising_hand_medium_light_skin_tone = "man_raising_hand_medium_light_skin_tone"
    man_raising_hand_tone3 = "man_raising_hand_tone3"
    man_raising_hand_medium_skin_tone = "man_raising_hand_medium_skin_tone"
    man_raising_hand_tone4 = "man_raising_hand_tone4"
    man_raising_hand_medium_dark_skin_tone = "man_raising_hand_medium_dark_skin_tone"
    man_raising_hand_tone5 = "man_raising_hand_tone5"
    man_raising_hand_dark_skin_tone = "man_raising_hand_dark_skin_tone"
    deaf_person = "deaf_person"
    deaf_person_tone1 = "deaf_person_tone1"
    deaf_person_light_skin_tone = "deaf_person_light_skin_tone"
    deaf_person_tone2 = "deaf_person_tone2"
    deaf_person_medium_light_skin_tone = "deaf_person_medium_light_skin_tone"
    deaf_person_tone3 = "deaf_person_tone3"
    deaf_person_medium_skin_tone = "deaf_person_medium_skin_tone"
    deaf_person_tone4 = "deaf_person_tone4"
    deaf_person_medium_dark_skin_tone = "deaf_person_medium_dark_skin_tone"
    deaf_person_tone5 = "deaf_person_tone5"
    deaf_person_dark_skin_tone = "deaf_person_dark_skin_tone"
    deaf_woman = "deaf_woman"
    deaf_woman_tone1 = "deaf_woman_tone1"
    deaf_woman_light_skin_tone = "deaf_woman_light_skin_tone"
    deaf_woman_tone2 = "deaf_woman_tone2"
    deaf_woman_medium_light_skin_tone = "deaf_woman_medium_light_skin_tone"
    deaf_woman_tone3 = "deaf_woman_tone3"
    deaf_woman_medium_skin_tone = "deaf_woman_medium_skin_tone"
    deaf_woman_tone4 = "deaf_woman_tone4"
    deaf_woman_medium_dark_skin_tone = "deaf_woman_medium_dark_skin_tone"
    deaf_woman_tone5 = "deaf_woman_tone5"
    deaf_woman_dark_skin_tone = "deaf_woman_dark_skin_tone"
    deaf_man = "deaf_man"
    deaf_man_tone1 = "deaf_man_tone1"
    deaf_man_light_skin_tone = "deaf_man_light_skin_tone"
    deaf_man_tone2 = "deaf_man_tone2"
    deaf_man_medium_light_skin_tone = "deaf_man_medium_light_skin_tone"
    deaf_man_tone3 = "deaf_man_tone3"
    deaf_man_medium_skin_tone = "deaf_man_medium_skin_tone"
    deaf_man_tone4 = "deaf_man_tone4"
    deaf_man_medium_dark_skin_tone = "deaf_man_medium_dark_skin_tone"
    deaf_man_tone5 = "deaf_man_tone5"
    deaf_man_dark_skin_tone = "deaf_man_dark_skin_tone"
    person_facepalming = "person_facepalming"
    face_palm = "face_palm"
    facepalm = "facepalm"
    person_facepalming_tone1 = "person_facepalming_tone1"
    face_palm_tone1 = "face_palm_tone1"
    facepalm_tone1 = "facepalm_tone1"
    person_facepalming_tone2 = "person_facepalming_tone2"
    face_palm_tone2 = "face_palm_tone2"
    facepalm_tone2 = "facepalm_tone2"
    person_facepalming_tone3 = "person_facepalming_tone3"
    face_palm_tone3 = "face_palm_tone3"
    facepalm_tone3 = "facepalm_tone3"
    person_facepalming_tone4 = "person_facepalming_tone4"
    face_palm_tone4 = "face_palm_tone4"
    facepalm_tone4 = "facepalm_tone4"
    person_facepalming_tone5 = "person_facepalming_tone5"
    face_palm_tone5 = "face_palm_tone5"
    facepalm_tone5 = "facepalm_tone5"
    woman_facepalming = "woman_facepalming"
    woman_facepalming_tone1 = "woman_facepalming_tone1"
    woman_facepalming_light_skin_tone = "woman_facepalming_light_skin_tone"
    woman_facepalming_tone2 = "woman_facepalming_tone2"
    woman_facepalming_medium_light_skin_tone = "woman_facepalming_medium_light_skin_tone"
    woman_facepalming_tone3 = "woman_facepalming_tone3"
    woman_facepalming_medium_skin_tone = "woman_facepalming_medium_skin_tone"
    woman_facepalming_tone4 = "woman_facepalming_tone4"
    woman_facepalming_medium_dark_skin_tone = "woman_facepalming_medium_dark_skin_tone"
    woman_facepalming_tone5 = "woman_facepalming_tone5"
    woman_facepalming_dark_skin_tone = "woman_facepalming_dark_skin_tone"
    man_facepalming = "man_facepalming"
    man_facepalming_tone1 = "man_facepalming_tone1"
    man_facepalming_light_skin_tone = "man_facepalming_light_skin_tone"
    man_facepalming_tone2 = "man_facepalming_tone2"
    man_facepalming_medium_light_skin_tone = "man_facepalming_medium_light_skin_tone"
    man_facepalming_tone3 = "man_facepalming_tone3"
    man_facepalming_medium_skin_tone = "man_facepalming_medium_skin_tone"
    man_facepalming_tone4 = "man_facepalming_tone4"
    man_facepalming_medium_dark_skin_tone = "man_facepalming_medium_dark_skin_tone"
    man_facepalming_tone5 = "man_facepalming_tone5"
    man_facepalming_dark_skin_tone = "man_facepalming_dark_skin_tone"
    person_shrugging = "person_shrugging"
    shrug = "shrug"
    person_shrugging_tone1 = "person_shrugging_tone1"
    shrug_tone1 = "shrug_tone1"
    person_shrugging_tone2 = "person_shrugging_tone2"
    shrug_tone2 = "shrug_tone2"
    person_shrugging_tone3 = "person_shrugging_tone3"
    shrug_tone3 = "shrug_tone3"
    person_shrugging_tone4 = "person_shrugging_tone4"
    shrug_tone4 = "shrug_tone4"
    person_shrugging_tone5 = "person_shrugging_tone5"
    shrug_tone5 = "shrug_tone5"
    woman_shrugging = "woman_shrugging"
    woman_shrugging_tone1 = "woman_shrugging_tone1"
    woman_shrugging_light_skin_tone = "woman_shrugging_light_skin_tone"
    woman_shrugging_tone2 = "woman_shrugging_tone2"
    woman_shrugging_medium_light_skin_tone = "woman_shrugging_medium_light_skin_tone"
    woman_shrugging_tone3 = "woman_shrugging_tone3"
    woman_shrugging_medium_skin_tone = "woman_shrugging_medium_skin_tone"
    woman_shrugging_tone4 = "woman_shrugging_tone4"
    woman_shrugging_medium_dark_skin_tone = "woman_shrugging_medium_dark_skin_tone"
    woman_shrugging_tone5 = "woman_shrugging_tone5"
    woman_shrugging_dark_skin_tone = "woman_shrugging_dark_skin_tone"
    man_shrugging = "man_shrugging"
    man_shrugging_tone1 = "man_shrugging_tone1"
    man_shrugging_light_skin_tone = "man_shrugging_light_skin_tone"
    man_shrugging_tone2 = "man_shrugging_tone2"
    man_shrugging_medium_light_skin_tone = "man_shrugging_medium_light_skin_tone"
    man_shrugging_tone3 = "man_shrugging_tone3"
    man_shrugging_medium_skin_tone = "man_shrugging_medium_skin_tone"
    man_shrugging_tone4 = "man_shrugging_tone4"
    man_shrugging_medium_dark_skin_tone = "man_shrugging_medium_dark_skin_tone"
    man_shrugging_tone5 = "man_shrugging_tone5"
    man_shrugging_dark_skin_tone = "man_shrugging_dark_skin_tone"
    person_pouting = "person_pouting"
    person_with_pouting_face = "person_with_pouting_face"
    person_pouting_tone1 = "person_pouting_tone1"
    person_with_pouting_face_tone1 = "person_with_pouting_face_tone1"
    person_pouting_tone2 = "person_pouting_tone2"
    person_with_pouting_face_tone2 = "person_with_pouting_face_tone2"
    person_pouting_tone3 = "person_pouting_tone3"
    person_with_pouting_face_tone3 = "person_with_pouting_face_tone3"
    person_pouting_tone4 = "person_pouting_tone4"
    person_with_pouting_face_tone4 = "person_with_pouting_face_tone4"
    person_pouting_tone5 = "person_pouting_tone5"
    person_with_pouting_face_tone5 = "person_with_pouting_face_tone5"
    woman_pouting = "woman_pouting"
    woman_pouting_tone1 = "woman_pouting_tone1"
    woman_pouting_light_skin_tone = "woman_pouting_light_skin_tone"
    woman_pouting_tone2 = "woman_pouting_tone2"
    woman_pouting_medium_light_skin_tone = "woman_pouting_medium_light_skin_tone"
    woman_pouting_tone3 = "woman_pouting_tone3"
    woman_pouting_medium_skin_tone = "woman_pouting_medium_skin_tone"
    woman_pouting_tone4 = "woman_pouting_tone4"
    woman_pouting_medium_dark_skin_tone = "woman_pouting_medium_dark_skin_tone"
    woman_pouting_tone5 = "woman_pouting_tone5"
    woman_pouting_dark_skin_tone = "woman_pouting_dark_skin_tone"
    man_pouting = "man_pouting"
    man_pouting_tone1 = "man_pouting_tone1"
    man_pouting_light_skin_tone = "man_pouting_light_skin_tone"
    man_pouting_tone2 = "man_pouting_tone2"
    man_pouting_medium_light_skin_tone = "man_pouting_medium_light_skin_tone"
    man_pouting_tone3 = "man_pouting_tone3"
    man_pouting_medium_skin_tone = "man_pouting_medium_skin_tone"
    man_pouting_tone4 = "man_pouting_tone4"
    man_pouting_medium_dark_skin_tone = "man_pouting_medium_dark_skin_tone"
    man_pouting_tone5 = "man_pouting_tone5"
    man_pouting_dark_skin_tone = "man_pouting_dark_skin_tone"
    person_frowning = "person_frowning"
    person_frowning_tone1 = "person_frowning_tone1"
    person_frowning_tone2 = "person_frowning_tone2"
    person_frowning_tone3 = "person_frowning_tone3"
    person_frowning_tone4 = "person_frowning_tone4"
    person_frowning_tone5 = "person_frowning_tone5"
    woman_frowning = "woman_frowning"
    woman_frowning_tone1 = "woman_frowning_tone1"
    woman_frowning_light_skin_tone = "woman_frowning_light_skin_tone"
    woman_frowning_tone2 = "woman_frowning_tone2"
    woman_frowning_medium_light_skin_tone = "woman_frowning_medium_light_skin_tone"
    woman_frowning_tone3 = "woman_frowning_tone3"
    woman_frowning_medium_skin_tone = "woman_frowning_medium_skin_tone"
    woman_frowning_tone4 = "woman_frowning_tone4"
    woman_frowning_medium_dark_skin_tone = "woman_frowning_medium_dark_skin_tone"
    woman_frowning_tone5 = "woman_frowning_tone5"
    woman_frowning_dark_skin_tone = "woman_frowning_dark_skin_tone"
    man_frowning = "man_frowning"
    man_frowning_tone1 = "man_frowning_tone1"
    man_frowning_light_skin_tone = "man_frowning_light_skin_tone"
    man_frowning_tone2 = "man_frowning_tone2"
    man_frowning_medium_light_skin_tone = "man_frowning_medium_light_skin_tone"
    man_frowning_tone3 = "man_frowning_tone3"
    man_frowning_medium_skin_tone = "man_frowning_medium_skin_tone"
    man_frowning_tone4 = "man_frowning_tone4"
    man_frowning_medium_dark_skin_tone = "man_frowning_medium_dark_skin_tone"
    man_frowning_tone5 = "man_frowning_tone5"
    man_frowning_dark_skin_tone = "man_frowning_dark_skin_tone"
    person_getting_haircut = "person_getting_haircut"
    haircut = "haircut"
    person_getting_haircut_tone1 = "person_getting_haircut_tone1"
    haircut_tone1 = "haircut_tone1"
    person_getting_haircut_tone2 = "person_getting_haircut_tone2"
    haircut_tone2 = "haircut_tone2"
    person_getting_haircut_tone3 = "person_getting_haircut_tone3"
    haircut_tone3 = "haircut_tone3"
    person_getting_haircut_tone4 = "person_getting_haircut_tone4"
    haircut_tone4 = "haircut_tone4"
    person_getting_haircut_tone5 = "person_getting_haircut_tone5"
    haircut_tone5 = "haircut_tone5"
    woman_getting_haircut = "woman_getting_haircut"
    woman_getting_haircut_tone1 = "woman_getting_haircut_tone1"
    woman_getting_haircut_light_skin_tone = "woman_getting_haircut_light_skin_tone"
    woman_getting_haircut_tone2 = "woman_getting_haircut_tone2"
    woman_getting_haircut_medium_light_skin_tone = "woman_getting_haircut_medium_light_skin_tone"
    woman_getting_haircut_tone3 = "woman_getting_haircut_tone3"
    woman_getting_haircut_medium_skin_tone = "woman_getting_haircut_medium_skin_tone"
    woman_getting_haircut_tone4 = "woman_getting_haircut_tone4"
    woman_getting_haircut_medium_dark_skin_tone = "woman_getting_haircut_medium_dark_skin_tone"
    woman_getting_haircut_tone5 = "woman_getting_haircut_tone5"
    woman_getting_haircut_dark_skin_tone = "woman_getting_haircut_dark_skin_tone"
    man_getting_haircut = "man_getting_haircut"
    man_getting_haircut_tone1 = "man_getting_haircut_tone1"
    man_getting_haircut_light_skin_tone = "man_getting_haircut_light_skin_tone"
    man_getting_haircut_tone2 = "man_getting_haircut_tone2"
    man_getting_haircut_medium_light_skin_tone = "man_getting_haircut_medium_light_skin_tone"
    man_getting_haircut_tone3 = "man_getting_haircut_tone3"
    man_getting_haircut_medium_skin_tone = "man_getting_haircut_medium_skin_tone"
    man_getting_haircut_tone4 = "man_getting_haircut_tone4"
    man_getting_haircut_medium_dark_skin_tone = "man_getting_haircut_medium_dark_skin_tone"
    man_getting_haircut_tone5 = "man_getting_haircut_tone5"
    man_getting_haircut_dark_skin_tone = "man_getting_haircut_dark_skin_tone"
    person_getting_massage = "person_getting_massage"
    massage = "massage"
    person_getting_massage_tone1 = "person_getting_massage_tone1"
    massage_tone1 = "massage_tone1"
    person_getting_massage_tone2 = "person_getting_massage_tone2"
    massage_tone2 = "massage_tone2"
    person_getting_massage_tone3 = "person_getting_massage_tone3"
    massage_tone3 = "massage_tone3"
    person_getting_massage_tone4 = "person_getting_massage_tone4"
    massage_tone4 = "massage_tone4"
    person_getting_massage_tone5 = "person_getting_massage_tone5"
    massage_tone5 = "massage_tone5"
    woman_getting_face_massage = "woman_getting_face_massage"
    woman_getting_face_massage_tone1 = "woman_getting_face_massage_tone1"
    woman_getting_face_massage_light_skin_tone = "woman_getting_face_massage_light_skin_tone"
    woman_getting_face_massage_tone2 = "woman_getting_face_massage_tone2"
    woman_getting_face_massage_medium_light_skin_tone = "woman_getting_face_massage_medium_light_skin_tone"
    woman_getting_face_massage_tone3 = "woman_getting_face_massage_tone3"
    woman_getting_face_massage_medium_skin_tone = "woman_getting_face_massage_medium_skin_tone"
    woman_getting_face_massage_tone4 = "woman_getting_face_massage_tone4"
    woman_getting_face_massage_medium_dark_skin_tone = "woman_getting_face_massage_medium_dark_skin_tone"
    woman_getting_face_massage_tone5 = "woman_getting_face_massage_tone5"
    woman_getting_face_massage_dark_skin_tone = "woman_getting_face_massage_dark_skin_tone"
    man_getting_face_massage = "man_getting_face_massage"
    man_getting_face_massage_tone1 = "man_getting_face_massage_tone1"
    man_getting_face_massage_light_skin_tone = "man_getting_face_massage_light_skin_tone"
    man_getting_face_massage_tone2 = "man_getting_face_massage_tone2"
    man_getting_face_massage_medium_light_skin_tone = "man_getting_face_massage_medium_light_skin_tone"
    man_getting_face_massage_tone3 = "man_getting_face_massage_tone3"
    man_getting_face_massage_medium_skin_tone = "man_getting_face_massage_medium_skin_tone"
    man_getting_face_massage_tone4 = "man_getting_face_massage_tone4"
    man_getting_face_massage_medium_dark_skin_tone = "man_getting_face_massage_medium_dark_skin_tone"
    man_getting_face_massage_tone5 = "man_getting_face_massage_tone5"
    man_getting_face_massage_dark_skin_tone = "man_getting_face_massage_dark_skin_tone"
    person_in_steamy_room = "person_in_steamy_room"
    person_in_steamy_room_tone1 = "person_in_steamy_room_tone1"
    person_in_steamy_room_light_skin_tone = "person_in_steamy_room_light_skin_tone"
    person_in_steamy_room_tone2 = "person_in_steamy_room_tone2"
    person_in_steamy_room_medium_light_skin_tone = "person_in_steamy_room_medium_light_skin_tone"
    person_in_steamy_room_tone3 = "person_in_steamy_room_tone3"
    person_in_steamy_room_medium_skin_tone = "person_in_steamy_room_medium_skin_tone"
    person_in_steamy_room_tone4 = "person_in_steamy_room_tone4"
    person_in_steamy_room_medium_dark_skin_tone = "person_in_steamy_room_medium_dark_skin_tone"
    person_in_steamy_room_tone5 = "person_in_steamy_room_tone5"
    person_in_steamy_room_dark_skin_tone = "person_in_steamy_room_dark_skin_tone"
    woman_in_steamy_room = "woman_in_steamy_room"
    woman_in_steamy_room_tone1 = "woman_in_steamy_room_tone1"
    woman_in_steamy_room_light_skin_tone = "woman_in_steamy_room_light_skin_tone"
    woman_in_steamy_room_tone2 = "woman_in_steamy_room_tone2"
    woman_in_steamy_room_medium_light_skin_tone = "woman_in_steamy_room_medium_light_skin_tone"
    woman_in_steamy_room_tone3 = "woman_in_steamy_room_tone3"
    woman_in_steamy_room_medium_skin_tone = "woman_in_steamy_room_medium_skin_tone"
    woman_in_steamy_room_tone4 = "woman_in_steamy_room_tone4"
    woman_in_steamy_room_medium_dark_skin_tone = "woman_in_steamy_room_medium_dark_skin_tone"
    woman_in_steamy_room_tone5 = "woman_in_steamy_room_tone5"
    woman_in_steamy_room_dark_skin_tone = "woman_in_steamy_room_dark_skin_tone"
    man_in_steamy_room = "man_in_steamy_room"
    man_in_steamy_room_tone1 = "man_in_steamy_room_tone1"
    man_in_steamy_room_light_skin_tone = "man_in_steamy_room_light_skin_tone"
    man_in_steamy_room_tone2 = "man_in_steamy_room_tone2"
    man_in_steamy_room_medium_light_skin_tone = "man_in_steamy_room_medium_light_skin_tone"
    man_in_steamy_room_tone3 = "man_in_steamy_room_tone3"
    man_in_steamy_room_medium_skin_tone = "man_in_steamy_room_medium_skin_tone"
    man_in_steamy_room_tone4 = "man_in_steamy_room_tone4"
    man_in_steamy_room_medium_dark_skin_tone = "man_in_steamy_room_medium_dark_skin_tone"
    man_in_steamy_room_tone5 = "man_in_steamy_room_tone5"
    man_in_steamy_room_dark_skin_tone = "man_in_steamy_room_dark_skin_tone"
    nail_care = "nail_care"
    nail_care_tone1 = "nail_care_tone1"
    nail_care_tone2 = "nail_care_tone2"
    nail_care_tone3 = "nail_care_tone3"
    nail_care_tone4 = "nail_care_tone4"
    nail_care_tone5 = "nail_care_tone5"
    selfie = "selfie"
    selfie_tone1 = "selfie_tone1"
    selfie_tone2 = "selfie_tone2"
    selfie_tone3 = "selfie_tone3"
    selfie_tone4 = "selfie_tone4"
    selfie_tone5 = "selfie_tone5"
    dancer = "dancer"
    dancer_tone1 = "dancer_tone1"
    dancer_tone2 = "dancer_tone2"
    dancer_tone3 = "dancer_tone3"
    dancer_tone4 = "dancer_tone4"
    dancer_tone5 = "dancer_tone5"
    man_dancing = "man_dancing"
    male_dancer = "male_dancer"
    man_dancing_tone1 = "man_dancing_tone1"
    male_dancer_tone1 = "male_dancer_tone1"
    man_dancing_tone2 = "man_dancing_tone2"
    male_dancer_tone2 = "male_dancer_tone2"
    man_dancing_tone3 = "man_dancing_tone3"
    male_dancer_tone3 = "male_dancer_tone3"
    man_dancing_tone5 = "man_dancing_tone5"
    male_dancer_tone5 = "male_dancer_tone5"
    man_dancing_tone4 = "man_dancing_tone4"
    male_dancer_tone4 = "male_dancer_tone4"
    people_with_bunny_ears_partying = "people_with_bunny_ears_partying"
    dancers = "dancers"
    women_with_bunny_ears_partying = "women_with_bunny_ears_partying"
    men_with_bunny_ears_partying = "men_with_bunny_ears_partying"
    levitate = "levitate"
    man_in_business_suit_levitating = "man_in_business_suit_levitating"
    levitate_tone1 = "levitate_tone1"
    man_in_business_suit_levitating_tone1 = "man_in_business_suit_levitating_tone1"
    man_in_business_suit_levitating_light_skin_tone = "man_in_business_suit_levitating_light_skin_tone"
    levitate_tone2 = "levitate_tone2"
    man_in_business_suit_levitating_tone2 = "man_in_business_suit_levitating_tone2"
    man_in_business_suit_levitating_medium_light_skin_tone = "man_in_business_suit_levitating_medium_light_skin_tone"
    levitate_tone3 = "levitate_tone3"
    man_in_business_suit_levitating_tone3 = "man_in_business_suit_levitating_tone3"
    man_in_business_suit_levitating_medium_skin_tone = "man_in_business_suit_levitating_medium_skin_tone"
    levitate_tone4 = "levitate_tone4"
    man_in_business_suit_levitating_tone4 = "man_in_business_suit_levitating_tone4"
    man_in_business_suit_levitating_medium_dark_skin_tone = "man_in_business_suit_levitating_medium_dark_skin_tone"
    levitate_tone5 = "levitate_tone5"
    man_in_business_suit_levitating_tone5 = "man_in_business_suit_levitating_tone5"
    man_in_business_suit_levitating_dark_skin_tone = "man_in_business_suit_levitating_dark_skin_tone"
    person_walking = "person_walking"
    walking = "walking"
    person_walking_tone1 = "person_walking_tone1"
    walking_tone1 = "walking_tone1"
    person_walking_tone2 = "person_walking_tone2"
    walking_tone2 = "walking_tone2"
    person_walking_tone3 = "person_walking_tone3"
    walking_tone3 = "walking_tone3"
    person_walking_tone4 = "person_walking_tone4"
    walking_tone4 = "walking_tone4"
    person_walking_tone5 = "person_walking_tone5"
    walking_tone5 = "walking_tone5"
    woman_walking = "woman_walking"
    woman_walking_tone1 = "woman_walking_tone1"
    woman_walking_light_skin_tone = "woman_walking_light_skin_tone"
    woman_walking_tone2 = "woman_walking_tone2"
    woman_walking_medium_light_skin_tone = "woman_walking_medium_light_skin_tone"
    woman_walking_tone3 = "woman_walking_tone3"
    woman_walking_medium_skin_tone = "woman_walking_medium_skin_tone"
    woman_walking_tone4 = "woman_walking_tone4"
    woman_walking_medium_dark_skin_tone = "woman_walking_medium_dark_skin_tone"
    woman_walking_tone5 = "woman_walking_tone5"
    woman_walking_dark_skin_tone = "woman_walking_dark_skin_tone"
    man_walking = "man_walking"
    man_walking_tone1 = "man_walking_tone1"
    man_walking_light_skin_tone = "man_walking_light_skin_tone"
    man_walking_tone2 = "man_walking_tone2"
    man_walking_medium_light_skin_tone = "man_walking_medium_light_skin_tone"
    man_walking_tone3 = "man_walking_tone3"
    man_walking_medium_skin_tone = "man_walking_medium_skin_tone"
    man_walking_tone4 = "man_walking_tone4"
    man_walking_medium_dark_skin_tone = "man_walking_medium_dark_skin_tone"
    man_walking_tone5 = "man_walking_tone5"
    man_walking_dark_skin_tone = "man_walking_dark_skin_tone"
    person_running = "person_running"
    runner = "runner"
    person_running_tone1 = "person_running_tone1"
    runner_tone1 = "runner_tone1"
    person_running_tone2 = "person_running_tone2"
    runner_tone2 = "runner_tone2"
    person_running_tone3 = "person_running_tone3"
    runner_tone3 = "runner_tone3"
    person_running_tone4 = "person_running_tone4"
    runner_tone4 = "runner_tone4"
    person_running_tone5 = "person_running_tone5"
    runner_tone5 = "runner_tone5"
    woman_running = "woman_running"
    woman_running_tone1 = "woman_running_tone1"
    woman_running_light_skin_tone = "woman_running_light_skin_tone"
    woman_running_tone2 = "woman_running_tone2"
    woman_running_medium_light_skin_tone = "woman_running_medium_light_skin_tone"
    woman_running_tone3 = "woman_running_tone3"
    woman_running_medium_skin_tone = "woman_running_medium_skin_tone"
    woman_running_tone4 = "woman_running_tone4"
    woman_running_medium_dark_skin_tone = "woman_running_medium_dark_skin_tone"
    woman_running_tone5 = "woman_running_tone5"
    woman_running_dark_skin_tone = "woman_running_dark_skin_tone"
    man_running = "man_running"
    man_running_tone1 = "man_running_tone1"
    man_running_light_skin_tone = "man_running_light_skin_tone"
    man_running_tone2 = "man_running_tone2"
    man_running_medium_light_skin_tone = "man_running_medium_light_skin_tone"
    man_running_tone3 = "man_running_tone3"
    man_running_medium_skin_tone = "man_running_medium_skin_tone"
    man_running_tone4 = "man_running_tone4"
    man_running_medium_dark_skin_tone = "man_running_medium_dark_skin_tone"
    man_running_tone5 = "man_running_tone5"
    man_running_dark_skin_tone = "man_running_dark_skin_tone"
    person_standing = "person_standing"
    person_standing_tone1 = "person_standing_tone1"
    person_standing_light_skin_tone = "person_standing_light_skin_tone"
    person_standing_tone2 = "person_standing_tone2"
    person_standing_medium_light_skin_tone = "person_standing_medium_light_skin_tone"
    person_standing_tone3 = "person_standing_tone3"
    person_standing_medium_skin_tone = "person_standing_medium_skin_tone"
    person_standing_tone4 = "person_standing_tone4"
    person_standing_medium_dark_skin_tone = "person_standing_medium_dark_skin_tone"
    person_standing_tone5 = "person_standing_tone5"
    person_standing_dark_skin_tone = "person_standing_dark_skin_tone"
    woman_standing = "woman_standing"
    woman_standing_tone1 = "woman_standing_tone1"
    woman_standing_light_skin_tone = "woman_standing_light_skin_tone"
    woman_standing_tone2 = "woman_standing_tone2"
    woman_standing_medium_light_skin_tone = "woman_standing_medium_light_skin_tone"
    woman_standing_tone3 = "woman_standing_tone3"
    woman_standing_medium_skin_tone = "woman_standing_medium_skin_tone"
    woman_standing_tone4 = "woman_standing_tone4"
    woman_standing_medium_dark_skin_tone = "woman_standing_medium_dark_skin_tone"
    woman_standing_tone5 = "woman_standing_tone5"
    woman_standing_dark_skin_tone = "woman_standing_dark_skin_tone"
    man_standing = "man_standing"
    man_standing_tone1 = "man_standing_tone1"
    man_standing_light_skin_tone = "man_standing_light_skin_tone"
    man_standing_tone2 = "man_standing_tone2"
    man_standing_medium_light_skin_tone = "man_standing_medium_light_skin_tone"
    man_standing_tone3 = "man_standing_tone3"
    man_standing_medium_skin_tone = "man_standing_medium_skin_tone"
    man_standing_tone4 = "man_standing_tone4"
    man_standing_medium_dark_skin_tone = "man_standing_medium_dark_skin_tone"
    man_standing_tone5 = "man_standing_tone5"
    man_standing_dark_skin_tone = "man_standing_dark_skin_tone"
    person_kneeling = "person_kneeling"
    person_kneeling_tone1 = "person_kneeling_tone1"
    person_kneeling_light_skin_tone = "person_kneeling_light_skin_tone"
    person_kneeling_tone2 = "person_kneeling_tone2"
    person_kneeling_medium_light_skin_tone = "person_kneeling_medium_light_skin_tone"
    person_kneeling_tone3 = "person_kneeling_tone3"
    person_kneeling_medium_skin_tone = "person_kneeling_medium_skin_tone"
    person_kneeling_tone4 = "person_kneeling_tone4"
    person_kneeling_medium_dark_skin_tone = "person_kneeling_medium_dark_skin_tone"
    person_kneeling_tone5 = "person_kneeling_tone5"
    person_kneeling_dark_skin_tone = "person_kneeling_dark_skin_tone"
    woman_kneeling = "woman_kneeling"
    woman_kneeling_tone1 = "woman_kneeling_tone1"
    woman_kneeling_light_skin_tone = "woman_kneeling_light_skin_tone"
    woman_kneeling_tone2 = "woman_kneeling_tone2"
    woman_kneeling_medium_light_skin_tone = "woman_kneeling_medium_light_skin_tone"
    woman_kneeling_tone3 = "woman_kneeling_tone3"
    woman_kneeling_medium_skin_tone = "woman_kneeling_medium_skin_tone"
    woman_kneeling_tone4 = "woman_kneeling_tone4"
    woman_kneeling_medium_dark_skin_tone = "woman_kneeling_medium_dark_skin_tone"
    woman_kneeling_tone5 = "woman_kneeling_tone5"
    woman_kneeling_dark_skin_tone = "woman_kneeling_dark_skin_tone"
    man_kneeling = "man_kneeling"
    man_kneeling_tone1 = "man_kneeling_tone1"
    man_kneeling_light_skin_tone = "man_kneeling_light_skin_tone"
    man_kneeling_tone2 = "man_kneeling_tone2"
    man_kneeling_medium_light_skin_tone = "man_kneeling_medium_light_skin_tone"
    man_kneeling_tone3 = "man_kneeling_tone3"
    man_kneeling_medium_skin_tone = "man_kneeling_medium_skin_tone"
    man_kneeling_tone4 = "man_kneeling_tone4"
    man_kneeling_medium_dark_skin_tone = "man_kneeling_medium_dark_skin_tone"
    man_kneeling_tone5 = "man_kneeling_tone5"
    man_kneeling_dark_skin_tone = "man_kneeling_dark_skin_tone"
    woman_with_probing_cane = "woman_with_probing_cane"
    woman_with_probing_cane_tone1 = "woman_with_probing_cane_tone1"
    woman_with_probing_cane_light_skin_tone = "woman_with_probing_cane_light_skin_tone"
    woman_with_probing_cane_tone2 = "woman_with_probing_cane_tone2"
    woman_with_probing_cane_medium_light_skin_tone = "woman_with_probing_cane_medium_light_skin_tone"
    woman_with_probing_cane_tone3 = "woman_with_probing_cane_tone3"
    woman_with_probing_cane_medium_skin_tone = "woman_with_probing_cane_medium_skin_tone"
    woman_with_probing_cane_tone4 = "woman_with_probing_cane_tone4"
    woman_with_probing_cane_medium_dark_skin_tone = "woman_with_probing_cane_medium_dark_skin_tone"
    woman_with_probing_cane_tone5 = "woman_with_probing_cane_tone5"
    woman_with_probing_cane_dark_skin_tone = "woman_with_probing_cane_dark_skin_tone"
    man_with_probing_cane = "man_with_probing_cane"
    man_with_probing_cane_tone1 = "man_with_probing_cane_tone1"
    man_with_probing_cane_light_skin_tone = "man_with_probing_cane_light_skin_tone"
    man_with_probing_cane_tone2 = "man_with_probing_cane_tone2"
    man_with_probing_cane_medium_light_skin_tone = "man_with_probing_cane_medium_light_skin_tone"
    man_with_probing_cane_tone3 = "man_with_probing_cane_tone3"
    man_with_probing_cane_medium_skin_tone = "man_with_probing_cane_medium_skin_tone"
    man_with_probing_cane_tone4 = "man_with_probing_cane_tone4"
    man_with_probing_cane_medium_dark_skin_tone = "man_with_probing_cane_medium_dark_skin_tone"
    man_with_probing_cane_tone5 = "man_with_probing_cane_tone5"
    man_with_probing_cane_dark_skin_tone = "man_with_probing_cane_dark_skin_tone"
    woman_in_motorized_wheelchair = "woman_in_motorized_wheelchair"
    woman_in_motorized_wheelchair_tone1 = "woman_in_motorized_wheelchair_tone1"
    woman_in_motorized_wheelchair_light_skin_tone = "woman_in_motorized_wheelchair_light_skin_tone"
    woman_in_motorized_wheelchair_tone2 = "woman_in_motorized_wheelchair_tone2"
    woman_in_motorized_wheelchair_medium_light_skin_tone = "woman_in_motorized_wheelchair_medium_light_skin_tone"
    woman_in_motorized_wheelchair_tone3 = "woman_in_motorized_wheelchair_tone3"
    woman_in_motorized_wheelchair_medium_skin_tone = "woman_in_motorized_wheelchair_medium_skin_tone"
    woman_in_motorized_wheelchair_tone4 = "woman_in_motorized_wheelchair_tone4"
    woman_in_motorized_wheelchair_medium_dark_skin_tone = "woman_in_motorized_wheelchair_medium_dark_skin_tone"
    woman_in_motorized_wheelchair_tone5 = "woman_in_motorized_wheelchair_tone5"
    woman_in_motorized_wheelchair_dark_skin_tone = "woman_in_motorized_wheelchair_dark_skin_tone"
    man_in_motorized_wheelchair = "man_in_motorized_wheelchair"
    man_in_motorized_wheelchair_tone1 = "man_in_motorized_wheelchair_tone1"
    man_in_motorized_wheelchair_light_skin_tone = "man_in_motorized_wheelchair_light_skin_tone"
    man_in_motorized_wheelchair_tone2 = "man_in_motorized_wheelchair_tone2"
    man_in_motorized_wheelchair_medium_light_skin_tone = "man_in_motorized_wheelchair_medium_light_skin_tone"
    man_in_motorized_wheelchair_tone3 = "man_in_motorized_wheelchair_tone3"
    man_in_motorized_wheelchair_medium_skin_tone = "man_in_motorized_wheelchair_medium_skin_tone"
    man_in_motorized_wheelchair_tone4 = "man_in_motorized_wheelchair_tone4"
    man_in_motorized_wheelchair_medium_dark_skin_tone = "man_in_motorized_wheelchair_medium_dark_skin_tone"
    man_in_motorized_wheelchair_tone5 = "man_in_motorized_wheelchair_tone5"
    man_in_motorized_wheelchair_dark_skin_tone = "man_in_motorized_wheelchair_dark_skin_tone"
    woman_in_manual_wheelchair = "woman_in_manual_wheelchair"
    woman_in_manual_wheelchair_tone1 = "woman_in_manual_wheelchair_tone1"
    woman_in_manual_wheelchair_light_skin_tone = "woman_in_manual_wheelchair_light_skin_tone"
    woman_in_manual_wheelchair_tone2 = "woman_in_manual_wheelchair_tone2"
    woman_in_manual_wheelchair_medium_light_skin_tone = "woman_in_manual_wheelchair_medium_light_skin_tone"
    woman_in_manual_wheelchair_tone3 = "woman_in_manual_wheelchair_tone3"
    woman_in_manual_wheelchair_medium_skin_tone = "woman_in_manual_wheelchair_medium_skin_tone"
    woman_in_manual_wheelchair_tone4 = "woman_in_manual_wheelchair_tone4"
    woman_in_manual_wheelchair_medium_dark_skin_tone = "woman_in_manual_wheelchair_medium_dark_skin_tone"
    woman_in_manual_wheelchair_tone5 = "woman_in_manual_wheelchair_tone5"
    woman_in_manual_wheelchair_dark_skin_tone = "woman_in_manual_wheelchair_dark_skin_tone"
    man_in_manual_wheelchair = "man_in_manual_wheelchair"
    man_in_manual_wheelchair_tone1 = "man_in_manual_wheelchair_tone1"
    man_in_manual_wheelchair_light_skin_tone = "man_in_manual_wheelchair_light_skin_tone"
    man_in_manual_wheelchair_tone2 = "man_in_manual_wheelchair_tone2"
    man_in_manual_wheelchair_medium_light_skin_tone = "man_in_manual_wheelchair_medium_light_skin_tone"
    man_in_manual_wheelchair_tone3 = "man_in_manual_wheelchair_tone3"
    man_in_manual_wheelchair_medium_skin_tone = "man_in_manual_wheelchair_medium_skin_tone"
    man_in_manual_wheelchair_tone4 = "man_in_manual_wheelchair_tone4"
    man_in_manual_wheelchair_medium_dark_skin_tone = "man_in_manual_wheelchair_medium_dark_skin_tone"
    man_in_manual_wheelchair_tone5 = "man_in_manual_wheelchair_tone5"
    man_in_manual_wheelchair_dark_skin_tone = "man_in_manual_wheelchair_dark_skin_tone"
    people_holding_hands = "people_holding_hands"
    couple = "couple"
    two_women_holding_hands = "two_women_holding_hands"
    two_men_holding_hands = "two_men_holding_hands"
    couple_with_heart = "couple_with_heart"
    couple_with_heart_woman_man = "couple_with_heart_woman_man"
    couple_ww = "couple_ww"
    couple_with_heart_ww = "couple_with_heart_ww"
    couple_mm = "couple_mm"
    couple_with_heart_mm = "couple_with_heart_mm"
    couplekiss = "couplekiss"
    kiss_woman_man = "kiss_woman_man"
    kiss_ww = "kiss_ww"
    couplekiss_ww = "couplekiss_ww"
    kiss_mm = "kiss_mm"
    couplekiss_mm = "couplekiss_mm"
    family = "family"
    family_man_woman_boy = "family_man_woman_boy"
    family_mwg = "family_mwg"
    family_mwgb = "family_mwgb"
    family_mwbb = "family_mwbb"
    family_mwgg = "family_mwgg"
    family_wwb = "family_wwb"
    family_wwg = "family_wwg"
    family_wwgb = "family_wwgb"
    family_wwbb = "family_wwbb"
    family_wwgg = "family_wwgg"
    family_mmb = "family_mmb"
    family_mmg = "family_mmg"
    family_mmgb = "family_mmgb"
    family_mmbb = "family_mmbb"
    family_mmgg = "family_mmgg"
    family_woman_boy = "family_woman_boy"
    family_woman_girl = "family_woman_girl"
    family_woman_girl_boy = "family_woman_girl_boy"
    family_woman_boy_boy = "family_woman_boy_boy"
    family_woman_girl_girl = "family_woman_girl_girl"
    family_man_boy = "family_man_boy"
    family_man_girl = "family_man_girl"
    family_man_girl_boy = "family_man_girl_boy"
    family_man_boy_boy = "family_man_boy_boy"
    family_man_girl_girl = "family_man_girl_girl"
    yarn = "yarn"
    thread = "thread"
    coat = "coat"
    lab_coat = "lab_coat"
    safety_vest = "safety_vest"
    womans_clothes = "womans_clothes"
    shirt = "shirt"
    jeans = "jeans"
    shorts = "shorts"
    necktie = "necktie"
    dress = "dress"
    bikini = "bikini"
    one_piece_swimsuit = "one_piece_swimsuit"
    kimono = "kimono"
    sari = "sari"
    womans_flat_shoe = "womans_flat_shoe"
    high_heel = "high_heel"
    sandal = "sandal"
    boot = "boot"
    ballet_shoes = "ballet_shoes"
    mans_shoe = "mans_shoe"
    athletic_shoe = "athletic_shoe"
    hiking_boot = "hiking_boot"
    briefs = "briefs"
    socks = "socks"
    gloves = "gloves"
    scarf = "scarf"
    tophat = "tophat"
    billed_cap = "billed_cap"
    womans_hat = "womans_hat"
    mortar_board = "mortar_board"
    helmet_with_cross = "helmet_with_cross"
    helmet_with_white_cross = "helmet_with_white_cross"
    crown = "crown"
    ring = "ring"
    pouch = "pouch"
    purse = "purse"
    handbag = "handbag"
    briefcase = "briefcase"
    school_satchel = "school_satchel"
    luggage = "luggage"
    eyeglasses = "eyeglasses"
    dark_sunglasses = "dark_sunglasses"
    goggles = "goggles"
    diving_mask = "diving_mask"
    closed_umbrella = "closed_umbrella"
    dog = "dog"
    cat = "cat"
    mouse = "mouse"
    hamster = "hamster"
    rabbit = "rabbit"
    fox = "fox"
    fox_face = "fox_face"
    bear = "bear"
    panda_face = "panda_face"
    koala = "koala"
    tiger = "tiger"
    lion_face = "lion_face"
    lion = "lion"
    cow = "cow"
    pig = "pig"
    pig_nose = "pig_nose"
    frog = "frog"
    monkey_face = "monkey_face"
    see_no_evil = "see_no_evil"
    hear_no_evil = "hear_no_evil"
    speak_no_evil = "speak_no_evil"
    monkey = "monkey"
    chicken = "chicken"
    penguin = "penguin"
    bird = "bird"
    baby_chick = "baby_chick"
    hatching_chick = "hatching_chick"
    hatched_chick = "hatched_chick"
    duck = "duck"
    eagle = "eagle"
    owl = "owl"
    bat = "bat"
    wolf = "wolf"
    boar = "boar"
    horse = "horse"
    unicorn = "unicorn"
    unicorn_face = "unicorn_face"
    bee = "bee"
    bug = "bug"
    butterfly = "butterfly"
    snail = "snail"
    shell = "shell"
    beetle = "beetle"
    ant = "ant"
    mosquito = "mosquito"
    cricket = "cricket"
    spider = "spider"
    spider_web = "spider_web"
    scorpion = "scorpion"
    turtle = "turtle"
    snake = "snake"
    lizard = "lizard"
    t_rex = "t_rex"
    sauropod = "sauropod"
    octopus = "octopus"
    squid = "squid"
    shrimp = "shrimp"
    lobster = "lobster"
    oyster = "oyster"
    crab = "crab"
    blowfish = "blowfish"
    tropical_fish = "tropical_fish"
    fish = "fish"
    dolphin = "dolphin"
    whale = "whale"
    whale2 = "whale2"
    shark = "shark"
    crocodile = "crocodile"
    tiger2 = "tiger2"
    leopard = "leopard"
    zebra = "zebra"
    gorilla = "gorilla"
    orangutan = "orangutan"
    elephant = "elephant"
    hippopotamus = "hippopotamus"
    rhino = "rhino"
    rhinoceros = "rhinoceros"
    dromedary_camel = "dromedary_camel"
    camel = "camel"
    giraffe = "giraffe"
    kangaroo = "kangaroo"
    water_buffalo = "water_buffalo"
    ox = "ox"
    cow2 = "cow2"
    racehorse = "racehorse"
    pig2 = "pig2"
    ram = "ram"
    llama = "llama"
    sheep = "sheep"
    goat = "goat"
    deer = "deer"
    dog2 = "dog2"
    guide_dog = "guide_dog"
    service_dog = "service_dog"
    poodle = "poodle"
    cat2 = "cat2"
    rooster = "rooster"
    turkey = "turkey"
    peacock = "peacock"
    parrot = "parrot"
    swan = "swan"
    flamingo = "flamingo"
    dove = "dove"
    dove_of_peace = "dove_of_peace"
    rabbit2 = "rabbit2"
    sloth = "sloth"
    otter = "otter"
    skunk = "skunk"
    raccoon = "raccoon"
    badger = "badger"
    mouse2 = "mouse2"
    rat = "rat"
    chipmunk = "chipmunk"
    hedgehog = "hedgehog"
    feet = "feet"
    paw_prints = "paw_prints"
    dragon = "dragon"
    dragon_face = "dragon_face"
    cactus = "cactus"
    christmas_tree = "christmas_tree"
    evergreen_tree = "evergreen_tree"
    deciduous_tree = "deciduous_tree"
    palm_tree = "palm_tree"
    seedling = "seedling"
    herb = "herb"
    shamrock = "shamrock"
    four_leaf_clover = "four_leaf_clover"
    bamboo = "bamboo"
    tanabata_tree = "tanabata_tree"
    leaves = "leaves"
    fallen_leaf = "fallen_leaf"
    maple_leaf = "maple_leaf"
    mushroom = "mushroom"
    ear_of_rice = "ear_of_rice"
    bouquet = "bouquet"
    tulip = "tulip"
    rose = "rose"
    wilted_rose = "wilted_rose"
    wilted_flower = "wilted_flower"
    hibiscus = "hibiscus"
    cherry_blossom = "cherry_blossom"
    blossom = "blossom"
    sunflower = "sunflower"
    sun_with_face = "sun_with_face"
    full_moon_with_face = "full_moon_with_face"
    first_quarter_moon_with_face = "first_quarter_moon_with_face"
    last_quarter_moon_with_face = "last_quarter_moon_with_face"
    new_moon_with_face = "new_moon_with_face"
    full_moon = "full_moon"
    waning_gibbous_moon = "waning_gibbous_moon"
    last_quarter_moon = "last_quarter_moon"
    waning_crescent_moon = "waning_crescent_moon"
    new_moon = "new_moon"
    waxing_crescent_moon = "waxing_crescent_moon"
    first_quarter_moon = "first_quarter_moon"
    waxing_gibbous_moon = "waxing_gibbous_moon"
    crescent_moon = "crescent_moon"
    earth_americas = "earth_americas"
    earth_africa = "earth_africa"
    earth_asia = "earth_asia"
    ringed_planet = "ringed_planet"
    dizzy = "dizzy"
    star = "star"
    star2 = "star2"
    sparkles = "sparkles"
    zap = "zap"
    comet = "comet"
    boom = "boom"
    fire = "fire"
    flame = "flame"
    cloud_tornado = "cloud_tornado"
    cloud_with_tornado = "cloud_with_tornado"
    rainbow = "rainbow"
    sunny = "sunny"
    white_sun_small_cloud = "white_sun_small_cloud"
    white_sun_with_small_cloud = "white_sun_with_small_cloud"
    partly_sunny = "partly_sunny"
    white_sun_cloud = "white_sun_cloud"
    white_sun_behind_cloud = "white_sun_behind_cloud"
    cloud = "cloud"
    white_sun_rain_cloud = "white_sun_rain_cloud"
    white_sun_behind_cloud_with_rain = "white_sun_behind_cloud_with_rain"
    cloud_rain = "cloud_rain"
    cloud_with_rain = "cloud_with_rain"
    thunder_cloud_rain = "thunder_cloud_rain"
    thunder_cloud_and_rain = "thunder_cloud_and_rain"
    cloud_lightning = "cloud_lightning"
    cloud_with_lightning = "cloud_with_lightning"
    cloud_snow = "cloud_snow"
    cloud_with_snow = "cloud_with_snow"
    snowflake = "snowflake"
    snowman2 = "snowman2"
    snowman = "snowman"
    wind_blowing_face = "wind_blowing_face"
    dash = "dash"
    droplet = "droplet"
    sweat_drops = "sweat_drops"
    umbrella = "umbrella"
    umbrella2 = "umbrella2"
    ocean = "ocean"
    fog = "fog"
    green_apple = "green_apple"
    apple = "apple"
    pear = "pear"
    tangerine = "tangerine"
    lemon = "lemon"
    banana = "banana"
    watermelon = "watermelon"
    grapes = "grapes"
    strawberry = "strawberry"
    melon = "melon"
    cherries = "cherries"
    peach = "peach"
    mango = "mango"
    pineapple = "pineapple"
    coconut = "coconut"
    kiwi = "kiwi"
    kiwifruit = "kiwifruit"
    tomato = "tomato"
    eggplant = "eggplant"
    avocado = "avocado"
    broccoli = "broccoli"
    leafy_green = "leafy_green"
    cucumber = "cucumber"
    hot_pepper = "hot_pepper"
    corn = "corn"
    carrot = "carrot"
    onion = "onion"
    garlic = "garlic"
    potato = "potato"
    sweet_potato = "sweet_potato"
    croissant = "croissant"
    bagel = "bagel"
    bread = "bread"
    french_bread = "french_bread"
    baguette_bread = "baguette_bread"
    pretzel = "pretzel"
    cheese = "cheese"
    cheese_wedge = "cheese_wedge"
    egg = "egg"
    cooking = "cooking"
    pancakes = "pancakes"
    waffle = "waffle"
    bacon = "bacon"
    cut_of_meat = "cut_of_meat"
    poultry_leg = "poultry_leg"
    meat_on_bone = "meat_on_bone"
    hotdog = "hotdog"
    hot_dog = "hot_dog"
    hamburger = "hamburger"
    fries = "fries"
    pizza = "pizza"
    sandwich = "sandwich"
    falafel = "falafel"
    stuffed_flatbread = "stuffed_flatbread"
    stuffed_pita = "stuffed_pita"
    taco = "taco"
    burrito = "burrito"
    salad = "salad"
    green_salad = "green_salad"
    shallow_pan_of_food = "shallow_pan_of_food"
    paella = "paella"
    canned_food = "canned_food"
    spaghetti = "spaghetti"
    ramen = "ramen"
    stew = "stew"
    curry = "curry"
    sushi = "sushi"
    bento = "bento"
    dumpling = "dumpling"
    fried_shrimp = "fried_shrimp"
    rice_ball = "rice_ball"
    rice = "rice"
    rice_cracker = "rice_cracker"
    fish_cake = "fish_cake"
    fortune_cookie = "fortune_cookie"
    moon_cake = "moon_cake"
    oden = "oden"
    dango = "dango"
    shaved_ice = "shaved_ice"
    ice_cream = "ice_cream"
    icecream = "icecream"
    pie = "pie"
    cupcake = "cupcake"
    cake = "cake"
    birthday = "birthday"
    custard = "custard"
    pudding = "pudding"
    flan = "flan"
    lollipop = "lollipop"
    candy = "candy"
    chocolate_bar = "chocolate_bar"
    popcorn = "popcorn"
    doughnut = "doughnut"
    cookie = "cookie"
    chestnut = "chestnut"
    peanuts = "peanuts"
    shelled_peanut = "shelled_peanut"
    honey_pot = "honey_pot"
    butter = "butter"
    milk = "milk"
    glass_of_milk = "glass_of_milk"
    baby_bottle = "baby_bottle"
    coffee = "coffee"
    tea = "tea"
    mate = "mate"
    cup_with_straw = "cup_with_straw"
    beverage_box = "beverage_box"
    ice_cube = "ice_cube"
    sake = "sake"
    beer = "beer"
    beers = "beers"
    champagne_glass = "champagne_glass"
    clinking_glass = "clinking_glass"
    wine_glass = "wine_glass"
    tumbler_glass = "tumbler_glass"
    whisky = "whisky"
    cocktail = "cocktail"
    tropical_drink = "tropical_drink"
    champagne = "champagne"
    bottle_with_popping_cork = "bottle_with_popping_cork"
    spoon = "spoon"
    fork_and_knife = "fork_and_knife"
    fork_knife_plate = "fork_knife_plate"
    fork_and_knife_with_plate = "fork_and_knife_with_plate"
    bowl_with_spoon = "bowl_with_spoon"
    takeout_box = "takeout_box"
    chopsticks = "chopsticks"
    salt = "salt"
    soccer = "soccer"
    basketball = "basketball"
    football = "football"
    baseball = "baseball"
    softball = "softball"
    tennis = "tennis"
    volleyball = "volleyball"
    rugby_football = "rugby_football"
    flying_disc = "flying_disc"
    eight_ball = "8ball"
    ping_pong = "ping_pong"
    table_tennis = "table_tennis"
    badminton = "badminton"
    hockey = "hockey"
    field_hockey = "field_hockey"
    lacrosse = "lacrosse"
    cricket_game = "cricket_game"
    cricket_bat_ball = "cricket_bat_ball"
    goal = "goal"
    goal_net = "goal_net"
    golf = "golf"
    bow_and_arrow = "bow_and_arrow"
    archery = "archery"
    fishing_pole_and_fish = "fishing_pole_and_fish"
    boxing_glove = "boxing_glove"
    boxing_gloves = "boxing_gloves"
    martial_arts_uniform = "martial_arts_uniform"
    karate_uniform = "karate_uniform"
    running_shirt_with_sash = "running_shirt_with_sash"
    skateboard = "skateboard"
    sled = "sled"
    parachute = "parachute"
    ice_skate = "ice_skate"
    curling_stone = "curling_stone"
    ski = "ski"
    skier = "skier"
    snowboarder = "snowboarder"
    snowboarder_tone1 = "snowboarder_tone1"
    snowboarder_light_skin_tone = "snowboarder_light_skin_tone"
    snowboarder_tone2 = "snowboarder_tone2"
    snowboarder_medium_light_skin_tone = "snowboarder_medium_light_skin_tone"
    snowboarder_tone3 = "snowboarder_tone3"
    snowboarder_medium_skin_tone = "snowboarder_medium_skin_tone"
    snowboarder_tone4 = "snowboarder_tone4"
    snowboarder_medium_dark_skin_tone = "snowboarder_medium_dark_skin_tone"
    snowboarder_tone5 = "snowboarder_tone5"
    snowboarder_dark_skin_tone = "snowboarder_dark_skin_tone"
    person_lifting_weights = "person_lifting_weights"
    lifter = "lifter"
    weight_lifter = "weight_lifter"
    person_lifting_weights_tone1 = "person_lifting_weights_tone1"
    lifter_tone1 = "lifter_tone1"
    weight_lifter_tone1 = "weight_lifter_tone1"
    person_lifting_weights_tone2 = "person_lifting_weights_tone2"
    lifter_tone2 = "lifter_tone2"
    weight_lifter_tone2 = "weight_lifter_tone2"
    person_lifting_weights_tone3 = "person_lifting_weights_tone3"
    lifter_tone3 = "lifter_tone3"
    weight_lifter_tone3 = "weight_lifter_tone3"
    person_lifting_weights_tone4 = "person_lifting_weights_tone4"
    lifter_tone4 = "lifter_tone4"
    weight_lifter_tone4 = "weight_lifter_tone4"
    person_lifting_weights_tone5 = "person_lifting_weights_tone5"
    lifter_tone5 = "lifter_tone5"
    weight_lifter_tone5 = "weight_lifter_tone5"
    woman_lifting_weights = "woman_lifting_weights"
    woman_lifting_weights_tone1 = "woman_lifting_weights_tone1"
    woman_lifting_weights_light_skin_tone = "woman_lifting_weights_light_skin_tone"
    woman_lifting_weights_tone2 = "woman_lifting_weights_tone2"
    woman_lifting_weights_medium_light_skin_tone = "woman_lifting_weights_medium_light_skin_tone"
    woman_lifting_weights_tone3 = "woman_lifting_weights_tone3"
    woman_lifting_weights_medium_skin_tone = "woman_lifting_weights_medium_skin_tone"
    woman_lifting_weights_tone4 = "woman_lifting_weights_tone4"
    woman_lifting_weights_medium_dark_skin_tone = "woman_lifting_weights_medium_dark_skin_tone"
    woman_lifting_weights_tone5 = "woman_lifting_weights_tone5"
    woman_lifting_weights_dark_skin_tone = "woman_lifting_weights_dark_skin_tone"
    man_lifting_weights = "man_lifting_weights"
    man_lifting_weights_tone1 = "man_lifting_weights_tone1"
    man_lifting_weights_light_skin_tone = "man_lifting_weights_light_skin_tone"
    man_lifting_weights_tone2 = "man_lifting_weights_tone2"
    man_lifting_weights_medium_light_skin_tone = "man_lifting_weights_medium_light_skin_tone"
    man_lifting_weights_tone3 = "man_lifting_weights_tone3"
    man_lifting_weights_medium_skin_tone = "man_lifting_weights_medium_skin_tone"
    man_lifting_weights_tone4 = "man_lifting_weights_tone4"
    man_lifting_weights_medium_dark_skin_tone = "man_lifting_weights_medium_dark_skin_tone"
    man_lifting_weights_tone5 = "man_lifting_weights_tone5"
    man_lifting_weights_dark_skin_tone = "man_lifting_weights_dark_skin_tone"
    people_wrestling = "people_wrestling"
    wrestlers = "wrestlers"
    wrestling = "wrestling"
    women_wrestling = "women_wrestling"
    men_wrestling = "men_wrestling"
    person_doing_cartwheel = "person_doing_cartwheel"
    cartwheel = "cartwheel"
    person_doing_cartwheel_tone1 = "person_doing_cartwheel_tone1"
    cartwheel_tone1 = "cartwheel_tone1"
    person_doing_cartwheel_tone2 = "person_doing_cartwheel_tone2"
    cartwheel_tone2 = "cartwheel_tone2"
    person_doing_cartwheel_tone3 = "person_doing_cartwheel_tone3"
    cartwheel_tone3 = "cartwheel_tone3"
    person_doing_cartwheel_tone4 = "person_doing_cartwheel_tone4"
    cartwheel_tone4 = "cartwheel_tone4"
    person_doing_cartwheel_tone5 = "person_doing_cartwheel_tone5"
    cartwheel_tone5 = "cartwheel_tone5"
    woman_cartwheeling = "woman_cartwheeling"
    woman_cartwheeling_tone1 = "woman_cartwheeling_tone1"
    woman_cartwheeling_light_skin_tone = "woman_cartwheeling_light_skin_tone"
    woman_cartwheeling_tone2 = "woman_cartwheeling_tone2"
    woman_cartwheeling_medium_light_skin_tone = "woman_cartwheeling_medium_light_skin_tone"
    woman_cartwheeling_tone3 = "woman_cartwheeling_tone3"
    woman_cartwheeling_medium_skin_tone = "woman_cartwheeling_medium_skin_tone"
    woman_cartwheeling_tone4 = "woman_cartwheeling_tone4"
    woman_cartwheeling_medium_dark_skin_tone = "woman_cartwheeling_medium_dark_skin_tone"
    woman_cartwheeling_tone5 = "woman_cartwheeling_tone5"
    woman_cartwheeling_dark_skin_tone = "woman_cartwheeling_dark_skin_tone"
    man_cartwheeling = "man_cartwheeling"
    man_cartwheeling_tone1 = "man_cartwheeling_tone1"
    man_cartwheeling_light_skin_tone = "man_cartwheeling_light_skin_tone"
    man_cartwheeling_tone2 = "man_cartwheeling_tone2"
    man_cartwheeling_medium_light_skin_tone = "man_cartwheeling_medium_light_skin_tone"
    man_cartwheeling_tone3 = "man_cartwheeling_tone3"
    man_cartwheeling_medium_skin_tone = "man_cartwheeling_medium_skin_tone"
    man_cartwheeling_tone4 = "man_cartwheeling_tone4"
    man_cartwheeling_medium_dark_skin_tone = "man_cartwheeling_medium_dark_skin_tone"
    man_cartwheeling_tone5 = "man_cartwheeling_tone5"
    man_cartwheeling_dark_skin_tone = "man_cartwheeling_dark_skin_tone"
    person_bouncing_ball = "person_bouncing_ball"
    basketball_player = "basketball_player"
    person_with_ball = "person_with_ball"
    person_bouncing_ball_tone1 = "person_bouncing_ball_tone1"
    basketball_player_tone1 = "basketball_player_tone1"
    person_with_ball_tone1 = "person_with_ball_tone1"
    person_bouncing_ball_tone2 = "person_bouncing_ball_tone2"
    basketball_player_tone2 = "basketball_player_tone2"
    person_with_ball_tone2 = "person_with_ball_tone2"
    person_bouncing_ball_tone3 = "person_bouncing_ball_tone3"
    basketball_player_tone3 = "basketball_player_tone3"
    person_with_ball_tone3 = "person_with_ball_tone3"
    person_bouncing_ball_tone4 = "person_bouncing_ball_tone4"
    basketball_player_tone4 = "basketball_player_tone4"
    person_with_ball_tone4 = "person_with_ball_tone4"
    person_bouncing_ball_tone5 = "person_bouncing_ball_tone5"
    basketball_player_tone5 = "basketball_player_tone5"
    person_with_ball_tone5 = "person_with_ball_tone5"
    woman_bouncing_ball = "woman_bouncing_ball"
    woman_bouncing_ball_tone1 = "woman_bouncing_ball_tone1"
    woman_bouncing_ball_light_skin_tone = "woman_bouncing_ball_light_skin_tone"
    woman_bouncing_ball_tone2 = "woman_bouncing_ball_tone2"
    woman_bouncing_ball_medium_light_skin_tone = "woman_bouncing_ball_medium_light_skin_tone"
    woman_bouncing_ball_tone3 = "woman_bouncing_ball_tone3"
    woman_bouncing_ball_medium_skin_tone = "woman_bouncing_ball_medium_skin_tone"
    woman_bouncing_ball_tone4 = "woman_bouncing_ball_tone4"
    woman_bouncing_ball_medium_dark_skin_tone = "woman_bouncing_ball_medium_dark_skin_tone"
    woman_bouncing_ball_tone5 = "woman_bouncing_ball_tone5"
    woman_bouncing_ball_dark_skin_tone = "woman_bouncing_ball_dark_skin_tone"
    man_bouncing_ball = "man_bouncing_ball"
    man_bouncing_ball_tone1 = "man_bouncing_ball_tone1"
    man_bouncing_ball_light_skin_tone = "man_bouncing_ball_light_skin_tone"
    man_bouncing_ball_tone2 = "man_bouncing_ball_tone2"
    man_bouncing_ball_medium_light_skin_tone = "man_bouncing_ball_medium_light_skin_tone"
    man_bouncing_ball_tone3 = "man_bouncing_ball_tone3"
    man_bouncing_ball_medium_skin_tone = "man_bouncing_ball_medium_skin_tone"
    man_bouncing_ball_tone4 = "man_bouncing_ball_tone4"
    man_bouncing_ball_medium_dark_skin_tone = "man_bouncing_ball_medium_dark_skin_tone"
    man_bouncing_ball_tone5 = "man_bouncing_ball_tone5"
    man_bouncing_ball_dark_skin_tone = "man_bouncing_ball_dark_skin_tone"
    person_fencing = "person_fencing"
    fencer = "fencer"
    fencing = "fencing"
    person_playing_handball = "person_playing_handball"
    handball = "handball"
    person_playing_handball_tone1 = "person_playing_handball_tone1"
    handball_tone1 = "handball_tone1"
    person_playing_handball_tone2 = "person_playing_handball_tone2"
    handball_tone2 = "handball_tone2"
    person_playing_handball_tone3 = "person_playing_handball_tone3"
    handball_tone3 = "handball_tone3"
    person_playing_handball_tone4 = "person_playing_handball_tone4"
    handball_tone4 = "handball_tone4"
    person_playing_handball_tone5 = "person_playing_handball_tone5"
    handball_tone5 = "handball_tone5"
    woman_playing_handball = "woman_playing_handball"
    woman_playing_handball_tone1 = "woman_playing_handball_tone1"
    woman_playing_handball_light_skin_tone = "woman_playing_handball_light_skin_tone"
    woman_playing_handball_tone2 = "woman_playing_handball_tone2"
    woman_playing_handball_medium_light_skin_tone = "woman_playing_handball_medium_light_skin_tone"
    woman_playing_handball_tone3 = "woman_playing_handball_tone3"
    woman_playing_handball_medium_skin_tone = "woman_playing_handball_medium_skin_tone"
    woman_playing_handball_tone4 = "woman_playing_handball_tone4"
    woman_playing_handball_medium_dark_skin_tone = "woman_playing_handball_medium_dark_skin_tone"
    woman_playing_handball_tone5 = "woman_playing_handball_tone5"
    woman_playing_handball_dark_skin_tone = "woman_playing_handball_dark_skin_tone"
    man_playing_handball = "man_playing_handball"
    man_playing_handball_tone1 = "man_playing_handball_tone1"
    man_playing_handball_light_skin_tone = "man_playing_handball_light_skin_tone"
    man_playing_handball_tone2 = "man_playing_handball_tone2"
    man_playing_handball_medium_light_skin_tone = "man_playing_handball_medium_light_skin_tone"
    man_playing_handball_tone3 = "man_playing_handball_tone3"
    man_playing_handball_medium_skin_tone = "man_playing_handball_medium_skin_tone"
    man_playing_handball_tone4 = "man_playing_handball_tone4"
    man_playing_handball_medium_dark_skin_tone = "man_playing_handball_medium_dark_skin_tone"
    man_playing_handball_tone5 = "man_playing_handball_tone5"
    man_playing_handball_dark_skin_tone = "man_playing_handball_dark_skin_tone"
    person_golfing = "person_golfing"
    golfer = "golfer"
    person_golfing_tone1 = "person_golfing_tone1"
    person_golfing_light_skin_tone = "person_golfing_light_skin_tone"
    person_golfing_tone2 = "person_golfing_tone2"
    person_golfing_medium_light_skin_tone = "person_golfing_medium_light_skin_tone"
    person_golfing_tone3 = "person_golfing_tone3"
    person_golfing_medium_skin_tone = "person_golfing_medium_skin_tone"
    person_golfing_tone4 = "person_golfing_tone4"
    person_golfing_medium_dark_skin_tone = "person_golfing_medium_dark_skin_tone"
    person_golfing_tone5 = "person_golfing_tone5"
    person_golfing_dark_skin_tone = "person_golfing_dark_skin_tone"
    woman_golfing = "woman_golfing"
    woman_golfing_tone1 = "woman_golfing_tone1"
    woman_golfing_light_skin_tone = "woman_golfing_light_skin_tone"
    woman_golfing_tone2 = "woman_golfing_tone2"
    woman_golfing_medium_light_skin_tone = "woman_golfing_medium_light_skin_tone"
    woman_golfing_tone3 = "woman_golfing_tone3"
    woman_golfing_medium_skin_tone = "woman_golfing_medium_skin_tone"
    woman_golfing_tone4 = "woman_golfing_tone4"
    woman_golfing_medium_dark_skin_tone = "woman_golfing_medium_dark_skin_tone"
    woman_golfing_tone5 = "woman_golfing_tone5"
    woman_golfing_dark_skin_tone = "woman_golfing_dark_skin_tone"
    man_golfing = "man_golfing"
    man_golfing_tone1 = "man_golfing_tone1"
    man_golfing_light_skin_tone = "man_golfing_light_skin_tone"
    man_golfing_tone2 = "man_golfing_tone2"
    man_golfing_medium_light_skin_tone = "man_golfing_medium_light_skin_tone"
    man_golfing_tone3 = "man_golfing_tone3"
    man_golfing_medium_skin_tone = "man_golfing_medium_skin_tone"
    man_golfing_tone4 = "man_golfing_tone4"
    man_golfing_medium_dark_skin_tone = "man_golfing_medium_dark_skin_tone"
    man_golfing_tone5 = "man_golfing_tone5"
    man_golfing_dark_skin_tone = "man_golfing_dark_skin_tone"
    horse_racing = "horse_racing"
    horse_racing_tone1 = "horse_racing_tone1"
    horse_racing_tone2 = "horse_racing_tone2"
    horse_racing_tone3 = "horse_racing_tone3"
    horse_racing_tone4 = "horse_racing_tone4"
    horse_racing_tone5 = "horse_racing_tone5"
    person_in_lotus_position = "person_in_lotus_position"
    person_in_lotus_position_tone1 = "person_in_lotus_position_tone1"
    person_in_lotus_position_light_skin_tone = "person_in_lotus_position_light_skin_tone"
    person_in_lotus_position_tone2 = "person_in_lotus_position_tone2"
    person_in_lotus_position_medium_light_skin_tone = "person_in_lotus_position_medium_light_skin_tone"
    person_in_lotus_position_tone3 = "person_in_lotus_position_tone3"
    person_in_lotus_position_medium_skin_tone = "person_in_lotus_position_medium_skin_tone"
    person_in_lotus_position_tone4 = "person_in_lotus_position_tone4"
    person_in_lotus_position_medium_dark_skin_tone = "person_in_lotus_position_medium_dark_skin_tone"
    person_in_lotus_position_tone5 = "person_in_lotus_position_tone5"
    person_in_lotus_position_dark_skin_tone = "person_in_lotus_position_dark_skin_tone"
    woman_in_lotus_position = "woman_in_lotus_position"
    woman_in_lotus_position_tone1 = "woman_in_lotus_position_tone1"
    woman_in_lotus_position_light_skin_tone = "woman_in_lotus_position_light_skin_tone"
    woman_in_lotus_position_tone2 = "woman_in_lotus_position_tone2"
    woman_in_lotus_position_medium_light_skin_tone = "woman_in_lotus_position_medium_light_skin_tone"
    woman_in_lotus_position_tone3 = "woman_in_lotus_position_tone3"
    woman_in_lotus_position_medium_skin_tone = "woman_in_lotus_position_medium_skin_tone"
    woman_in_lotus_position_tone4 = "woman_in_lotus_position_tone4"
    woman_in_lotus_position_medium_dark_skin_tone = "woman_in_lotus_position_medium_dark_skin_tone"
    woman_in_lotus_position_tone5 = "woman_in_lotus_position_tone5"
    woman_in_lotus_position_dark_skin_tone = "woman_in_lotus_position_dark_skin_tone"
    man_in_lotus_position = "man_in_lotus_position"
    man_in_lotus_position_tone1 = "man_in_lotus_position_tone1"
    man_in_lotus_position_light_skin_tone = "man_in_lotus_position_light_skin_tone"
    man_in_lotus_position_tone2 = "man_in_lotus_position_tone2"
    man_in_lotus_position_medium_light_skin_tone = "man_in_lotus_position_medium_light_skin_tone"
    man_in_lotus_position_tone3 = "man_in_lotus_position_tone3"
    man_in_lotus_position_medium_skin_tone = "man_in_lotus_position_medium_skin_tone"
    man_in_lotus_position_tone4 = "man_in_lotus_position_tone4"
    man_in_lotus_position_medium_dark_skin_tone = "man_in_lotus_position_medium_dark_skin_tone"
    man_in_lotus_position_tone5 = "man_in_lotus_position_tone5"
    man_in_lotus_position_dark_skin_tone = "man_in_lotus_position_dark_skin_tone"
    person_surfing = "person_surfing"
    surfer = "surfer"
    person_surfing_tone1 = "person_surfing_tone1"
    surfer_tone1 = "surfer_tone1"
    person_surfing_tone2 = "person_surfing_tone2"
    surfer_tone2 = "surfer_tone2"
    person_surfing_tone3 = "person_surfing_tone3"
    surfer_tone3 = "surfer_tone3"
    person_surfing_tone4 = "person_surfing_tone4"
    surfer_tone4 = "surfer_tone4"
    person_surfing_tone5 = "person_surfing_tone5"
    surfer_tone5 = "surfer_tone5"
    woman_surfing = "woman_surfing"
    woman_surfing_tone1 = "woman_surfing_tone1"
    woman_surfing_light_skin_tone = "woman_surfing_light_skin_tone"
    woman_surfing_tone2 = "woman_surfing_tone2"
    woman_surfing_medium_light_skin_tone = "woman_surfing_medium_light_skin_tone"
    woman_surfing_tone3 = "woman_surfing_tone3"
    woman_surfing_medium_skin_tone = "woman_surfing_medium_skin_tone"
    woman_surfing_tone4 = "woman_surfing_tone4"
    woman_surfing_medium_dark_skin_tone = "woman_surfing_medium_dark_skin_tone"
    woman_surfing_tone5 = "woman_surfing_tone5"
    woman_surfing_dark_skin_tone = "woman_surfing_dark_skin_tone"
    man_surfing = "man_surfing"
    man_surfing_tone1 = "man_surfing_tone1"
    man_surfing_light_skin_tone = "man_surfing_light_skin_tone"
    man_surfing_tone2 = "man_surfing_tone2"
    man_surfing_medium_light_skin_tone = "man_surfing_medium_light_skin_tone"
    man_surfing_tone3 = "man_surfing_tone3"
    man_surfing_medium_skin_tone = "man_surfing_medium_skin_tone"
    man_surfing_tone4 = "man_surfing_tone4"
    man_surfing_medium_dark_skin_tone = "man_surfing_medium_dark_skin_tone"
    man_surfing_tone5 = "man_surfing_tone5"
    man_surfing_dark_skin_tone = "man_surfing_dark_skin_tone"
    person_swimming = "person_swimming"
    swimmer = "swimmer"
    person_swimming_tone1 = "person_swimming_tone1"
    swimmer_tone1 = "swimmer_tone1"
    person_swimming_tone2 = "person_swimming_tone2"
    swimmer_tone2 = "swimmer_tone2"
    person_swimming_tone3 = "person_swimming_tone3"
    swimmer_tone3 = "swimmer_tone3"
    person_swimming_tone4 = "person_swimming_tone4"
    swimmer_tone4 = "swimmer_tone4"
    person_swimming_tone5 = "person_swimming_tone5"
    swimmer_tone5 = "swimmer_tone5"
    woman_swimming = "woman_swimming"
    woman_swimming_tone1 = "woman_swimming_tone1"
    woman_swimming_light_skin_tone = "woman_swimming_light_skin_tone"
    woman_swimming_tone2 = "woman_swimming_tone2"
    woman_swimming_medium_light_skin_tone = "woman_swimming_medium_light_skin_tone"
    woman_swimming_tone3 = "woman_swimming_tone3"
    woman_swimming_medium_skin_tone = "woman_swimming_medium_skin_tone"
    woman_swimming_tone4 = "woman_swimming_tone4"
    woman_swimming_medium_dark_skin_tone = "woman_swimming_medium_dark_skin_tone"
    woman_swimming_tone5 = "woman_swimming_tone5"
    woman_swimming_dark_skin_tone = "woman_swimming_dark_skin_tone"
    man_swimming = "man_swimming"
    man_swimming_tone1 = "man_swimming_tone1"
    man_swimming_light_skin_tone = "man_swimming_light_skin_tone"
    man_swimming_tone2 = "man_swimming_tone2"
    man_swimming_medium_light_skin_tone = "man_swimming_medium_light_skin_tone"
    man_swimming_tone3 = "man_swimming_tone3"
    man_swimming_medium_skin_tone = "man_swimming_medium_skin_tone"
    man_swimming_tone4 = "man_swimming_tone4"
    man_swimming_medium_dark_skin_tone = "man_swimming_medium_dark_skin_tone"
    man_swimming_tone5 = "man_swimming_tone5"
    man_swimming_dark_skin_tone = "man_swimming_dark_skin_tone"
    person_playing_water_polo = "person_playing_water_polo"
    water_polo = "water_polo"
    person_playing_water_polo_tone1 = "person_playing_water_polo_tone1"
    water_polo_tone1 = "water_polo_tone1"
    person_playing_water_polo_tone2 = "person_playing_water_polo_tone2"
    water_polo_tone2 = "water_polo_tone2"
    person_playing_water_polo_tone3 = "person_playing_water_polo_tone3"
    water_polo_tone3 = "water_polo_tone3"
    person_playing_water_polo_tone4 = "person_playing_water_polo_tone4"
    water_polo_tone4 = "water_polo_tone4"
    person_playing_water_polo_tone5 = "person_playing_water_polo_tone5"
    water_polo_tone5 = "water_polo_tone5"
    woman_playing_water_polo = "woman_playing_water_polo"
    woman_playing_water_polo_tone1 = "woman_playing_water_polo_tone1"
    woman_playing_water_polo_light_skin_tone = "woman_playing_water_polo_light_skin_tone"
    woman_playing_water_polo_tone2 = "woman_playing_water_polo_tone2"
    woman_playing_water_polo_medium_light_skin_tone = "woman_playing_water_polo_medium_light_skin_tone"
    woman_playing_water_polo_tone3 = "woman_playing_water_polo_tone3"
    woman_playing_water_polo_medium_skin_tone = "woman_playing_water_polo_medium_skin_tone"
    woman_playing_water_polo_tone4 = "woman_playing_water_polo_tone4"
    woman_playing_water_polo_medium_dark_skin_tone = "woman_playing_water_polo_medium_dark_skin_tone"
    woman_playing_water_polo_tone5 = "woman_playing_water_polo_tone5"
    woman_playing_water_polo_dark_skin_tone = "woman_playing_water_polo_dark_skin_tone"
    man_playing_water_polo = "man_playing_water_polo"
    man_playing_water_polo_tone1 = "man_playing_water_polo_tone1"
    man_playing_water_polo_light_skin_tone = "man_playing_water_polo_light_skin_tone"
    man_playing_water_polo_tone2 = "man_playing_water_polo_tone2"
    man_playing_water_polo_medium_light_skin_tone = "man_playing_water_polo_medium_light_skin_tone"
    man_playing_water_polo_tone3 = "man_playing_water_polo_tone3"
    man_playing_water_polo_medium_skin_tone = "man_playing_water_polo_medium_skin_tone"
    man_playing_water_polo_tone4 = "man_playing_water_polo_tone4"
    man_playing_water_polo_medium_dark_skin_tone = "man_playing_water_polo_medium_dark_skin_tone"
    man_playing_water_polo_tone5 = "man_playing_water_polo_tone5"
    man_playing_water_polo_dark_skin_tone = "man_playing_water_polo_dark_skin_tone"
    person_rowing_boat = "person_rowing_boat"
    rowboat = "rowboat"
    person_rowing_boat_tone1 = "person_rowing_boat_tone1"
    rowboat_tone1 = "rowboat_tone1"
    person_rowing_boat_tone2 = "person_rowing_boat_tone2"
    rowboat_tone2 = "rowboat_tone2"
    person_rowing_boat_tone3 = "person_rowing_boat_tone3"
    rowboat_tone3 = "rowboat_tone3"
    person_rowing_boat_tone4 = "person_rowing_boat_tone4"
    rowboat_tone4 = "rowboat_tone4"
    person_rowing_boat_tone5 = "person_rowing_boat_tone5"
    rowboat_tone5 = "rowboat_tone5"
    woman_rowing_boat = "woman_rowing_boat"
    woman_rowing_boat_tone1 = "woman_rowing_boat_tone1"
    woman_rowing_boat_light_skin_tone = "woman_rowing_boat_light_skin_tone"
    woman_rowing_boat_tone2 = "woman_rowing_boat_tone2"
    woman_rowing_boat_medium_light_skin_tone = "woman_rowing_boat_medium_light_skin_tone"
    woman_rowing_boat_tone3 = "woman_rowing_boat_tone3"
    woman_rowing_boat_medium_skin_tone = "woman_rowing_boat_medium_skin_tone"
    woman_rowing_boat_tone4 = "woman_rowing_boat_tone4"
    woman_rowing_boat_medium_dark_skin_tone = "woman_rowing_boat_medium_dark_skin_tone"
    woman_rowing_boat_tone5 = "woman_rowing_boat_tone5"
    woman_rowing_boat_dark_skin_tone = "woman_rowing_boat_dark_skin_tone"
    man_rowing_boat = "man_rowing_boat"
    man_rowing_boat_tone1 = "man_rowing_boat_tone1"
    man_rowing_boat_light_skin_tone = "man_rowing_boat_light_skin_tone"
    man_rowing_boat_tone2 = "man_rowing_boat_tone2"
    man_rowing_boat_medium_light_skin_tone = "man_rowing_boat_medium_light_skin_tone"
    man_rowing_boat_tone3 = "man_rowing_boat_tone3"
    man_rowing_boat_medium_skin_tone = "man_rowing_boat_medium_skin_tone"
    man_rowing_boat_tone4 = "man_rowing_boat_tone4"
    man_rowing_boat_medium_dark_skin_tone = "man_rowing_boat_medium_dark_skin_tone"
    man_rowing_boat_tone5 = "man_rowing_boat_tone5"
    man_rowing_boat_dark_skin_tone = "man_rowing_boat_dark_skin_tone"
    person_climbing = "person_climbing"
    person_climbing_tone1 = "person_climbing_tone1"
    person_climbing_light_skin_tone = "person_climbing_light_skin_tone"
    person_climbing_tone2 = "person_climbing_tone2"
    person_climbing_medium_light_skin_tone = "person_climbing_medium_light_skin_tone"
    person_climbing_tone3 = "person_climbing_tone3"
    person_climbing_medium_skin_tone = "person_climbing_medium_skin_tone"
    person_climbing_tone4 = "person_climbing_tone4"
    person_climbing_medium_dark_skin_tone = "person_climbing_medium_dark_skin_tone"
    person_climbing_tone5 = "person_climbing_tone5"
    person_climbing_dark_skin_tone = "person_climbing_dark_skin_tone"
    woman_climbing = "woman_climbing"
    woman_climbing_tone1 = "woman_climbing_tone1"
    woman_climbing_light_skin_tone = "woman_climbing_light_skin_tone"
    woman_climbing_tone2 = "woman_climbing_tone2"
    woman_climbing_medium_light_skin_tone = "woman_climbing_medium_light_skin_tone"
    woman_climbing_tone3 = "woman_climbing_tone3"
    woman_climbing_medium_skin_tone = "woman_climbing_medium_skin_tone"
    woman_climbing_tone4 = "woman_climbing_tone4"
    woman_climbing_medium_dark_skin_tone = "woman_climbing_medium_dark_skin_tone"
    woman_climbing_tone5 = "woman_climbing_tone5"
    woman_climbing_dark_skin_tone = "woman_climbing_dark_skin_tone"
    man_climbing = "man_climbing"
    man_climbing_tone1 = "man_climbing_tone1"
    man_climbing_light_skin_tone = "man_climbing_light_skin_tone"
    man_climbing_tone2 = "man_climbing_tone2"
    man_climbing_medium_light_skin_tone = "man_climbing_medium_light_skin_tone"
    man_climbing_tone3 = "man_climbing_tone3"
    man_climbing_medium_skin_tone = "man_climbing_medium_skin_tone"
    man_climbing_tone4 = "man_climbing_tone4"
    man_climbing_medium_dark_skin_tone = "man_climbing_medium_dark_skin_tone"
    man_climbing_tone5 = "man_climbing_tone5"
    man_climbing_dark_skin_tone = "man_climbing_dark_skin_tone"
    person_mountain_biking = "person_mountain_biking"
    mountain_bicyclist = "mountain_bicyclist"
    person_mountain_biking_tone1 = "person_mountain_biking_tone1"
    mountain_bicyclist_tone1 = "mountain_bicyclist_tone1"
    person_mountain_biking_tone2 = "person_mountain_biking_tone2"
    mountain_bicyclist_tone2 = "mountain_bicyclist_tone2"
    person_mountain_biking_tone3 = "person_mountain_biking_tone3"
    mountain_bicyclist_tone3 = "mountain_bicyclist_tone3"
    person_mountain_biking_tone4 = "person_mountain_biking_tone4"
    mountain_bicyclist_tone4 = "mountain_bicyclist_tone4"
    person_mountain_biking_tone5 = "person_mountain_biking_tone5"
    mountain_bicyclist_tone5 = "mountain_bicyclist_tone5"
    woman_mountain_biking = "woman_mountain_biking"
    woman_mountain_biking_tone1 = "woman_mountain_biking_tone1"
    woman_mountain_biking_light_skin_tone = "woman_mountain_biking_light_skin_tone"
    woman_mountain_biking_tone2 = "woman_mountain_biking_tone2"
    woman_mountain_biking_medium_light_skin_tone = "woman_mountain_biking_medium_light_skin_tone"
    woman_mountain_biking_tone3 = "woman_mountain_biking_tone3"
    woman_mountain_biking_medium_skin_tone = "woman_mountain_biking_medium_skin_tone"
    woman_mountain_biking_tone4 = "woman_mountain_biking_tone4"
    woman_mountain_biking_medium_dark_skin_tone = "woman_mountain_biking_medium_dark_skin_tone"
    woman_mountain_biking_tone5 = "woman_mountain_biking_tone5"
    woman_mountain_biking_dark_skin_tone = "woman_mountain_biking_dark_skin_tone"
    man_mountain_biking = "man_mountain_biking"
    man_mountain_biking_tone1 = "man_mountain_biking_tone1"
    man_mountain_biking_light_skin_tone = "man_mountain_biking_light_skin_tone"
    man_mountain_biking_tone2 = "man_mountain_biking_tone2"
    man_mountain_biking_medium_light_skin_tone = "man_mountain_biking_medium_light_skin_tone"
    man_mountain_biking_tone3 = "man_mountain_biking_tone3"
    man_mountain_biking_medium_skin_tone = "man_mountain_biking_medium_skin_tone"
    man_mountain_biking_tone4 = "man_mountain_biking_tone4"
    man_mountain_biking_medium_dark_skin_tone = "man_mountain_biking_medium_dark_skin_tone"
    man_mountain_biking_tone5 = "man_mountain_biking_tone5"
    man_mountain_biking_dark_skin_tone = "man_mountain_biking_dark_skin_tone"
    person_biking = "person_biking"
    bicyclist = "bicyclist"
    person_biking_tone1 = "person_biking_tone1"
    bicyclist_tone1 = "bicyclist_tone1"
    person_biking_tone2 = "person_biking_tone2"
    bicyclist_tone2 = "bicyclist_tone2"
    person_biking_tone3 = "person_biking_tone3"
    bicyclist_tone3 = "bicyclist_tone3"
    person_biking_tone4 = "person_biking_tone4"
    bicyclist_tone4 = "bicyclist_tone4"
    person_biking_tone5 = "person_biking_tone5"
    bicyclist_tone5 = "bicyclist_tone5"
    woman_biking = "woman_biking"
    woman_biking_tone1 = "woman_biking_tone1"
    woman_biking_light_skin_tone = "woman_biking_light_skin_tone"
    woman_biking_tone2 = "woman_biking_tone2"
    woman_biking_medium_light_skin_tone = "woman_biking_medium_light_skin_tone"
    woman_biking_tone3 = "woman_biking_tone3"
    woman_biking_medium_skin_tone = "woman_biking_medium_skin_tone"
    woman_biking_tone4 = "woman_biking_tone4"
    woman_biking_medium_dark_skin_tone = "woman_biking_medium_dark_skin_tone"
    woman_biking_tone5 = "woman_biking_tone5"
    woman_biking_dark_skin_tone = "woman_biking_dark_skin_tone"
    man_biking = "man_biking"
    man_biking_tone1 = "man_biking_tone1"
    man_biking_light_skin_tone = "man_biking_light_skin_tone"
    man_biking_tone2 = "man_biking_tone2"
    man_biking_medium_light_skin_tone = "man_biking_medium_light_skin_tone"
    man_biking_tone3 = "man_biking_tone3"
    man_biking_medium_skin_tone = "man_biking_medium_skin_tone"
    man_biking_tone4 = "man_biking_tone4"
    man_biking_medium_dark_skin_tone = "man_biking_medium_dark_skin_tone"
    man_biking_tone5 = "man_biking_tone5"
    man_biking_dark_skin_tone = "man_biking_dark_skin_tone"
    trophy = "trophy"
    first_place = "first_place"
    first_place_medal = "first_place_medal"
    second_place = "second_place"
    second_place_medal = "second_place_medal"
    third_place = "third_place"
    third_place_medal = "third_place_medal"
    medal = "medal"
    sports_medal = "sports_medal"
    military_medal = "military_medal"
    rosette = "rosette"
    reminder_ribbon = "reminder_ribbon"
    ticket = "ticket"
    tickets = "tickets"
    admission_tickets = "admission_tickets"
    circus_tent = "circus_tent"
    person_juggling = "person_juggling"
    juggling = "juggling"
    juggler = "juggler"
    person_juggling_tone1 = "person_juggling_tone1"
    juggling_tone1 = "juggling_tone1"
    juggler_tone1 = "juggler_tone1"
    person_juggling_tone2 = "person_juggling_tone2"
    juggling_tone2 = "juggling_tone2"
    juggler_tone2 = "juggler_tone2"
    person_juggling_tone3 = "person_juggling_tone3"
    juggling_tone3 = "juggling_tone3"
    juggler_tone3 = "juggler_tone3"
    person_juggling_tone4 = "person_juggling_tone4"
    juggling_tone4 = "juggling_tone4"
    juggler_tone4 = "juggler_tone4"
    person_juggling_tone5 = "person_juggling_tone5"
    juggling_tone5 = "juggling_tone5"
    juggler_tone5 = "juggler_tone5"
    woman_juggling = "woman_juggling"
    woman_juggling_tone1 = "woman_juggling_tone1"
    woman_juggling_light_skin_tone = "woman_juggling_light_skin_tone"
    woman_juggling_tone2 = "woman_juggling_tone2"
    woman_juggling_medium_light_skin_tone = "woman_juggling_medium_light_skin_tone"
    woman_juggling_tone3 = "woman_juggling_tone3"
    woman_juggling_medium_skin_tone = "woman_juggling_medium_skin_tone"
    woman_juggling_tone4 = "woman_juggling_tone4"
    woman_juggling_medium_dark_skin_tone = "woman_juggling_medium_dark_skin_tone"
    woman_juggling_tone5 = "woman_juggling_tone5"
    woman_juggling_dark_skin_tone = "woman_juggling_dark_skin_tone"
    man_juggling = "man_juggling"
    man_juggling_tone1 = "man_juggling_tone1"
    man_juggling_light_skin_tone = "man_juggling_light_skin_tone"
    man_juggling_tone2 = "man_juggling_tone2"
    man_juggling_medium_light_skin_tone = "man_juggling_medium_light_skin_tone"
    man_juggling_tone3 = "man_juggling_tone3"
    man_juggling_medium_skin_tone = "man_juggling_medium_skin_tone"
    man_juggling_tone4 = "man_juggling_tone4"
    man_juggling_medium_dark_skin_tone = "man_juggling_medium_dark_skin_tone"
    man_juggling_tone5 = "man_juggling_tone5"
    man_juggling_dark_skin_tone = "man_juggling_dark_skin_tone"
    performing_arts = "performing_arts"
    art = "art"
    clapper = "clapper"
    microphone = "microphone"
    headphones = "headphones"
    musical_score = "musical_score"
    musical_keyboard = "musical_keyboard"
    drum = "drum"
    drum_with_drumsticks = "drum_with_drumsticks"
    saxophone = "saxophone"
    trumpet = "trumpet"
    banjo = "banjo"
    guitar = "guitar"
    violin = "violin"
    game_die = "game_die"
    chess_pawn = "chess_pawn"
    dart = "dart"
    kite = "kite"
    yo_yo = "yo_yo"
    bowling = "bowling"
    video_game = "video_game"
    slot_machine = "slot_machine"
    jigsaw = "jigsaw"
    red_car = "red_car"
    taxi = "taxi"
    blue_car = "blue_car"
    bus = "bus"
    trolleybus = "trolleybus"
    race_car = "race_car"
    racing_car = "racing_car"
    police_car = "police_car"
    ambulance = "ambulance"
    fire_engine = "fire_engine"
    minibus = "minibus"
    truck = "truck"
    articulated_lorry = "articulated_lorry"
    tractor = "tractor"
    auto_rickshaw = "auto_rickshaw"
    motor_scooter = "motor_scooter"
    motorbike = "motorbike"
    motorcycle = "motorcycle"
    racing_motorcycle = "racing_motorcycle"
    scooter = "scooter"
    bike = "bike"
    motorized_wheelchair = "motorized_wheelchair"
    manual_wheelchair = "manual_wheelchair"
    rotating_light = "rotating_light"
    oncoming_police_car = "oncoming_police_car"
    oncoming_bus = "oncoming_bus"
    oncoming_automobile = "oncoming_automobile"
    oncoming_taxi = "oncoming_taxi"
    aerial_tramway = "aerial_tramway"
    mountain_cableway = "mountain_cableway"
    suspension_railway = "suspension_railway"
    railway_car = "railway_car"
    train = "train"
    mountain_railway = "mountain_railway"
    monorail = "monorail"
    bullettrain_side = "bullettrain_side"
    bullettrain_front = "bullettrain_front"
    light_rail = "light_rail"
    steam_locomotive = "steam_locomotive"
    train2 = "train2"
    metro = "metro"
    tram = "tram"
    station = "station"
    airplane = "airplane"
    airplane_departure = "airplane_departure"
    airplane_arriving = "airplane_arriving"
    airplane_small = "airplane_small"
    small_airplane = "small_airplane"
    seat = "seat"
    satellite_orbital = "satellite_orbital"
    rocket = "rocket"
    flying_saucer = "flying_saucer"
    helicopter = "helicopter"
    canoe = "canoe"
    kayak = "kayak"
    sailboat = "sailboat"
    speedboat = "speedboat"
    motorboat = "motorboat"
    cruise_ship = "cruise_ship"
    passenger_ship = "passenger_ship"
    ferry = "ferry"
    ship = "ship"
    anchor = "anchor"
    fuelpump = "fuelpump"
    construction = "construction"
    vertical_traffic_light = "vertical_traffic_light"
    traffic_light = "traffic_light"
    busstop = "busstop"
    map = "map"
    world_map = "world_map"
    moyai = "moyai"
    statue_of_liberty = "statue_of_liberty"
    tokyo_tower = "tokyo_tower"
    european_castle = "european_castle"
    japanese_castle = "japanese_castle"
    stadium = "stadium"
    ferris_wheel = "ferris_wheel"
    roller_coaster = "roller_coaster"
    carousel_horse = "carousel_horse"
    fountain = "fountain"
    beach_umbrella = "beach_umbrella"
    umbrella_on_ground = "umbrella_on_ground"
    beach = "beach"
    beach_with_umbrella = "beach_with_umbrella"
    island = "island"
    desert_island = "desert_island"
    desert = "desert"
    volcano = "volcano"
    mountain = "mountain"
    mountain_snow = "mountain_snow"
    snow_capped_mountain = "snow_capped_mountain"
    mount_fuji = "mount_fuji"
    camping = "camping"
    tent = "tent"
    house = "house"
    house_with_garden = "house_with_garden"
    homes = "homes"
    house_buildings = "house_buildings"
    house_abandoned = "house_abandoned"
    derelict_house_building = "derelict_house_building"
    construction_site = "construction_site"
    building_construction = "building_construction"
    factory = "factory"
    office = "office"
    department_store = "department_store"
    post_office = "post_office"
    european_post_office = "european_post_office"
    hospital = "hospital"
    bank = "bank"
    hotel = "hotel"
    convenience_store = "convenience_store"
    school = "school"
    love_hotel = "love_hotel"
    wedding = "wedding"
    classical_building = "classical_building"
    church = "church"
    mosque = "mosque"
    hindu_temple = "hindu_temple"
    synagogue = "synagogue"
    kaaba = "kaaba"
    shinto_shrine = "shinto_shrine"
    railway_track = "railway_track"
    railroad_track = "railroad_track"
    motorway = "motorway"
    japan = "japan"
    rice_scene = "rice_scene"
    park = "park"
    national_park = "national_park"
    sunrise = "sunrise"
    sunrise_over_mountains = "sunrise_over_mountains"
    stars = "stars"
    sparkler = "sparkler"
    fireworks = "fireworks"
    city_sunset = "city_sunset"
    city_sunrise = "city_sunrise"
    city_dusk = "city_dusk"
    cityscape = "cityscape"
    night_with_stars = "night_with_stars"
    milky_way = "milky_way"
    bridge_at_night = "bridge_at_night"
    foggy = "foggy"
    watch = "watch"
    iphone = "iphone"
    calling = "calling"
    computer = "computer"
    keyboard = "keyboard"
    desktop = "desktop"
    desktop_computer = "desktop_computer"
    printer = "printer"
    mouse_three_button = "mouse_three_button"
    three_button_mouse = "three_button_mouse"
    trackball = "trackball"
    joystick = "joystick"
    compression = "compression"
    minidisc = "minidisc"
    floppy_disk = "floppy_disk"
    cd = "cd"
    dvd = "dvd"
    vhs = "vhs"
    camera = "camera"
    camera_with_flash = "camera_with_flash"
    video_camera = "video_camera"
    movie_camera = "movie_camera"
    projector = "projector"
    film_projector = "film_projector"
    film_frames = "film_frames"
    telephone_receiver = "telephone_receiver"
    telephone = "telephone"
    pager = "pager"
    fax = "fax"
    tv = "tv"
    radio = "radio"
    microphone2 = "microphone2"
    studio_microphone = "studio_microphone"
    level_slider = "level_slider"
    control_knobs = "control_knobs"
    compass = "compass"
    stopwatch = "stopwatch"
    timer = "timer"
    timer_clock = "timer_clock"
    alarm_clock = "alarm_clock"
    clock = "clock"
    mantlepiece_clock = "mantlepiece_clock"
    hourglass = "hourglass"
    hourglass_flowing_sand = "hourglass_flowing_sand"
    satellite = "satellite"
    battery = "battery"
    electric_plug = "electric_plug"
    bulb = "bulb"
    flashlight = "flashlight"
    candle = "candle"
    fire_extinguisher = "fire_extinguisher"
    oil = "oil"
    oil_drum = "oil_drum"
    money_with_wings = "money_with_wings"
    dollar = "dollar"
    yen = "yen"
    euro = "euro"
    pound = "pound"
    moneybag = "moneybag"
    credit_card = "credit_card"
    gem = "gem"
    scales = "scales"
    toolbox = "toolbox"
    wrench = "wrench"
    hammer = "hammer"
    hammer_pick = "hammer_pick"
    hammer_and_pick = "hammer_and_pick"
    tools = "tools"
    hammer_and_wrench = "hammer_and_wrench"
    pick = "pick"
    nut_and_bolt = "nut_and_bolt"
    gear = "gear"
    bricks = "bricks"
    chains = "chains"
    magnet = "magnet"
    gun = "gun"
    bomb = "bomb"
    firecracker = "firecracker"
    axe = "axe"
    razor = "razor"
    knife = "knife"
    dagger = "dagger"
    dagger_knife = "dagger_knife"
    crossed_swords = "crossed_swords"
    shield = "shield"
    smoking = "smoking"
    coffin = "coffin"
    urn = "urn"
    funeral_urn = "funeral_urn"
    amphora = "amphora"
    diya_lamp = "diya_lamp"
    crystal_ball = "crystal_ball"
    prayer_beads = "prayer_beads"
    nazar_amulet = "nazar_amulet"
    barber = "barber"
    alembic = "alembic"
    telescope = "telescope"
    microscope = "microscope"
    hole = "hole"
    probing_cane = "probing_cane"
    stethoscope = "stethoscope"
    adhesive_bandage = "adhesive_bandage"
    pill = "pill"
    syringe = "syringe"
    drop_of_blood = "drop_of_blood"
    dna = "dna"
    microbe = "microbe"
    petri_dish = "petri_dish"
    test_tube = "test_tube"
    thermometer = "thermometer"
    chair = "chair"
    broom = "broom"
    basket = "basket"
    roll_of_paper = "roll_of_paper"
    toilet = "toilet"
    potable_water = "potable_water"
    shower = "shower"
    bathtub = "bathtub"
    bath = "bath"
    bath_tone1 = "bath_tone1"
    bath_tone2 = "bath_tone2"
    bath_tone3 = "bath_tone3"
    bath_tone4 = "bath_tone4"
    bath_tone5 = "bath_tone5"
    soap = "soap"
    sponge = "sponge"
    squeeze_bottle = "squeeze_bottle"
    bellhop = "bellhop"
    bellhop_bell = "bellhop_bell"
    key = "key"
    key2 = "key2"
    old_key = "old_key"
    door = "door"
    couch = "couch"
    couch_and_lamp = "couch_and_lamp"
    bed = "bed"
    sleeping_accommodation = "sleeping_accommodation"
    person_in_bed_tone1 = "person_in_bed_tone1"
    person_in_bed_light_skin_tone = "person_in_bed_light_skin_tone"
    person_in_bed_tone2 = "person_in_bed_tone2"
    person_in_bed_medium_light_skin_tone = "person_in_bed_medium_light_skin_tone"
    person_in_bed_tone3 = "person_in_bed_tone3"
    person_in_bed_medium_skin_tone = "person_in_bed_medium_skin_tone"
    person_in_bed_tone4 = "person_in_bed_tone4"
    person_in_bed_medium_dark_skin_tone = "person_in_bed_medium_dark_skin_tone"
    person_in_bed_tone5 = "person_in_bed_tone5"
    person_in_bed_dark_skin_tone = "person_in_bed_dark_skin_tone"
    teddy_bear = "teddy_bear"
    frame_photo = "frame_photo"
    frame_with_picture = "frame_with_picture"
    shopping_bags = "shopping_bags"
    shopping_cart = "shopping_cart"
    shopping_trolley = "shopping_trolley"
    gift = "gift"
    balloon = "balloon"
    flags = "flags"
    ribbon = "ribbon"
    confetti_ball = "confetti_ball"
    tada = "tada"
    dolls = "dolls"
    izakaya_lantern = "izakaya_lantern"
    wind_chime = "wind_chime"
    red_envelope = "red_envelope"
    envelope = "envelope"
    envelope_with_arrow = "envelope_with_arrow"
    incoming_envelope = "incoming_envelope"
    e_mail = "e_mail"
    email = "email"
    love_letter = "love_letter"
    inbox_tray = "inbox_tray"
    outbox_tray = "outbox_tray"
    package = "package"
    label = "label"
    mailbox_closed = "mailbox_closed"
    mailbox = "mailbox"
    mailbox_with_mail = "mailbox_with_mail"
    mailbox_with_no_mail = "mailbox_with_no_mail"
    postbox = "postbox"
    postal_horn = "postal_horn"
    scroll = "scroll"
    page_with_curl = "page_with_curl"
    page_facing_up = "page_facing_up"
    bookmark_tabs = "bookmark_tabs"
    receipt = "receipt"
    bar_chart = "bar_chart"
    chart_with_upwards_trend = "chart_with_upwards_trend"
    chart_with_downwards_trend = "chart_with_downwards_trend"
    notepad_spiral = "notepad_spiral"
    spiral_note_pad = "spiral_note_pad"
    calendar_spiral = "calendar_spiral"
    spiral_calendar_pad = "spiral_calendar_pad"
    calendar = "calendar"
    date = "date"
    wastebasket = "wastebasket"
    card_index = "card_index"
    card_box = "card_box"
    card_file_box = "card_file_box"
    ballot_box = "ballot_box"
    ballot_box_with_ballot = "ballot_box_with_ballot"
    file_cabinet = "file_cabinet"
    clipboard = "clipboard"
    file_folder = "file_folder"
    open_file_folder = "open_file_folder"
    dividers = "dividers"
    card_index_dividers = "card_index_dividers"
    newspaper2 = "newspaper2"
    rolled_up_newspaper = "rolled_up_newspaper"
    newspaper = "newspaper"
    notebook = "notebook"
    notebook_with_decorative_cover = "notebook_with_decorative_cover"
    ledger = "ledger"
    closed_book = "closed_book"
    green_book = "green_book"
    blue_book = "blue_book"
    orange_book = "orange_book"
    books = "books"
    book = "book"
    bookmark = "bookmark"
    safety_pin = "safety_pin"
    link = "link"
    paperclip = "paperclip"
    paperclips = "paperclips"
    linked_paperclips = "linked_paperclips"
    triangular_ruler = "triangular_ruler"
    straight_ruler = "straight_ruler"
    abacus = "abacus"
    pushpin = "pushpin"
    round_pushpin = "round_pushpin"
    scissors = "scissors"
    pen_ballpoint = "pen_ballpoint"
    lower_left_ballpoint_pen = "lower_left_ballpoint_pen"
    pen_fountain = "pen_fountain"
    lower_left_fountain_pen = "lower_left_fountain_pen"
    black_nib = "black_nib"
    paintbrush = "paintbrush"
    lower_left_paintbrush = "lower_left_paintbrush"
    crayon = "crayon"
    lower_left_crayon = "lower_left_crayon"
    pencil = "pencil"
    memo = "memo"
    pencil2 = "pencil2"
    mag = "mag"
    mag_right = "mag_right"
    lock_with_ink_pen = "lock_with_ink_pen"
    closed_lock_with_key = "closed_lock_with_key"
    lock = "lock"
    unlock = "unlock"
    heart = "heart"
    orange_heart = "orange_heart"
    yellow_heart = "yellow_heart"
    green_heart = "green_heart"
    blue_heart = "blue_heart"
    purple_heart = "purple_heart"
    black_heart = "black_heart"
    brown_heart = "brown_heart"
    white_heart = "white_heart"
    broken_heart = "broken_heart"
    heart_exclamation = "heart_exclamation"
    heavy_heart_exclamation_mark_ornament = "heavy_heart_exclamation_mark_ornament"
    two_hearts = "two_hearts"
    revolving_hearts = "revolving_hearts"
    heartbeat = "heartbeat"
    heartpulse = "heartpulse"
    sparkling_heart = "sparkling_heart"
    cupid = "cupid"
    gift_heart = "gift_heart"
    heart_decoration = "heart_decoration"
    peace = "peace"
    peace_symbol = "peace_symbol"
    cross = "cross"
    latin_cross = "latin_cross"
    star_and_crescent = "star_and_crescent"
    om_symbol = "om_symbol"
    wheel_of_dharma = "wheel_of_dharma"
    star_of_david = "star_of_david"
    six_pointed_star = "six_pointed_star"
    menorah = "menorah"
    yin_yang = "yin_yang"
    orthodox_cross = "orthodox_cross"
    place_of_worship = "place_of_worship"
    worship_symbol = "worship_symbol"
    ophiuchus = "ophiuchus"
    aries = "aries"
    taurus = "taurus"
    gemini = "gemini"
    cancer = "cancer"
    leo = "leo"
    virgo = "virgo"
    libra = "libra"
    scorpius = "scorpius"
    sagittarius = "sagittarius"
    capricorn = "capricorn"
    aquarius = "aquarius"
    pisces = "pisces"
    id = "id"
    atom = "atom"
    atom_symbol = "atom_symbol"
    accept = "accept"
    radioactive = "radioactive"
    radioactive_sign = "radioactive_sign"
    biohazard = "biohazard"
    biohazard_sign = "biohazard_sign"
    mobile_phone_off = "mobile_phone_off"
    vibration_mode = "vibration_mode"
    u6709 = "u6709"
    u7121 = "u7121"
    u7533 = "u7533"
    u55b6 = "u55b6"
    u6708 = "u6708"
    eight_pointed_black_star = "eight_pointed_black_star"
    vs = "vs"
    white_flower = "white_flower"
    ideograph_advantage = "ideograph_advantage"
    secret = "secret"
    congratulations = "congratulations"
    u6e80 = "u6e80"
    u5272 = "u5272"
    u7981 = "u7981"
    a = "a"
    b = "b"
    ab = "ab"
    cl = "cl"
    o2 = "o2"
    sos = "sos"
    x = "x"
    o = "o"
    octagonal_sign = "octagonal_sign"
    stop_sign = "stop_sign"
    no_entry = "no_entry"
    name_badge = "name_badge"
    no_entry_sign = "no_entry_sign"
    anger = "anger"
    hotsprings = "hotsprings"
    no_pedestrians = "no_pedestrians"
    do_not_litter = "do_not_litter"
    no_bicycles = "no_bicycles"
    non_potable_water = "non_potable_water"
    underage = "underage"
    no_mobile_phones = "no_mobile_phones"
    no_smoking = "no_smoking"
    exclamation = "exclamation"
    grey_exclamation = "grey_exclamation"
    question = "question"
    grey_question = "grey_question"
    bangbang = "bangbang"
    interrobang = "interrobang"
    low_brightness = "low_brightness"
    high_brightness = "high_brightness"
    part_alternation_mark = "part_alternation_mark"
    warning = "warning"
    children_crossing = "children_crossing"
    trident = "trident"
    fleur_de_lis = "fleur_de_lis"
    beginner = "beginner"
    recycle = "recycle"
    white_check_mark = "white_check_mark"
    u6307 = "u6307"
    chart = "chart"
    sparkle = "sparkle"
    eight_spoked_asterisk = "eight_spoked_asterisk"
    negative_squared_cross_mark = "negative_squared_cross_mark"
    globe_with_meridians = "globe_with_meridians"
    diamond_shape_with_a_dot_inside = "diamond_shape_with_a_dot_inside"
    m = "m"
    cyclone = "cyclone"
    zzz = "zzz"
    atm = "atm"
    wc = "wc"
    wheelchair = "wheelchair"
    parking = "parking"
    u7a7a = "u7a7a"
    sa = "sa"
    customs = "customs"
    baggage_claim = "baggage_claim"
    left_luggage = "left_luggage"
    mens = "mens"
    womens = "womens"
    baby_symbol = "baby_symbol"
    restroom = "restroom"
    put_litter_in_its_place = "put_litter_in_its_place"
    cinema = "cinema"
    signal_strength = "signal_strength"
    koko = "koko"
    symbols = "symbols"
    information_source = "information_source"
    abc = "abc"
    abcd = "abcd"
    capital_abcd = "capital_abcd"
    ng = "ng"
    ok = "ok"
    up = "up"
    cool = "cool"
    new = "new"
    free = "free"
    zero = "zero"
    one = "one"
    two = "two"
    three = "three"
    four = "four"
    five = "five"
    six = "six"
    seven = "seven"
    eight = "eight"
    nine = "nine"
    keycap_ten = "keycap_ten"
    hash = "hash"
    keycap_asterisk = "keycap_asterisk"
    eject = "eject"
    eject_symbol = "eject_symbol"
    arrow_forward = "arrow_forward"
    pause_button = "pause_button"
    double_vertical_bar = "double_vertical_bar"
    play_pause = "play_pause"
    stop_button = "stop_button"
    record_button = "record_button"
    track_next = "track_next"
    next_track = "next_track"
    track_previous = "track_previous"
    previous_track = "previous_track"
    fast_forward = "fast_forward"
    rewind = "rewind"
    arrow_double_up = "arrow_double_up"
    arrow_double_down = "arrow_double_down"
    arrow_backward = "arrow_backward"
    arrow_up_small = "arrow_up_small"
    arrow_down_small = "arrow_down_small"
    arrow_right = "arrow_right"
    arrow_left = "arrow_left"
    arrow_up = "arrow_up"
    arrow_down = "arrow_down"
    arrow_upper_right = "arrow_upper_right"
    arrow_lower_right = "arrow_lower_right"
    arrow_lower_left = "arrow_lower_left"
    arrow_upper_left = "arrow_upper_left"
    arrow_up_down = "arrow_up_down"
    left_right_arrow = "left_right_arrow"
    arrow_right_hook = "arrow_right_hook"
    leftwards_arrow_with_hook = "leftwards_arrow_with_hook"
    arrow_heading_up = "arrow_heading_up"
    arrow_heading_down = "arrow_heading_down"
    twisted_rightwards_arrows = "twisted_rightwards_arrows"
    repeat = "repeat"
    repeat_one = "repeat_one"
    arrows_counterclockwise = "arrows_counterclockwise"
    arrows_clockwise = "arrows_clockwise"
    musical_note = "musical_note"
    notes = "notes"
    heavy_plus_sign = "heavy_plus_sign"
    heavy_minus_sign = "heavy_minus_sign"
    heavy_division_sign = "heavy_division_sign"
    heavy_multiplication_x = "heavy_multiplication_x"
    infinity = "infinity"
    heavy_dollar_sign = "heavy_dollar_sign"
    currency_exchange = "currency_exchange"
    tm = "tm"
    copyright = "copyright"
    registered = "registered"
    wavy_dash = "wavy_dash"
    curly_loop = "curly_loop"
    loop = "loop"
    end = "end"
    back = "back"
    on = "on"
    top = "top"
    soon = "soon"
    heavy_check_mark = "heavy_check_mark"
    ballot_box_with_check = "ballot_box_with_check"
    radio_button = "radio_button"
    white_circle = "white_circle"
    black_circle = "black_circle"
    red_circle = "red_circle"
    blue_circle = "blue_circle"
    brown_circle = "brown_circle"
    purple_circle = "purple_circle"
    green_circle = "green_circle"
    yellow_circle = "yellow_circle"
    orange_circle = "orange_circle"
    small_red_triangle = "small_red_triangle"
    small_red_triangle_down = "small_red_triangle_down"
    small_orange_diamond = "small_orange_diamond"
    small_blue_diamond = "small_blue_diamond"
    large_orange_diamond = "large_orange_diamond"
    large_blue_diamond = "large_blue_diamond"
    white_square_button = "white_square_button"
    black_square_button = "black_square_button"
    black_small_square = "black_small_square"
    white_small_square = "white_small_square"
    black_medium_small_square = "black_medium_small_square"
    white_medium_small_square = "white_medium_small_square"
    black_medium_square = "black_medium_square"
    white_medium_square = "white_medium_square"
    black_large_square = "black_large_square"
    white_large_square = "white_large_square"
    orange_square = "orange_square"
    blue_square = "blue_square"
    red_square = "red_square"
    brown_square = "brown_square"
    purple_square = "purple_square"
    green_square = "green_square"
    yellow_square = "yellow_square"
    speaker = "speaker"
    mute = "mute"
    sound = "sound"
    loud_sound = "loud_sound"
    bell = "bell"
    no_bell = "no_bell"
    mega = "mega"
    loudspeaker = "loudspeaker"
    speech_left = "speech_left"
    left_speech_bubble = "left_speech_bubble"
    eye_in_speech_bubble = "eye_in_speech_bubble"
    speech_balloon = "speech_balloon"
    thought_balloon = "thought_balloon"
    anger_right = "anger_right"
    right_anger_bubble = "right_anger_bubble"
    spades = "spades"
    clubs = "clubs"
    hearts = "hearts"
    diamonds = "diamonds"
    black_joker = "black_joker"
    flower_playing_cards = "flower_playing_cards"
    mahjong = "mahjong"
    clock1 = "clock1"
    clock2 = "clock2"
    clock3 = "clock3"
    clock4 = "clock4"
    clock5 = "clock5"
    clock6 = "clock6"
    clock7 = "clock7"
    clock8 = "clock8"
    clock9 = "clock9"
    clock10 = "clock10"
    clock11 = "clock11"
    clock12 = "clock12"
    clock130 = "clock130"
    clock230 = "clock230"
    clock330 = "clock330"
    clock430 = "clock430"
    clock530 = "clock530"
    clock630 = "clock630"
    clock730 = "clock730"
    clock830 = "clock830"
    clock930 = "clock930"
    clock1030 = "clock1030"
    clock1130 = "clock1130"
    clock1230 = "clock1230"
    female_sign = "female_sign"
    male_sign = "male_sign"
    medical_symbol = "medical_symbol"
    regional_indicator_z = "regional_indicator_z"
    regional_indicator_y = "regional_indicator_y"
    regional_indicator_x = "regional_indicator_x"
    regional_indicator_w = "regional_indicator_w"
    regional_indicator_v = "regional_indicator_v"
    regional_indicator_u = "regional_indicator_u"
    regional_indicator_t = "regional_indicator_t"
    regional_indicator_s = "regional_indicator_s"
    regional_indicator_r = "regional_indicator_r"
    regional_indicator_q = "regional_indicator_q"
    regional_indicator_p = "regional_indicator_p"
    regional_indicator_o = "regional_indicator_o"
    regional_indicator_n = "regional_indicator_n"
    regional_indicator_m = "regional_indicator_m"
    regional_indicator_l = "regional_indicator_l"
    regional_indicator_k = "regional_indicator_k"
    regional_indicator_j = "regional_indicator_j"
    regional_indicator_i = "regional_indicator_i"
    regional_indicator_h = "regional_indicator_h"
    regional_indicator_g = "regional_indicator_g"
    regional_indicator_f = "regional_indicator_f"
    regional_indicator_e = "regional_indicator_e"
    regional_indicator_d = "regional_indicator_d"
    regional_indicator_c = "regional_indicator_c"
    regional_indicator_b = "regional_indicator_b"
    regional_indicator_a = "regional_indicator_a"
    flag_white = "flag_white"
    flag_black = "flag_black"
    checkered_flag = "checkered_flag"
    triangular_flag_on_post = "triangular_flag_on_post"
    rainbow_flag = "rainbow_flag"
    gay_pride_flag = "gay_pride_flag"
    pirate_flag = "pirate_flag"
    flag_af = "flag_af"
    flag_ax = "flag_ax"
    flag_al = "flag_al"
    flag_dz = "flag_dz"
    flag_as = "flag_as"
    flag_ad = "flag_ad"
    flag_ao = "flag_ao"
    flag_ai = "flag_ai"
    flag_aq = "flag_aq"
    flag_ag = "flag_ag"
    flag_ar = "flag_ar"
    flag_am = "flag_am"
    flag_aw = "flag_aw"
    flag_au = "flag_au"
    flag_at = "flag_at"
    flag_az = "flag_az"
    flag_bs = "flag_bs"
    flag_bh = "flag_bh"
    flag_bd = "flag_bd"
    flag_bb = "flag_bb"
    flag_by = "flag_by"
    flag_be = "flag_be"
    flag_bz = "flag_bz"
    flag_bj = "flag_bj"
    flag_bm = "flag_bm"
    flag_bt = "flag_bt"
    flag_bo = "flag_bo"
    flag_ba = "flag_ba"
    flag_bw = "flag_bw"
    flag_br = "flag_br"
    flag_io = "flag_io"
    flag_vg = "flag_vg"
    flag_bn = "flag_bn"
    flag_bg = "flag_bg"
    flag_bf = "flag_bf"
    flag_bi = "flag_bi"
    flag_kh = "flag_kh"
    flag_cm = "flag_cm"
    flag_ca = "flag_ca"
    flag_ic = "flag_ic"
    flag_cv = "flag_cv"
    flag_bq = "flag_bq"
    flag_ky = "flag_ky"
    flag_cf = "flag_cf"
    flag_td = "flag_td"
    flag_cl = "flag_cl"
    flag_cn = "flag_cn"
    flag_cx = "flag_cx"
    flag_cc = "flag_cc"
    flag_co = "flag_co"
    flag_km = "flag_km"
    flag_cg = "flag_cg"
    flag_cd = "flag_cd"
    flag_ck = "flag_ck"
    flag_cr = "flag_cr"
    flag_ci = "flag_ci"
    flag_hr = "flag_hr"
    flag_cu = "flag_cu"
    flag_cw = "flag_cw"
    flag_cy = "flag_cy"
    flag_cz = "flag_cz"
    flag_dk = "flag_dk"
    flag_dj = "flag_dj"
    flag_dm = "flag_dm"
    flag_do = "flag_do"
    flag_ec = "flag_ec"
    flag_eg = "flag_eg"
    flag_sv = "flag_sv"
    flag_gq = "flag_gq"
    flag_er = "flag_er"
    flag_ee = "flag_ee"
    flag_et = "flag_et"
    flag_eu = "flag_eu"
    flag_fk = "flag_fk"
    flag_fo = "flag_fo"
    flag_fj = "flag_fj"
    flag_fi = "flag_fi"
    flag_fr = "flag_fr"
    flag_gf = "flag_gf"
    flag_pf = "flag_pf"
    flag_tf = "flag_tf"
    flag_ga = "flag_ga"
    flag_gm = "flag_gm"
    flag_ge = "flag_ge"
    flag_de = "flag_de"
    flag_gh = "flag_gh"
    flag_gi = "flag_gi"
    flag_gr = "flag_gr"
    flag_gl = "flag_gl"
    flag_gd = "flag_gd"
    flag_gp = "flag_gp"
    flag_gu = "flag_gu"
    flag_gt = "flag_gt"
    flag_gg = "flag_gg"
    flag_gn = "flag_gn"
    flag_gw = "flag_gw"
    flag_gy = "flag_gy"
    flag_ht = "flag_ht"
    flag_hn = "flag_hn"
    flag_hk = "flag_hk"
    flag_hu = "flag_hu"
    flag_is = "flag_is"
    flag_in = "flag_in"
    flag_id = "flag_id"
    flag_ir = "flag_ir"
    flag_iq = "flag_iq"
    flag_ie = "flag_ie"
    flag_im = "flag_im"
    flag_il = "flag_il"
    flag_it = "flag_it"
    flag_jm = "flag_jm"
    flag_jp = "flag_jp"
    crossed_flags = "crossed_flags"
    flag_je = "flag_je"
    flag_jo = "flag_jo"
    flag_kz = "flag_kz"
    flag_ke = "flag_ke"
    flag_ki = "flag_ki"
    flag_xk = "flag_xk"
    flag_kw = "flag_kw"
    flag_kg = "flag_kg"
    flag_la = "flag_la"
    flag_lv = "flag_lv"
    flag_lb = "flag_lb"
    flag_ls = "flag_ls"
    flag_lr = "flag_lr"
    flag_ly = "flag_ly"
    flag_li = "flag_li"
    flag_lt = "flag_lt"
    flag_lu = "flag_lu"
    flag_mo = "flag_mo"
    flag_mk = "flag_mk"
    flag_mg = "flag_mg"
    flag_mw = "flag_mw"
    flag_my = "flag_my"
    flag_mv = "flag_mv"
    flag_ml = "flag_ml"
    flag_mt = "flag_mt"
    flag_mh = "flag_mh"
    flag_mq = "flag_mq"
    flag_mr = "flag_mr"
    flag_mu = "flag_mu"
    flag_yt = "flag_yt"
    flag_mx = "flag_mx"
    flag_fm = "flag_fm"
    flag_md = "flag_md"
    flag_mc = "flag_mc"
    flag_mn = "flag_mn"
    flag_me = "flag_me"
    flag_ms = "flag_ms"
    flag_ma = "flag_ma"
    flag_mz = "flag_mz"
    flag_mm = "flag_mm"
    flag_na = "flag_na"
    flag_nr = "flag_nr"
    flag_np = "flag_np"
    flag_nl = "flag_nl"
    flag_nc = "flag_nc"
    flag_nz = "flag_nz"
    flag_ni = "flag_ni"
    flag_ne = "flag_ne"
    flag_ng = "flag_ng"
    flag_nu = "flag_nu"
    flag_nf = "flag_nf"
    flag_kp = "flag_kp"
    flag_mp = "flag_mp"
    flag_no = "flag_no"
    flag_om = "flag_om"
    flag_pk = "flag_pk"
    flag_pw = "flag_pw"
    flag_ps = "flag_ps"
    flag_pa = "flag_pa"
    flag_pg = "flag_pg"
    flag_py = "flag_py"
    flag_pe = "flag_pe"
    flag_ph = "flag_ph"
    flag_pn = "flag_pn"
    flag_pl = "flag_pl"
    flag_pt = "flag_pt"
    flag_pr = "flag_pr"
    flag_qa = "flag_qa"
    flag_re = "flag_re"
    flag_ro = "flag_ro"
    flag_ru = "flag_ru"
    flag_rw = "flag_rw"
    flag_ws = "flag_ws"
    flag_sm = "flag_sm"
    flag_st = "flag_st"
    flag_sa = "flag_sa"
    flag_sn = "flag_sn"
    flag_rs = "flag_rs"
    flag_sc = "flag_sc"
    flag_sl = "flag_sl"
    flag_sg = "flag_sg"
    flag_sx = "flag_sx"
    flag_sk = "flag_sk"
    flag_si = "flag_si"
    flag_gs = "flag_gs"
    flag_sb = "flag_sb"
    flag_so = "flag_so"
    flag_za = "flag_za"
    flag_kr = "flag_kr"
    flag_ss = "flag_ss"
    flag_es = "flag_es"
    flag_lk = "flag_lk"
    flag_bl = "flag_bl"
    flag_sh = "flag_sh"
    flag_kn = "flag_kn"
    flag_lc = "flag_lc"
    flag_pm = "flag_pm"
    flag_vc = "flag_vc"
    flag_sd = "flag_sd"
    flag_sr = "flag_sr"
    flag_sz = "flag_sz"
    flag_se = "flag_se"
    flag_ch = "flag_ch"
    flag_sy = "flag_sy"
    flag_tw = "flag_tw"
    flag_tj = "flag_tj"
    flag_tz = "flag_tz"
    flag_th = "flag_th"
    flag_tl = "flag_tl"
    flag_tg = "flag_tg"
    flag_tk = "flag_tk"
    flag_to = "flag_to"
    flag_tt = "flag_tt"
    flag_tn = "flag_tn"
    flag_tr = "flag_tr"
    flag_tm = "flag_tm"
    flag_tc = "flag_tc"
    flag_vi = "flag_vi"
    flag_tv = "flag_tv"
    flag_ug = "flag_ug"
    flag_ua = "flag_ua"
    flag_ae = "flag_ae"
    flag_gb = "flag_gb"
    england = "england"
    scotland = "scotland"
    wales = "wales"
    flag_us = "flag_us"
    flag_uy = "flag_uy"
    flag_uz = "flag_uz"
    flag_vu = "flag_vu"
    flag_va = "flag_va"
    flag_ve = "flag_ve"
    flag_vn = "flag_vn"
    flag_wf = "flag_wf"
    flag_eh = "flag_eh"
    flag_ye = "flag_ye"
    flag_zm = "flag_zm"
    flag_zw = "flag_zw"
    flag_ac = "flag_ac"
    flag_bv = "flag_bv"
    flag_cp = "flag_cp"
    flag_ea = "flag_ea"
    flag_dg = "flag_dg"
    flag_hm = "flag_hm"
    flag_mf = "flag_mf"
    flag_sj = "flag_sj"
    flag_ta = "flag_ta"
    flag_um = "flag_um"
    united_nations = "united_nations"
