from enum import Enum


__all__ = (
    "discord_emoji_converter",
    "discord_emoji_converter_inverse",
    "EmojiUnicodeType",
    "EmojiNameType",
)


discord_emoji_converter = {
    "100": "💯",
    "1234": "🔢",
    "grinning": "😀",
    "smiley": "😃",
    "smile": "😄",
    "grin": "😁",
    "laughing": "😆",
    "satisfied": "😆",
    "sweat_smile": "😅",
    "joy": "😂",
    "rofl": "🤣",
    "rolling_on_the_floor_laughing": "🤣",
    "relaxed": "☺",
    "blush": "😊",
    "innocent": "😇",
    "slight_smile": "🙂",
    "slightly_smiling_face": "🙂",
    "upside_down": "🙃",
    "upside_down_face": "🙃",
    "wink": "😉",
    "relieved": "😌",
    "heart_eyes": "😍",
    "smiling_face_with_3_hearts": "🥰",
    "kissing_heart": "😘",
    "kissing": "😗",
    "kissing_smiling_eyes": "😙",
    "kissing_closed_eyes": "😚",
    "yum": "😋",
    "stuck_out_tongue": "😛",
    "stuck_out_tongue_closed_eyes": "😝",
    "stuck_out_tongue_winking_eye": "😜",
    "zany_face": "🤪",
    "face_with_raised_eyebrow": "🤨",
    "face_with_monocle": "🧐",
    "nerd": "🤓",
    "nerd_face": "🤓",
    "sunglasses": "😎",
    "star_struck": "🤩",
    "partying_face": "🥳",
    "smirk": "😏",
    "unamused": "😒",
    "disappointed": "😞",
    "pensive": "😔",
    "worried": "😟",
    "confused": "😕",
    "slight_frown": "🙁",
    "slightly_frowning_face": "🙁",
    "frowning2": "☹",
    "white_frowning_face": "☹",
    "persevere": "😣",
    "confounded": "😖",
    "tired_face": "😫",
    "weary": "😩",
    "pleading_face": "🥺",
    "cry": "😢",
    "sob": "😭",
    "triumph": "😤",
    "angry": "😠",
    "rage": "😡",
    "face_with_symbols_over_mouth": "🤬",
    "exploding_head": "🤯",
    "flushed": "😳",
    "hot_face": "🥵",
    "cold_face": "🥶",
    "scream": "😱",
    "fearful": "😨",
    "cold_sweat": "😰",
    "disappointed_relieved": "😥",
    "sweat": "😓",
    "hugging": "🤗",
    "hugging_face": "🤗",
    "thinking": "🤔",
    "thinking_face": "🤔",
    "face_with_hand_over_mouth": "🤭",
    "yawning_face": "🥱",
    "shushing_face": "🤫",
    "lying_face": "🤥",
    "liar": "🤥",
    "no_mouth": "😶",
    "neutral_face": "😐",
    "expressionless": "😑",
    "grimacing": "😬",
    "rolling_eyes": "🙄",
    "face_with_rolling_eyes": "🙄",
    "hushed": "😯",
    "frowning": "😦",
    "anguished": "😧",
    "open_mouth": "😮",
    "astonished": "😲",
    "sleeping": "😴",
    "drooling_face": "🤤",
    "drool": "🤤",
    "sleepy": "😪",
    "dizzy_face": "😵",
    "zipper_mouth": "🤐",
    "zipper_mouth_face": "🤐",
    "woozy_face": "🥴",
    "nauseated_face": "🤢",
    "sick": "🤢",
    "face_vomiting": "🤮",
    "sneezing_face": "🤧",
    "sneeze": "🤧",
    "mask": "😷",
    "thermometer_face": "🤒",
    "face_with_thermometer": "🤒",
    "head_bandage": "🤕",
    "face_with_head_bandage": "🤕",
    "money_mouth": "🤑",
    "money_mouth_face": "🤑",
    "cowboy": "🤠",
    "face_with_cowboy_hat": "🤠",
    "smiling_imp": "😈",
    "imp": "👿",
    "japanese_ogre": "👹",
    "japanese_goblin": "👺",
    "clown": "🤡",
    "clown_face": "🤡",
    "poop": "💩",
    "shit": "💩",
    "hankey": "💩",
    "poo": "💩",
    "ghost": "👻",
    "skull": "💀",
    "skeleton": "💀",
    "skull_crossbones": "☠",
    "skull_and_crossbones": "☠",
    "alien": "👽",
    "space_invader": "👾",
    "robot": "🤖",
    "robot_face": "🤖",
    "jack_o_lantern": "🎃",
    "smiley_cat": "😺",
    "smile_cat": "😸",
    "joy_cat": "😹",
    "heart_eyes_cat": "😻",
    "smirk_cat": "😼",
    "kissing_cat": "😽",
    "scream_cat": "🙀",
    "crying_cat_face": "😿",
    "pouting_cat": "😾",
    "palms_up_together": "🤲",
    "palms_up_together_tone1": "🤲🏻",
    "palms_up_together_light_skin_tone": "🤲🏻",
    "palms_up_together_tone2": "🤲🏼",
    "palms_up_together_medium_light_skin_tone": "🤲🏼",
    "palms_up_together_tone3": "🤲🏽",
    "palms_up_together_medium_skin_tone": "🤲🏽",
    "palms_up_together_tone4": "🤲🏾",
    "palms_up_together_medium_dark_skin_tone": "🤲🏾",
    "palms_up_together_tone5": "🤲🏿",
    "palms_up_together_dark_skin_tone": "🤲🏿",
    "open_hands": "👐",
    "open_hands_tone1": "👐🏻",
    "open_hands_tone2": "👐🏼",
    "open_hands_tone3": "👐🏽",
    "open_hands_tone4": "👐🏾",
    "open_hands_tone5": "👐🏿",
    "raised_hands": "🙌",
    "raised_hands_tone1": "🙌🏻",
    "raised_hands_tone2": "🙌🏼",
    "raised_hands_tone3": "🙌🏽",
    "raised_hands_tone4": "🙌🏾",
    "raised_hands_tone5": "🙌🏿",
    "clap": "👏",
    "clap_tone1": "👏🏻",
    "clap_tone2": "👏🏼",
    "clap_tone3": "👏🏽",
    "clap_tone4": "👏🏾",
    "clap_tone5": "👏🏿",
    "handshake": "🤝",
    "shaking_hands": "🤝",
    "thumbsup": "👍",
    "+1": "👍",
    "thumbup": "👍",
    "thumbsup_tone1": "👍🏻",
    "+1_tone1": "👍🏻",
    "thumbup_tone1": "👍🏻",
    "thumbsup_tone2": "👍🏼",
    "+1_tone2": "👍🏼",
    "thumbup_tone2": "👍🏼",
    "thumbsup_tone3": "👍🏽",
    "+1_tone3": "👍🏽",
    "thumbup_tone3": "👍🏽",
    "thumbsup_tone4": "👍🏾",
    "+1_tone4": "👍🏾",
    "thumbup_tone4": "👍🏾",
    "thumbsup_tone5": "👍🏿",
    "+1_tone5": "👍🏿",
    "thumbup_tone5": "👍🏿",
    "thumbsdown": "👎",
    "-1": "👎",
    "thumbdown": "👎",
    "thumbsdown_tone1": "👎🏻",
    "_1_tone1": "👎🏻",
    "thumbdown_tone1": "👎🏻",
    "thumbsdown_tone2": "👎🏼",
    "_1_tone2": "👎🏼",
    "thumbdown_tone2": "👎🏼",
    "thumbsdown_tone3": "👎🏽",
    "_1_tone3": "👎🏽",
    "thumbdown_tone3": "👎🏽",
    "thumbsdown_tone4": "👎🏾",
    "_1_tone4": "👎🏾",
    "thumbdown_tone4": "👎🏾",
    "thumbsdown_tone5": "👎🏿",
    "_1_tone5": "👎🏿",
    "thumbdown_tone5": "👎🏿",
    "punch": "👊",
    "punch_tone1": "👊🏻",
    "punch_tone2": "👊🏼",
    "punch_tone3": "👊🏽",
    "punch_tone4": "👊🏾",
    "punch_tone5": "👊🏿",
    "fist": "✊",
    "fist_tone1": "✊🏻",
    "fist_tone2": "✊🏼",
    "fist_tone3": "✊🏽",
    "fist_tone4": "✊🏾",
    "fist_tone5": "✊🏿",
    "left_facing_fist": "🤛",
    "left_fist": "🤛",
    "left_facing_fist_tone1": "🤛🏻",
    "left_fist_tone1": "🤛🏻",
    "left_facing_fist_tone2": "🤛🏼",
    "left_fist_tone2": "🤛🏼",
    "left_facing_fist_tone3": "🤛🏽",
    "left_fist_tone3": "🤛🏽",
    "left_facing_fist_tone4": "🤛🏾",
    "left_fist_tone4": "🤛🏾",
    "left_facing_fist_tone5": "🤛🏿",
    "left_fist_tone5": "🤛🏿",
    "right_facing_fist": "🤜",
    "right_fist": "🤜",
    "right_facing_fist_tone1": "🤜🏻",
    "right_fist_tone1": "🤜🏻",
    "right_facing_fist_tone2": "🤜🏼",
    "right_fist_tone2": "🤜🏼",
    "right_facing_fist_tone3": "🤜🏽",
    "right_fist_tone3": "🤜🏽",
    "right_facing_fist_tone4": "🤜🏾",
    "right_fist_tone4": "🤜🏾",
    "right_facing_fist_tone5": "🤜🏿",
    "right_fist_tone5": "🤜🏿",
    "fingers_crossed": "🤞",
    "hand_with_index_and_middle_finger_crossed": "🤞",
    "fingers_crossed_tone1": "🤞🏻",
    "hand_with_index_and_middle_fingers_crossed_tone1": "🤞🏻",
    "fingers_crossed_tone2": "🤞🏼",
    "hand_with_index_and_middle_fingers_crossed_tone2": "🤞🏼",
    "fingers_crossed_tone3": "🤞🏽",
    "hand_with_index_and_middle_fingers_crossed_tone3": "🤞🏽",
    "fingers_crossed_tone4": "🤞🏾",
    "hand_with_index_and_middle_fingers_crossed_tone4": "🤞🏾",
    "fingers_crossed_tone5": "🤞🏿",
    "hand_with_index_and_middle_fingers_crossed_tone5": "🤞🏿",
    "v": "✌",
    "v_tone1": "✌🏻",
    "v_tone2": "✌🏼",
    "v_tone3": "✌🏽",
    "v_tone4": "✌🏾",
    "v_tone5": "✌🏿",
    "love_you_gesture": "🤟",
    "love_you_gesture_tone1": "🤟🏻",
    "love_you_gesture_light_skin_tone": "🤟🏻",
    "love_you_gesture_tone2": "🤟🏼",
    "love_you_gesture_medium_light_skin_tone": "🤟🏼",
    "love_you_gesture_tone3": "🤟🏽",
    "love_you_gesture_medium_skin_tone": "🤟🏽",
    "love_you_gesture_tone4": "🤟🏾",
    "love_you_gesture_medium_dark_skin_tone": "🤟🏾",
    "love_you_gesture_tone5": "🤟🏿",
    "love_you_gesture_dark_skin_tone": "🤟🏿",
    "metal": "🤘",
    "sign_of_the_horns": "🤘",
    "metal_tone1": "🤘🏻",
    "sign_of_the_horns_tone1": "🤘🏻",
    "metal_tone2": "🤘🏼",
    "sign_of_the_horns_tone2": "🤘🏼",
    "metal_tone3": "🤘🏽",
    "sign_of_the_horns_tone3": "🤘🏽",
    "metal_tone4": "🤘🏾",
    "sign_of_the_horns_tone4": "🤘🏾",
    "metal_tone5": "🤘🏿",
    "sign_of_the_horns_tone5": "🤘🏿",
    "ok_hand": "👌",
    "ok_hand_tone1": "👌🏻",
    "ok_hand_tone2": "👌🏼",
    "ok_hand_tone3": "👌🏽",
    "ok_hand_tone4": "👌🏾",
    "ok_hand_tone5": "👌🏿",
    "pinching_hand": "🤏",
    "pinching_hand_tone1": "🤏🏻",
    "pinching_hand_light_skin_tone": "🤏🏻",
    "pinching_hand_tone2": "🤏🏼",
    "pinching_hand_medium_light_skin_tone": "🤏🏼",
    "pinching_hand_tone3": "🤏🏽",
    "pinching_hand_medium_skin_tone": "🤏🏽",
    "pinching_hand_tone4": "🤏🏾",
    "pinching_hand_medium_dark_skin_tone": "🤏🏾",
    "pinching_hand_tone5": "🤏🏿",
    "pinching_hand_dark_skin_tone": "🤏🏿",
    "point_left": "👈",
    "point_left_tone1": "👈🏻",
    "point_left_tone2": "👈🏼",
    "point_left_tone3": "👈🏽",
    "point_left_tone4": "👈🏾",
    "point_left_tone5": "👈🏿",
    "point_right": "👉",
    "point_right_tone1": "👉🏻",
    "point_right_tone2": "👉🏼",
    "point_right_tone3": "👉🏽",
    "point_right_tone4": "👉🏾",
    "point_right_tone5": "👉🏿",
    "point_up_2": "👆",
    "point_up_2_tone1": "👆🏻",
    "point_up_2_tone2": "👆🏼",
    "point_up_2_tone3": "👆🏽",
    "point_up_2_tone4": "👆🏾",
    "point_up_2_tone5": "👆🏿",
    "point_down": "👇",
    "point_down_tone1": "👇🏻",
    "point_down_tone2": "👇🏼",
    "point_down_tone3": "👇🏽",
    "point_down_tone4": "👇🏾",
    "point_down_tone5": "👇🏿",
    "point_up": "☝",
    "point_up_tone1": "☝🏻",
    "point_up_tone2": "☝🏼",
    "point_up_tone3": "☝🏽",
    "point_up_tone4": "☝🏾",
    "point_up_tone5": "☝🏿",
    "raised_hand": "✋",
    "raised_hand_tone1": "✋🏻",
    "raised_hand_tone2": "✋🏼",
    "raised_hand_tone3": "✋🏽",
    "raised_hand_tone4": "✋🏾",
    "raised_hand_tone5": "✋🏿",
    "raised_back_of_hand": "🤚",
    "back_of_hand": "🤚",
    "raised_back_of_hand_tone1": "🤚🏻",
    "back_of_hand_tone1": "🤚🏻",
    "raised_back_of_hand_tone2": "🤚🏼",
    "back_of_hand_tone2": "🤚🏼",
    "raised_back_of_hand_tone3": "🤚🏽",
    "back_of_hand_tone3": "🤚🏽",
    "raised_back_of_hand_tone4": "🤚🏾",
    "back_of_hand_tone4": "🤚🏾",
    "raised_back_of_hand_tone5": "🤚🏿",
    "back_of_hand_tone5": "🤚🏿",
    "hand_splayed": "🖐",
    "raised_hand_with_fingers_splayed": "🖐",
    "hand_splayed_tone1": "🖐🏻",
    "raised_hand_with_fingers_splayed_tone1": "🖐🏻",
    "hand_splayed_tone2": "🖐🏼",
    "raised_hand_with_fingers_splayed_tone2": "🖐🏼",
    "hand_splayed_tone3": "🖐🏽",
    "raised_hand_with_fingers_splayed_tone3": "🖐🏽",
    "hand_splayed_tone4": "🖐🏾",
    "raised_hand_with_fingers_splayed_tone4": "🖐🏾",
    "hand_splayed_tone5": "🖐🏿",
    "raised_hand_with_fingers_splayed_tone5": "🖐🏿",
    "vulcan": "🖖",
    "raised_hand_with_part_between_middle_and_ring_fingers": "🖖",
    "vulcan_tone1": "🖖🏻",
    "raised_hand_with_part_between_middle_and_ring_fingers_tone1": "🖖🏻",
    "vulcan_tone2": "🖖🏼",
    "raised_hand_with_part_between_middle_and_ring_fingers_tone2": "🖖🏼",
    "vulcan_tone3": "🖖🏽",
    "raised_hand_with_part_between_middle_and_ring_fingers_tone3": "🖖🏽",
    "vulcan_tone4": "🖖🏾",
    "raised_hand_with_part_between_middle_and_ring_fingers_tone4": "🖖🏾",
    "vulcan_tone5": "🖖🏿",
    "raised_hand_with_part_between_middle_and_ring_fingers_tone5": "🖖🏿",
    "wave": "👋",
    "wave_tone1": "👋🏻",
    "wave_tone2": "👋🏼",
    "wave_tone3": "👋🏽",
    "wave_tone4": "👋🏾",
    "wave_tone5": "👋🏿",
    "call_me": "🤙",
    "call_me_hand": "🤙",
    "call_me_tone1": "🤙🏻",
    "call_me_hand_tone1": "🤙🏻",
    "call_me_tone2": "🤙🏼",
    "call_me_hand_tone2": "🤙🏼",
    "call_me_tone3": "🤙🏽",
    "call_me_hand_tone3": "🤙🏽",
    "call_me_tone4": "🤙🏾",
    "call_me_hand_tone4": "🤙🏾",
    "call_me_tone5": "🤙🏿",
    "call_me_hand_tone5": "🤙🏿",
    "muscle": "💪",
    "muscle_tone1": "💪🏻",
    "muscle_tone2": "💪🏼",
    "muscle_tone3": "💪🏽",
    "muscle_tone4": "💪🏾",
    "muscle_tone5": "💪🏿",
    "mechanical_arm": "🦾",
    "middle_finger": "🖕",
    "reversed_hand_with_middle_finger_extended": "🖕",
    "middle_finger_tone1": "🖕🏻",
    "reversed_hand_with_middle_finger_extended_tone1": "🖕🏻",
    "middle_finger_tone2": "🖕🏼",
    "reversed_hand_with_middle_finger_extended_tone2": "🖕🏼",
    "middle_finger_tone3": "🖕🏽",
    "reversed_hand_with_middle_finger_extended_tone3": "🖕🏽",
    "middle_finger_tone4": "🖕🏾",
    "reversed_hand_with_middle_finger_extended_tone4": "🖕🏾",
    "middle_finger_tone5": "🖕🏿",
    "reversed_hand_with_middle_finger_extended_tone5": "🖕🏿",
    "writing_hand": "✍",
    "writing_hand_tone1": "✍🏻",
    "writing_hand_tone2": "✍🏼",
    "writing_hand_tone3": "✍🏽",
    "writing_hand_tone4": "✍🏾",
    "writing_hand_tone5": "✍🏿",
    "pray": "🙏",
    "pray_tone1": "🙏🏻",
    "pray_tone2": "🙏🏼",
    "pray_tone3": "🙏🏽",
    "pray_tone4": "🙏🏾",
    "pray_tone5": "🙏🏿",
    "foot": "🦶",
    "foot_tone1": "🦶🏻",
    "foot_light_skin_tone": "🦶🏻",
    "foot_tone2": "🦶🏼",
    "foot_medium_light_skin_tone": "🦶🏼",
    "foot_tone3": "🦶🏽",
    "foot_medium_skin_tone": "🦶🏽",
    "foot_tone4": "🦶🏾",
    "foot_medium_dark_skin_tone": "🦶🏾",
    "foot_tone5": "🦶🏿",
    "foot_dark_skin_tone": "🦶🏿",
    "leg": "🦵",
    "leg_tone1": "🦵🏻",
    "leg_light_skin_tone": "🦵🏻",
    "leg_tone2": "🦵🏼",
    "leg_medium_light_skin_tone": "🦵🏼",
    "leg_tone3": "🦵🏽",
    "leg_medium_skin_tone": "🦵🏽",
    "leg_tone4": "🦵🏾",
    "leg_medium_dark_skin_tone": "🦵🏾",
    "leg_tone5": "🦵🏿",
    "leg_dark_skin_tone": "🦵🏿",
    "mechanical_leg": "🦿",
    "lipstick": "💄",
    "kiss": "💋",
    "lips": "👄",
    "tooth": "🦷",
    "bone": "🦴",
    "tongue": "👅",
    "ear": "👂",
    "ear_tone1": "👂🏻",
    "ear_tone2": "👂🏼",
    "ear_tone3": "👂🏽",
    "ear_tone4": "👂🏾",
    "ear_tone5": "👂🏿",
    "ear_with_hearing_aid": "🦻",
    "ear_with_hearing_aid_tone1": "🦻🏻",
    "ear_with_hearing_aid_light_skin_tone": "🦻🏻",
    "ear_with_hearing_aid_tone2": "🦻🏼",
    "ear_with_hearing_aid_medium_light_skin_tone": "🦻🏼",
    "ear_with_hearing_aid_tone3": "🦻🏽",
    "ear_with_hearing_aid_medium_skin_tone": "🦻🏽",
    "ear_with_hearing_aid_tone4": "🦻🏾",
    "ear_with_hearing_aid_medium_dark_skin_tone": "🦻🏾",
    "ear_with_hearing_aid_tone5": "🦻🏿",
    "ear_with_hearing_aid_dark_skin_tone": "🦻🏿",
    "nose": "👃",
    "nose_tone1": "👃🏻",
    "nose_tone2": "👃🏼",
    "nose_tone3": "👃🏽",
    "nose_tone4": "👃🏾",
    "nose_tone5": "👃🏿",
    "footprints": "👣",
    "eye": "👁",
    "eyes": "👀",
    "brain": "🧠",
    "speaking_head": "🗣",
    "speaking_head_in_silhouette": "🗣",
    "bust_in_silhouette": "👤",
    "busts_in_silhouette": "👥",
    "baby": "👶",
    "baby_tone1": "👶🏻",
    "baby_tone2": "👶🏼",
    "baby_tone3": "👶🏽",
    "baby_tone4": "👶🏾",
    "baby_tone5": "👶🏿",
    "girl": "👧",
    "girl_tone1": "👧🏻",
    "girl_tone2": "👧🏼",
    "girl_tone3": "👧🏽",
    "girl_tone4": "👧🏾",
    "girl_tone5": "👧🏿",
    "child": "🧒",
    "child_tone1": "🧒🏻",
    "child_light_skin_tone": "🧒🏻",
    "child_tone2": "🧒🏼",
    "child_medium_light_skin_tone": "🧒🏼",
    "child_tone3": "🧒🏽",
    "child_medium_skin_tone": "🧒🏽",
    "child_tone4": "🧒🏾",
    "child_medium_dark_skin_tone": "🧒🏾",
    "child_tone5": "🧒🏿",
    "child_dark_skin_tone": "🧒🏿",
    "boy": "👦",
    "boy_tone1": "👦🏻",
    "boy_tone2": "👦🏼",
    "boy_tone3": "👦🏽",
    "boy_tone4": "👦🏾",
    "boy_tone5": "👦🏿",
    "woman": "👩",
    "woman_tone1": "👩🏻",
    "woman_tone2": "👩🏼",
    "woman_tone3": "👩🏽",
    "woman_tone4": "👩🏾",
    "woman_tone5": "👩🏿",
    "adult": "🧑",
    "adult_tone1": "🧑🏻",
    "adult_light_skin_tone": "🧑🏻",
    "adult_tone2": "🧑🏼",
    "adult_medium_light_skin_tone": "🧑🏼",
    "adult_tone3": "🧑🏽",
    "adult_medium_skin_tone": "🧑🏽",
    "adult_tone4": "🧑🏾",
    "adult_medium_dark_skin_tone": "🧑🏾",
    "adult_tone5": "🧑🏿",
    "adult_dark_skin_tone": "🧑🏿",
    "man": "👨",
    "man_tone1": "👨🏻",
    "man_tone2": "👨🏼",
    "man_tone3": "👨🏽",
    "man_tone4": "👨🏾",
    "man_tone5": "👨🏿",
    "woman_curly_haired": "👩🦱",
    "woman_curly_haired_tone1": "👩🏻🦱",
    "woman_curly_haired_light_skin_tone": "👩🏻🦱",
    "woman_curly_haired_tone2": "👩🏼🦱",
    "woman_curly_haired_medium_light_skin_tone": "👩🏼🦱",
    "woman_curly_haired_tone3": "👩🏽🦱",
    "woman_curly_haired_medium_skin_tone": "👩🏽🦱",
    "woman_curly_haired_tone4": "👩🏾🦱",
    "woman_curly_haired_medium_dark_skin_tone": "👩🏾🦱",
    "woman_curly_haired_tone5": "👩🏿🦱",
    "woman_curly_haired_dark_skin_tone": "👩🏿🦱",
    "man_curly_haired": "👨🦱",
    "man_curly_haired_tone1": "👨🏻🦱",
    "man_curly_haired_light_skin_tone": "👨🏻🦱",
    "man_curly_haired_tone2": "👨🏼🦱",
    "man_curly_haired_medium_light_skin_tone": "👨🏼🦱",
    "man_curly_haired_tone3": "👨🏽🦱",
    "man_curly_haired_medium_skin_tone": "👨🏽🦱",
    "man_curly_haired_tone4": "👨🏾🦱",
    "man_curly_haired_medium_dark_skin_tone": "👨🏾🦱",
    "man_curly_haired_tone5": "👨🏿🦱",
    "man_curly_haired_dark_skin_tone": "👨🏿🦱",
    "woman_red_haired": "👩🦰",
    "woman_red_haired_tone1": "👩🏻🦰",
    "woman_red_haired_light_skin_tone": "👩🏻🦰",
    "woman_red_haired_tone2": "👩🏼🦰",
    "woman_red_haired_medium_light_skin_tone": "👩🏼🦰",
    "woman_red_haired_tone3": "👩🏽🦰",
    "woman_red_haired_medium_skin_tone": "👩🏽🦰",
    "woman_red_haired_tone4": "👩🏾🦰",
    "woman_red_haired_medium_dark_skin_tone": "👩🏾🦰",
    "woman_red_haired_tone5": "👩🏿🦰",
    "woman_red_haired_dark_skin_tone": "👩🏿🦰",
    "man_red_haired": "👨🦰",
    "man_red_haired_tone1": "👨🏻🦰",
    "man_red_haired_light_skin_tone": "👨🏻🦰",
    "man_red_haired_tone2": "👨🏼🦰",
    "man_red_haired_medium_light_skin_tone": "👨🏼🦰",
    "man_red_haired_tone3": "👨🏽🦰",
    "man_red_haired_medium_skin_tone": "👨🏽🦰",
    "man_red_haired_tone4": "👨🏾🦰",
    "man_red_haired_medium_dark_skin_tone": "👨🏾🦰",
    "man_red_haired_tone5": "👨🏿🦰",
    "man_red_haired_dark_skin_tone": "👨🏿🦰",
    "blond_haired_woman": "👱♀",
    "blond_haired_woman_tone1": "👱🏻♀",
    "blond_haired_woman_light_skin_tone": "👱🏻♀",
    "blond_haired_woman_tone2": "👱🏼♀",
    "blond_haired_woman_medium_light_skin_tone": "👱🏼♀",
    "blond_haired_woman_tone3": "👱🏽♀",
    "blond_haired_woman_medium_skin_tone": "👱🏽♀",
    "blond_haired_woman_tone4": "👱🏾♀",
    "blond_haired_woman_medium_dark_skin_tone": "👱🏾♀",
    "blond_haired_woman_tone5": "👱🏿♀",
    "blond_haired_woman_dark_skin_tone": "👱🏿♀",
    "blond_haired_person": "👱",
    "person_with_blond_hair": "👱",
    "blond_haired_person_tone1": "👱🏻",
    "person_with_blond_hair_tone1": "👱🏻",
    "blond_haired_person_tone2": "👱🏼",
    "person_with_blond_hair_tone2": "👱🏼",
    "blond_haired_person_tone3": "👱🏽",
    "person_with_blond_hair_tone3": "👱🏽",
    "blond_haired_person_tone4": "👱🏾",
    "person_with_blond_hair_tone4": "👱🏾",
    "blond_haired_person_tone5": "👱🏿",
    "person_with_blond_hair_tone5": "👱🏿",
    "blond_haired_man": "👱♂",
    "blond_haired_man_tone1": "👱🏻♂",
    "blond_haired_man_light_skin_tone": "👱🏻♂",
    "blond_haired_man_tone2": "👱🏼♂",
    "blond_haired_man_medium_light_skin_tone": "👱🏼♂",
    "blond_haired_man_tone3": "👱🏽♂",
    "blond_haired_man_medium_skin_tone": "👱🏽♂",
    "blond_haired_man_tone4": "👱🏾♂",
    "blond_haired_man_medium_dark_skin_tone": "👱🏾♂",
    "blond_haired_man_tone5": "👱🏿♂",
    "blond_haired_man_dark_skin_tone": "👱🏿♂",
    "woman_white_haired": "👩🦳",
    "woman_white_haired_tone1": "👩🏻🦳",
    "woman_white_haired_light_skin_tone": "👩🏻🦳",
    "woman_white_haired_tone2": "👩🏼🦳",
    "woman_white_haired_medium_light_skin_tone": "👩🏼🦳",
    "woman_white_haired_tone3": "👩🏽🦳",
    "woman_white_haired_medium_skin_tone": "👩🏽🦳",
    "woman_white_haired_tone4": "👩🏾🦳",
    "woman_white_haired_medium_dark_skin_tone": "👩🏾🦳",
    "woman_white_haired_tone5": "👩🏿🦳",
    "woman_white_haired_dark_skin_tone": "👩🏿🦳",
    "man_white_haired": "👨🦳",
    "man_white_haired_tone1": "👨🏻🦳",
    "man_white_haired_light_skin_tone": "👨🏻🦳",
    "man_white_haired_tone2": "👨🏼🦳",
    "man_white_haired_medium_light_skin_tone": "👨🏼🦳",
    "man_white_haired_tone3": "👨🏽🦳",
    "man_white_haired_medium_skin_tone": "👨🏽🦳",
    "man_white_haired_tone4": "👨🏾🦳",
    "man_white_haired_medium_dark_skin_tone": "👨🏾🦳",
    "man_white_haired_tone5": "👨🏿🦳",
    "man_white_haired_dark_skin_tone": "👨🏿🦳",
    "woman_bald": "👩🦲",
    "woman_bald_tone1": "👩🏻🦲",
    "woman_bald_light_skin_tone": "👩🏻🦲",
    "woman_bald_tone2": "👩🏼🦲",
    "woman_bald_medium_light_skin_tone": "👩🏼🦲",
    "woman_bald_tone3": "👩🏽🦲",
    "woman_bald_medium_skin_tone": "👩🏽🦲",
    "woman_bald_tone4": "👩🏾🦲",
    "woman_bald_medium_dark_skin_tone": "👩🏾🦲",
    "woman_bald_tone5": "👩🏿🦲",
    "woman_bald_dark_skin_tone": "👩🏿🦲",
    "man_bald": "👨🦲",
    "man_bald_tone1": "👨🏻🦲",
    "man_bald_light_skin_tone": "👨🏻🦲",
    "man_bald_tone2": "👨🏼🦲",
    "man_bald_medium_light_skin_tone": "👨🏼🦲",
    "man_bald_tone3": "👨🏽🦲",
    "man_bald_medium_skin_tone": "👨🏽🦲",
    "man_bald_tone4": "👨🏾🦲",
    "man_bald_medium_dark_skin_tone": "👨🏾🦲",
    "man_bald_tone5": "👨🏿🦲",
    "man_bald_dark_skin_tone": "👨🏿🦲",
    "bearded_person": "🧔",
    "bearded_person_tone1": "🧔🏻",
    "bearded_person_light_skin_tone": "🧔🏻",
    "bearded_person_tone2": "🧔🏼",
    "bearded_person_medium_light_skin_tone": "🧔🏼",
    "bearded_person_tone3": "🧔🏽",
    "bearded_person_medium_skin_tone": "🧔🏽",
    "bearded_person_tone4": "🧔🏾",
    "bearded_person_medium_dark_skin_tone": "🧔🏾",
    "bearded_person_tone5": "🧔🏿",
    "bearded_person_dark_skin_tone": "🧔🏿",
    "older_woman": "👵",
    "grandma": "👵",
    "older_woman_tone1": "👵🏻",
    "grandma_tone1": "👵🏻",
    "older_woman_tone2": "👵🏼",
    "grandma_tone2": "👵🏼",
    "older_woman_tone3": "👵🏽",
    "grandma_tone3": "👵🏽",
    "older_woman_tone4": "👵🏾",
    "grandma_tone4": "👵🏾",
    "older_woman_tone5": "👵🏿",
    "grandma_tone5": "👵🏿",
    "older_adult": "🧓",
    "older_adult_tone1": "🧓🏻",
    "older_adult_light_skin_tone": "🧓🏻",
    "older_adult_tone2": "🧓🏼",
    "older_adult_medium_light_skin_tone": "🧓🏼",
    "older_adult_tone3": "🧓🏽",
    "older_adult_medium_skin_tone": "🧓🏽",
    "older_adult_tone4": "🧓🏾",
    "older_adult_medium_dark_skin_tone": "🧓🏾",
    "older_adult_tone5": "🧓🏿",
    "older_adult_dark_skin_tone": "🧓🏿",
    "older_man": "👴",
    "older_man_tone1": "👴🏻",
    "older_man_tone2": "👴🏼",
    "older_man_tone3": "👴🏽",
    "older_man_tone4": "👴🏾",
    "older_man_tone5": "👴🏿",
    "man_with_chinese_cap": "👲",
    "man_with_gua_pi_mao": "👲",
    "man_with_chinese_cap_tone1": "👲🏻",
    "man_with_gua_pi_mao_tone1": "👲🏻",
    "man_with_chinese_cap_tone2": "👲🏼",
    "man_with_gua_pi_mao_tone2": "👲🏼",
    "man_with_chinese_cap_tone3": "👲🏽",
    "man_with_gua_pi_mao_tone3": "👲🏽",
    "man_with_chinese_cap_tone4": "👲🏾",
    "man_with_gua_pi_mao_tone4": "👲🏾",
    "man_with_chinese_cap_tone5": "👲🏿",
    "man_with_gua_pi_mao_tone5": "👲🏿",
    "person_wearing_turban": "👳",
    "man_with_turban": "👳",
    "person_wearing_turban_tone1": "👳🏻",
    "man_with_turban_tone1": "👳🏻",
    "person_wearing_turban_tone2": "👳🏼",
    "man_with_turban_tone2": "👳🏼",
    "person_wearing_turban_tone3": "👳🏽",
    "man_with_turban_tone3": "👳🏽",
    "person_wearing_turban_tone4": "👳🏾",
    "man_with_turban_tone4": "👳🏾",
    "person_wearing_turban_tone5": "👳🏿",
    "man_with_turban_tone5": "👳🏿",
    "woman_wearing_turban": "👳♀",
    "woman_wearing_turban_tone1": "👳🏻♀",
    "woman_wearing_turban_light_skin_tone": "👳🏻♀",
    "woman_wearing_turban_tone2": "👳🏼♀",
    "woman_wearing_turban_medium_light_skin_tone": "👳🏼♀",
    "woman_wearing_turban_tone3": "👳🏽♀",
    "woman_wearing_turban_medium_skin_tone": "👳🏽♀",
    "woman_wearing_turban_tone4": "👳🏾♀",
    "woman_wearing_turban_medium_dark_skin_tone": "👳🏾♀",
    "woman_wearing_turban_tone5": "👳🏿♀",
    "woman_wearing_turban_dark_skin_tone": "👳🏿♀",
    "man_wearing_turban": "👳♂",
    "man_wearing_turban_tone1": "👳🏻♂",
    "man_wearing_turban_light_skin_tone": "👳🏻♂",
    "man_wearing_turban_tone2": "👳🏼♂",
    "man_wearing_turban_medium_light_skin_tone": "👳🏼♂",
    "man_wearing_turban_tone3": "👳🏽♂",
    "man_wearing_turban_medium_skin_tone": "👳🏽♂",
    "man_wearing_turban_tone4": "👳🏾♂",
    "man_wearing_turban_medium_dark_skin_tone": "👳🏾♂",
    "man_wearing_turban_tone5": "👳🏿♂",
    "man_wearing_turban_dark_skin_tone": "👳🏿♂",
    "woman_with_headscarf": "🧕",
    "woman_with_headscarf_tone1": "🧕🏻",
    "woman_with_headscarf_light_skin_tone": "🧕🏻",
    "woman_with_headscarf_tone2": "🧕🏼",
    "woman_with_headscarf_medium_light_skin_tone": "🧕🏼",
    "woman_with_headscarf_tone3": "🧕🏽",
    "woman_with_headscarf_medium_skin_tone": "🧕🏽",
    "woman_with_headscarf_tone4": "🧕🏾",
    "woman_with_headscarf_medium_dark_skin_tone": "🧕🏾",
    "woman_with_headscarf_tone5": "🧕🏿",
    "woman_with_headscarf_dark_skin_tone": "🧕🏿",
    "police_officer": "👮",
    "cop": "👮",
    "police_officer_tone1": "👮🏻",
    "cop_tone1": "👮🏻",
    "police_officer_tone2": "👮🏼",
    "cop_tone2": "👮🏼",
    "police_officer_tone3": "👮🏽",
    "cop_tone3": "👮🏽",
    "police_officer_tone4": "👮🏾",
    "cop_tone4": "👮🏾",
    "police_officer_tone5": "👮🏿",
    "cop_tone5": "👮🏿",
    "woman_police_officer": "👮♀",
    "woman_police_officer_tone1": "👮🏻♀",
    "woman_police_officer_light_skin_tone": "👮🏻♀",
    "woman_police_officer_tone2": "👮🏼♀",
    "woman_police_officer_medium_light_skin_tone": "👮🏼♀",
    "woman_police_officer_tone3": "👮🏽♀",
    "woman_police_officer_medium_skin_tone": "👮🏽♀",
    "woman_police_officer_tone4": "👮🏾♀",
    "woman_police_officer_medium_dark_skin_tone": "👮🏾♀",
    "woman_police_officer_tone5": "👮🏿♀",
    "woman_police_officer_dark_skin_tone": "👮🏿♀",
    "man_police_officer": "👮♂",
    "man_police_officer_tone1": "👮🏻♂",
    "man_police_officer_light_skin_tone": "👮🏻♂",
    "man_police_officer_tone2": "👮🏼♂",
    "man_police_officer_medium_light_skin_tone": "👮🏼♂",
    "man_police_officer_tone3": "👮🏽♂",
    "man_police_officer_medium_skin_tone": "👮🏽♂",
    "man_police_officer_tone4": "👮🏾♂",
    "man_police_officer_medium_dark_skin_tone": "👮🏾♂",
    "man_police_officer_tone5": "👮🏿♂",
    "man_police_officer_dark_skin_tone": "👮🏿♂",
    "construction_worker": "👷",
    "construction_worker_tone1": "👷🏻",
    "construction_worker_tone2": "👷🏼",
    "construction_worker_tone3": "👷🏽",
    "construction_worker_tone4": "👷🏾",
    "construction_worker_tone5": "👷🏿",
    "woman_construction_worker": "👷♀",
    "woman_construction_worker_tone1": "👷🏻♀",
    "woman_construction_worker_light_skin_tone": "👷🏻♀",
    "woman_construction_worker_tone2": "👷🏼♀",
    "woman_construction_worker_medium_light_skin_tone": "👷🏼♀",
    "woman_construction_worker_tone3": "👷🏽♀",
    "woman_construction_worker_medium_skin_tone": "👷🏽♀",
    "woman_construction_worker_tone4": "👷🏾♀",
    "woman_construction_worker_medium_dark_skin_tone": "👷🏾♀",
    "woman_construction_worker_tone5": "👷🏿♀",
    "woman_construction_worker_dark_skin_tone": "👷🏿♀",
    "man_construction_worker": "👷♂",
    "man_construction_worker_tone1": "👷🏻♂",
    "man_construction_worker_light_skin_tone": "👷🏻♂",
    "man_construction_worker_tone2": "👷🏼♂",
    "man_construction_worker_medium_light_skin_tone": "👷🏼♂",
    "man_construction_worker_tone3": "👷🏽♂",
    "man_construction_worker_medium_skin_tone": "👷🏽♂",
    "man_construction_worker_tone4": "👷🏾♂",
    "man_construction_worker_medium_dark_skin_tone": "👷🏾♂",
    "man_construction_worker_tone5": "👷🏿♂",
    "man_construction_worker_dark_skin_tone": "👷🏿♂",
    "guard": "💂",
    "guardsman": "💂",
    "guard_tone1": "💂🏻",
    "guardsman_tone1": "💂🏻",
    "guard_tone2": "💂🏼",
    "guardsman_tone2": "💂🏼",
    "guard_tone3": "💂🏽",
    "guardsman_tone3": "💂🏽",
    "guard_tone4": "💂🏾",
    "guardsman_tone4": "💂🏾",
    "guard_tone5": "💂🏿",
    "guardsman_tone5": "💂🏿",
    "woman_guard": "💂♀",
    "woman_guard_tone1": "💂🏻♀",
    "woman_guard_light_skin_tone": "💂🏻♀",
    "woman_guard_tone2": "💂🏼♀",
    "woman_guard_medium_light_skin_tone": "💂🏼♀",
    "woman_guard_tone3": "💂🏽♀",
    "woman_guard_medium_skin_tone": "💂🏽♀",
    "woman_guard_tone4": "💂🏾♀",
    "woman_guard_medium_dark_skin_tone": "💂🏾♀",
    "woman_guard_tone5": "💂🏿♀",
    "woman_guard_dark_skin_tone": "💂🏿♀",
    "man_guard": "💂♂",
    "man_guard_tone1": "💂🏻♂",
    "man_guard_light_skin_tone": "💂🏻♂",
    "man_guard_tone2": "💂🏼♂",
    "man_guard_medium_light_skin_tone": "💂🏼♂",
    "man_guard_tone3": "💂🏽♂",
    "man_guard_medium_skin_tone": "💂🏽♂",
    "man_guard_tone4": "💂🏾♂",
    "man_guard_medium_dark_skin_tone": "💂🏾♂",
    "man_guard_tone5": "💂🏿♂",
    "man_guard_dark_skin_tone": "💂🏿♂",
    "detective": "🕵",
    "spy": "🕵",
    "sleuth_or_spy": "🕵",
    "detective_tone1": "🕵🏻",
    "spy_tone1": "🕵🏻",
    "sleuth_or_spy_tone1": "🕵🏻",
    "detective_tone2": "🕵🏼",
    "spy_tone2": "🕵🏼",
    "sleuth_or_spy_tone2": "🕵🏼",
    "detective_tone3": "🕵🏽",
    "spy_tone3": "🕵🏽",
    "sleuth_or_spy_tone3": "🕵🏽",
    "detective_tone4": "🕵🏾",
    "spy_tone4": "🕵🏾",
    "sleuth_or_spy_tone4": "🕵🏾",
    "detective_tone5": "🕵🏿",
    "spy_tone5": "🕵🏿",
    "sleuth_or_spy_tone5": "🕵🏿",
    "woman_detective": "🕵♀",
    "woman_detective_tone1": "🕵🏻♀",
    "woman_detective_light_skin_tone": "🕵🏻♀",
    "woman_detective_tone2": "🕵🏼♀",
    "woman_detective_medium_light_skin_tone": "🕵🏼♀",
    "woman_detective_tone3": "🕵🏽♀",
    "woman_detective_medium_skin_tone": "🕵🏽♀",
    "woman_detective_tone4": "🕵🏾♀",
    "woman_detective_medium_dark_skin_tone": "🕵🏾♀",
    "woman_detective_tone5": "🕵🏿♀",
    "woman_detective_dark_skin_tone": "🕵🏿♀",
    "man_detective": "🕵♂",
    "man_detective_tone1": "🕵🏻♂",
    "man_detective_light_skin_tone": "🕵🏻♂",
    "man_detective_tone2": "🕵🏼♂",
    "man_detective_medium_light_skin_tone": "🕵🏼♂",
    "man_detective_tone3": "🕵🏽♂",
    "man_detective_medium_skin_tone": "🕵🏽♂",
    "man_detective_tone4": "🕵🏾♂",
    "man_detective_medium_dark_skin_tone": "🕵🏾♂",
    "man_detective_tone5": "🕵🏿♂",
    "man_detective_dark_skin_tone": "🕵🏿♂",
    "woman_health_worker": "👩⚕",
    "woman_health_worker_tone1": "👩🏻⚕",
    "woman_health_worker_light_skin_tone": "👩🏻⚕",
    "woman_health_worker_tone2": "👩🏼⚕",
    "woman_health_worker_medium_light_skin_tone": "👩🏼⚕",
    "woman_health_worker_tone3": "👩🏽⚕",
    "woman_health_worker_medium_skin_tone": "👩🏽⚕",
    "woman_health_worker_tone4": "👩🏾⚕",
    "woman_health_worker_medium_dark_skin_tone": "👩🏾⚕",
    "woman_health_worker_tone5": "👩🏿⚕",
    "woman_health_worker_dark_skin_tone": "👩🏿⚕",
    "man_health_worker": "👨⚕",
    "man_health_worker_tone1": "👨🏻⚕",
    "man_health_worker_light_skin_tone": "👨🏻⚕",
    "man_health_worker_tone2": "👨🏼⚕",
    "man_health_worker_medium_light_skin_tone": "👨🏼⚕",
    "man_health_worker_tone3": "👨🏽⚕",
    "man_health_worker_medium_skin_tone": "👨🏽⚕",
    "man_health_worker_tone4": "👨🏾⚕",
    "man_health_worker_medium_dark_skin_tone": "👨🏾⚕",
    "man_health_worker_tone5": "👨🏿⚕",
    "man_health_worker_dark_skin_tone": "👨🏿⚕",
    "woman_farmer": "👩🌾",
    "woman_farmer_tone1": "👩🏻🌾",
    "woman_farmer_light_skin_tone": "👩🏻🌾",
    "woman_farmer_tone2": "👩🏼🌾",
    "woman_farmer_medium_light_skin_tone": "👩🏼🌾",
    "woman_farmer_tone3": "👩🏽🌾",
    "woman_farmer_medium_skin_tone": "👩🏽🌾",
    "woman_farmer_tone4": "👩🏾🌾",
    "woman_farmer_medium_dark_skin_tone": "👩🏾🌾",
    "woman_farmer_tone5": "👩🏿🌾",
    "woman_farmer_dark_skin_tone": "👩🏿🌾",
    "man_farmer": "👨🌾",
    "man_farmer_tone1": "👨🏻🌾",
    "man_farmer_light_skin_tone": "👨🏻🌾",
    "man_farmer_tone2": "👨🏼🌾",
    "man_farmer_medium_light_skin_tone": "👨🏼🌾",
    "man_farmer_tone3": "👨🏽🌾",
    "man_farmer_medium_skin_tone": "👨🏽🌾",
    "man_farmer_tone4": "👨🏾🌾",
    "man_farmer_medium_dark_skin_tone": "👨🏾🌾",
    "man_farmer_tone5": "👨🏿🌾",
    "man_farmer_dark_skin_tone": "👨🏿🌾",
    "woman_cook": "👩🍳",
    "woman_cook_tone1": "👩🏻🍳",
    "woman_cook_light_skin_tone": "👩🏻🍳",
    "woman_cook_tone2": "👩🏼🍳",
    "woman_cook_medium_light_skin_tone": "👩🏼🍳",
    "woman_cook_tone3": "👩🏽🍳",
    "woman_cook_medium_skin_tone": "👩🏽🍳",
    "woman_cook_tone4": "👩🏾🍳",
    "woman_cook_medium_dark_skin_tone": "👩🏾🍳",
    "woman_cook_tone5": "👩🏿🍳",
    "woman_cook_dark_skin_tone": "👩🏿🍳",
    "man_cook": "👨🍳",
    "man_cook_tone1": "👨🏻🍳",
    "man_cook_light_skin_tone": "👨🏻🍳",
    "man_cook_tone2": "👨🏼🍳",
    "man_cook_medium_light_skin_tone": "👨🏼🍳",
    "man_cook_tone3": "👨🏽🍳",
    "man_cook_medium_skin_tone": "👨🏽🍳",
    "man_cook_tone4": "👨🏾🍳",
    "man_cook_medium_dark_skin_tone": "👨🏾🍳",
    "man_cook_tone5": "👨🏿🍳",
    "man_cook_dark_skin_tone": "👨🏿🍳",
    "woman_student": "👩🎓",
    "woman_student_tone1": "👩🏻🎓",
    "woman_student_light_skin_tone": "👩🏻🎓",
    "woman_student_tone2": "👩🏼🎓",
    "woman_student_medium_light_skin_tone": "👩🏼🎓",
    "woman_student_tone3": "👩🏽🎓",
    "woman_student_medium_skin_tone": "👩🏽🎓",
    "woman_student_tone4": "👩🏾🎓",
    "woman_student_medium_dark_skin_tone": "👩🏾🎓",
    "woman_student_tone5": "👩🏿🎓",
    "woman_student_dark_skin_tone": "👩🏿🎓",
    "man_student": "👨🎓",
    "man_student_tone1": "👨🏻🎓",
    "man_student_light_skin_tone": "👨🏻🎓",
    "man_student_tone2": "👨🏼🎓",
    "man_student_medium_light_skin_tone": "👨🏼🎓",
    "man_student_tone3": "👨🏽🎓",
    "man_student_medium_skin_tone": "👨🏽🎓",
    "man_student_tone4": "👨🏾🎓",
    "man_student_medium_dark_skin_tone": "👨🏾🎓",
    "man_student_tone5": "👨🏿🎓",
    "man_student_dark_skin_tone": "👨🏿🎓",
    "woman_singer": "👩🎤",
    "woman_singer_tone1": "👩🏻🎤",
    "woman_singer_light_skin_tone": "👩🏻🎤",
    "woman_singer_tone2": "👩🏼🎤",
    "woman_singer_medium_light_skin_tone": "👩🏼🎤",
    "woman_singer_tone3": "👩🏽🎤",
    "woman_singer_medium_skin_tone": "👩🏽🎤",
    "woman_singer_tone4": "👩🏾🎤",
    "woman_singer_medium_dark_skin_tone": "👩🏾🎤",
    "woman_singer_tone5": "👩🏿🎤",
    "woman_singer_dark_skin_tone": "👩🏿🎤",
    "man_singer": "👨🎤",
    "man_singer_tone1": "👨🏻🎤",
    "man_singer_light_skin_tone": "👨🏻🎤",
    "man_singer_tone2": "👨🏼🎤",
    "man_singer_medium_light_skin_tone": "👨🏼🎤",
    "man_singer_tone3": "👨🏽🎤",
    "man_singer_medium_skin_tone": "👨🏽🎤",
    "man_singer_tone4": "👨🏾🎤",
    "man_singer_medium_dark_skin_tone": "👨🏾🎤",
    "man_singer_tone5": "👨🏿🎤",
    "man_singer_dark_skin_tone": "👨🏿🎤",
    "woman_teacher": "👩🏫",
    "woman_teacher_tone1": "👩🏻🏫",
    "woman_teacher_light_skin_tone": "👩🏻🏫",
    "woman_teacher_tone2": "👩🏼🏫",
    "woman_teacher_medium_light_skin_tone": "👩🏼🏫",
    "woman_teacher_tone3": "👩🏽🏫",
    "woman_teacher_medium_skin_tone": "👩🏽🏫",
    "woman_teacher_tone4": "👩🏾🏫",
    "woman_teacher_medium_dark_skin_tone": "👩🏾🏫",
    "woman_teacher_tone5": "👩🏿🏫",
    "woman_teacher_dark_skin_tone": "👩🏿🏫",
    "man_teacher": "👨🏫",
    "man_teacher_tone1": "👨🏻🏫",
    "man_teacher_light_skin_tone": "👨🏻🏫",
    "man_teacher_tone2": "👨🏼🏫",
    "man_teacher_medium_light_skin_tone": "👨🏼🏫",
    "man_teacher_tone3": "👨🏽🏫",
    "man_teacher_medium_skin_tone": "👨🏽🏫",
    "man_teacher_tone4": "👨🏾🏫",
    "man_teacher_medium_dark_skin_tone": "👨🏾🏫",
    "man_teacher_tone5": "👨🏿🏫",
    "man_teacher_dark_skin_tone": "👨🏿🏫",
    "woman_factory_worker": "👩🏭",
    "woman_factory_worker_tone1": "👩🏻🏭",
    "woman_factory_worker_light_skin_tone": "👩🏻🏭",
    "woman_factory_worker_tone2": "👩🏼🏭",
    "woman_factory_worker_medium_light_skin_tone": "👩🏼🏭",
    "woman_factory_worker_tone3": "👩🏽🏭",
    "woman_factory_worker_medium_skin_tone": "👩🏽🏭",
    "woman_factory_worker_tone4": "👩🏾🏭",
    "woman_factory_worker_medium_dark_skin_tone": "👩🏾🏭",
    "woman_factory_worker_tone5": "👩🏿🏭",
    "woman_factory_worker_dark_skin_tone": "👩🏿🏭",
    "man_factory_worker": "👨🏭",
    "man_factory_worker_tone1": "👨🏻🏭",
    "man_factory_worker_light_skin_tone": "👨🏻🏭",
    "man_factory_worker_tone2": "👨🏼🏭",
    "man_factory_worker_medium_light_skin_tone": "👨🏼🏭",
    "man_factory_worker_tone3": "👨🏽🏭",
    "man_factory_worker_medium_skin_tone": "👨🏽🏭",
    "man_factory_worker_tone4": "👨🏾🏭",
    "man_factory_worker_medium_dark_skin_tone": "👨🏾🏭",
    "man_factory_worker_tone5": "👨🏿🏭",
    "man_factory_worker_dark_skin_tone": "👨🏿🏭",
    "woman_technologist": "👩💻",
    "woman_technologist_tone1": "👩🏻💻",
    "woman_technologist_light_skin_tone": "👩🏻💻",
    "woman_technologist_tone2": "👩🏼💻",
    "woman_technologist_medium_light_skin_tone": "👩🏼💻",
    "woman_technologist_tone3": "👩🏽💻",
    "woman_technologist_medium_skin_tone": "👩🏽💻",
    "woman_technologist_tone4": "👩🏾💻",
    "woman_technologist_medium_dark_skin_tone": "👩🏾💻",
    "woman_technologist_tone5": "👩🏿💻",
    "woman_technologist_dark_skin_tone": "👩🏿💻",
    "man_technologist": "👨💻",
    "man_technologist_tone1": "👨🏻💻",
    "man_technologist_light_skin_tone": "👨🏻💻",
    "man_technologist_tone2": "👨🏼💻",
    "man_technologist_medium_light_skin_tone": "👨🏼💻",
    "man_technologist_tone3": "👨🏽💻",
    "man_technologist_medium_skin_tone": "👨🏽💻",
    "man_technologist_tone4": "👨🏾💻",
    "man_technologist_medium_dark_skin_tone": "👨🏾💻",
    "man_technologist_tone5": "👨🏿💻",
    "man_technologist_dark_skin_tone": "👨🏿💻",
    "woman_office_worker": "👩💼",
    "woman_office_worker_tone1": "👩🏻💼",
    "woman_office_worker_light_skin_tone": "👩🏻💼",
    "woman_office_worker_tone2": "👩🏼💼",
    "woman_office_worker_medium_light_skin_tone": "👩🏼💼",
    "woman_office_worker_tone3": "👩🏽💼",
    "woman_office_worker_medium_skin_tone": "👩🏽💼",
    "woman_office_worker_tone4": "👩🏾💼",
    "woman_office_worker_medium_dark_skin_tone": "👩🏾💼",
    "woman_office_worker_tone5": "👩🏿💼",
    "woman_office_worker_dark_skin_tone": "👩🏿💼",
    "man_office_worker": "👨💼",
    "man_office_worker_tone1": "👨🏻💼",
    "man_office_worker_light_skin_tone": "👨🏻💼",
    "man_office_worker_tone2": "👨🏼💼",
    "man_office_worker_medium_light_skin_tone": "👨🏼💼",
    "man_office_worker_tone3": "👨🏽💼",
    "man_office_worker_medium_skin_tone": "👨🏽💼",
    "man_office_worker_tone4": "👨🏾💼",
    "man_office_worker_medium_dark_skin_tone": "👨🏾💼",
    "man_office_worker_tone5": "👨🏿💼",
    "man_office_worker_dark_skin_tone": "👨🏿💼",
    "woman_mechanic": "👩🔧",
    "woman_mechanic_tone1": "👩🏻🔧",
    "woman_mechanic_light_skin_tone": "👩🏻🔧",
    "woman_mechanic_tone2": "👩🏼🔧",
    "woman_mechanic_medium_light_skin_tone": "👩🏼🔧",
    "woman_mechanic_tone3": "👩🏽🔧",
    "woman_mechanic_medium_skin_tone": "👩🏽🔧",
    "woman_mechanic_tone4": "👩🏾🔧",
    "woman_mechanic_medium_dark_skin_tone": "👩🏾🔧",
    "woman_mechanic_tone5": "👩🏿🔧",
    "woman_mechanic_dark_skin_tone": "👩🏿🔧",
    "man_mechanic": "👨🔧",
    "man_mechanic_tone1": "👨🏻🔧",
    "man_mechanic_light_skin_tone": "👨🏻🔧",
    "man_mechanic_tone2": "👨🏼🔧",
    "man_mechanic_medium_light_skin_tone": "👨🏼🔧",
    "man_mechanic_tone3": "👨🏽🔧",
    "man_mechanic_medium_skin_tone": "👨🏽🔧",
    "man_mechanic_tone4": "👨🏾🔧",
    "man_mechanic_medium_dark_skin_tone": "👨🏾🔧",
    "man_mechanic_tone5": "👨🏿🔧",
    "man_mechanic_dark_skin_tone": "👨🏿🔧",
    "woman_scientist": "👩🔬",
    "woman_scientist_tone1": "👩🏻🔬",
    "woman_scientist_light_skin_tone": "👩🏻🔬",
    "woman_scientist_tone2": "👩🏼🔬",
    "woman_scientist_medium_light_skin_tone": "👩🏼🔬",
    "woman_scientist_tone3": "👩🏽🔬",
    "woman_scientist_medium_skin_tone": "👩🏽🔬",
    "woman_scientist_tone4": "👩🏾🔬",
    "woman_scientist_medium_dark_skin_tone": "👩🏾🔬",
    "woman_scientist_tone5": "👩🏿🔬",
    "woman_scientist_dark_skin_tone": "👩🏿🔬",
    "man_scientist": "👨🔬",
    "man_scientist_tone1": "👨🏻🔬",
    "man_scientist_light_skin_tone": "👨🏻🔬",
    "man_scientist_tone2": "👨🏼🔬",
    "man_scientist_medium_light_skin_tone": "👨🏼🔬",
    "man_scientist_tone3": "👨🏽🔬",
    "man_scientist_medium_skin_tone": "👨🏽🔬",
    "man_scientist_tone4": "👨🏾🔬",
    "man_scientist_medium_dark_skin_tone": "👨🏾🔬",
    "man_scientist_tone5": "👨🏿🔬",
    "man_scientist_dark_skin_tone": "👨🏿🔬",
    "woman_artist": "👩🎨",
    "woman_artist_tone1": "👩🏻🎨",
    "woman_artist_light_skin_tone": "👩🏻🎨",
    "woman_artist_tone2": "👩🏼🎨",
    "woman_artist_medium_light_skin_tone": "👩🏼🎨",
    "woman_artist_tone3": "👩🏽🎨",
    "woman_artist_medium_skin_tone": "👩🏽🎨",
    "woman_artist_tone4": "👩🏾🎨",
    "woman_artist_medium_dark_skin_tone": "👩🏾🎨",
    "woman_artist_tone5": "👩🏿🎨",
    "woman_artist_dark_skin_tone": "👩🏿🎨",
    "man_artist": "👨🎨",
    "man_artist_tone1": "👨🏻🎨",
    "man_artist_light_skin_tone": "👨🏻🎨",
    "man_artist_tone2": "👨🏼🎨",
    "man_artist_medium_light_skin_tone": "👨🏼🎨",
    "man_artist_tone3": "👨🏽🎨",
    "man_artist_medium_skin_tone": "👨🏽🎨",
    "man_artist_tone4": "👨🏾🎨",
    "man_artist_medium_dark_skin_tone": "👨🏾🎨",
    "man_artist_tone5": "👨🏿🎨",
    "man_artist_dark_skin_tone": "👨🏿🎨",
    "woman_firefighter": "👩🚒",
    "woman_firefighter_tone1": "👩🏻🚒",
    "woman_firefighter_light_skin_tone": "👩🏻🚒",
    "woman_firefighter_tone2": "👩🏼🚒",
    "woman_firefighter_medium_light_skin_tone": "👩🏼🚒",
    "woman_firefighter_tone3": "👩🏽🚒",
    "woman_firefighter_medium_skin_tone": "👩🏽🚒",
    "woman_firefighter_tone4": "👩🏾🚒",
    "woman_firefighter_medium_dark_skin_tone": "👩🏾🚒",
    "woman_firefighter_tone5": "👩🏿🚒",
    "woman_firefighter_dark_skin_tone": "👩🏿🚒",
    "man_firefighter": "👨🚒",
    "man_firefighter_tone1": "👨🏻🚒",
    "man_firefighter_light_skin_tone": "👨🏻🚒",
    "man_firefighter_tone2": "👨🏼🚒",
    "man_firefighter_medium_light_skin_tone": "👨🏼🚒",
    "man_firefighter_tone3": "👨🏽🚒",
    "man_firefighter_medium_skin_tone": "👨🏽🚒",
    "man_firefighter_tone4": "👨🏾🚒",
    "man_firefighter_medium_dark_skin_tone": "👨🏾🚒",
    "man_firefighter_tone5": "👨🏿🚒",
    "man_firefighter_dark_skin_tone": "👨🏿🚒",
    "woman_pilot": "👩✈",
    "woman_pilot_tone1": "👩🏻✈",
    "woman_pilot_light_skin_tone": "👩🏻✈",
    "woman_pilot_tone2": "👩🏼✈",
    "woman_pilot_medium_light_skin_tone": "👩🏼✈",
    "woman_pilot_tone3": "👩🏽✈",
    "woman_pilot_medium_skin_tone": "👩🏽✈",
    "woman_pilot_tone4": "👩🏾✈",
    "woman_pilot_medium_dark_skin_tone": "👩🏾✈",
    "woman_pilot_tone5": "👩🏿✈",
    "woman_pilot_dark_skin_tone": "👩🏿✈",
    "man_pilot": "👨✈",
    "man_pilot_tone1": "👨🏻✈",
    "man_pilot_light_skin_tone": "👨🏻✈",
    "man_pilot_tone2": "👨🏼✈",
    "man_pilot_medium_light_skin_tone": "👨🏼✈",
    "man_pilot_tone3": "👨🏽✈",
    "man_pilot_medium_skin_tone": "👨🏽✈",
    "man_pilot_tone4": "👨🏾✈",
    "man_pilot_medium_dark_skin_tone": "👨🏾✈",
    "man_pilot_tone5": "👨🏿✈",
    "man_pilot_dark_skin_tone": "👨🏿✈",
    "woman_astronaut": "👩🚀",
    "woman_astronaut_tone1": "👩🏻🚀",
    "woman_astronaut_light_skin_tone": "👩🏻🚀",
    "woman_astronaut_tone2": "👩🏼🚀",
    "woman_astronaut_medium_light_skin_tone": "👩🏼🚀",
    "woman_astronaut_tone3": "👩🏽🚀",
    "woman_astronaut_medium_skin_tone": "👩🏽🚀",
    "woman_astronaut_tone4": "👩🏾🚀",
    "woman_astronaut_medium_dark_skin_tone": "👩🏾🚀",
    "woman_astronaut_tone5": "👩🏿🚀",
    "woman_astronaut_dark_skin_tone": "👩🏿🚀",
    "man_astronaut": "👨🚀",
    "man_astronaut_tone1": "👨🏻🚀",
    "man_astronaut_light_skin_tone": "👨🏻🚀",
    "man_astronaut_tone2": "👨🏼🚀",
    "man_astronaut_medium_light_skin_tone": "👨🏼🚀",
    "man_astronaut_tone3": "👨🏽🚀",
    "man_astronaut_medium_skin_tone": "👨🏽🚀",
    "man_astronaut_tone4": "👨🏾🚀",
    "man_astronaut_medium_dark_skin_tone": "👨🏾🚀",
    "man_astronaut_tone5": "👨🏿🚀",
    "man_astronaut_dark_skin_tone": "👨🏿🚀",
    "woman_judge": "👩⚖",
    "woman_judge_tone1": "👩🏻⚖",
    "woman_judge_light_skin_tone": "👩🏻⚖",
    "woman_judge_tone2": "👩🏼⚖",
    "woman_judge_medium_light_skin_tone": "👩🏼⚖",
    "woman_judge_tone3": "👩🏽⚖",
    "woman_judge_medium_skin_tone": "👩🏽⚖",
    "woman_judge_tone4": "👩🏾⚖",
    "woman_judge_medium_dark_skin_tone": "👩🏾⚖",
    "woman_judge_tone5": "👩🏿⚖",
    "woman_judge_dark_skin_tone": "👩🏿⚖",
    "man_judge": "👨⚖",
    "man_judge_tone1": "👨🏻⚖",
    "man_judge_light_skin_tone": "👨🏻⚖",
    "man_judge_tone2": "👨🏼⚖",
    "man_judge_medium_light_skin_tone": "👨🏼⚖",
    "man_judge_tone3": "👨🏽⚖",
    "man_judge_medium_skin_tone": "👨🏽⚖",
    "man_judge_tone4": "👨🏾⚖",
    "man_judge_medium_dark_skin_tone": "👨🏾⚖",
    "man_judge_tone5": "👨🏿⚖",
    "man_judge_dark_skin_tone": "👨🏿⚖",
    "bride_with_veil": "👰",
    "bride_with_veil_tone1": "👰🏻",
    "bride_with_veil_tone2": "👰🏼",
    "bride_with_veil_tone3": "👰🏽",
    "bride_with_veil_tone4": "👰🏾",
    "bride_with_veil_tone5": "👰🏿",
    "man_in_tuxedo": "🤵",
    "man_in_tuxedo_tone1": "🤵🏻",
    "tuxedo_tone1": "🤵🏻",
    "man_in_tuxedo_tone2": "🤵🏼",
    "tuxedo_tone2": "🤵🏼",
    "man_in_tuxedo_tone3": "🤵🏽",
    "tuxedo_tone3": "🤵🏽",
    "man_in_tuxedo_tone4": "🤵🏾",
    "tuxedo_tone4": "🤵🏾",
    "man_in_tuxedo_tone5": "🤵🏿",
    "tuxedo_tone5": "🤵🏿",
    "princess": "👸",
    "princess_tone1": "👸🏻",
    "princess_tone2": "👸🏼",
    "princess_tone3": "👸🏽",
    "princess_tone4": "👸🏾",
    "princess_tone5": "👸🏿",
    "prince": "🤴",
    "prince_tone1": "🤴🏻",
    "prince_tone2": "🤴🏼",
    "prince_tone3": "🤴🏽",
    "prince_tone4": "🤴🏾",
    "prince_tone5": "🤴🏿",
    "superhero": "🦸",
    "superhero_tone1": "🦸🏻",
    "superhero_light_skin_tone": "🦸🏻",
    "superhero_tone2": "🦸🏼",
    "superhero_medium_light_skin_tone": "🦸🏼",
    "superhero_tone3": "🦸🏽",
    "superhero_medium_skin_tone": "🦸🏽",
    "superhero_tone4": "🦸🏾",
    "superhero_medium_dark_skin_tone": "🦸🏾",
    "superhero_tone5": "🦸🏿",
    "superhero_dark_skin_tone": "🦸🏿",
    "woman_superhero": "🦸♀",
    "woman_superhero_tone1": "🦸🏻♀",
    "woman_superhero_light_skin_tone": "🦸🏻♀",
    "woman_superhero_tone2": "🦸🏼♀",
    "woman_superhero_medium_light_skin_tone": "🦸🏼♀",
    "woman_superhero_tone3": "🦸🏽♀",
    "woman_superhero_medium_skin_tone": "🦸🏽♀",
    "woman_superhero_tone4": "🦸🏾♀",
    "woman_superhero_medium_dark_skin_tone": "🦸🏾♀",
    "woman_superhero_tone5": "🦸🏿♀",
    "woman_superhero_dark_skin_tone": "🦸🏿♀",
    "man_superhero": "🦸♂",
    "man_superhero_tone1": "🦸🏻♂",
    "man_superhero_light_skin_tone": "🦸🏻♂",
    "man_superhero_tone2": "🦸🏼♂",
    "man_superhero_medium_light_skin_tone": "🦸🏼♂",
    "man_superhero_tone3": "🦸🏽♂",
    "man_superhero_medium_skin_tone": "🦸🏽♂",
    "man_superhero_tone4": "🦸🏾♂",
    "man_superhero_medium_dark_skin_tone": "🦸🏾♂",
    "man_superhero_tone5": "🦸🏿♂",
    "man_superhero_dark_skin_tone": "🦸🏿♂",
    "supervillain": "🦹",
    "supervillain_tone1": "🦹🏻",
    "supervillain_light_skin_tone": "🦹🏻",
    "supervillain_tone2": "🦹🏼",
    "supervillain_medium_light_skin_tone": "🦹🏼",
    "supervillain_tone3": "🦹🏽",
    "supervillain_medium_skin_tone": "🦹🏽",
    "supervillain_tone4": "🦹🏾",
    "supervillain_medium_dark_skin_tone": "🦹🏾",
    "supervillain_tone5": "🦹🏿",
    "supervillain_dark_skin_tone": "🦹🏿",
    "woman_supervillain": "🦹♀",
    "woman_supervillain_tone1": "🦹🏻♀",
    "woman_supervillain_light_skin_tone": "🦹🏻♀",
    "woman_supervillain_tone2": "🦹🏼♀",
    "woman_supervillain_medium_light_skin_tone": "🦹🏼♀",
    "woman_supervillain_tone3": "🦹🏽♀",
    "woman_supervillain_medium_skin_tone": "🦹🏽♀",
    "woman_supervillain_tone4": "🦹🏾♀",
    "woman_supervillain_medium_dark_skin_tone": "🦹🏾♀",
    "woman_supervillain_tone5": "🦹🏿♀",
    "woman_supervillain_dark_skin_tone": "🦹🏿♀",
    "man_supervillain": "🦹♂",
    "man_supervillain_tone1": "🦹🏻♂",
    "man_supervillain_light_skin_tone": "🦹🏻♂",
    "man_supervillain_tone2": "🦹🏼♂",
    "man_supervillain_medium_light_skin_tone": "🦹🏼♂",
    "man_supervillain_tone3": "🦹🏽♂",
    "man_supervillain_medium_skin_tone": "🦹🏽♂",
    "man_supervillain_tone4": "🦹🏾♂",
    "man_supervillain_medium_dark_skin_tone": "🦹🏾♂",
    "man_supervillain_tone5": "🦹🏿♂",
    "man_supervillain_dark_skin_tone": "🦹🏿♂",
    "mrs_claus": "🤶",
    "mother_christmas": "🤶",
    "mrs_claus_tone1": "🤶🏻",
    "mother_christmas_tone1": "🤶🏻",
    "mrs_claus_tone2": "🤶🏼",
    "mother_christmas_tone2": "🤶🏼",
    "mrs_claus_tone3": "🤶🏽",
    "mother_christmas_tone3": "🤶🏽",
    "mrs_claus_tone4": "🤶🏾",
    "mother_christmas_tone4": "🤶🏾",
    "mrs_claus_tone5": "🤶🏿",
    "mother_christmas_tone5": "🤶🏿",
    "santa": "🎅",
    "santa_tone1": "🎅🏻",
    "santa_tone2": "🎅🏼",
    "santa_tone3": "🎅🏽",
    "santa_tone4": "🎅🏾",
    "santa_tone5": "🎅🏿",
    "mage": "🧙",
    "mage_tone1": "🧙🏻",
    "mage_light_skin_tone": "🧙🏻",
    "mage_tone2": "🧙🏼",
    "mage_medium_light_skin_tone": "🧙🏼",
    "mage_tone3": "🧙🏽",
    "mage_medium_skin_tone": "🧙🏽",
    "mage_tone4": "🧙🏾",
    "mage_medium_dark_skin_tone": "🧙🏾",
    "mage_tone5": "🧙🏿",
    "mage_dark_skin_tone": "🧙🏿",
    "woman_mage": "🧙♀",
    "woman_mage_tone1": "🧙🏻♀",
    "woman_mage_light_skin_tone": "🧙🏻♀",
    "woman_mage_tone2": "🧙🏼♀",
    "woman_mage_medium_light_skin_tone": "🧙🏼♀",
    "woman_mage_tone3": "🧙🏽♀",
    "woman_mage_medium_skin_tone": "🧙🏽♀",
    "woman_mage_tone4": "🧙🏾♀",
    "woman_mage_medium_dark_skin_tone": "🧙🏾♀",
    "woman_mage_tone5": "🧙🏿♀",
    "woman_mage_dark_skin_tone": "🧙🏿♀",
    "man_mage": "🧙♂",
    "man_mage_tone1": "🧙🏻♂",
    "man_mage_light_skin_tone": "🧙🏻♂",
    "man_mage_tone2": "🧙🏼♂",
    "man_mage_medium_light_skin_tone": "🧙🏼♂",
    "man_mage_tone3": "🧙🏽♂",
    "man_mage_medium_skin_tone": "🧙🏽♂",
    "man_mage_tone4": "🧙🏾♂",
    "man_mage_medium_dark_skin_tone": "🧙🏾♂",
    "man_mage_tone5": "🧙🏿♂",
    "man_mage_dark_skin_tone": "🧙🏿♂",
    "elf": "🧝",
    "elf_tone1": "🧝🏻",
    "elf_light_skin_tone": "🧝🏻",
    "elf_tone2": "🧝🏼",
    "elf_medium_light_skin_tone": "🧝🏼",
    "elf_tone3": "🧝🏽",
    "elf_medium_skin_tone": "🧝🏽",
    "elf_tone4": "🧝🏾",
    "elf_medium_dark_skin_tone": "🧝🏾",
    "elf_tone5": "🧝🏿",
    "elf_dark_skin_tone": "🧝🏿",
    "woman_elf": "🧝♀",
    "woman_elf_tone1": "🧝🏻♀",
    "woman_elf_light_skin_tone": "🧝🏻♀",
    "woman_elf_tone2": "🧝🏼♀",
    "woman_elf_medium_light_skin_tone": "🧝🏼♀",
    "woman_elf_tone3": "🧝🏽♀",
    "woman_elf_medium_skin_tone": "🧝🏽♀",
    "woman_elf_tone4": "🧝🏾♀",
    "woman_elf_medium_dark_skin_tone": "🧝🏾♀",
    "woman_elf_tone5": "🧝🏿♀",
    "woman_elf_dark_skin_tone": "🧝🏿♀",
    "man_elf": "🧝♂",
    "man_elf_tone1": "🧝🏻♂",
    "man_elf_light_skin_tone": "🧝🏻♂",
    "man_elf_tone2": "🧝🏼♂",
    "man_elf_medium_light_skin_tone": "🧝🏼♂",
    "man_elf_tone3": "🧝🏽♂",
    "man_elf_medium_skin_tone": "🧝🏽♂",
    "man_elf_tone4": "🧝🏾♂",
    "man_elf_medium_dark_skin_tone": "🧝🏾♂",
    "man_elf_tone5": "🧝🏿♂",
    "man_elf_dark_skin_tone": "🧝🏿♂",
    "vampire": "🧛",
    "vampire_tone1": "🧛🏻",
    "vampire_light_skin_tone": "🧛🏻",
    "vampire_tone2": "🧛🏼",
    "vampire_medium_light_skin_tone": "🧛🏼",
    "vampire_tone3": "🧛🏽",
    "vampire_medium_skin_tone": "🧛🏽",
    "vampire_tone4": "🧛🏾",
    "vampire_medium_dark_skin_tone": "🧛🏾",
    "vampire_tone5": "🧛🏿",
    "vampire_dark_skin_tone": "🧛🏿",
    "woman_vampire": "🧛♀",
    "woman_vampire_tone1": "🧛🏻♀",
    "woman_vampire_light_skin_tone": "🧛🏻♀",
    "woman_vampire_tone2": "🧛🏼♀",
    "woman_vampire_medium_light_skin_tone": "🧛🏼♀",
    "woman_vampire_tone3": "🧛🏽♀",
    "woman_vampire_medium_skin_tone": "🧛🏽♀",
    "woman_vampire_tone4": "🧛🏾♀",
    "woman_vampire_medium_dark_skin_tone": "🧛🏾♀",
    "woman_vampire_tone5": "🧛🏿♀",
    "woman_vampire_dark_skin_tone": "🧛🏿♀",
    "man_vampire": "🧛♂",
    "man_vampire_tone1": "🧛🏻♂",
    "man_vampire_light_skin_tone": "🧛🏻♂",
    "man_vampire_tone2": "🧛🏼♂",
    "man_vampire_medium_light_skin_tone": "🧛🏼♂",
    "man_vampire_tone3": "🧛🏽♂",
    "man_vampire_medium_skin_tone": "🧛🏽♂",
    "man_vampire_tone4": "🧛🏾♂",
    "man_vampire_medium_dark_skin_tone": "🧛🏾♂",
    "man_vampire_tone5": "🧛🏿♂",
    "man_vampire_dark_skin_tone": "🧛🏿♂",
    "zombie": "🧟",
    "woman_zombie": "🧟♀",
    "man_zombie": "🧟♂",
    "genie": "🧞",
    "woman_genie": "🧞♀",
    "man_genie": "🧞♂",
    "merperson": "🧜",
    "merperson_tone1": "🧜🏻",
    "merperson_light_skin_tone": "🧜🏻",
    "merperson_tone2": "🧜🏼",
    "merperson_medium_light_skin_tone": "🧜🏼",
    "merperson_tone3": "🧜🏽",
    "merperson_medium_skin_tone": "🧜🏽",
    "merperson_tone4": "🧜🏾",
    "merperson_medium_dark_skin_tone": "🧜🏾",
    "merperson_tone5": "🧜🏿",
    "merperson_dark_skin_tone": "🧜🏿",
    "mermaid": "🧜♀",
    "mermaid_tone1": "🧜🏻♀",
    "mermaid_light_skin_tone": "🧜🏻♀",
    "mermaid_tone2": "🧜🏼♀",
    "mermaid_medium_light_skin_tone": "🧜🏼♀",
    "mermaid_tone3": "🧜🏽♀",
    "mermaid_medium_skin_tone": "🧜🏽♀",
    "mermaid_tone4": "🧜🏾♀",
    "mermaid_medium_dark_skin_tone": "🧜🏾♀",
    "mermaid_tone5": "🧜🏿♀",
    "mermaid_dark_skin_tone": "🧜🏿♀",
    "merman": "🧜♂",
    "merman_tone1": "🧜🏻♂",
    "merman_light_skin_tone": "🧜🏻♂",
    "merman_tone2": "🧜🏼♂",
    "merman_medium_light_skin_tone": "🧜🏼♂",
    "merman_tone3": "🧜🏽♂",
    "merman_medium_skin_tone": "🧜🏽♂",
    "merman_tone4": "🧜🏾♂",
    "merman_medium_dark_skin_tone": "🧜🏾♂",
    "merman_tone5": "🧜🏿♂",
    "merman_dark_skin_tone": "🧜🏿♂",
    "fairy": "🧚",
    "fairy_tone1": "🧚🏻",
    "fairy_light_skin_tone": "🧚🏻",
    "fairy_tone2": "🧚🏼",
    "fairy_medium_light_skin_tone": "🧚🏼",
    "fairy_tone3": "🧚🏽",
    "fairy_medium_skin_tone": "🧚🏽",
    "fairy_tone4": "🧚🏾",
    "fairy_medium_dark_skin_tone": "🧚🏾",
    "fairy_tone5": "🧚🏿",
    "fairy_dark_skin_tone": "🧚🏿",
    "woman_fairy": "🧚♀",
    "woman_fairy_tone1": "🧚🏻♀",
    "woman_fairy_light_skin_tone": "🧚🏻♀",
    "woman_fairy_tone2": "🧚🏼♀",
    "woman_fairy_medium_light_skin_tone": "🧚🏼♀",
    "woman_fairy_tone3": "🧚🏽♀",
    "woman_fairy_medium_skin_tone": "🧚🏽♀",
    "woman_fairy_tone4": "🧚🏾♀",
    "woman_fairy_medium_dark_skin_tone": "🧚🏾♀",
    "woman_fairy_tone5": "🧚🏿♀",
    "woman_fairy_dark_skin_tone": "🧚🏿♀",
    "man_fairy": "🧚♂",
    "man_fairy_tone1": "🧚🏻♂",
    "man_fairy_light_skin_tone": "🧚🏻♂",
    "man_fairy_tone2": "🧚🏼♂",
    "man_fairy_medium_light_skin_tone": "🧚🏼♂",
    "man_fairy_tone3": "🧚🏽♂",
    "man_fairy_medium_skin_tone": "🧚🏽♂",
    "man_fairy_tone4": "🧚🏾♂",
    "man_fairy_medium_dark_skin_tone": "🧚🏾♂",
    "man_fairy_tone5": "🧚🏿♂",
    "man_fairy_dark_skin_tone": "🧚🏿♂",
    "angel": "👼",
    "angel_tone1": "👼🏻",
    "angel_tone2": "👼🏼",
    "angel_tone3": "👼🏽",
    "angel_tone4": "👼🏾",
    "angel_tone5": "👼🏿",
    "pregnant_woman": "🤰",
    "expecting_woman": "🤰",
    "pregnant_woman_tone1": "🤰🏻",
    "expecting_woman_tone1": "🤰🏻",
    "pregnant_woman_tone2": "🤰🏼",
    "expecting_woman_tone2": "🤰🏼",
    "pregnant_woman_tone3": "🤰🏽",
    "expecting_woman_tone3": "🤰🏽",
    "pregnant_woman_tone4": "🤰🏾",
    "expecting_woman_tone4": "🤰🏾",
    "pregnant_woman_tone5": "🤰🏿",
    "expecting_woman_tone5": "🤰🏿",
    "breast_feeding": "🤱",
    "breast_feeding_tone1": "🤱🏻",
    "breast_feeding_light_skin_tone": "🤱🏻",
    "breast_feeding_tone2": "🤱🏼",
    "breast_feeding_medium_light_skin_tone": "🤱🏼",
    "breast_feeding_tone3": "🤱🏽",
    "breast_feeding_medium_skin_tone": "🤱🏽",
    "breast_feeding_tone4": "🤱🏾",
    "breast_feeding_medium_dark_skin_tone": "🤱🏾",
    "breast_feeding_tone5": "🤱🏿",
    "breast_feeding_dark_skin_tone": "🤱🏿",
    "person_bowing": "🙇",
    "bow": "🙇",
    "person_bowing_tone1": "🙇🏻",
    "bow_tone1": "🙇🏻",
    "person_bowing_tone2": "🙇🏼",
    "bow_tone2": "🙇🏼",
    "person_bowing_tone3": "🙇🏽",
    "bow_tone3": "🙇🏽",
    "person_bowing_tone4": "🙇🏾",
    "bow_tone4": "🙇🏾",
    "person_bowing_tone5": "🙇🏿",
    "bow_tone5": "🙇🏿",
    "woman_bowing": "🙇♀",
    "woman_bowing_tone1": "🙇🏻♀",
    "woman_bowing_light_skin_tone": "🙇🏻♀",
    "woman_bowing_tone2": "🙇🏼♀",
    "woman_bowing_medium_light_skin_tone": "🙇🏼♀",
    "woman_bowing_tone3": "🙇🏽♀",
    "woman_bowing_medium_skin_tone": "🙇🏽♀",
    "woman_bowing_tone4": "🙇🏾♀",
    "woman_bowing_medium_dark_skin_tone": "🙇🏾♀",
    "woman_bowing_tone5": "🙇🏿♀",
    "woman_bowing_dark_skin_tone": "🙇🏿♀",
    "man_bowing": "🙇♂",
    "man_bowing_tone1": "🙇🏻♂",
    "man_bowing_light_skin_tone": "🙇🏻♂",
    "man_bowing_tone2": "🙇🏼♂",
    "man_bowing_medium_light_skin_tone": "🙇🏼♂",
    "man_bowing_tone3": "🙇🏽♂",
    "man_bowing_medium_skin_tone": "🙇🏽♂",
    "man_bowing_tone4": "🙇🏾♂",
    "man_bowing_medium_dark_skin_tone": "🙇🏾♂",
    "man_bowing_tone5": "🙇🏿♂",
    "man_bowing_dark_skin_tone": "🙇🏿♂",
    "person_tipping_hand": "💁",
    "information_desk_person": "💁",
    "person_tipping_hand_tone1": "💁🏻",
    "information_desk_person_tone1": "💁🏻",
    "person_tipping_hand_tone2": "💁🏼",
    "information_desk_person_tone2": "💁🏼",
    "person_tipping_hand_tone3": "💁🏽",
    "information_desk_person_tone3": "💁🏽",
    "person_tipping_hand_tone4": "💁🏾",
    "information_desk_person_tone4": "💁🏾",
    "person_tipping_hand_tone5": "💁🏿",
    "information_desk_person_tone5": "💁🏿",
    "woman_tipping_hand": "💁♀",
    "woman_tipping_hand_tone1": "💁🏻♀",
    "woman_tipping_hand_light_skin_tone": "💁🏻♀",
    "woman_tipping_hand_tone2": "💁🏼♀",
    "woman_tipping_hand_medium_light_skin_tone": "💁🏼♀",
    "woman_tipping_hand_tone3": "💁🏽♀",
    "woman_tipping_hand_medium_skin_tone": "💁🏽♀",
    "woman_tipping_hand_tone4": "💁🏾♀",
    "woman_tipping_hand_medium_dark_skin_tone": "💁🏾♀",
    "woman_tipping_hand_tone5": "💁🏿♀",
    "woman_tipping_hand_dark_skin_tone": "💁🏿♀",
    "man_tipping_hand": "💁♂",
    "man_tipping_hand_tone1": "💁🏻♂",
    "man_tipping_hand_light_skin_tone": "💁🏻♂",
    "man_tipping_hand_tone2": "💁🏼♂",
    "man_tipping_hand_medium_light_skin_tone": "💁🏼♂",
    "man_tipping_hand_tone3": "💁🏽♂",
    "man_tipping_hand_medium_skin_tone": "💁🏽♂",
    "man_tipping_hand_tone4": "💁🏾♂",
    "man_tipping_hand_medium_dark_skin_tone": "💁🏾♂",
    "man_tipping_hand_tone5": "💁🏿♂",
    "man_tipping_hand_dark_skin_tone": "💁🏿♂",
    "person_gesturing_no": "🙅",
    "no_good": "🙅",
    "person_gesturing_no_tone1": "🙅🏻",
    "no_good_tone1": "🙅🏻",
    "person_gesturing_no_tone2": "🙅🏼",
    "no_good_tone2": "🙅🏼",
    "person_gesturing_no_tone3": "🙅🏽",
    "no_good_tone3": "🙅🏽",
    "person_gesturing_no_tone4": "🙅🏾",
    "no_good_tone4": "🙅🏾",
    "person_gesturing_no_tone5": "🙅🏿",
    "no_good_tone5": "🙅🏿",
    "woman_gesturing_no": "🙅♀",
    "woman_gesturing_no_tone1": "🙅🏻♀",
    "woman_gesturing_no_light_skin_tone": "🙅🏻♀",
    "woman_gesturing_no_tone2": "🙅🏼♀",
    "woman_gesturing_no_medium_light_skin_tone": "🙅🏼♀",
    "woman_gesturing_no_tone3": "🙅🏽♀",
    "woman_gesturing_no_medium_skin_tone": "🙅🏽♀",
    "woman_gesturing_no_tone4": "🙅🏾♀",
    "woman_gesturing_no_medium_dark_skin_tone": "🙅🏾♀",
    "woman_gesturing_no_tone5": "🙅🏿♀",
    "woman_gesturing_no_dark_skin_tone": "🙅🏿♀",
    "man_gesturing_no": "🙅♂",
    "man_gesturing_no_tone1": "🙅🏻♂",
    "man_gesturing_no_light_skin_tone": "🙅🏻♂",
    "man_gesturing_no_tone2": "🙅🏼♂",
    "man_gesturing_no_medium_light_skin_tone": "🙅🏼♂",
    "man_gesturing_no_tone3": "🙅🏽♂",
    "man_gesturing_no_medium_skin_tone": "🙅🏽♂",
    "man_gesturing_no_tone4": "🙅🏾♂",
    "man_gesturing_no_medium_dark_skin_tone": "🙅🏾♂",
    "man_gesturing_no_tone5": "🙅🏿♂",
    "man_gesturing_no_dark_skin_tone": "🙅🏿♂",
    "person_gesturing_ok": "🙆",
    "ok_woman": "🙆",
    "person_gesturing_ok_tone1": "🙆🏻",
    "ok_woman_tone1": "🙆🏻",
    "person_gesturing_ok_tone2": "🙆🏼",
    "ok_woman_tone2": "🙆🏼",
    "person_gesturing_ok_tone3": "🙆🏽",
    "ok_woman_tone3": "🙆🏽",
    "person_gesturing_ok_tone4": "🙆🏾",
    "ok_woman_tone4": "🙆🏾",
    "person_gesturing_ok_tone5": "🙆🏿",
    "ok_woman_tone5": "🙆🏿",
    "woman_gesturing_ok": "🙆♀",
    "woman_gesturing_ok_tone1": "🙆🏻♀",
    "woman_gesturing_ok_light_skin_tone": "🙆🏻♀",
    "woman_gesturing_ok_tone2": "🙆🏼♀",
    "woman_gesturing_ok_medium_light_skin_tone": "🙆🏼♀",
    "woman_gesturing_ok_tone3": "🙆🏽♀",
    "woman_gesturing_ok_medium_skin_tone": "🙆🏽♀",
    "woman_gesturing_ok_tone4": "🙆🏾♀",
    "woman_gesturing_ok_medium_dark_skin_tone": "🙆🏾♀",
    "woman_gesturing_ok_tone5": "🙆🏿♀",
    "woman_gesturing_ok_dark_skin_tone": "🙆🏿♀",
    "man_gesturing_ok": "🙆♂",
    "man_gesturing_ok_tone1": "🙆🏻♂",
    "man_gesturing_ok_light_skin_tone": "🙆🏻♂",
    "man_gesturing_ok_tone2": "🙆🏼♂",
    "man_gesturing_ok_medium_light_skin_tone": "🙆🏼♂",
    "man_gesturing_ok_tone3": "🙆🏽♂",
    "man_gesturing_ok_medium_skin_tone": "🙆🏽♂",
    "man_gesturing_ok_tone4": "🙆🏾♂",
    "man_gesturing_ok_medium_dark_skin_tone": "🙆🏾♂",
    "man_gesturing_ok_tone5": "🙆🏿♂",
    "man_gesturing_ok_dark_skin_tone": "🙆🏿♂",
    "person_raising_hand": "🙋",
    "raising_hand": "🙋",
    "person_raising_hand_tone1": "🙋🏻",
    "raising_hand_tone1": "🙋🏻",
    "person_raising_hand_tone2": "🙋🏼",
    "raising_hand_tone2": "🙋🏼",
    "person_raising_hand_tone3": "🙋🏽",
    "raising_hand_tone3": "🙋🏽",
    "person_raising_hand_tone4": "🙋🏾",
    "raising_hand_tone4": "🙋🏾",
    "person_raising_hand_tone5": "🙋🏿",
    "raising_hand_tone5": "🙋🏿",
    "woman_raising_hand": "🙋♀",
    "woman_raising_hand_tone1": "🙋🏻♀",
    "woman_raising_hand_light_skin_tone": "🙋🏻♀",
    "woman_raising_hand_tone2": "🙋🏼♀",
    "woman_raising_hand_medium_light_skin_tone": "🙋🏼♀",
    "woman_raising_hand_tone3": "🙋🏽♀",
    "woman_raising_hand_medium_skin_tone": "🙋🏽♀",
    "woman_raising_hand_tone4": "🙋🏾♀",
    "woman_raising_hand_medium_dark_skin_tone": "🙋🏾♀",
    "woman_raising_hand_tone5": "🙋🏿♀",
    "woman_raising_hand_dark_skin_tone": "🙋🏿♀",
    "man_raising_hand": "🙋♂",
    "man_raising_hand_tone1": "🙋🏻♂",
    "man_raising_hand_light_skin_tone": "🙋🏻♂",
    "man_raising_hand_tone2": "🙋🏼♂",
    "man_raising_hand_medium_light_skin_tone": "🙋🏼♂",
    "man_raising_hand_tone3": "🙋🏽♂",
    "man_raising_hand_medium_skin_tone": "🙋🏽♂",
    "man_raising_hand_tone4": "🙋🏾♂",
    "man_raising_hand_medium_dark_skin_tone": "🙋🏾♂",
    "man_raising_hand_tone5": "🙋🏿♂",
    "man_raising_hand_dark_skin_tone": "🙋🏿♂",
    "deaf_person": "🧏",
    "deaf_person_tone1": "🧏🏻",
    "deaf_person_light_skin_tone": "🧏🏻",
    "deaf_person_tone2": "🧏🏼",
    "deaf_person_medium_light_skin_tone": "🧏🏼",
    "deaf_person_tone3": "🧏🏽",
    "deaf_person_medium_skin_tone": "🧏🏽",
    "deaf_person_tone4": "🧏🏾",
    "deaf_person_medium_dark_skin_tone": "🧏🏾",
    "deaf_person_tone5": "🧏🏿",
    "deaf_person_dark_skin_tone": "🧏🏿",
    "deaf_woman": "🧏♀",
    "deaf_woman_tone1": "🧏🏻♀",
    "deaf_woman_light_skin_tone": "🧏🏻♀",
    "deaf_woman_tone2": "🧏🏼♀",
    "deaf_woman_medium_light_skin_tone": "🧏🏼♀",
    "deaf_woman_tone3": "🧏🏽♀",
    "deaf_woman_medium_skin_tone": "🧏🏽♀",
    "deaf_woman_tone4": "🧏🏾♀",
    "deaf_woman_medium_dark_skin_tone": "🧏🏾♀",
    "deaf_woman_tone5": "🧏🏿♀",
    "deaf_woman_dark_skin_tone": "🧏🏿♀",
    "deaf_man": "🧏♂",
    "deaf_man_tone1": "🧏🏻♂",
    "deaf_man_light_skin_tone": "🧏🏻♂",
    "deaf_man_tone2": "🧏🏼♂",
    "deaf_man_medium_light_skin_tone": "🧏🏼♂",
    "deaf_man_tone3": "🧏🏽♂",
    "deaf_man_medium_skin_tone": "🧏🏽♂",
    "deaf_man_tone4": "🧏🏾♂",
    "deaf_man_medium_dark_skin_tone": "🧏🏾♂",
    "deaf_man_tone5": "🧏🏿♂",
    "deaf_man_dark_skin_tone": "🧏🏿♂",
    "person_facepalming": "🤦",
    "face_palm": "🤦",
    "facepalm": "🤦",
    "person_facepalming_tone1": "🤦🏻",
    "face_palm_tone1": "🤦🏻",
    "facepalm_tone1": "🤦🏻",
    "person_facepalming_tone2": "🤦🏼",
    "face_palm_tone2": "🤦🏼",
    "facepalm_tone2": "🤦🏼",
    "person_facepalming_tone3": "🤦🏽",
    "face_palm_tone3": "🤦🏽",
    "facepalm_tone3": "🤦🏽",
    "person_facepalming_tone4": "🤦🏾",
    "face_palm_tone4": "🤦🏾",
    "facepalm_tone4": "🤦🏾",
    "person_facepalming_tone5": "🤦🏿",
    "face_palm_tone5": "🤦🏿",
    "facepalm_tone5": "🤦🏿",
    "woman_facepalming": "🤦♀",
    "woman_facepalming_tone1": "🤦🏻♀",
    "woman_facepalming_light_skin_tone": "🤦🏻♀",
    "woman_facepalming_tone2": "🤦🏼♀",
    "woman_facepalming_medium_light_skin_tone": "🤦🏼♀",
    "woman_facepalming_tone3": "🤦🏽♀",
    "woman_facepalming_medium_skin_tone": "🤦🏽♀",
    "woman_facepalming_tone4": "🤦🏾♀",
    "woman_facepalming_medium_dark_skin_tone": "🤦🏾♀",
    "woman_facepalming_tone5": "🤦🏿♀",
    "woman_facepalming_dark_skin_tone": "🤦🏿♀",
    "man_facepalming": "🤦♂",
    "man_facepalming_tone1": "🤦🏻♂",
    "man_facepalming_light_skin_tone": "🤦🏻♂",
    "man_facepalming_tone2": "🤦🏼♂",
    "man_facepalming_medium_light_skin_tone": "🤦🏼♂",
    "man_facepalming_tone3": "🤦🏽♂",
    "man_facepalming_medium_skin_tone": "🤦🏽♂",
    "man_facepalming_tone4": "🤦🏾♂",
    "man_facepalming_medium_dark_skin_tone": "🤦🏾♂",
    "man_facepalming_tone5": "🤦🏿♂",
    "man_facepalming_dark_skin_tone": "🤦🏿♂",
    "person_shrugging": "🤷",
    "shrug": "🤷",
    "person_shrugging_tone1": "🤷🏻",
    "shrug_tone1": "🤷🏻",
    "person_shrugging_tone2": "🤷🏼",
    "shrug_tone2": "🤷🏼",
    "person_shrugging_tone3": "🤷🏽",
    "shrug_tone3": "🤷🏽",
    "person_shrugging_tone4": "🤷🏾",
    "shrug_tone4": "🤷🏾",
    "person_shrugging_tone5": "🤷🏿",
    "shrug_tone5": "🤷🏿",
    "woman_shrugging": "🤷♀",
    "woman_shrugging_tone1": "🤷🏻♀",
    "woman_shrugging_light_skin_tone": "🤷🏻♀",
    "woman_shrugging_tone2": "🤷🏼♀",
    "woman_shrugging_medium_light_skin_tone": "🤷🏼♀",
    "woman_shrugging_tone3": "🤷🏽♀",
    "woman_shrugging_medium_skin_tone": "🤷🏽♀",
    "woman_shrugging_tone4": "🤷🏾♀",
    "woman_shrugging_medium_dark_skin_tone": "🤷🏾♀",
    "woman_shrugging_tone5": "🤷🏿♀",
    "woman_shrugging_dark_skin_tone": "🤷🏿♀",
    "man_shrugging": "🤷♂",
    "man_shrugging_tone1": "🤷🏻♂",
    "man_shrugging_light_skin_tone": "🤷🏻♂",
    "man_shrugging_tone2": "🤷🏼♂",
    "man_shrugging_medium_light_skin_tone": "🤷🏼♂",
    "man_shrugging_tone3": "🤷🏽♂",
    "man_shrugging_medium_skin_tone": "🤷🏽♂",
    "man_shrugging_tone4": "🤷🏾♂",
    "man_shrugging_medium_dark_skin_tone": "🤷🏾♂",
    "man_shrugging_tone5": "🤷🏿♂",
    "man_shrugging_dark_skin_tone": "🤷🏿♂",
    "person_pouting": "🙎",
    "person_with_pouting_face": "🙎",
    "person_pouting_tone1": "🙎🏻",
    "person_with_pouting_face_tone1": "🙎🏻",
    "person_pouting_tone2": "🙎🏼",
    "person_with_pouting_face_tone2": "🙎🏼",
    "person_pouting_tone3": "🙎🏽",
    "person_with_pouting_face_tone3": "🙎🏽",
    "person_pouting_tone4": "🙎🏾",
    "person_with_pouting_face_tone4": "🙎🏾",
    "person_pouting_tone5": "🙎🏿",
    "person_with_pouting_face_tone5": "🙎🏿",
    "woman_pouting": "🙎♀",
    "woman_pouting_tone1": "🙎🏻♀",
    "woman_pouting_light_skin_tone": "🙎🏻♀",
    "woman_pouting_tone2": "🙎🏼♀",
    "woman_pouting_medium_light_skin_tone": "🙎🏼♀",
    "woman_pouting_tone3": "🙎🏽♀",
    "woman_pouting_medium_skin_tone": "🙎🏽♀",
    "woman_pouting_tone4": "🙎🏾♀",
    "woman_pouting_medium_dark_skin_tone": "🙎🏾♀",
    "woman_pouting_tone5": "🙎🏿♀",
    "woman_pouting_dark_skin_tone": "🙎🏿♀",
    "man_pouting": "🙎♂",
    "man_pouting_tone1": "🙎🏻♂",
    "man_pouting_light_skin_tone": "🙎🏻♂",
    "man_pouting_tone2": "🙎🏼♂",
    "man_pouting_medium_light_skin_tone": "🙎🏼♂",
    "man_pouting_tone3": "🙎🏽♂",
    "man_pouting_medium_skin_tone": "🙎🏽♂",
    "man_pouting_tone4": "🙎🏾♂",
    "man_pouting_medium_dark_skin_tone": "🙎🏾♂",
    "man_pouting_tone5": "🙎🏿♂",
    "man_pouting_dark_skin_tone": "🙎🏿♂",
    "person_frowning": "🙍",
    "person_frowning_tone1": "🙍🏻",
    "person_frowning_tone2": "🙍🏼",
    "person_frowning_tone3": "🙍🏽",
    "person_frowning_tone4": "🙍🏾",
    "person_frowning_tone5": "🙍🏿",
    "woman_frowning": "🙍♀",
    "woman_frowning_tone1": "🙍🏻♀",
    "woman_frowning_light_skin_tone": "🙍🏻♀",
    "woman_frowning_tone2": "🙍🏼♀",
    "woman_frowning_medium_light_skin_tone": "🙍🏼♀",
    "woman_frowning_tone3": "🙍🏽♀",
    "woman_frowning_medium_skin_tone": "🙍🏽♀",
    "woman_frowning_tone4": "🙍🏾♀",
    "woman_frowning_medium_dark_skin_tone": "🙍🏾♀",
    "woman_frowning_tone5": "🙍🏿♀",
    "woman_frowning_dark_skin_tone": "🙍🏿♀",
    "man_frowning": "🙍♂",
    "man_frowning_tone1": "🙍🏻♂",
    "man_frowning_light_skin_tone": "🙍🏻♂",
    "man_frowning_tone2": "🙍🏼♂",
    "man_frowning_medium_light_skin_tone": "🙍🏼♂",
    "man_frowning_tone3": "🙍🏽♂",
    "man_frowning_medium_skin_tone": "🙍🏽♂",
    "man_frowning_tone4": "🙍🏾♂",
    "man_frowning_medium_dark_skin_tone": "🙍🏾♂",
    "man_frowning_tone5": "🙍🏿♂",
    "man_frowning_dark_skin_tone": "🙍🏿♂",
    "person_getting_haircut": "💇",
    "haircut": "💇",
    "person_getting_haircut_tone1": "💇🏻",
    "haircut_tone1": "💇🏻",
    "person_getting_haircut_tone2": "💇🏼",
    "haircut_tone2": "💇🏼",
    "person_getting_haircut_tone3": "💇🏽",
    "haircut_tone3": "💇🏽",
    "person_getting_haircut_tone4": "💇🏾",
    "haircut_tone4": "💇🏾",
    "person_getting_haircut_tone5": "💇🏿",
    "haircut_tone5": "💇🏿",
    "woman_getting_haircut": "💇♀",
    "woman_getting_haircut_tone1": "💇🏻♀",
    "woman_getting_haircut_light_skin_tone": "💇🏻♀",
    "woman_getting_haircut_tone2": "💇🏼♀",
    "woman_getting_haircut_medium_light_skin_tone": "💇🏼♀",
    "woman_getting_haircut_tone3": "💇🏽♀",
    "woman_getting_haircut_medium_skin_tone": "💇🏽♀",
    "woman_getting_haircut_tone4": "💇🏾♀",
    "woman_getting_haircut_medium_dark_skin_tone": "💇🏾♀",
    "woman_getting_haircut_tone5": "💇🏿♀",
    "woman_getting_haircut_dark_skin_tone": "💇🏿♀",
    "man_getting_haircut": "💇♂",
    "man_getting_haircut_tone1": "💇🏻♂",
    "man_getting_haircut_light_skin_tone": "💇🏻♂",
    "man_getting_haircut_tone2": "💇🏼♂",
    "man_getting_haircut_medium_light_skin_tone": "💇🏼♂",
    "man_getting_haircut_tone3": "💇🏽♂",
    "man_getting_haircut_medium_skin_tone": "💇🏽♂",
    "man_getting_haircut_tone4": "💇🏾♂",
    "man_getting_haircut_medium_dark_skin_tone": "💇🏾♂",
    "man_getting_haircut_tone5": "💇🏿♂",
    "man_getting_haircut_dark_skin_tone": "💇🏿♂",
    "person_getting_massage": "💆",
    "massage": "💆",
    "person_getting_massage_tone1": "💆🏻",
    "massage_tone1": "💆🏻",
    "person_getting_massage_tone2": "💆🏼",
    "massage_tone2": "💆🏼",
    "person_getting_massage_tone3": "💆🏽",
    "massage_tone3": "💆🏽",
    "person_getting_massage_tone4": "💆🏾",
    "massage_tone4": "💆🏾",
    "person_getting_massage_tone5": "💆🏿",
    "massage_tone5": "💆🏿",
    "woman_getting_face_massage": "💆♀",
    "woman_getting_face_massage_tone1": "💆🏻♀",
    "woman_getting_face_massage_light_skin_tone": "💆🏻♀",
    "woman_getting_face_massage_tone2": "💆🏼♀",
    "woman_getting_face_massage_medium_light_skin_tone": "💆🏼♀",
    "woman_getting_face_massage_tone3": "💆🏽♀",
    "woman_getting_face_massage_medium_skin_tone": "💆🏽♀",
    "woman_getting_face_massage_tone4": "💆🏾♀",
    "woman_getting_face_massage_medium_dark_skin_tone": "💆🏾♀",
    "woman_getting_face_massage_tone5": "💆🏿♀",
    "woman_getting_face_massage_dark_skin_tone": "💆🏿♀",
    "man_getting_face_massage": "💆♂",
    "man_getting_face_massage_tone1": "💆🏻♂",
    "man_getting_face_massage_light_skin_tone": "💆🏻♂",
    "man_getting_face_massage_tone2": "💆🏼♂",
    "man_getting_face_massage_medium_light_skin_tone": "💆🏼♂",
    "man_getting_face_massage_tone3": "💆🏽♂",
    "man_getting_face_massage_medium_skin_tone": "💆🏽♂",
    "man_getting_face_massage_tone4": "💆🏾♂",
    "man_getting_face_massage_medium_dark_skin_tone": "💆🏾♂",
    "man_getting_face_massage_tone5": "💆🏿♂",
    "man_getting_face_massage_dark_skin_tone": "💆🏿♂",
    "person_in_steamy_room": "🧖",
    "person_in_steamy_room_tone1": "🧖🏻",
    "person_in_steamy_room_light_skin_tone": "🧖🏻",
    "person_in_steamy_room_tone2": "🧖🏼",
    "person_in_steamy_room_medium_light_skin_tone": "🧖🏼",
    "person_in_steamy_room_tone3": "🧖🏽",
    "person_in_steamy_room_medium_skin_tone": "🧖🏽",
    "person_in_steamy_room_tone4": "🧖🏾",
    "person_in_steamy_room_medium_dark_skin_tone": "🧖🏾",
    "person_in_steamy_room_tone5": "🧖🏿",
    "person_in_steamy_room_dark_skin_tone": "🧖🏿",
    "woman_in_steamy_room": "🧖♀",
    "woman_in_steamy_room_tone1": "🧖🏻♀",
    "woman_in_steamy_room_light_skin_tone": "🧖🏻♀",
    "woman_in_steamy_room_tone2": "🧖🏼♀",
    "woman_in_steamy_room_medium_light_skin_tone": "🧖🏼♀",
    "woman_in_steamy_room_tone3": "🧖🏽♀",
    "woman_in_steamy_room_medium_skin_tone": "🧖🏽♀",
    "woman_in_steamy_room_tone4": "🧖🏾♀",
    "woman_in_steamy_room_medium_dark_skin_tone": "🧖🏾♀",
    "woman_in_steamy_room_tone5": "🧖🏿♀",
    "woman_in_steamy_room_dark_skin_tone": "🧖🏿♀",
    "man_in_steamy_room": "🧖♂",
    "man_in_steamy_room_tone1": "🧖🏻♂",
    "man_in_steamy_room_light_skin_tone": "🧖🏻♂",
    "man_in_steamy_room_tone2": "🧖🏼♂",
    "man_in_steamy_room_medium_light_skin_tone": "🧖🏼♂",
    "man_in_steamy_room_tone3": "🧖🏽♂",
    "man_in_steamy_room_medium_skin_tone": "🧖🏽♂",
    "man_in_steamy_room_tone4": "🧖🏾♂",
    "man_in_steamy_room_medium_dark_skin_tone": "🧖🏾♂",
    "man_in_steamy_room_tone5": "🧖🏿♂",
    "man_in_steamy_room_dark_skin_tone": "🧖🏿♂",
    "nail_care": "💅",
    "nail_care_tone1": "💅🏻",
    "nail_care_tone2": "💅🏼",
    "nail_care_tone3": "💅🏽",
    "nail_care_tone4": "💅🏾",
    "nail_care_tone5": "💅🏿",
    "selfie": "🤳",
    "selfie_tone1": "🤳🏻",
    "selfie_tone2": "🤳🏼",
    "selfie_tone3": "🤳🏽",
    "selfie_tone4": "🤳🏾",
    "selfie_tone5": "🤳🏿",
    "dancer": "💃",
    "dancer_tone1": "💃🏻",
    "dancer_tone2": "💃🏼",
    "dancer_tone3": "💃🏽",
    "dancer_tone4": "💃🏾",
    "dancer_tone5": "💃🏿",
    "man_dancing": "🕺",
    "male_dancer": "🕺",
    "man_dancing_tone1": "🕺🏻",
    "male_dancer_tone1": "🕺🏻",
    "man_dancing_tone2": "🕺🏼",
    "male_dancer_tone2": "🕺🏼",
    "man_dancing_tone3": "🕺🏽",
    "male_dancer_tone3": "🕺🏽",
    "man_dancing_tone5": "🕺🏿",
    "male_dancer_tone5": "🕺🏿",
    "man_dancing_tone4": "🕺🏾",
    "male_dancer_tone4": "🕺🏾",
    "people_with_bunny_ears_partying": "👯",
    "dancers": "👯",
    "women_with_bunny_ears_partying": "👯♀",
    "men_with_bunny_ears_partying": "👯♂",
    "levitate": "🕴",
    "man_in_business_suit_levitating": "🕴",
    "levitate_tone1": "🕴🏻",
    "man_in_business_suit_levitating_tone1": "🕴🏻",
    "man_in_business_suit_levitating_light_skin_tone": "🕴🏻",
    "levitate_tone2": "🕴🏼",
    "man_in_business_suit_levitating_tone2": "🕴🏼",
    "man_in_business_suit_levitating_medium_light_skin_tone": "🕴🏼",
    "levitate_tone3": "🕴🏽",
    "man_in_business_suit_levitating_tone3": "🕴🏽",
    "man_in_business_suit_levitating_medium_skin_tone": "🕴🏽",
    "levitate_tone4": "🕴🏾",
    "man_in_business_suit_levitating_tone4": "🕴🏾",
    "man_in_business_suit_levitating_medium_dark_skin_tone": "🕴🏾",
    "levitate_tone5": "🕴🏿",
    "man_in_business_suit_levitating_tone5": "🕴🏿",
    "man_in_business_suit_levitating_dark_skin_tone": "🕴🏿",
    "person_walking": "🚶",
    "walking": "🚶",
    "person_walking_tone1": "🚶🏻",
    "walking_tone1": "🚶🏻",
    "person_walking_tone2": "🚶🏼",
    "walking_tone2": "🚶🏼",
    "person_walking_tone3": "🚶🏽",
    "walking_tone3": "🚶🏽",
    "person_walking_tone4": "🚶🏾",
    "walking_tone4": "🚶🏾",
    "person_walking_tone5": "🚶🏿",
    "walking_tone5": "🚶🏿",
    "woman_walking": "🚶♀",
    "woman_walking_tone1": "🚶🏻♀",
    "woman_walking_light_skin_tone": "🚶🏻♀",
    "woman_walking_tone2": "🚶🏼♀",
    "woman_walking_medium_light_skin_tone": "🚶🏼♀",
    "woman_walking_tone3": "🚶🏽♀",
    "woman_walking_medium_skin_tone": "🚶🏽♀",
    "woman_walking_tone4": "🚶🏾♀",
    "woman_walking_medium_dark_skin_tone": "🚶🏾♀",
    "woman_walking_tone5": "🚶🏿♀",
    "woman_walking_dark_skin_tone": "🚶🏿♀",
    "man_walking": "🚶♂",
    "man_walking_tone1": "🚶🏻♂",
    "man_walking_light_skin_tone": "🚶🏻♂",
    "man_walking_tone2": "🚶🏼♂",
    "man_walking_medium_light_skin_tone": "🚶🏼♂",
    "man_walking_tone3": "🚶🏽♂",
    "man_walking_medium_skin_tone": "🚶🏽♂",
    "man_walking_tone4": "🚶🏾♂",
    "man_walking_medium_dark_skin_tone": "🚶🏾♂",
    "man_walking_tone5": "🚶🏿♂",
    "man_walking_dark_skin_tone": "🚶🏿♂",
    "person_running": "🏃",
    "runner": "🏃",
    "person_running_tone1": "🏃🏻",
    "runner_tone1": "🏃🏻",
    "person_running_tone2": "🏃🏼",
    "runner_tone2": "🏃🏼",
    "person_running_tone3": "🏃🏽",
    "runner_tone3": "🏃🏽",
    "person_running_tone4": "🏃🏾",
    "runner_tone4": "🏃🏾",
    "person_running_tone5": "🏃🏿",
    "runner_tone5": "🏃🏿",
    "woman_running": "🏃♀",
    "woman_running_tone1": "🏃🏻♀",
    "woman_running_light_skin_tone": "🏃🏻♀",
    "woman_running_tone2": "🏃🏼♀",
    "woman_running_medium_light_skin_tone": "🏃🏼♀",
    "woman_running_tone3": "🏃🏽♀",
    "woman_running_medium_skin_tone": "🏃🏽♀",
    "woman_running_tone4": "🏃🏾♀",
    "woman_running_medium_dark_skin_tone": "🏃🏾♀",
    "woman_running_tone5": "🏃🏿♀",
    "woman_running_dark_skin_tone": "🏃🏿♀",
    "man_running": "🏃♂",
    "man_running_tone1": "🏃🏻♂",
    "man_running_light_skin_tone": "🏃🏻♂",
    "man_running_tone2": "🏃🏼♂",
    "man_running_medium_light_skin_tone": "🏃🏼♂",
    "man_running_tone3": "🏃🏽♂",
    "man_running_medium_skin_tone": "🏃🏽♂",
    "man_running_tone4": "🏃🏾♂",
    "man_running_medium_dark_skin_tone": "🏃🏾♂",
    "man_running_tone5": "🏃🏿♂",
    "man_running_dark_skin_tone": "🏃🏿♂",
    "person_standing": "🧍",
    "person_standing_tone1": "🧍🏻",
    "person_standing_light_skin_tone": "🧍🏻",
    "person_standing_tone2": "🧍🏼",
    "person_standing_medium_light_skin_tone": "🧍🏼",
    "person_standing_tone3": "🧍🏽",
    "person_standing_medium_skin_tone": "🧍🏽",
    "person_standing_tone4": "🧍🏾",
    "person_standing_medium_dark_skin_tone": "🧍🏾",
    "person_standing_tone5": "🧍🏿",
    "person_standing_dark_skin_tone": "🧍🏿",
    "woman_standing": "🧍♀",
    "woman_standing_tone1": "🧍🏻♀",
    "woman_standing_light_skin_tone": "🧍🏻♀",
    "woman_standing_tone2": "🧍🏼♀",
    "woman_standing_medium_light_skin_tone": "🧍🏼♀",
    "woman_standing_tone3": "🧍🏽♀",
    "woman_standing_medium_skin_tone": "🧍🏽♀",
    "woman_standing_tone4": "🧍🏾♀",
    "woman_standing_medium_dark_skin_tone": "🧍🏾♀",
    "woman_standing_tone5": "🧍🏿♀",
    "woman_standing_dark_skin_tone": "🧍🏿♀",
    "man_standing": "🧍♂",
    "man_standing_tone1": "🧍🏻♂",
    "man_standing_light_skin_tone": "🧍🏻♂",
    "man_standing_tone2": "🧍🏼♂",
    "man_standing_medium_light_skin_tone": "🧍🏼♂",
    "man_standing_tone3": "🧍🏽♂",
    "man_standing_medium_skin_tone": "🧍🏽♂",
    "man_standing_tone4": "🧍🏾♂",
    "man_standing_medium_dark_skin_tone": "🧍🏾♂",
    "man_standing_tone5": "🧍🏿♂",
    "man_standing_dark_skin_tone": "🧍🏿♂",
    "person_kneeling": "🧎",
    "person_kneeling_tone1": "🧎🏻",
    "person_kneeling_light_skin_tone": "🧎🏻",
    "person_kneeling_tone2": "🧎🏼",
    "person_kneeling_medium_light_skin_tone": "🧎🏼",
    "person_kneeling_tone3": "🧎🏽",
    "person_kneeling_medium_skin_tone": "🧎🏽",
    "person_kneeling_tone4": "🧎🏾",
    "person_kneeling_medium_dark_skin_tone": "🧎🏾",
    "person_kneeling_tone5": "🧎🏿",
    "person_kneeling_dark_skin_tone": "🧎🏿",
    "woman_kneeling": "🧎♀",
    "woman_kneeling_tone1": "🧎🏻♀",
    "woman_kneeling_light_skin_tone": "🧎🏻♀",
    "woman_kneeling_tone2": "🧎🏼♀",
    "woman_kneeling_medium_light_skin_tone": "🧎🏼♀",
    "woman_kneeling_tone3": "🧎🏽♀",
    "woman_kneeling_medium_skin_tone": "🧎🏽♀",
    "woman_kneeling_tone4": "🧎🏾♀",
    "woman_kneeling_medium_dark_skin_tone": "🧎🏾♀",
    "woman_kneeling_tone5": "🧎🏿♀",
    "woman_kneeling_dark_skin_tone": "🧎🏿♀",
    "man_kneeling": "🧎♂",
    "man_kneeling_tone1": "🧎🏻♂",
    "man_kneeling_light_skin_tone": "🧎🏻♂",
    "man_kneeling_tone2": "🧎🏼♂",
    "man_kneeling_medium_light_skin_tone": "🧎🏼♂",
    "man_kneeling_tone3": "🧎🏽♂",
    "man_kneeling_medium_skin_tone": "🧎🏽♂",
    "man_kneeling_tone4": "🧎🏾♂",
    "man_kneeling_medium_dark_skin_tone": "🧎🏾♂",
    "man_kneeling_tone5": "🧎🏿♂",
    "man_kneeling_dark_skin_tone": "🧎🏿♂",
    "woman_with_probing_cane": "👩🦯",
    "woman_with_probing_cane_tone1": "👩🏻🦯",
    "woman_with_probing_cane_light_skin_tone": "👩🏻🦯",
    "woman_with_probing_cane_tone2": "👩🏼🦯",
    "woman_with_probing_cane_medium_light_skin_tone": "👩🏼🦯",
    "woman_with_probing_cane_tone3": "👩🏽🦯",
    "woman_with_probing_cane_medium_skin_tone": "👩🏽🦯",
    "woman_with_probing_cane_tone4": "👩🏾🦯",
    "woman_with_probing_cane_medium_dark_skin_tone": "👩🏾🦯",
    "woman_with_probing_cane_tone5": "👩🏿🦯",
    "woman_with_probing_cane_dark_skin_tone": "👩🏿🦯",
    "man_with_probing_cane": "👨🦯",
    "man_with_probing_cane_tone1": "👨🏻🦯",
    "man_with_probing_cane_light_skin_tone": "👨🏻🦯",
    "man_with_probing_cane_tone2": "👨🏼🦯",
    "man_with_probing_cane_medium_light_skin_tone": "👨🏼🦯",
    "man_with_probing_cane_tone3": "👨🏽🦯",
    "man_with_probing_cane_medium_skin_tone": "👨🏽🦯",
    "man_with_probing_cane_tone4": "👨🏾🦯",
    "man_with_probing_cane_medium_dark_skin_tone": "👨🏾🦯",
    "man_with_probing_cane_tone5": "👨🏿🦯",
    "man_with_probing_cane_dark_skin_tone": "👨🏿🦯",
    "woman_in_motorized_wheelchair": "👩🦼",
    "woman_in_motorized_wheelchair_tone1": "👩🏻🦼",
    "woman_in_motorized_wheelchair_light_skin_tone": "👩🏻🦼",
    "woman_in_motorized_wheelchair_tone2": "👩🏼🦼",
    "woman_in_motorized_wheelchair_medium_light_skin_tone": "👩🏼🦼",
    "woman_in_motorized_wheelchair_tone3": "👩🏽🦼",
    "woman_in_motorized_wheelchair_medium_skin_tone": "👩🏽🦼",
    "woman_in_motorized_wheelchair_tone4": "👩🏾🦼",
    "woman_in_motorized_wheelchair_medium_dark_skin_tone": "👩🏾🦼",
    "woman_in_motorized_wheelchair_tone5": "👩🏿🦼",
    "woman_in_motorized_wheelchair_dark_skin_tone": "👩🏿🦼",
    "man_in_motorized_wheelchair": "👨🦼",
    "man_in_motorized_wheelchair_tone1": "👨🏻🦼",
    "man_in_motorized_wheelchair_light_skin_tone": "👨🏻🦼",
    "man_in_motorized_wheelchair_tone2": "👨🏼🦼",
    "man_in_motorized_wheelchair_medium_light_skin_tone": "👨🏼🦼",
    "man_in_motorized_wheelchair_tone3": "👨🏽🦼",
    "man_in_motorized_wheelchair_medium_skin_tone": "👨🏽🦼",
    "man_in_motorized_wheelchair_tone4": "👨🏾🦼",
    "man_in_motorized_wheelchair_medium_dark_skin_tone": "👨🏾🦼",
    "man_in_motorized_wheelchair_tone5": "👨🏿🦼",
    "man_in_motorized_wheelchair_dark_skin_tone": "👨🏿🦼",
    "woman_in_manual_wheelchair": "👩🦽",
    "woman_in_manual_wheelchair_tone1": "👩🏻🦽",
    "woman_in_manual_wheelchair_light_skin_tone": "👩🏻🦽",
    "woman_in_manual_wheelchair_tone2": "👩🏼🦽",
    "woman_in_manual_wheelchair_medium_light_skin_tone": "👩🏼🦽",
    "woman_in_manual_wheelchair_tone3": "👩🏽🦽",
    "woman_in_manual_wheelchair_medium_skin_tone": "👩🏽🦽",
    "woman_in_manual_wheelchair_tone4": "👩🏾🦽",
    "woman_in_manual_wheelchair_medium_dark_skin_tone": "👩🏾🦽",
    "woman_in_manual_wheelchair_tone5": "👩🏿🦽",
    "woman_in_manual_wheelchair_dark_skin_tone": "👩🏿🦽",
    "man_in_manual_wheelchair": "👨🦽",
    "man_in_manual_wheelchair_tone1": "👨🏻🦽",
    "man_in_manual_wheelchair_light_skin_tone": "👨🏻🦽",
    "man_in_manual_wheelchair_tone2": "👨🏼🦽",
    "man_in_manual_wheelchair_medium_light_skin_tone": "👨🏼🦽",
    "man_in_manual_wheelchair_tone3": "👨🏽🦽",
    "man_in_manual_wheelchair_medium_skin_tone": "👨🏽🦽",
    "man_in_manual_wheelchair_tone4": "👨🏾🦽",
    "man_in_manual_wheelchair_medium_dark_skin_tone": "👨🏾🦽",
    "man_in_manual_wheelchair_tone5": "👨🏿🦽",
    "man_in_manual_wheelchair_dark_skin_tone": "👨🏿🦽",
    "people_holding_hands": "🧑🤝🧑",
    "couple": "👫",
    "two_women_holding_hands": "👭",
    "two_men_holding_hands": "👬",
    "couple_with_heart": "💑",
    "couple_with_heart_woman_man": "👩❤👨",
    "couple_ww": "👩❤👩",
    "couple_with_heart_ww": "👩❤👩",
    "couple_mm": "👨❤👨",
    "couple_with_heart_mm": "👨❤👨",
    "couplekiss": "💏",
    "kiss_woman_man": "👩❤💋👨",
    "kiss_ww": "👩❤💋👩",
    "couplekiss_ww": "👩❤💋👩",
    "kiss_mm": "👨❤💋👨",
    "couplekiss_mm": "👨❤💋👨",
    "family": "👪",
    "family_man_woman_boy": "👨👩👦",
    "family_mwg": "👨👩👧",
    "family_mwgb": "👨👩👧👦",
    "family_mwbb": "👨👩👦👦",
    "family_mwgg": "👨👩👧👧",
    "family_wwb": "👩👩👦",
    "family_wwg": "👩👩👧",
    "family_wwgb": "👩👩👧👦",
    "family_wwbb": "👩👩👦👦",
    "family_wwgg": "👩👩👧👧",
    "family_mmb": "👨👨👦",
    "family_mmg": "👨👨👧",
    "family_mmgb": "👨👨👧👦",
    "family_mmbb": "👨👨👦👦",
    "family_mmgg": "👨👨👧👧",
    "family_woman_boy": "👩👦",
    "family_woman_girl": "👩👧",
    "family_woman_girl_boy": "👩👧👦",
    "family_woman_boy_boy": "👩👦👦",
    "family_woman_girl_girl": "👩👧👧",
    "family_man_boy": "👨👦",
    "family_man_girl": "👨👧",
    "family_man_girl_boy": "👨👧👦",
    "family_man_boy_boy": "👨👦👦",
    "family_man_girl_girl": "👨👧👧",
    "yarn": "🧶",
    "thread": "🧵",
    "coat": "🧥",
    "lab_coat": "🥼",
    "safety_vest": "🦺",
    "womans_clothes": "👚",
    "shirt": "👕",
    "jeans": "👖",
    "shorts": "🩳",
    "necktie": "👔",
    "dress": "👗",
    "bikini": "👙",
    "one_piece_swimsuit": "🩱",
    "kimono": "👘",
    "sari": "🥻",
    "womans_flat_shoe": "🥿",
    "high_heel": "👠",
    "sandal": "👡",
    "boot": "👢",
    "ballet_shoes": "🩰",
    "mans_shoe": "👞",
    "athletic_shoe": "👟",
    "hiking_boot": "🥾",
    "briefs": "🩲",
    "socks": "🧦",
    "gloves": "🧤",
    "scarf": "🧣",
    "tophat": "🎩",
    "billed_cap": "🧢",
    "womans_hat": "👒",
    "mortar_board": "🎓",
    "helmet_with_cross": "⛑",
    "helmet_with_white_cross": "⛑",
    "crown": "👑",
    "ring": "💍",
    "pouch": "👝",
    "purse": "👛",
    "handbag": "👜",
    "briefcase": "💼",
    "school_satchel": "🎒",
    "luggage": "🧳",
    "eyeglasses": "👓",
    "dark_sunglasses": "🕶",
    "goggles": "🥽",
    "diving_mask": "🤿",
    "closed_umbrella": "🌂",
    "dog": "🐶",
    "cat": "🐱",
    "mouse": "🐭",
    "hamster": "🐹",
    "rabbit": "🐰",
    "fox": "🦊",
    "fox_face": "🦊",
    "bear": "🐻",
    "panda_face": "🐼",
    "koala": "🐨",
    "tiger": "🐯",
    "lion_face": "🦁",
    "lion": "🦁",
    "cow": "🐮",
    "pig": "🐷",
    "pig_nose": "🐽",
    "frog": "🐸",
    "monkey_face": "🐵",
    "see_no_evil": "🙈",
    "hear_no_evil": "🙉",
    "speak_no_evil": "🙊",
    "monkey": "🐒",
    "chicken": "🐔",
    "penguin": "🐧",
    "bird": "🐦",
    "baby_chick": "🐤",
    "hatching_chick": "🐣",
    "hatched_chick": "🐥",
    "duck": "🦆",
    "eagle": "🦅",
    "owl": "🦉",
    "bat": "🦇",
    "wolf": "🐺",
    "boar": "🐗",
    "horse": "🐴",
    "unicorn": "🦄",
    "unicorn_face": "🦄",
    "bee": "🐝",
    "bug": "🐛",
    "butterfly": "🦋",
    "snail": "🐌",
    "shell": "🐚",
    "beetle": "🐞",
    "ant": "🐜",
    "mosquito": "🦟",
    "cricket": "🦗",
    "spider": "🕷",
    "spider_web": "🕸",
    "scorpion": "🦂",
    "turtle": "🐢",
    "snake": "🐍",
    "lizard": "🦎",
    "t_rex": "🦖",
    "sauropod": "🦕",
    "octopus": "🐙",
    "squid": "🦑",
    "shrimp": "🦐",
    "lobster": "🦞",
    "oyster": "🦪",
    "crab": "🦀",
    "blowfish": "🐡",
    "tropical_fish": "🐠",
    "fish": "🐟",
    "dolphin": "🐬",
    "whale": "🐳",
    "whale2": "🐋",
    "shark": "🦈",
    "crocodile": "🐊",
    "tiger2": "🐅",
    "leopard": "🐆",
    "zebra": "🦓",
    "gorilla": "🦍",
    "orangutan": "🦧",
    "elephant": "🐘",
    "hippopotamus": "🦛",
    "rhino": "🦏",
    "rhinoceros": "🦏",
    "dromedary_camel": "🐪",
    "camel": "🐫",
    "giraffe": "🦒",
    "kangaroo": "🦘",
    "water_buffalo": "🐃",
    "ox": "🐂",
    "cow2": "🐄",
    "racehorse": "🐎",
    "pig2": "🐖",
    "ram": "🐏",
    "llama": "🦙",
    "sheep": "🐑",
    "goat": "🐐",
    "deer": "🦌",
    "dog2": "🐕",
    "guide_dog": "🦮",
    "service_dog": "🐕🦺",
    "poodle": "🐩",
    "cat2": "🐈",
    "rooster": "🐓",
    "turkey": "🦃",
    "peacock": "🦚",
    "parrot": "🦜",
    "swan": "🦢",
    "flamingo": "🦩",
    "dove": "🕊",
    "dove_of_peace": "🕊",
    "rabbit2": "🐇",
    "sloth": "🦥",
    "otter": "🦦",
    "skunk": "🦨",
    "raccoon": "🦝",
    "badger": "🦡",
    "mouse2": "🐁",
    "rat": "🐀",
    "chipmunk": "🐿",
    "hedgehog": "🦔",
    "feet": "🐾",
    "paw_prints": "🐾",
    "dragon": "🐉",
    "dragon_face": "🐲",
    "cactus": "🌵",
    "christmas_tree": "🎄",
    "evergreen_tree": "🌲",
    "deciduous_tree": "🌳",
    "palm_tree": "🌴",
    "seedling": "🌱",
    "herb": "🌿",
    "shamrock": "☘",
    "four_leaf_clover": "🍀",
    "bamboo": "🎍",
    "tanabata_tree": "🎋",
    "leaves": "🍃",
    "fallen_leaf": "🍂",
    "maple_leaf": "🍁",
    "mushroom": "🍄",
    "ear_of_rice": "🌾",
    "bouquet": "💐",
    "tulip": "🌷",
    "rose": "🌹",
    "wilted_rose": "🥀",
    "wilted_flower": "🥀",
    "hibiscus": "🌺",
    "cherry_blossom": "🌸",
    "blossom": "🌼",
    "sunflower": "🌻",
    "sun_with_face": "🌞",
    "full_moon_with_face": "🌝",
    "first_quarter_moon_with_face": "🌛",
    "last_quarter_moon_with_face": "🌜",
    "new_moon_with_face": "🌚",
    "full_moon": "🌕",
    "waning_gibbous_moon": "🌖",
    "last_quarter_moon": "🌗",
    "waning_crescent_moon": "🌘",
    "new_moon": "🌑",
    "waxing_crescent_moon": "🌒",
    "first_quarter_moon": "🌓",
    "waxing_gibbous_moon": "🌔",
    "crescent_moon": "🌙",
    "earth_americas": "🌎",
    "earth_africa": "🌍",
    "earth_asia": "🌏",
    "ringed_planet": "🪐",
    "dizzy": "💫",
    "star": "⭐",
    "star2": "🌟",
    "sparkles": "✨",
    "zap": "⚡",
    "comet": "☄",
    "boom": "💥",
    "fire": "🔥",
    "flame": "🔥",
    "cloud_tornado": "🌪",
    "cloud_with_tornado": "🌪",
    "rainbow": "🌈",
    "sunny": "☀",
    "white_sun_small_cloud": "🌤",
    "white_sun_with_small_cloud": "🌤",
    "partly_sunny": "⛅",
    "white_sun_cloud": "🌥",
    "white_sun_behind_cloud": "🌥",
    "cloud": "☁",
    "white_sun_rain_cloud": "🌦",
    "white_sun_behind_cloud_with_rain": "🌦",
    "cloud_rain": "🌧",
    "cloud_with_rain": "🌧",
    "thunder_cloud_rain": "⛈",
    "thunder_cloud_and_rain": "⛈",
    "cloud_lightning": "🌩",
    "cloud_with_lightning": "🌩",
    "cloud_snow": "🌨",
    "cloud_with_snow": "🌨",
    "snowflake": "❄",
    "snowman2": "☃",
    "snowman": "⛄",
    "wind_blowing_face": "🌬",
    "dash": "💨",
    "droplet": "💧",
    "sweat_drops": "💦",
    "umbrella": "☔",
    "umbrella2": "☂",
    "ocean": "🌊",
    "fog": "🌫",
    "green_apple": "🍏",
    "apple": "🍎",
    "pear": "🍐",
    "tangerine": "🍊",
    "lemon": "🍋",
    "banana": "🍌",
    "watermelon": "🍉",
    "grapes": "🍇",
    "strawberry": "🍓",
    "melon": "🍈",
    "cherries": "🍒",
    "peach": "🍑",
    "mango": "🥭",
    "pineapple": "🍍",
    "coconut": "🥥",
    "kiwi": "🥝",
    "kiwifruit": "🥝",
    "tomato": "🍅",
    "eggplant": "🍆",
    "avocado": "🥑",
    "broccoli": "🥦",
    "leafy_green": "🥬",
    "cucumber": "🥒",
    "hot_pepper": "🌶",
    "corn": "🌽",
    "carrot": "🥕",
    "onion": "🧅",
    "garlic": "🧄",
    "potato": "🥔",
    "sweet_potato": "🍠",
    "croissant": "🥐",
    "bagel": "🥯",
    "bread": "🍞",
    "french_bread": "🥖",
    "baguette_bread": "🥖",
    "pretzel": "🥨",
    "cheese": "🧀",
    "cheese_wedge": "🧀",
    "egg": "🥚",
    "cooking": "🍳",
    "pancakes": "🥞",
    "waffle": "🧇",
    "bacon": "🥓",
    "cut_of_meat": "🥩",
    "poultry_leg": "🍗",
    "meat_on_bone": "🍖",
    "hotdog": "🌭",
    "hot_dog": "🌭",
    "hamburger": "🍔",
    "fries": "🍟",
    "pizza": "🍕",
    "sandwich": "🥪",
    "falafel": "🧆",
    "stuffed_flatbread": "🥙",
    "stuffed_pita": "🥙",
    "taco": "🌮",
    "burrito": "🌯",
    "salad": "🥗",
    "green_salad": "🥗",
    "shallow_pan_of_food": "🥘",
    "paella": "🥘",
    "canned_food": "🥫",
    "spaghetti": "🍝",
    "ramen": "🍜",
    "stew": "🍲",
    "curry": "🍛",
    "sushi": "🍣",
    "bento": "🍱",
    "dumpling": "🥟",
    "fried_shrimp": "🍤",
    "rice_ball": "🍙",
    "rice": "🍚",
    "rice_cracker": "🍘",
    "fish_cake": "🍥",
    "fortune_cookie": "🥠",
    "moon_cake": "🥮",
    "oden": "🍢",
    "dango": "🍡",
    "shaved_ice": "🍧",
    "ice_cream": "🍨",
    "icecream": "🍦",
    "pie": "🥧",
    "cupcake": "🧁",
    "cake": "🍰",
    "birthday": "🎂",
    "custard": "🍮",
    "pudding": "🍮",
    "flan": "🍮",
    "lollipop": "🍭",
    "candy": "🍬",
    "chocolate_bar": "🍫",
    "popcorn": "🍿",
    "doughnut": "🍩",
    "cookie": "🍪",
    "chestnut": "🌰",
    "peanuts": "🥜",
    "shelled_peanut": "🥜",
    "honey_pot": "🍯",
    "butter": "🧈",
    "milk": "🥛",
    "glass_of_milk": "🥛",
    "baby_bottle": "🍼",
    "coffee": "☕",
    "tea": "🍵",
    "mate": "🧉",
    "cup_with_straw": "🥤",
    "beverage_box": "🧃",
    "ice_cube": "🧊",
    "sake": "🍶",
    "beer": "🍺",
    "beers": "🍻",
    "champagne_glass": "🥂",
    "clinking_glass": "🥂",
    "wine_glass": "🍷",
    "tumbler_glass": "🥃",
    "whisky": "🥃",
    "cocktail": "🍸",
    "tropical_drink": "🍹",
    "champagne": "🍾",
    "bottle_with_popping_cork": "🍾",
    "spoon": "🥄",
    "fork_and_knife": "🍴",
    "fork_knife_plate": "🍽",
    "fork_and_knife_with_plate": "🍽",
    "bowl_with_spoon": "🥣",
    "takeout_box": "🥡",
    "chopsticks": "🥢",
    "salt": "🧂",
    "soccer": "⚽",
    "basketball": "🏀",
    "football": "🏈",
    "baseball": "⚾",
    "softball": "🥎",
    "tennis": "🎾",
    "volleyball": "🏐",
    "rugby_football": "🏉",
    "flying_disc": "🥏",
    "8ball": "🎱",
    "ping_pong": "🏓",
    "table_tennis": "🏓",
    "badminton": "🏸",
    "hockey": "🏒",
    "field_hockey": "🏑",
    "lacrosse": "🥍",
    "cricket_game": "🏏",
    "cricket_bat_ball": "🏏",
    "goal": "🥅",
    "goal_net": "🥅",
    "golf": "⛳",
    "bow_and_arrow": "🏹",
    "archery": "🏹",
    "fishing_pole_and_fish": "🎣",
    "boxing_glove": "🥊",
    "boxing_gloves": "🥊",
    "martial_arts_uniform": "🥋",
    "karate_uniform": "🥋",
    "running_shirt_with_sash": "🎽",
    "skateboard": "🛹",
    "sled": "🛷",
    "parachute": "🪂",
    "ice_skate": "⛸",
    "curling_stone": "🥌",
    "ski": "🎿",
    "skier": "⛷",
    "snowboarder": "🏂",
    "snowboarder_tone1": "🏂🏻",
    "snowboarder_light_skin_tone": "🏂🏻",
    "snowboarder_tone2": "🏂🏼",
    "snowboarder_medium_light_skin_tone": "🏂🏼",
    "snowboarder_tone3": "🏂🏽",
    "snowboarder_medium_skin_tone": "🏂🏽",
    "snowboarder_tone4": "🏂🏾",
    "snowboarder_medium_dark_skin_tone": "🏂🏾",
    "snowboarder_tone5": "🏂🏿",
    "snowboarder_dark_skin_tone": "🏂🏿",
    "person_lifting_weights": "🏋",
    "lifter": "🏋",
    "weight_lifter": "🏋",
    "person_lifting_weights_tone1": "🏋🏻",
    "lifter_tone1": "🏋🏻",
    "weight_lifter_tone1": "🏋🏻",
    "person_lifting_weights_tone2": "🏋🏼",
    "lifter_tone2": "🏋🏼",
    "weight_lifter_tone2": "🏋🏼",
    "person_lifting_weights_tone3": "🏋🏽",
    "lifter_tone3": "🏋🏽",
    "weight_lifter_tone3": "🏋🏽",
    "person_lifting_weights_tone4": "🏋🏾",
    "lifter_tone4": "🏋🏾",
    "weight_lifter_tone4": "🏋🏾",
    "person_lifting_weights_tone5": "🏋🏿",
    "lifter_tone5": "🏋🏿",
    "weight_lifter_tone5": "🏋🏿",
    "woman_lifting_weights": "🏋♀",
    "woman_lifting_weights_tone1": "🏋🏻♀",
    "woman_lifting_weights_light_skin_tone": "🏋🏻♀",
    "woman_lifting_weights_tone2": "🏋🏼♀",
    "woman_lifting_weights_medium_light_skin_tone": "🏋🏼♀",
    "woman_lifting_weights_tone3": "🏋🏽♀",
    "woman_lifting_weights_medium_skin_tone": "🏋🏽♀",
    "woman_lifting_weights_tone4": "🏋🏾♀",
    "woman_lifting_weights_medium_dark_skin_tone": "🏋🏾♀",
    "woman_lifting_weights_tone5": "🏋🏿♀",
    "woman_lifting_weights_dark_skin_tone": "🏋🏿♀",
    "man_lifting_weights": "🏋♂",
    "man_lifting_weights_tone1": "🏋🏻♂",
    "man_lifting_weights_light_skin_tone": "🏋🏻♂",
    "man_lifting_weights_tone2": "🏋🏼♂",
    "man_lifting_weights_medium_light_skin_tone": "🏋🏼♂",
    "man_lifting_weights_tone3": "🏋🏽♂",
    "man_lifting_weights_medium_skin_tone": "🏋🏽♂",
    "man_lifting_weights_tone4": "🏋🏾♂",
    "man_lifting_weights_medium_dark_skin_tone": "🏋🏾♂",
    "man_lifting_weights_tone5": "🏋🏿♂",
    "man_lifting_weights_dark_skin_tone": "🏋🏿♂",
    "people_wrestling": "🤼",
    "wrestlers": "🤼",
    "wrestling": "🤼",
    "women_wrestling": "🤼♀",
    "men_wrestling": "🤼♂",
    "person_doing_cartwheel": "🤸",
    "cartwheel": "🤸",
    "person_doing_cartwheel_tone1": "🤸🏻",
    "cartwheel_tone1": "🤸🏻",
    "person_doing_cartwheel_tone2": "🤸🏼",
    "cartwheel_tone2": "🤸🏼",
    "person_doing_cartwheel_tone3": "🤸🏽",
    "cartwheel_tone3": "🤸🏽",
    "person_doing_cartwheel_tone4": "🤸🏾",
    "cartwheel_tone4": "🤸🏾",
    "person_doing_cartwheel_tone5": "🤸🏿",
    "cartwheel_tone5": "🤸🏿",
    "woman_cartwheeling": "🤸♀",
    "woman_cartwheeling_tone1": "🤸🏻♀",
    "woman_cartwheeling_light_skin_tone": "🤸🏻♀",
    "woman_cartwheeling_tone2": "🤸🏼♀",
    "woman_cartwheeling_medium_light_skin_tone": "🤸🏼♀",
    "woman_cartwheeling_tone3": "🤸🏽♀",
    "woman_cartwheeling_medium_skin_tone": "🤸🏽♀",
    "woman_cartwheeling_tone4": "🤸🏾♀",
    "woman_cartwheeling_medium_dark_skin_tone": "🤸🏾♀",
    "woman_cartwheeling_tone5": "🤸🏿♀",
    "woman_cartwheeling_dark_skin_tone": "🤸🏿♀",
    "man_cartwheeling": "🤸♂",
    "man_cartwheeling_tone1": "🤸🏻♂",
    "man_cartwheeling_light_skin_tone": "🤸🏻♂",
    "man_cartwheeling_tone2": "🤸🏼♂",
    "man_cartwheeling_medium_light_skin_tone": "🤸🏼♂",
    "man_cartwheeling_tone3": "🤸🏽♂",
    "man_cartwheeling_medium_skin_tone": "🤸🏽♂",
    "man_cartwheeling_tone4": "🤸🏾♂",
    "man_cartwheeling_medium_dark_skin_tone": "🤸🏾♂",
    "man_cartwheeling_tone5": "🤸🏿♂",
    "man_cartwheeling_dark_skin_tone": "🤸🏿♂",
    "person_bouncing_ball": "⛹",
    "basketball_player": "⛹",
    "person_with_ball": "⛹",
    "person_bouncing_ball_tone1": "⛹🏻",
    "basketball_player_tone1": "⛹🏻",
    "person_with_ball_tone1": "⛹🏻",
    "person_bouncing_ball_tone2": "⛹🏼",
    "basketball_player_tone2": "⛹🏼",
    "person_with_ball_tone2": "⛹🏼",
    "person_bouncing_ball_tone3": "⛹🏽",
    "basketball_player_tone3": "⛹🏽",
    "person_with_ball_tone3": "⛹🏽",
    "person_bouncing_ball_tone4": "⛹🏾",
    "basketball_player_tone4": "⛹🏾",
    "person_with_ball_tone4": "⛹🏾",
    "person_bouncing_ball_tone5": "⛹🏿",
    "basketball_player_tone5": "⛹🏿",
    "person_with_ball_tone5": "⛹🏿",
    "woman_bouncing_ball": "⛹♀",
    "woman_bouncing_ball_tone1": "⛹🏻♀",
    "woman_bouncing_ball_light_skin_tone": "⛹🏻♀",
    "woman_bouncing_ball_tone2": "⛹🏼♀",
    "woman_bouncing_ball_medium_light_skin_tone": "⛹🏼♀",
    "woman_bouncing_ball_tone3": "⛹🏽♀",
    "woman_bouncing_ball_medium_skin_tone": "⛹🏽♀",
    "woman_bouncing_ball_tone4": "⛹🏾♀",
    "woman_bouncing_ball_medium_dark_skin_tone": "⛹🏾♀",
    "woman_bouncing_ball_tone5": "⛹🏿♀",
    "woman_bouncing_ball_dark_skin_tone": "⛹🏿♀",
    "man_bouncing_ball": "⛹♂",
    "man_bouncing_ball_tone1": "⛹🏻♂",
    "man_bouncing_ball_light_skin_tone": "⛹🏻♂",
    "man_bouncing_ball_tone2": "⛹🏼♂",
    "man_bouncing_ball_medium_light_skin_tone": "⛹🏼♂",
    "man_bouncing_ball_tone3": "⛹🏽♂",
    "man_bouncing_ball_medium_skin_tone": "⛹🏽♂",
    "man_bouncing_ball_tone4": "⛹🏾♂",
    "man_bouncing_ball_medium_dark_skin_tone": "⛹🏾♂",
    "man_bouncing_ball_tone5": "⛹🏿♂",
    "man_bouncing_ball_dark_skin_tone": "⛹🏿♂",
    "person_fencing": "🤺",
    "fencer": "🤺",
    "fencing": "🤺",
    "person_playing_handball": "🤾",
    "handball": "🤾",
    "person_playing_handball_tone1": "🤾🏻",
    "handball_tone1": "🤾🏻",
    "person_playing_handball_tone2": "🤾🏼",
    "handball_tone2": "🤾🏼",
    "person_playing_handball_tone3": "🤾🏽",
    "handball_tone3": "🤾🏽",
    "person_playing_handball_tone4": "🤾🏾",
    "handball_tone4": "🤾🏾",
    "person_playing_handball_tone5": "🤾🏿",
    "handball_tone5": "🤾🏿",
    "woman_playing_handball": "🤾♀",
    "woman_playing_handball_tone1": "🤾🏻♀",
    "woman_playing_handball_light_skin_tone": "🤾🏻♀",
    "woman_playing_handball_tone2": "🤾🏼♀",
    "woman_playing_handball_medium_light_skin_tone": "🤾🏼♀",
    "woman_playing_handball_tone3": "🤾🏽♀",
    "woman_playing_handball_medium_skin_tone": "🤾🏽♀",
    "woman_playing_handball_tone4": "🤾🏾♀",
    "woman_playing_handball_medium_dark_skin_tone": "🤾🏾♀",
    "woman_playing_handball_tone5": "🤾🏿♀",
    "woman_playing_handball_dark_skin_tone": "🤾🏿♀",
    "man_playing_handball": "🤾♂",
    "man_playing_handball_tone1": "🤾🏻♂",
    "man_playing_handball_light_skin_tone": "🤾🏻♂",
    "man_playing_handball_tone2": "🤾🏼♂",
    "man_playing_handball_medium_light_skin_tone": "🤾🏼♂",
    "man_playing_handball_tone3": "🤾🏽♂",
    "man_playing_handball_medium_skin_tone": "🤾🏽♂",
    "man_playing_handball_tone4": "🤾🏾♂",
    "man_playing_handball_medium_dark_skin_tone": "🤾🏾♂",
    "man_playing_handball_tone5": "🤾🏿♂",
    "man_playing_handball_dark_skin_tone": "🤾🏿♂",
    "person_golfing": "🏌",
    "golfer": "🏌",
    "person_golfing_tone1": "🏌🏻",
    "person_golfing_light_skin_tone": "🏌🏻",
    "person_golfing_tone2": "🏌🏼",
    "person_golfing_medium_light_skin_tone": "🏌🏼",
    "person_golfing_tone3": "🏌🏽",
    "person_golfing_medium_skin_tone": "🏌🏽",
    "person_golfing_tone4": "🏌🏾",
    "person_golfing_medium_dark_skin_tone": "🏌🏾",
    "person_golfing_tone5": "🏌🏿",
    "person_golfing_dark_skin_tone": "🏌🏿",
    "woman_golfing": "🏌♀",
    "woman_golfing_tone1": "🏌🏻♀",
    "woman_golfing_light_skin_tone": "🏌🏻♀",
    "woman_golfing_tone2": "🏌🏼♀",
    "woman_golfing_medium_light_skin_tone": "🏌🏼♀",
    "woman_golfing_tone3": "🏌🏽♀",
    "woman_golfing_medium_skin_tone": "🏌🏽♀",
    "woman_golfing_tone4": "🏌🏾♀",
    "woman_golfing_medium_dark_skin_tone": "🏌🏾♀",
    "woman_golfing_tone5": "🏌🏿♀",
    "woman_golfing_dark_skin_tone": "🏌🏿♀",
    "man_golfing": "🏌♂",
    "man_golfing_tone1": "🏌🏻♂",
    "man_golfing_light_skin_tone": "🏌🏻♂",
    "man_golfing_tone2": "🏌🏼♂",
    "man_golfing_medium_light_skin_tone": "🏌🏼♂",
    "man_golfing_tone3": "🏌🏽♂",
    "man_golfing_medium_skin_tone": "🏌🏽♂",
    "man_golfing_tone4": "🏌🏾♂",
    "man_golfing_medium_dark_skin_tone": "🏌🏾♂",
    "man_golfing_tone5": "🏌🏿♂",
    "man_golfing_dark_skin_tone": "🏌🏿♂",
    "horse_racing": "🏇",
    "horse_racing_tone1": "🏇🏻",
    "horse_racing_tone2": "🏇🏼",
    "horse_racing_tone3": "🏇🏽",
    "horse_racing_tone4": "🏇🏾",
    "horse_racing_tone5": "🏇🏿",
    "person_in_lotus_position": "🧘",
    "person_in_lotus_position_tone1": "🧘🏻",
    "person_in_lotus_position_light_skin_tone": "🧘🏻",
    "person_in_lotus_position_tone2": "🧘🏼",
    "person_in_lotus_position_medium_light_skin_tone": "🧘🏼",
    "person_in_lotus_position_tone3": "🧘🏽",
    "person_in_lotus_position_medium_skin_tone": "🧘🏽",
    "person_in_lotus_position_tone4": "🧘🏾",
    "person_in_lotus_position_medium_dark_skin_tone": "🧘🏾",
    "person_in_lotus_position_tone5": "🧘🏿",
    "person_in_lotus_position_dark_skin_tone": "🧘🏿",
    "woman_in_lotus_position": "🧘♀",
    "woman_in_lotus_position_tone1": "🧘🏻♀",
    "woman_in_lotus_position_light_skin_tone": "🧘🏻♀",
    "woman_in_lotus_position_tone2": "🧘🏼♀",
    "woman_in_lotus_position_medium_light_skin_tone": "🧘🏼♀",
    "woman_in_lotus_position_tone3": "🧘🏽♀",
    "woman_in_lotus_position_medium_skin_tone": "🧘🏽♀",
    "woman_in_lotus_position_tone4": "🧘🏾♀",
    "woman_in_lotus_position_medium_dark_skin_tone": "🧘🏾♀",
    "woman_in_lotus_position_tone5": "🧘🏿♀",
    "woman_in_lotus_position_dark_skin_tone": "🧘🏿♀",
    "man_in_lotus_position": "🧘♂",
    "man_in_lotus_position_tone1": "🧘🏻♂",
    "man_in_lotus_position_light_skin_tone": "🧘🏻♂",
    "man_in_lotus_position_tone2": "🧘🏼♂",
    "man_in_lotus_position_medium_light_skin_tone": "🧘🏼♂",
    "man_in_lotus_position_tone3": "🧘🏽♂",
    "man_in_lotus_position_medium_skin_tone": "🧘🏽♂",
    "man_in_lotus_position_tone4": "🧘🏾♂",
    "man_in_lotus_position_medium_dark_skin_tone": "🧘🏾♂",
    "man_in_lotus_position_tone5": "🧘🏿♂",
    "man_in_lotus_position_dark_skin_tone": "🧘🏿♂",
    "person_surfing": "🏄",
    "surfer": "🏄",
    "person_surfing_tone1": "🏄🏻",
    "surfer_tone1": "🏄🏻",
    "person_surfing_tone2": "🏄🏼",
    "surfer_tone2": "🏄🏼",
    "person_surfing_tone3": "🏄🏽",
    "surfer_tone3": "🏄🏽",
    "person_surfing_tone4": "🏄🏾",
    "surfer_tone4": "🏄🏾",
    "person_surfing_tone5": "🏄🏿",
    "surfer_tone5": "🏄🏿",
    "woman_surfing": "🏄♀",
    "woman_surfing_tone1": "🏄🏻♀",
    "woman_surfing_light_skin_tone": "🏄🏻♀",
    "woman_surfing_tone2": "🏄🏼♀",
    "woman_surfing_medium_light_skin_tone": "🏄🏼♀",
    "woman_surfing_tone3": "🏄🏽♀",
    "woman_surfing_medium_skin_tone": "🏄🏽♀",
    "woman_surfing_tone4": "🏄🏾♀",
    "woman_surfing_medium_dark_skin_tone": "🏄🏾♀",
    "woman_surfing_tone5": "🏄🏿♀",
    "woman_surfing_dark_skin_tone": "🏄🏿♀",
    "man_surfing": "🏄♂",
    "man_surfing_tone1": "🏄🏻♂",
    "man_surfing_light_skin_tone": "🏄🏻♂",
    "man_surfing_tone2": "🏄🏼♂",
    "man_surfing_medium_light_skin_tone": "🏄🏼♂",
    "man_surfing_tone3": "🏄🏽♂",
    "man_surfing_medium_skin_tone": "🏄🏽♂",
    "man_surfing_tone4": "🏄🏾♂",
    "man_surfing_medium_dark_skin_tone": "🏄🏾♂",
    "man_surfing_tone5": "🏄🏿♂",
    "man_surfing_dark_skin_tone": "🏄🏿♂",
    "person_swimming": "🏊",
    "swimmer": "🏊",
    "person_swimming_tone1": "🏊🏻",
    "swimmer_tone1": "🏊🏻",
    "person_swimming_tone2": "🏊🏼",
    "swimmer_tone2": "🏊🏼",
    "person_swimming_tone3": "🏊🏽",
    "swimmer_tone3": "🏊🏽",
    "person_swimming_tone4": "🏊🏾",
    "swimmer_tone4": "🏊🏾",
    "person_swimming_tone5": "🏊🏿",
    "swimmer_tone5": "🏊🏿",
    "woman_swimming": "🏊♀",
    "woman_swimming_tone1": "🏊🏻♀",
    "woman_swimming_light_skin_tone": "🏊🏻♀",
    "woman_swimming_tone2": "🏊🏼♀",
    "woman_swimming_medium_light_skin_tone": "🏊🏼♀",
    "woman_swimming_tone3": "🏊🏽♀",
    "woman_swimming_medium_skin_tone": "🏊🏽♀",
    "woman_swimming_tone4": "🏊🏾♀",
    "woman_swimming_medium_dark_skin_tone": "🏊🏾♀",
    "woman_swimming_tone5": "🏊🏿♀",
    "woman_swimming_dark_skin_tone": "🏊🏿♀",
    "man_swimming": "🏊♂",
    "man_swimming_tone1": "🏊🏻♂",
    "man_swimming_light_skin_tone": "🏊🏻♂",
    "man_swimming_tone2": "🏊🏼♂",
    "man_swimming_medium_light_skin_tone": "🏊🏼♂",
    "man_swimming_tone3": "🏊🏽♂",
    "man_swimming_medium_skin_tone": "🏊🏽♂",
    "man_swimming_tone4": "🏊🏾♂",
    "man_swimming_medium_dark_skin_tone": "🏊🏾♂",
    "man_swimming_tone5": "🏊🏿♂",
    "man_swimming_dark_skin_tone": "🏊🏿♂",
    "person_playing_water_polo": "🤽",
    "water_polo": "🤽",
    "person_playing_water_polo_tone1": "🤽🏻",
    "water_polo_tone1": "🤽🏻",
    "person_playing_water_polo_tone2": "🤽🏼",
    "water_polo_tone2": "🤽🏼",
    "person_playing_water_polo_tone3": "🤽🏽",
    "water_polo_tone3": "🤽🏽",
    "person_playing_water_polo_tone4": "🤽🏾",
    "water_polo_tone4": "🤽🏾",
    "person_playing_water_polo_tone5": "🤽🏿",
    "water_polo_tone5": "🤽🏿",
    "woman_playing_water_polo": "🤽♀",
    "woman_playing_water_polo_tone1": "🤽🏻♀",
    "woman_playing_water_polo_light_skin_tone": "🤽🏻♀",
    "woman_playing_water_polo_tone2": "🤽🏼♀",
    "woman_playing_water_polo_medium_light_skin_tone": "🤽🏼♀",
    "woman_playing_water_polo_tone3": "🤽🏽♀",
    "woman_playing_water_polo_medium_skin_tone": "🤽🏽♀",
    "woman_playing_water_polo_tone4": "🤽🏾♀",
    "woman_playing_water_polo_medium_dark_skin_tone": "🤽🏾♀",
    "woman_playing_water_polo_tone5": "🤽🏿♀",
    "woman_playing_water_polo_dark_skin_tone": "🤽🏿♀",
    "man_playing_water_polo": "🤽♂",
    "man_playing_water_polo_tone1": "🤽🏻♂",
    "man_playing_water_polo_light_skin_tone": "🤽🏻♂",
    "man_playing_water_polo_tone2": "🤽🏼♂",
    "man_playing_water_polo_medium_light_skin_tone": "🤽🏼♂",
    "man_playing_water_polo_tone3": "🤽🏽♂",
    "man_playing_water_polo_medium_skin_tone": "🤽🏽♂",
    "man_playing_water_polo_tone4": "🤽🏾♂",
    "man_playing_water_polo_medium_dark_skin_tone": "🤽🏾♂",
    "man_playing_water_polo_tone5": "🤽🏿♂",
    "man_playing_water_polo_dark_skin_tone": "🤽🏿♂",
    "person_rowing_boat": "🚣",
    "rowboat": "🚣",
    "person_rowing_boat_tone1": "🚣🏻",
    "rowboat_tone1": "🚣🏻",
    "person_rowing_boat_tone2": "🚣🏼",
    "rowboat_tone2": "🚣🏼",
    "person_rowing_boat_tone3": "🚣🏽",
    "rowboat_tone3": "🚣🏽",
    "person_rowing_boat_tone4": "🚣🏾",
    "rowboat_tone4": "🚣🏾",
    "person_rowing_boat_tone5": "🚣🏿",
    "rowboat_tone5": "🚣🏿",
    "woman_rowing_boat": "🚣♀",
    "woman_rowing_boat_tone1": "🚣🏻♀",
    "woman_rowing_boat_light_skin_tone": "🚣🏻♀",
    "woman_rowing_boat_tone2": "🚣🏼♀",
    "woman_rowing_boat_medium_light_skin_tone": "🚣🏼♀",
    "woman_rowing_boat_tone3": "🚣🏽♀",
    "woman_rowing_boat_medium_skin_tone": "🚣🏽♀",
    "woman_rowing_boat_tone4": "🚣🏾♀",
    "woman_rowing_boat_medium_dark_skin_tone": "🚣🏾♀",
    "woman_rowing_boat_tone5": "🚣🏿♀",
    "woman_rowing_boat_dark_skin_tone": "🚣🏿♀",
    "man_rowing_boat": "🚣♂",
    "man_rowing_boat_tone1": "🚣🏻♂",
    "man_rowing_boat_light_skin_tone": "🚣🏻♂",
    "man_rowing_boat_tone2": "🚣🏼♂",
    "man_rowing_boat_medium_light_skin_tone": "🚣🏼♂",
    "man_rowing_boat_tone3": "🚣🏽♂",
    "man_rowing_boat_medium_skin_tone": "🚣🏽♂",
    "man_rowing_boat_tone4": "🚣🏾♂",
    "man_rowing_boat_medium_dark_skin_tone": "🚣🏾♂",
    "man_rowing_boat_tone5": "🚣🏿♂",
    "man_rowing_boat_dark_skin_tone": "🚣🏿♂",
    "person_climbing": "🧗",
    "person_climbing_tone1": "🧗🏻",
    "person_climbing_light_skin_tone": "🧗🏻",
    "person_climbing_tone2": "🧗🏼",
    "person_climbing_medium_light_skin_tone": "🧗🏼",
    "person_climbing_tone3": "🧗🏽",
    "person_climbing_medium_skin_tone": "🧗🏽",
    "person_climbing_tone4": "🧗🏾",
    "person_climbing_medium_dark_skin_tone": "🧗🏾",
    "person_climbing_tone5": "🧗🏿",
    "person_climbing_dark_skin_tone": "🧗🏿",
    "woman_climbing": "🧗♀",
    "woman_climbing_tone1": "🧗🏻♀",
    "woman_climbing_light_skin_tone": "🧗🏻♀",
    "woman_climbing_tone2": "🧗🏼♀",
    "woman_climbing_medium_light_skin_tone": "🧗🏼♀",
    "woman_climbing_tone3": "🧗🏽♀",
    "woman_climbing_medium_skin_tone": "🧗🏽♀",
    "woman_climbing_tone4": "🧗🏾♀",
    "woman_climbing_medium_dark_skin_tone": "🧗🏾♀",
    "woman_climbing_tone5": "🧗🏿♀",
    "woman_climbing_dark_skin_tone": "🧗🏿♀",
    "man_climbing": "🧗♂",
    "man_climbing_tone1": "🧗🏻♂",
    "man_climbing_light_skin_tone": "🧗🏻♂",
    "man_climbing_tone2": "🧗🏼♂",
    "man_climbing_medium_light_skin_tone": "🧗🏼♂",
    "man_climbing_tone3": "🧗🏽♂",
    "man_climbing_medium_skin_tone": "🧗🏽♂",
    "man_climbing_tone4": "🧗🏾♂",
    "man_climbing_medium_dark_skin_tone": "🧗🏾♂",
    "man_climbing_tone5": "🧗🏿♂",
    "man_climbing_dark_skin_tone": "🧗🏿♂",
    "person_mountain_biking": "🚵",
    "mountain_bicyclist": "🚵",
    "person_mountain_biking_tone1": "🚵🏻",
    "mountain_bicyclist_tone1": "🚵🏻",
    "person_mountain_biking_tone2": "🚵🏼",
    "mountain_bicyclist_tone2": "🚵🏼",
    "person_mountain_biking_tone3": "🚵🏽",
    "mountain_bicyclist_tone3": "🚵🏽",
    "person_mountain_biking_tone4": "🚵🏾",
    "mountain_bicyclist_tone4": "🚵🏾",
    "person_mountain_biking_tone5": "🚵🏿",
    "mountain_bicyclist_tone5": "🚵🏿",
    "woman_mountain_biking": "🚵♀",
    "woman_mountain_biking_tone1": "🚵🏻♀",
    "woman_mountain_biking_light_skin_tone": "🚵🏻♀",
    "woman_mountain_biking_tone2": "🚵🏼♀",
    "woman_mountain_biking_medium_light_skin_tone": "🚵🏼♀",
    "woman_mountain_biking_tone3": "🚵🏽♀",
    "woman_mountain_biking_medium_skin_tone": "🚵🏽♀",
    "woman_mountain_biking_tone4": "🚵🏾♀",
    "woman_mountain_biking_medium_dark_skin_tone": "🚵🏾♀",
    "woman_mountain_biking_tone5": "🚵🏿♀",
    "woman_mountain_biking_dark_skin_tone": "🚵🏿♀",
    "man_mountain_biking": "🚵♂",
    "man_mountain_biking_tone1": "🚵🏻♂",
    "man_mountain_biking_light_skin_tone": "🚵🏻♂",
    "man_mountain_biking_tone2": "🚵🏼♂",
    "man_mountain_biking_medium_light_skin_tone": "🚵🏼♂",
    "man_mountain_biking_tone3": "🚵🏽♂",
    "man_mountain_biking_medium_skin_tone": "🚵🏽♂",
    "man_mountain_biking_tone4": "🚵🏾♂",
    "man_mountain_biking_medium_dark_skin_tone": "🚵🏾♂",
    "man_mountain_biking_tone5": "🚵🏿♂",
    "man_mountain_biking_dark_skin_tone": "🚵🏿♂",
    "person_biking": "🚴",
    "bicyclist": "🚴",
    "person_biking_tone1": "🚴🏻",
    "bicyclist_tone1": "🚴🏻",
    "person_biking_tone2": "🚴🏼",
    "bicyclist_tone2": "🚴🏼",
    "person_biking_tone3": "🚴🏽",
    "bicyclist_tone3": "🚴🏽",
    "person_biking_tone4": "🚴🏾",
    "bicyclist_tone4": "🚴🏾",
    "person_biking_tone5": "🚴🏿",
    "bicyclist_tone5": "🚴🏿",
    "woman_biking": "🚴♀",
    "woman_biking_tone1": "🚴🏻♀",
    "woman_biking_light_skin_tone": "🚴🏻♀",
    "woman_biking_tone2": "🚴🏼♀",
    "woman_biking_medium_light_skin_tone": "🚴🏼♀",
    "woman_biking_tone3": "🚴🏽♀",
    "woman_biking_medium_skin_tone": "🚴🏽♀",
    "woman_biking_tone4": "🚴🏾♀",
    "woman_biking_medium_dark_skin_tone": "🚴🏾♀",
    "woman_biking_tone5": "🚴🏿♀",
    "woman_biking_dark_skin_tone": "🚴🏿♀",
    "man_biking": "🚴♂",
    "man_biking_tone1": "🚴🏻♂",
    "man_biking_light_skin_tone": "🚴🏻♂",
    "man_biking_tone2": "🚴🏼♂",
    "man_biking_medium_light_skin_tone": "🚴🏼♂",
    "man_biking_tone3": "🚴🏽♂",
    "man_biking_medium_skin_tone": "🚴🏽♂",
    "man_biking_tone4": "🚴🏾♂",
    "man_biking_medium_dark_skin_tone": "🚴🏾♂",
    "man_biking_tone5": "🚴🏿♂",
    "man_biking_dark_skin_tone": "🚴🏿♂",
    "trophy": "🏆",
    "first_place": "🥇",
    "first_place_medal": "🥇",
    "second_place": "🥈",
    "second_place_medal": "🥈",
    "third_place": "🥉",
    "third_place_medal": "🥉",
    "medal": "🏅",
    "sports_medal": "🏅",
    "military_medal": "🎖",
    "rosette": "🏵",
    "reminder_ribbon": "🎗",
    "ticket": "🎫",
    "tickets": "🎟",
    "admission_tickets": "🎟",
    "circus_tent": "🎪",
    "person_juggling": "🤹",
    "juggling": "🤹",
    "juggler": "🤹",
    "person_juggling_tone1": "🤹🏻",
    "juggling_tone1": "🤹🏻",
    "juggler_tone1": "🤹🏻",
    "person_juggling_tone2": "🤹🏼",
    "juggling_tone2": "🤹🏼",
    "juggler_tone2": "🤹🏼",
    "person_juggling_tone3": "🤹🏽",
    "juggling_tone3": "🤹🏽",
    "juggler_tone3": "🤹🏽",
    "person_juggling_tone4": "🤹🏾",
    "juggling_tone4": "🤹🏾",
    "juggler_tone4": "🤹🏾",
    "person_juggling_tone5": "🤹🏿",
    "juggling_tone5": "🤹🏿",
    "juggler_tone5": "🤹🏿",
    "woman_juggling": "🤹♀",
    "woman_juggling_tone1": "🤹🏻♀",
    "woman_juggling_light_skin_tone": "🤹🏻♀",
    "woman_juggling_tone2": "🤹🏼♀",
    "woman_juggling_medium_light_skin_tone": "🤹🏼♀",
    "woman_juggling_tone3": "🤹🏽♀",
    "woman_juggling_medium_skin_tone": "🤹🏽♀",
    "woman_juggling_tone4": "🤹🏾♀",
    "woman_juggling_medium_dark_skin_tone": "🤹🏾♀",
    "woman_juggling_tone5": "🤹🏿♀",
    "woman_juggling_dark_skin_tone": "🤹🏿♀",
    "man_juggling": "🤹♂",
    "man_juggling_tone1": "🤹🏻♂",
    "man_juggling_light_skin_tone": "🤹🏻♂",
    "man_juggling_tone2": "🤹🏼♂",
    "man_juggling_medium_light_skin_tone": "🤹🏼♂",
    "man_juggling_tone3": "🤹🏽♂",
    "man_juggling_medium_skin_tone": "🤹🏽♂",
    "man_juggling_tone4": "🤹🏾♂",
    "man_juggling_medium_dark_skin_tone": "🤹🏾♂",
    "man_juggling_tone5": "🤹🏿♂",
    "man_juggling_dark_skin_tone": "🤹🏿♂",
    "performing_arts": "🎭",
    "art": "🎨",
    "clapper": "🎬",
    "microphone": "🎤",
    "headphones": "🎧",
    "musical_score": "🎼",
    "musical_keyboard": "🎹",
    "drum": "🥁",
    "drum_with_drumsticks": "🥁",
    "saxophone": "🎷",
    "trumpet": "🎺",
    "banjo": "🪕",
    "guitar": "🎸",
    "violin": "🎻",
    "game_die": "🎲",
    "chess_pawn": "♟",
    "dart": "🎯",
    "kite": "🪁",
    "yo_yo": "🪀",
    "bowling": "🎳",
    "video_game": "🎮",
    "slot_machine": "🎰",
    "jigsaw": "🧩",
    "red_car": "🚗",
    "taxi": "🚕",
    "blue_car": "🚙",
    "bus": "🚌",
    "trolleybus": "🚎",
    "race_car": "🏎",
    "racing_car": "🏎",
    "police_car": "🚓",
    "ambulance": "🚑",
    "fire_engine": "🚒",
    "minibus": "🚐",
    "truck": "🚚",
    "articulated_lorry": "🚛",
    "tractor": "🚜",
    "auto_rickshaw": "🛺",
    "motor_scooter": "🛵",
    "motorbike": "🛵",
    "motorcycle": "🏍",
    "racing_motorcycle": "🏍",
    "scooter": "🛴",
    "bike": "🚲",
    "motorized_wheelchair": "🦼",
    "manual_wheelchair": "🦽",
    "rotating_light": "🚨",
    "oncoming_police_car": "🚔",
    "oncoming_bus": "🚍",
    "oncoming_automobile": "🚘",
    "oncoming_taxi": "🚖",
    "aerial_tramway": "🚡",
    "mountain_cableway": "🚠",
    "suspension_railway": "🚟",
    "railway_car": "🚃",
    "train": "🚋",
    "mountain_railway": "🚞",
    "monorail": "🚝",
    "bullettrain_side": "🚄",
    "bullettrain_front": "🚅",
    "light_rail": "🚈",
    "steam_locomotive": "🚂",
    "train2": "🚆",
    "metro": "🚇",
    "tram": "🚊",
    "station": "🚉",
    "airplane": "✈",
    "airplane_departure": "🛫",
    "airplane_arriving": "🛬",
    "airplane_small": "🛩",
    "small_airplane": "🛩",
    "seat": "💺",
    "satellite_orbital": "🛰",
    "rocket": "🚀",
    "flying_saucer": "🛸",
    "helicopter": "🚁",
    "canoe": "🛶",
    "kayak": "🛶",
    "sailboat": "⛵",
    "speedboat": "🚤",
    "motorboat": "🛥",
    "cruise_ship": "🛳",
    "passenger_ship": "🛳",
    "ferry": "⛴",
    "ship": "🚢",
    "anchor": "⚓",
    "fuelpump": "⛽",
    "construction": "🚧",
    "vertical_traffic_light": "🚦",
    "traffic_light": "🚥",
    "busstop": "🚏",
    "map": "🗺",
    "world_map": "🗺",
    "moyai": "🗿",
    "statue_of_liberty": "🗽",
    "tokyo_tower": "🗼",
    "european_castle": "🏰",
    "japanese_castle": "🏯",
    "stadium": "🏟",
    "ferris_wheel": "🎡",
    "roller_coaster": "🎢",
    "carousel_horse": "🎠",
    "fountain": "⛲",
    "beach_umbrella": "⛱",
    "umbrella_on_ground": "⛱",
    "beach": "🏖",
    "beach_with_umbrella": "🏖",
    "island": "🏝",
    "desert_island": "🏝",
    "desert": "🏜",
    "volcano": "🌋",
    "mountain": "⛰",
    "mountain_snow": "🏔",
    "snow_capped_mountain": "🏔",
    "mount_fuji": "🗻",
    "camping": "🏕",
    "tent": "⛺",
    "house": "🏠",
    "house_with_garden": "🏡",
    "homes": "🏘",
    "house_buildings": "🏘",
    "house_abandoned": "🏚",
    "derelict_house_building": "🏚",
    "construction_site": "🏗",
    "building_construction": "🏗",
    "factory": "🏭",
    "office": "🏢",
    "department_store": "🏬",
    "post_office": "🏣",
    "european_post_office": "🏤",
    "hospital": "🏥",
    "bank": "🏦",
    "hotel": "🏨",
    "convenience_store": "🏪",
    "school": "🏫",
    "love_hotel": "🏩",
    "wedding": "💒",
    "classical_building": "🏛",
    "church": "⛪",
    "mosque": "🕌",
    "hindu_temple": "🛕",
    "synagogue": "🕍",
    "kaaba": "🕋",
    "shinto_shrine": "⛩",
    "railway_track": "🛤",
    "railroad_track": "🛤",
    "motorway": "🛣",
    "japan": "🗾",
    "rice_scene": "🎑",
    "park": "🏞",
    "national_park": "🏞",
    "sunrise": "🌅",
    "sunrise_over_mountains": "🌄",
    "stars": "🌠",
    "sparkler": "🎇",
    "fireworks": "🎆",
    "city_sunset": "🌇",
    "city_sunrise": "🌇",
    "city_dusk": "🌆",
    "cityscape": "🏙",
    "night_with_stars": "🌃",
    "milky_way": "🌌",
    "bridge_at_night": "🌉",
    "foggy": "🌁",
    "watch": "⌚",
    "iphone": "📱",
    "calling": "📲",
    "computer": "💻",
    "keyboard": "⌨",
    "desktop": "🖥",
    "desktop_computer": "🖥",
    "printer": "🖨",
    "mouse_three_button": "🖱",
    "three_button_mouse": "🖱",
    "trackball": "🖲",
    "joystick": "🕹",
    "compression": "🗜",
    "minidisc": "💽",
    "floppy_disk": "💾",
    "cd": "💿",
    "dvd": "📀",
    "vhs": "📼",
    "camera": "📷",
    "camera_with_flash": "📸",
    "video_camera": "📹",
    "movie_camera": "🎥",
    "projector": "📽",
    "film_projector": "📽",
    "film_frames": "🎞",
    "telephone_receiver": "📞",
    "telephone": "☎",
    "pager": "📟",
    "fax": "📠",
    "tv": "📺",
    "radio": "📻",
    "microphone2": "🎙",
    "studio_microphone": "🎙",
    "level_slider": "🎚",
    "control_knobs": "🎛",
    "compass": "🧭",
    "stopwatch": "⏱",
    "timer": "⏲",
    "timer_clock": "⏲",
    "alarm_clock": "⏰",
    "clock": "🕰",
    "mantlepiece_clock": "🕰",
    "hourglass": "⌛",
    "hourglass_flowing_sand": "⏳",
    "satellite": "📡",
    "battery": "🔋",
    "electric_plug": "🔌",
    "bulb": "💡",
    "flashlight": "🔦",
    "candle": "🕯",
    "fire_extinguisher": "🧯",
    "oil": "🛢",
    "oil_drum": "🛢",
    "money_with_wings": "💸",
    "dollar": "💵",
    "yen": "💴",
    "euro": "💶",
    "pound": "💷",
    "moneybag": "💰",
    "credit_card": "💳",
    "gem": "💎",
    "scales": "⚖",
    "toolbox": "🧰",
    "wrench": "🔧",
    "hammer": "🔨",
    "hammer_pick": "⚒",
    "hammer_and_pick": "⚒",
    "tools": "🛠",
    "hammer_and_wrench": "🛠",
    "pick": "⛏",
    "nut_and_bolt": "🔩",
    "gear": "⚙",
    "bricks": "🧱",
    "chains": "⛓",
    "magnet": "🧲",
    "gun": "🔫",
    "bomb": "💣",
    "firecracker": "🧨",
    "axe": "🪓",
    "razor": "🪒",
    "knife": "🔪",
    "dagger": "🗡",
    "dagger_knife": "🗡",
    "crossed_swords": "⚔",
    "shield": "🛡",
    "smoking": "🚬",
    "coffin": "⚰",
    "urn": "⚱",
    "funeral_urn": "⚱",
    "amphora": "🏺",
    "diya_lamp": "🪔",
    "crystal_ball": "🔮",
    "prayer_beads": "📿",
    "nazar_amulet": "🧿",
    "barber": "💈",
    "alembic": "⚗",
    "telescope": "🔭",
    "microscope": "🔬",
    "hole": "🕳",
    "probing_cane": "🦯",
    "stethoscope": "🩺",
    "adhesive_bandage": "🩹",
    "pill": "💊",
    "syringe": "💉",
    "drop_of_blood": "🩸",
    "dna": "🧬",
    "microbe": "🦠",
    "petri_dish": "🧫",
    "test_tube": "🧪",
    "thermometer": "🌡",
    "chair": "🪑",
    "broom": "🧹",
    "basket": "🧺",
    "roll_of_paper": "🧻",
    "toilet": "🚽",
    "potable_water": "🚰",
    "shower": "🚿",
    "bathtub": "🛁",
    "bath": "🛀",
    "bath_tone1": "🛀🏻",
    "bath_tone2": "🛀🏼",
    "bath_tone3": "🛀🏽",
    "bath_tone4": "🛀🏾",
    "bath_tone5": "🛀🏿",
    "soap": "🧼",
    "sponge": "🧽",
    "squeeze_bottle": "🧴",
    "bellhop": "🛎",
    "bellhop_bell": "🛎",
    "key": "🔑",
    "key2": "🗝",
    "old_key": "🗝",
    "door": "🚪",
    "couch": "🛋",
    "couch_and_lamp": "🛋",
    "bed": "🛏",
    "sleeping_accommodation": "🛌",
    "person_in_bed_tone1": "🛌🏻",
    "person_in_bed_light_skin_tone": "🛌🏻",
    "person_in_bed_tone2": "🛌🏼",
    "person_in_bed_medium_light_skin_tone": "🛌🏼",
    "person_in_bed_tone3": "🛌🏽",
    "person_in_bed_medium_skin_tone": "🛌🏽",
    "person_in_bed_tone4": "🛌🏾",
    "person_in_bed_medium_dark_skin_tone": "🛌🏾",
    "person_in_bed_tone5": "🛌🏿",
    "person_in_bed_dark_skin_tone": "🛌🏿",
    "teddy_bear": "🧸",
    "frame_photo": "🖼",
    "frame_with_picture": "🖼",
    "shopping_bags": "🛍",
    "shopping_cart": "🛒",
    "shopping_trolley": "🛒",
    "gift": "🎁",
    "balloon": "🎈",
    "flags": "🎏",
    "ribbon": "🎀",
    "confetti_ball": "🎊",
    "tada": "🎉",
    "dolls": "🎎",
    "izakaya_lantern": "🏮",
    "wind_chime": "🎐",
    "red_envelope": "🧧",
    "envelope": "✉",
    "envelope_with_arrow": "📩",
    "incoming_envelope": "📨",
    "e_mail": "📧",
    "email": "📧",
    "love_letter": "💌",
    "inbox_tray": "📥",
    "outbox_tray": "📤",
    "package": "📦",
    "label": "🏷",
    "mailbox_closed": "📪",
    "mailbox": "📫",
    "mailbox_with_mail": "📬",
    "mailbox_with_no_mail": "📭",
    "postbox": "📮",
    "postal_horn": "📯",
    "scroll": "📜",
    "page_with_curl": "📃",
    "page_facing_up": "📄",
    "bookmark_tabs": "📑",
    "receipt": "🧾",
    "bar_chart": "📊",
    "chart_with_upwards_trend": "📈",
    "chart_with_downwards_trend": "📉",
    "notepad_spiral": "🗒",
    "spiral_note_pad": "🗒",
    "calendar_spiral": "🗓",
    "spiral_calendar_pad": "🗓",
    "calendar": "📆",
    "date": "📅",
    "wastebasket": "🗑",
    "card_index": "📇",
    "card_box": "🗃",
    "card_file_box": "🗃",
    "ballot_box": "🗳",
    "ballot_box_with_ballot": "🗳",
    "file_cabinet": "🗄",
    "clipboard": "📋",
    "file_folder": "📁",
    "open_file_folder": "📂",
    "dividers": "🗂",
    "card_index_dividers": "🗂",
    "newspaper2": "🗞",
    "rolled_up_newspaper": "🗞",
    "newspaper": "📰",
    "notebook": "📓",
    "notebook_with_decorative_cover": "📔",
    "ledger": "📒",
    "closed_book": "📕",
    "green_book": "📗",
    "blue_book": "📘",
    "orange_book": "📙",
    "books": "📚",
    "book": "📖",
    "bookmark": "🔖",
    "safety_pin": "🧷",
    "link": "🔗",
    "paperclip": "📎",
    "paperclips": "🖇",
    "linked_paperclips": "🖇",
    "triangular_ruler": "📐",
    "straight_ruler": "📏",
    "abacus": "🧮",
    "pushpin": "📌",
    "round_pushpin": "📍",
    "scissors": "✂",
    "pen_ballpoint": "🖊",
    "lower_left_ballpoint_pen": "🖊",
    "pen_fountain": "🖋",
    "lower_left_fountain_pen": "🖋",
    "black_nib": "✒",
    "paintbrush": "🖌",
    "lower_left_paintbrush": "🖌",
    "crayon": "🖍",
    "lower_left_crayon": "🖍",
    "pencil": "📝",
    "memo": "📝",
    "pencil2": "✏",
    "mag": "🔍",
    "mag_right": "🔎",
    "lock_with_ink_pen": "🔏",
    "closed_lock_with_key": "🔐",
    "lock": "🔒",
    "unlock": "🔓",
    "heart": "❤",
    "orange_heart": "🧡",
    "yellow_heart": "💛",
    "green_heart": "💚",
    "blue_heart": "💙",
    "purple_heart": "💜",
    "black_heart": "🖤",
    "brown_heart": "🤎",
    "white_heart": "🤍",
    "broken_heart": "💔",
    "heart_exclamation": "❣",
    "heavy_heart_exclamation_mark_ornament": "❣",
    "two_hearts": "💕",
    "revolving_hearts": "💞",
    "heartbeat": "💓",
    "heartpulse": "💗",
    "sparkling_heart": "💖",
    "cupid": "💘",
    "gift_heart": "💝",
    "heart_decoration": "💟",
    "peace": "☮",
    "peace_symbol": "☮",
    "cross": "✝",
    "latin_cross": "✝",
    "star_and_crescent": "☪",
    "om_symbol": "🕉",
    "wheel_of_dharma": "☸",
    "star_of_david": "✡",
    "six_pointed_star": "🔯",
    "menorah": "🕎",
    "yin_yang": "☯",
    "orthodox_cross": "☦",
    "place_of_worship": "🛐",
    "worship_symbol": "🛐",
    "ophiuchus": "⛎",
    "aries": "♈",
    "taurus": "♉",
    "gemini": "♊",
    "cancer": "♋",
    "leo": "♌",
    "virgo": "♍",
    "libra": "♎",
    "scorpius": "♏",
    "sagittarius": "♐",
    "capricorn": "♑",
    "aquarius": "♒",
    "pisces": "♓",
    "id": "🆔",
    "atom": "⚛",
    "atom_symbol": "⚛",
    "accept": "🉑",
    "radioactive": "☢",
    "radioactive_sign": "☢",
    "biohazard": "☣",
    "biohazard_sign": "☣",
    "mobile_phone_off": "📴",
    "vibration_mode": "📳",
    "u6709": "🈶",
    "u7121": "🈚",
    "u7533": "🈸",
    "u55b6": "🈺",
    "u6708": "🈷",
    "eight_pointed_black_star": "✴",
    "vs": "🆚",
    "white_flower": "💮",
    "ideograph_advantage": "🉐",
    "secret": "㊙",
    "congratulations": "㊗",
    "u6e80": "🈵",
    "u5272": "🈹",
    "u7981": "🈲",
    "a": "🅰",
    "b": "🅱",
    "ab": "🆎",
    "cl": "🆑",
    "o2": "🅾",
    "sos": "🆘",
    "x": "❌",
    "o": "⭕",
    "octagonal_sign": "🛑",
    "stop_sign": "🛑",
    "no_entry": "⛔",
    "name_badge": "📛",
    "no_entry_sign": "🚫",
    "anger": "💢",
    "hotsprings": "♨",
    "no_pedestrians": "🚷",
    "do_not_litter": "🚯",
    "no_bicycles": "🚳",
    "non_potable_water": "🚱",
    "underage": "🔞",
    "no_mobile_phones": "📵",
    "no_smoking": "🚭",
    "exclamation": "❗",
    "grey_exclamation": "❕",
    "question": "❓",
    "grey_question": "❔",
    "bangbang": "‼",
    "interrobang": "⁉",
    "low_brightness": "🔅",
    "high_brightness": "🔆",
    "part_alternation_mark": "〽",
    "warning": "⚠",
    "children_crossing": "🚸",
    "trident": "🔱",
    "fleur_de_lis": "⚜",
    "beginner": "🔰",
    "recycle": "♻",
    "white_check_mark": "✅",
    "u6307": "🈯",
    "chart": "💹",
    "sparkle": "❇",
    "eight_spoked_asterisk": "✳",
    "negative_squared_cross_mark": "❎",
    "globe_with_meridians": "🌐",
    "diamond_shape_with_a_dot_inside": "💠",
    "m": "Ⓜ",
    "cyclone": "🌀",
    "zzz": "💤",
    "atm": "🏧",
    "wc": "🚾",
    "wheelchair": "♿",
    "parking": "🅿",
    "u7a7a": "🈳",
    "sa": "🈂",
    "customs": "🛃",
    "baggage_claim": "🛄",
    "left_luggage": "🛅",
    "mens": "🚹",
    "womens": "🚺",
    "baby_symbol": "🚼",
    "restroom": "🚻",
    "put_litter_in_its_place": "🚮",
    "cinema": "🎦",
    "signal_strength": "📶",
    "koko": "🈁",
    "symbols": "🔣",
    "information_source": "ℹ",
    "abc": "🔤",
    "abcd": "🔡",
    "capital_abcd": "🔠",
    "ng": "🆖",
    "ok": "🆗",
    "up": "🆙",
    "cool": "🆒",
    "new": "🆕",
    "free": "🆓",
    "zero": "0️⃣",
    "one": "1️⃣",
    "two": "2️⃣",
    "three": "3️⃣",
    "four": "4️⃣",
    "five": "5️⃣",
    "six": "6️⃣",
    "seven": "7️⃣",
    "eight": "8️⃣",
    "nine": "9️⃣",
    "keycap_ten": "🔟",
    "hash": "#️⃣",
    "keycap_asterisk": "*️⃣",
    "eject": "⏏",
    "eject_symbol": "⏏",
    "arrow_forward": "▶",
    "pause_button": "⏸",
    "double_vertical_bar": "⏸",
    "play_pause": "⏯",
    "stop_button": "⏹",
    "record_button": "⏺",
    "track_next": "⏭",
    "next_track": "⏭",
    "track_previous": "⏮",
    "previous_track": "⏮",
    "fast_forward": "⏩",
    "rewind": "⏪",
    "arrow_double_up": "⏫",
    "arrow_double_down": "⏬",
    "arrow_backward": "◀",
    "arrow_up_small": "🔼",
    "arrow_down_small": "🔽",
    "arrow_right": "➡",
    "arrow_left": "⬅",
    "arrow_up": "⬆",
    "arrow_down": "⬇",
    "arrow_upper_right": "↗",
    "arrow_lower_right": "↘",
    "arrow_lower_left": "↙",
    "arrow_upper_left": "↖",
    "arrow_up_down": "↕",
    "left_right_arrow": "↔",
    "arrow_right_hook": "↪",
    "leftwards_arrow_with_hook": "↩",
    "arrow_heading_up": "⤴",
    "arrow_heading_down": "⤵",
    "twisted_rightwards_arrows": "🔀",
    "repeat": "🔁",
    "repeat_one": "🔂",
    "arrows_counterclockwise": "🔄",
    "arrows_clockwise": "🔃",
    "musical_note": "🎵",
    "notes": "🎶",
    "heavy_plus_sign": "➕",
    "heavy_minus_sign": "➖",
    "heavy_division_sign": "➗",
    "heavy_multiplication_x": "✖",
    "infinity": "♾",
    "heavy_dollar_sign": "💲",
    "currency_exchange": "💱",
    "tm": "™",
    "copyright": "©",
    "registered": "®",
    "wavy_dash": "〰",
    "curly_loop": "➰",
    "loop": "➿",
    "end": "🔚",
    "back": "🔙",
    "on": "🔛",
    "top": "🔝",
    "soon": "🔜",
    "heavy_check_mark": "✔",
    "ballot_box_with_check": "☑",
    "radio_button": "🔘",
    "white_circle": "⚪",
    "black_circle": "⚫",
    "red_circle": "🔴",
    "blue_circle": "🔵",
    "brown_circle": "🟤",
    "purple_circle": "🟣",
    "green_circle": "🟢",
    "yellow_circle": "🟡",
    "orange_circle": "🟠",
    "small_red_triangle": "🔺",
    "small_red_triangle_down": "🔻",
    "small_orange_diamond": "🔸",
    "small_blue_diamond": "🔹",
    "large_orange_diamond": "🔶",
    "large_blue_diamond": "🔷",
    "white_square_button": "🔳",
    "black_square_button": "🔲",
    "black_small_square": "▪",
    "white_small_square": "▫",
    "black_medium_small_square": "◾",
    "white_medium_small_square": "◽",
    "black_medium_square": "◼",
    "white_medium_square": "◻",
    "black_large_square": "⬛",
    "white_large_square": "⬜",
    "orange_square": "🟧",
    "blue_square": "🟦",
    "red_square": "🟥",
    "brown_square": "🟫",
    "purple_square": "🟪",
    "green_square": "🟩",
    "yellow_square": "🟨",
    "speaker": "🔈",
    "mute": "🔇",
    "sound": "🔉",
    "loud_sound": "🔊",
    "bell": "🔔",
    "no_bell": "🔕",
    "mega": "📣",
    "loudspeaker": "📢",
    "speech_left": "🗨",
    "left_speech_bubble": "🗨",
    "eye_in_speech_bubble": "👁🗨",
    "speech_balloon": "💬",
    "thought_balloon": "💭",
    "anger_right": "🗯",
    "right_anger_bubble": "🗯",
    "spades": "♠",
    "clubs": "♣",
    "hearts": "♥",
    "diamonds": "♦",
    "black_joker": "🃏",
    "flower_playing_cards": "🎴",
    "mahjong": "🀄",
    "clock1": "🕐",
    "clock2": "🕑",
    "clock3": "🕒",
    "clock4": "🕓",
    "clock5": "🕔",
    "clock6": "🕕",
    "clock7": "🕖",
    "clock8": "🕗",
    "clock9": "🕘",
    "clock10": "🕙",
    "clock11": "🕚",
    "clock12": "🕛",
    "clock130": "🕜",
    "clock230": "🕝",
    "clock330": "🕞",
    "clock430": "🕟",
    "clock530": "🕠",
    "clock630": "🕡",
    "clock730": "🕢",
    "clock830": "🕣",
    "clock930": "🕤",
    "clock1030": "🕥",
    "clock1130": "🕦",
    "clock1230": "🕧",
    "female_sign": "♀",
    "male_sign": "♂",
    "medical_symbol": "⚕",
    "regional_indicator_z": "🇿",
    "regional_indicator_y": "🇾",
    "regional_indicator_x": "🇽",
    "regional_indicator_w": "🇼",
    "regional_indicator_v": "🇻",
    "regional_indicator_u": "🇺",
    "regional_indicator_t": "🇹",
    "regional_indicator_s": "🇸",
    "regional_indicator_r": "🇷",
    "regional_indicator_q": "🇶",
    "regional_indicator_p": "🇵",
    "regional_indicator_o": "🇴",
    "regional_indicator_n": "🇳",
    "regional_indicator_m": "🇲",
    "regional_indicator_l": "🇱",
    "regional_indicator_k": "🇰",
    "regional_indicator_j": "🇯",
    "regional_indicator_i": "🇮",
    "regional_indicator_h": "🇭",
    "regional_indicator_g": "🇬",
    "regional_indicator_f": "🇫",
    "regional_indicator_e": "🇪",
    "regional_indicator_d": "🇩",
    "regional_indicator_c": "🇨",
    "regional_indicator_b": "🇧",
    "regional_indicator_a": "🇦",
    "flag_white": "🏳",
    "flag_black": "🏴",
    "checkered_flag": "🏁",
    "triangular_flag_on_post": "🚩",
    "rainbow_flag": "🏳🌈",
    "gay_pride_flag": "🏳🌈",
    "pirate_flag": "🏴☠",
    "flag_af": "🇦🇫",
    "flag_ax": "🇦🇽",
    "flag_al": "🇦🇱",
    "flag_dz": "🇩🇿",
    "flag_as": "🇦🇸",
    "flag_ad": "🇦🇩",
    "flag_ao": "🇦🇴",
    "flag_ai": "🇦🇮",
    "flag_aq": "🇦🇶",
    "flag_ag": "🇦🇬",
    "flag_ar": "🇦🇷",
    "flag_am": "🇦🇲",
    "flag_aw": "🇦🇼",
    "flag_au": "🇦🇺",
    "flag_at": "🇦🇹",
    "flag_az": "🇦🇿",
    "flag_bs": "🇧🇸",
    "flag_bh": "🇧🇭",
    "flag_bd": "🇧🇩",
    "flag_bb": "🇧🇧",
    "flag_by": "🇧🇾",
    "flag_be": "🇧🇪",
    "flag_bz": "🇧🇿",
    "flag_bj": "🇧🇯",
    "flag_bm": "🇧🇲",
    "flag_bt": "🇧🇹",
    "flag_bo": "🇧🇴",
    "flag_ba": "🇧🇦",
    "flag_bw": "🇧🇼",
    "flag_br": "🇧🇷",
    "flag_io": "🇮🇴",
    "flag_vg": "🇻🇬",
    "flag_bn": "🇧🇳",
    "flag_bg": "🇧🇬",
    "flag_bf": "🇧🇫",
    "flag_bi": "🇧🇮",
    "flag_kh": "🇰🇭",
    "flag_cm": "🇨🇲",
    "flag_ca": "🇨🇦",
    "flag_ic": "🇮🇨",
    "flag_cv": "🇨🇻",
    "flag_bq": "🇧🇶",
    "flag_ky": "🇰🇾",
    "flag_cf": "🇨🇫",
    "flag_td": "🇹🇩",
    "flag_cl": "🇨🇱",
    "flag_cn": "🇨🇳",
    "flag_cx": "🇨🇽",
    "flag_cc": "🇨🇨",
    "flag_co": "🇨🇴",
    "flag_km": "🇰🇲",
    "flag_cg": "🇨🇬",
    "flag_cd": "🇨🇩",
    "flag_ck": "🇨🇰",
    "flag_cr": "🇨🇷",
    "flag_ci": "🇨🇮",
    "flag_hr": "🇭🇷",
    "flag_cu": "🇨🇺",
    "flag_cw": "🇨🇼",
    "flag_cy": "🇨🇾",
    "flag_cz": "🇨🇿",
    "flag_dk": "🇩🇰",
    "flag_dj": "🇩🇯",
    "flag_dm": "🇩🇲",
    "flag_do": "🇩🇴",
    "flag_ec": "🇪🇨",
    "flag_eg": "🇪🇬",
    "flag_sv": "🇸🇻",
    "flag_gq": "🇬🇶",
    "flag_er": "🇪🇷",
    "flag_ee": "🇪🇪",
    "flag_et": "🇪🇹",
    "flag_eu": "🇪🇺",
    "flag_fk": "🇫🇰",
    "flag_fo": "🇫🇴",
    "flag_fj": "🇫🇯",
    "flag_fi": "🇫🇮",
    "flag_fr": "🇫🇷",
    "flag_gf": "🇬🇫",
    "flag_pf": "🇵🇫",
    "flag_tf": "🇹🇫",
    "flag_ga": "🇬🇦",
    "flag_gm": "🇬🇲",
    "flag_ge": "🇬🇪",
    "flag_de": "🇩🇪",
    "flag_gh": "🇬🇭",
    "flag_gi": "🇬🇮",
    "flag_gr": "🇬🇷",
    "flag_gl": "🇬🇱",
    "flag_gd": "🇬🇩",
    "flag_gp": "🇬🇵",
    "flag_gu": "🇬🇺",
    "flag_gt": "🇬🇹",
    "flag_gg": "🇬🇬",
    "flag_gn": "🇬🇳",
    "flag_gw": "🇬🇼",
    "flag_gy": "🇬🇾",
    "flag_ht": "🇭🇹",
    "flag_hn": "🇭🇳",
    "flag_hk": "🇭🇰",
    "flag_hu": "🇭🇺",
    "flag_is": "🇮🇸",
    "flag_in": "🇮🇳",
    "flag_id": "🇮🇩",
    "flag_ir": "🇮🇷",
    "flag_iq": "🇮🇶",
    "flag_ie": "🇮🇪",
    "flag_im": "🇮🇲",
    "flag_il": "🇮🇱",
    "flag_it": "🇮🇹",
    "flag_jm": "🇯🇲",
    "flag_jp": "🇯🇵",
    "crossed_flags": "🎌",
    "flag_je": "🇯🇪",
    "flag_jo": "🇯🇴",
    "flag_kz": "🇰🇿",
    "flag_ke": "🇰🇪",
    "flag_ki": "🇰🇮",
    "flag_xk": "🇽🇰",
    "flag_kw": "🇰🇼",
    "flag_kg": "🇰🇬",
    "flag_la": "🇱🇦",
    "flag_lv": "🇱🇻",
    "flag_lb": "🇱🇧",
    "flag_ls": "🇱🇸",
    "flag_lr": "🇱🇷",
    "flag_ly": "🇱🇾",
    "flag_li": "🇱🇮",
    "flag_lt": "🇱🇹",
    "flag_lu": "🇱🇺",
    "flag_mo": "🇲🇴",
    "flag_mk": "🇲🇰",
    "flag_mg": "🇲🇬",
    "flag_mw": "🇲🇼",
    "flag_my": "🇲🇾",
    "flag_mv": "🇲🇻",
    "flag_ml": "🇲🇱",
    "flag_mt": "🇲🇹",
    "flag_mh": "🇲🇭",
    "flag_mq": "🇲🇶",
    "flag_mr": "🇲🇷",
    "flag_mu": "🇲🇺",
    "flag_yt": "🇾🇹",
    "flag_mx": "🇲🇽",
    "flag_fm": "🇫🇲",
    "flag_md": "🇲🇩",
    "flag_mc": "🇲🇨",
    "flag_mn": "🇲🇳",
    "flag_me": "🇲🇪",
    "flag_ms": "🇲🇸",
    "flag_ma": "🇲🇦",
    "flag_mz": "🇲🇿",
    "flag_mm": "🇲🇲",
    "flag_na": "🇳🇦",
    "flag_nr": "🇳🇷",
    "flag_np": "🇳🇵",
    "flag_nl": "🇳🇱",
    "flag_nc": "🇳🇨",
    "flag_nz": "🇳🇿",
    "flag_ni": "🇳🇮",
    "flag_ne": "🇳🇪",
    "flag_ng": "🇳🇬",
    "flag_nu": "🇳🇺",
    "flag_nf": "🇳🇫",
    "flag_kp": "🇰🇵",
    "flag_mp": "🇲🇵",
    "flag_no": "🇳🇴",
    "flag_om": "🇴🇲",
    "flag_pk": "🇵🇰",
    "flag_pw": "🇵🇼",
    "flag_ps": "🇵🇸",
    "flag_pa": "🇵🇦",
    "flag_pg": "🇵🇬",
    "flag_py": "🇵🇾",
    "flag_pe": "🇵🇪",
    "flag_ph": "🇵🇭",
    "flag_pn": "🇵🇳",
    "flag_pl": "🇵🇱",
    "flag_pt": "🇵🇹",
    "flag_pr": "🇵🇷",
    "flag_qa": "🇶🇦",
    "flag_re": "🇷🇪",
    "flag_ro": "🇷🇴",
    "flag_ru": "🇷🇺",
    "flag_rw": "🇷🇼",
    "flag_ws": "🇼🇸",
    "flag_sm": "🇸🇲",
    "flag_st": "🇸🇹",
    "flag_sa": "🇸🇦",
    "flag_sn": "🇸🇳",
    "flag_rs": "🇷🇸",
    "flag_sc": "🇸🇨",
    "flag_sl": "🇸🇱",
    "flag_sg": "🇸🇬",
    "flag_sx": "🇸🇽",
    "flag_sk": "🇸🇰",
    "flag_si": "🇸🇮",
    "flag_gs": "🇬🇸",
    "flag_sb": "🇸🇧",
    "flag_so": "🇸🇴",
    "flag_za": "🇿🇦",
    "flag_kr": "🇰🇷",
    "flag_ss": "🇸🇸",
    "flag_es": "🇪🇸",
    "flag_lk": "🇱🇰",
    "flag_bl": "🇧🇱",
    "flag_sh": "🇸🇭",
    "flag_kn": "🇰🇳",
    "flag_lc": "🇱🇨",
    "flag_pm": "🇵🇲",
    "flag_vc": "🇻🇨",
    "flag_sd": "🇸🇩",
    "flag_sr": "🇸🇷",
    "flag_sz": "🇸🇿",
    "flag_se": "🇸🇪",
    "flag_ch": "🇨🇭",
    "flag_sy": "🇸🇾",
    "flag_tw": "🇹🇼",
    "flag_tj": "🇹🇯",
    "flag_tz": "🇹🇿",
    "flag_th": "🇹🇭",
    "flag_tl": "🇹🇱",
    "flag_tg": "🇹🇬",
    "flag_tk": "🇹🇰",
    "flag_to": "🇹🇴",
    "flag_tt": "🇹🇹",
    "flag_tn": "🇹🇳",
    "flag_tr": "🇹🇷",
    "flag_tm": "🇹🇲",
    "flag_tc": "🇹🇨",
    "flag_vi": "🇻🇮",
    "flag_tv": "🇹🇻",
    "flag_ug": "🇺🇬",
    "flag_ua": "🇺🇦",
    "flag_ae": "🇦🇪",
    "flag_gb": "🇬🇧",
    "england": "🏴",
    "scotland": "🏴",
    "wales": "🏴",
    "flag_us": "🇺🇸",
    "flag_uy": "🇺🇾",
    "flag_uz": "🇺🇿",
    "flag_vu": "🇻🇺",
    "flag_va": "🇻🇦",
    "flag_ve": "🇻🇪",
    "flag_vn": "🇻🇳",
    "flag_wf": "🇼🇫",
    "flag_eh": "🇪🇭",
    "flag_ye": "🇾🇪",
    "flag_zm": "🇿🇲",
    "flag_zw": "🇿🇼",
    "flag_ac": "🇦🇨",
    "flag_bv": "🇧🇻",
    "flag_cp": "🇨🇵",
    "flag_ea": "🇪🇦",
    "flag_dg": "🇩🇬",
    "flag_hm": "🇭🇲",
    "flag_mf": "🇲🇫",
    "flag_sj": "🇸🇯",
    "flag_ta": "🇹🇦",
    "flag_um": "🇺🇲",
    "united_nations": "🇺🇳",
}


discord_emoji_converter_inverse = {value: key for key, value in discord_emoji_converter.items()}


class EmojiUnicodeType (str, Enum):
    hundred = "💯"
    one_two_three_four = "🔢"
    grinning = "😀"
    smiley = "😃"
    smile = "😄"
    grin = "😁"
    laughing = "😆"
    satisfied = "😆"
    sweat_smile = "😅"
    joy = "😂"
    rofl = "🤣"
    rolling_on_the_floor_laughing = "🤣"
    relaxed = "☺"
    blush = "😊"
    innocent = "😇"
    slight_smile = "🙂"
    slightly_smiling_face = "🙂"
    upside_down = "🙃"
    upside_down_face = "🙃"
    wink = "😉"
    relieved = "😌"
    heart_eyes = "😍"
    smiling_face_with_3_hearts = "🥰"
    kissing_heart = "😘"
    kissing = "😗"
    kissing_smiling_eyes = "😙"
    kissing_closed_eyes = "😚"
    yum = "😋"
    stuck_out_tongue = "😛"
    stuck_out_tongue_closed_eyes = "😝"
    stuck_out_tongue_winking_eye = "😜"
    zany_face = "🤪"
    face_with_raised_eyebrow = "🤨"
    face_with_monocle = "🧐"
    nerd = "🤓"
    nerd_face = "🤓"
    sunglasses = "😎"
    star_struck = "🤩"
    partying_face = "🥳"
    smirk = "😏"
    unamused = "😒"
    disappointed = "😞"
    pensive = "😔"
    worried = "😟"
    confused = "😕"
    slight_frown = "🙁"
    slightly_frowning_face = "🙁"
    frowning2 = "☹"
    white_frowning_face = "☹"
    persevere = "😣"
    confounded = "😖"
    tired_face = "😫"
    weary = "😩"
    pleading_face = "🥺"
    cry = "😢"
    sob = "😭"
    triumph = "😤"
    angry = "😠"
    rage = "😡"
    face_with_symbols_over_mouth = "🤬"
    exploding_head = "🤯"
    flushed = "😳"
    hot_face = "🥵"
    cold_face = "🥶"
    scream = "😱"
    fearful = "😨"
    cold_sweat = "😰"
    disappointed_relieved = "😥"
    sweat = "😓"
    hugging = "🤗"
    hugging_face = "🤗"
    thinking = "🤔"
    thinking_face = "🤔"
    face_with_hand_over_mouth = "🤭"
    yawning_face = "🥱"
    shushing_face = "🤫"
    lying_face = "🤥"
    liar = "🤥"
    no_mouth = "😶"
    neutral_face = "😐"
    expressionless = "😑"
    grimacing = "😬"
    rolling_eyes = "🙄"
    face_with_rolling_eyes = "🙄"
    hushed = "😯"
    frowning = "😦"
    anguished = "😧"
    open_mouth = "😮"
    astonished = "😲"
    sleeping = "😴"
    drooling_face = "🤤"
    drool = "🤤"
    sleepy = "😪"
    dizzy_face = "😵"
    zipper_mouth = "🤐"
    zipper_mouth_face = "🤐"
    woozy_face = "🥴"
    nauseated_face = "🤢"
    sick = "🤢"
    face_vomiting = "🤮"
    sneezing_face = "🤧"
    sneeze = "🤧"
    mask = "😷"
    thermometer_face = "🤒"
    face_with_thermometer = "🤒"
    head_bandage = "🤕"
    face_with_head_bandage = "🤕"
    money_mouth = "🤑"
    money_mouth_face = "🤑"
    cowboy = "🤠"
    face_with_cowboy_hat = "🤠"
    smiling_imp = "😈"
    imp = "👿"
    japanese_ogre = "👹"
    japanese_goblin = "👺"
    clown = "🤡"
    clown_face = "🤡"
    poop = "💩"
    shit = "💩"
    hankey = "💩"
    poo = "💩"
    ghost = "👻"
    skull = "💀"
    skeleton = "💀"
    skull_crossbones = "☠"
    skull_and_crossbones = "☠"
    alien = "👽"
    space_invader = "👾"
    robot = "🤖"
    robot_face = "🤖"
    jack_o_lantern = "🎃"
    smiley_cat = "😺"
    smile_cat = "😸"
    joy_cat = "😹"
    heart_eyes_cat = "😻"
    smirk_cat = "😼"
    kissing_cat = "😽"
    scream_cat = "🙀"
    crying_cat_face = "😿"
    pouting_cat = "😾"
    palms_up_together = "🤲"
    palms_up_together_tone1 = "🤲🏻"
    palms_up_together_light_skin_tone = "🤲🏻"
    palms_up_together_tone2 = "🤲🏼"
    palms_up_together_medium_light_skin_tone = "🤲🏼"
    palms_up_together_tone3 = "🤲🏽"
    palms_up_together_medium_skin_tone = "🤲🏽"
    palms_up_together_tone4 = "🤲🏾"
    palms_up_together_medium_dark_skin_tone = "🤲🏾"
    palms_up_together_tone5 = "🤲🏿"
    palms_up_together_dark_skin_tone = "🤲🏿"
    open_hands = "👐"
    open_hands_tone1 = "👐🏻"
    open_hands_tone2 = "👐🏼"
    open_hands_tone3 = "👐🏽"
    open_hands_tone4 = "👐🏾"
    open_hands_tone5 = "👐🏿"
    raised_hands = "🙌"
    raised_hands_tone1 = "🙌🏻"
    raised_hands_tone2 = "🙌🏼"
    raised_hands_tone3 = "🙌🏽"
    raised_hands_tone4 = "🙌🏾"
    raised_hands_tone5 = "🙌🏿"
    clap = "👏"
    clap_tone1 = "👏🏻"
    clap_tone2 = "👏🏼"
    clap_tone3 = "👏🏽"
    clap_tone4 = "👏🏾"
    clap_tone5 = "👏🏿"
    handshake = "🤝"
    shaking_hands = "🤝"
    thumbsup = "👍"
    plus_one = "👍"
    thumbup = "👍"
    thumbsup_tone1 = "👍🏻"
    plus_one_tone1 = "👍🏻"
    thumbup_tone1 = "👍🏻"
    thumbsup_tone2 = "👍🏼"
    plus_one_tone2 = "👍🏼"
    thumbup_tone2 = "👍🏼"
    thumbsup_tone3 = "👍🏽"
    plus_one_tone3 = "👍🏽"
    thumbup_tone3 = "👍🏽"
    thumbsup_tone4 = "👍🏾"
    plus_one_tone4 = "👍🏾"
    thumbup_tone4 = "👍🏾"
    thumbsup_tone5 = "👍🏿"
    plus_one_tone5 = "👍🏿"
    thumbup_tone5 = "👍🏿"
    thumbsdown = "👎"
    minus_one = "👎"
    thumbdown = "👎"
    thumbsdown_tone1 = "👎🏻"
    minus_one_tone1 = "👎🏻"
    thumbdown_tone1 = "👎🏻"
    thumbsdown_tone2 = "👎🏼"
    minus_one_tone2 = "👎🏼"
    thumbdown_tone2 = "👎🏼"
    thumbsdown_tone3 = "👎🏽"
    minus_one_tone3 = "👎🏽"
    thumbdown_tone3 = "👎🏽"
    thumbsdown_tone4 = "👎🏾"
    minus_one_tone4 = "👎🏾"
    thumbdown_tone4 = "👎🏾"
    thumbsdown_tone5 = "👎🏿"
    minus_one_tone5 = "👎🏿"
    thumbdown_tone5 = "👎🏿"
    punch = "👊"
    punch_tone1 = "👊🏻"
    punch_tone2 = "👊🏼"
    punch_tone3 = "👊🏽"
    punch_tone4 = "👊🏾"
    punch_tone5 = "👊🏿"
    fist = "✊"
    fist_tone1 = "✊🏻"
    fist_tone2 = "✊🏼"
    fist_tone3 = "✊🏽"
    fist_tone4 = "✊🏾"
    fist_tone5 = "✊🏿"
    left_facing_fist = "🤛"
    left_fist = "🤛"
    left_facing_fist_tone1 = "🤛🏻"
    left_fist_tone1 = "🤛🏻"
    left_facing_fist_tone2 = "🤛🏼"
    left_fist_tone2 = "🤛🏼"
    left_facing_fist_tone3 = "🤛🏽"
    left_fist_tone3 = "🤛🏽"
    left_facing_fist_tone4 = "🤛🏾"
    left_fist_tone4 = "🤛🏾"
    left_facing_fist_tone5 = "🤛🏿"
    left_fist_tone5 = "🤛🏿"
    right_facing_fist = "🤜"
    right_fist = "🤜"
    right_facing_fist_tone1 = "🤜🏻"
    right_fist_tone1 = "🤜🏻"
    right_facing_fist_tone2 = "🤜🏼"
    right_fist_tone2 = "🤜🏼"
    right_facing_fist_tone3 = "🤜🏽"
    right_fist_tone3 = "🤜🏽"
    right_facing_fist_tone4 = "🤜🏾"
    right_fist_tone4 = "🤜🏾"
    right_facing_fist_tone5 = "🤜🏿"
    right_fist_tone5 = "🤜🏿"
    fingers_crossed = "🤞"
    hand_with_index_and_middle_finger_crossed = "🤞"
    fingers_crossed_tone1 = "🤞🏻"
    hand_with_index_and_middle_fingers_crossed_tone1 = "🤞🏻"
    fingers_crossed_tone2 = "🤞🏼"
    hand_with_index_and_middle_fingers_crossed_tone2 = "🤞🏼"
    fingers_crossed_tone3 = "🤞🏽"
    hand_with_index_and_middle_fingers_crossed_tone3 = "🤞🏽"
    fingers_crossed_tone4 = "🤞🏾"
    hand_with_index_and_middle_fingers_crossed_tone4 = "🤞🏾"
    fingers_crossed_tone5 = "🤞🏿"
    hand_with_index_and_middle_fingers_crossed_tone5 = "🤞🏿"
    v = "✌"
    v_tone1 = "✌🏻"
    v_tone2 = "✌🏼"
    v_tone3 = "✌🏽"
    v_tone4 = "✌🏾"
    v_tone5 = "✌🏿"
    love_you_gesture = "🤟"
    love_you_gesture_tone1 = "🤟🏻"
    love_you_gesture_light_skin_tone = "🤟🏻"
    love_you_gesture_tone2 = "🤟🏼"
    love_you_gesture_medium_light_skin_tone = "🤟🏼"
    love_you_gesture_tone3 = "🤟🏽"
    love_you_gesture_medium_skin_tone = "🤟🏽"
    love_you_gesture_tone4 = "🤟🏾"
    love_you_gesture_medium_dark_skin_tone = "🤟🏾"
    love_you_gesture_tone5 = "🤟🏿"
    love_you_gesture_dark_skin_tone = "🤟🏿"
    metal = "🤘"
    sign_of_the_horns = "🤘"
    metal_tone1 = "🤘🏻"
    sign_of_the_horns_tone1 = "🤘🏻"
    metal_tone2 = "🤘🏼"
    sign_of_the_horns_tone2 = "🤘🏼"
    metal_tone3 = "🤘🏽"
    sign_of_the_horns_tone3 = "🤘🏽"
    metal_tone4 = "🤘🏾"
    sign_of_the_horns_tone4 = "🤘🏾"
    metal_tone5 = "🤘🏿"
    sign_of_the_horns_tone5 = "🤘🏿"
    ok_hand = "👌"
    ok_hand_tone1 = "👌🏻"
    ok_hand_tone2 = "👌🏼"
    ok_hand_tone3 = "👌🏽"
    ok_hand_tone4 = "👌🏾"
    ok_hand_tone5 = "👌🏿"
    pinching_hand = "🤏"
    pinching_hand_tone1 = "🤏🏻"
    pinching_hand_light_skin_tone = "🤏🏻"
    pinching_hand_tone2 = "🤏🏼"
    pinching_hand_medium_light_skin_tone = "🤏🏼"
    pinching_hand_tone3 = "🤏🏽"
    pinching_hand_medium_skin_tone = "🤏🏽"
    pinching_hand_tone4 = "🤏🏾"
    pinching_hand_medium_dark_skin_tone = "🤏🏾"
    pinching_hand_tone5 = "🤏🏿"
    pinching_hand_dark_skin_tone = "🤏🏿"
    point_left = "👈"
    point_left_tone1 = "👈🏻"
    point_left_tone2 = "👈🏼"
    point_left_tone3 = "👈🏽"
    point_left_tone4 = "👈🏾"
    point_left_tone5 = "👈🏿"
    point_right = "👉"
    point_right_tone1 = "👉🏻"
    point_right_tone2 = "👉🏼"
    point_right_tone3 = "👉🏽"
    point_right_tone4 = "👉🏾"
    point_right_tone5 = "👉🏿"
    point_up_2 = "👆"
    point_up_2_tone1 = "👆🏻"
    point_up_2_tone2 = "👆🏼"
    point_up_2_tone3 = "👆🏽"
    point_up_2_tone4 = "👆🏾"
    point_up_2_tone5 = "👆🏿"
    point_down = "👇"
    point_down_tone1 = "👇🏻"
    point_down_tone2 = "👇🏼"
    point_down_tone3 = "👇🏽"
    point_down_tone4 = "👇🏾"
    point_down_tone5 = "👇🏿"
    point_up = "☝"
    point_up_tone1 = "☝🏻"
    point_up_tone2 = "☝🏼"
    point_up_tone3 = "☝🏽"
    point_up_tone4 = "☝🏾"
    point_up_tone5 = "☝🏿"
    raised_hand = "✋"
    raised_hand_tone1 = "✋🏻"
    raised_hand_tone2 = "✋🏼"
    raised_hand_tone3 = "✋🏽"
    raised_hand_tone4 = "✋🏾"
    raised_hand_tone5 = "✋🏿"
    raised_back_of_hand = "🤚"
    back_of_hand = "🤚"
    raised_back_of_hand_tone1 = "🤚🏻"
    back_of_hand_tone1 = "🤚🏻"
    raised_back_of_hand_tone2 = "🤚🏼"
    back_of_hand_tone2 = "🤚🏼"
    raised_back_of_hand_tone3 = "🤚🏽"
    back_of_hand_tone3 = "🤚🏽"
    raised_back_of_hand_tone4 = "🤚🏾"
    back_of_hand_tone4 = "🤚🏾"
    raised_back_of_hand_tone5 = "🤚🏿"
    back_of_hand_tone5 = "🤚🏿"
    hand_splayed = "🖐"
    raised_hand_with_fingers_splayed = "🖐"
    hand_splayed_tone1 = "🖐🏻"
    raised_hand_with_fingers_splayed_tone1 = "🖐🏻"
    hand_splayed_tone2 = "🖐🏼"
    raised_hand_with_fingers_splayed_tone2 = "🖐🏼"
    hand_splayed_tone3 = "🖐🏽"
    raised_hand_with_fingers_splayed_tone3 = "🖐🏽"
    hand_splayed_tone4 = "🖐🏾"
    raised_hand_with_fingers_splayed_tone4 = "🖐🏾"
    hand_splayed_tone5 = "🖐🏿"
    raised_hand_with_fingers_splayed_tone5 = "🖐🏿"
    vulcan = "🖖"
    raised_hand_with_part_between_middle_and_ring_fingers = "🖖"
    vulcan_tone1 = "🖖🏻"
    raised_hand_with_part_between_middle_and_ring_fingers_tone1 = "🖖🏻"
    vulcan_tone2 = "🖖🏼"
    raised_hand_with_part_between_middle_and_ring_fingers_tone2 = "🖖🏼"
    vulcan_tone3 = "🖖🏽"
    raised_hand_with_part_between_middle_and_ring_fingers_tone3 = "🖖🏽"
    vulcan_tone4 = "🖖🏾"
    raised_hand_with_part_between_middle_and_ring_fingers_tone4 = "🖖🏾"
    vulcan_tone5 = "🖖🏿"
    raised_hand_with_part_between_middle_and_ring_fingers_tone5 = "🖖🏿"
    wave = "👋"
    wave_tone1 = "👋🏻"
    wave_tone2 = "👋🏼"
    wave_tone3 = "👋🏽"
    wave_tone4 = "👋🏾"
    wave_tone5 = "👋🏿"
    call_me = "🤙"
    call_me_hand = "🤙"
    call_me_tone1 = "🤙🏻"
    call_me_hand_tone1 = "🤙🏻"
    call_me_tone2 = "🤙🏼"
    call_me_hand_tone2 = "🤙🏼"
    call_me_tone3 = "🤙🏽"
    call_me_hand_tone3 = "🤙🏽"
    call_me_tone4 = "🤙🏾"
    call_me_hand_tone4 = "🤙🏾"
    call_me_tone5 = "🤙🏿"
    call_me_hand_tone5 = "🤙🏿"
    muscle = "💪"
    muscle_tone1 = "💪🏻"
    muscle_tone2 = "💪🏼"
    muscle_tone3 = "💪🏽"
    muscle_tone4 = "💪🏾"
    muscle_tone5 = "💪🏿"
    mechanical_arm = "🦾"
    middle_finger = "🖕"
    reversed_hand_with_middle_finger_extended = "🖕"
    middle_finger_tone1 = "🖕🏻"
    reversed_hand_with_middle_finger_extended_tone1 = "🖕🏻"
    middle_finger_tone2 = "🖕🏼"
    reversed_hand_with_middle_finger_extended_tone2 = "🖕🏼"
    middle_finger_tone3 = "🖕🏽"
    reversed_hand_with_middle_finger_extended_tone3 = "🖕🏽"
    middle_finger_tone4 = "🖕🏾"
    reversed_hand_with_middle_finger_extended_tone4 = "🖕🏾"
    middle_finger_tone5 = "🖕🏿"
    reversed_hand_with_middle_finger_extended_tone5 = "🖕🏿"
    writing_hand = "✍"
    writing_hand_tone1 = "✍🏻"
    writing_hand_tone2 = "✍🏼"
    writing_hand_tone3 = "✍🏽"
    writing_hand_tone4 = "✍🏾"
    writing_hand_tone5 = "✍🏿"
    pray = "🙏"
    pray_tone1 = "🙏🏻"
    pray_tone2 = "🙏🏼"
    pray_tone3 = "🙏🏽"
    pray_tone4 = "🙏🏾"
    pray_tone5 = "🙏🏿"
    foot = "🦶"
    foot_tone1 = "🦶🏻"
    foot_light_skin_tone = "🦶🏻"
    foot_tone2 = "🦶🏼"
    foot_medium_light_skin_tone = "🦶🏼"
    foot_tone3 = "🦶🏽"
    foot_medium_skin_tone = "🦶🏽"
    foot_tone4 = "🦶🏾"
    foot_medium_dark_skin_tone = "🦶🏾"
    foot_tone5 = "🦶🏿"
    foot_dark_skin_tone = "🦶🏿"
    leg = "🦵"
    leg_tone1 = "🦵🏻"
    leg_light_skin_tone = "🦵🏻"
    leg_tone2 = "🦵🏼"
    leg_medium_light_skin_tone = "🦵🏼"
    leg_tone3 = "🦵🏽"
    leg_medium_skin_tone = "🦵🏽"
    leg_tone4 = "🦵🏾"
    leg_medium_dark_skin_tone = "🦵🏾"
    leg_tone5 = "🦵🏿"
    leg_dark_skin_tone = "🦵🏿"
    mechanical_leg = "🦿"
    lipstick = "💄"
    kiss = "💋"
    lips = "👄"
    tooth = "🦷"
    bone = "🦴"
    tongue = "👅"
    ear = "👂"
    ear_tone1 = "👂🏻"
    ear_tone2 = "👂🏼"
    ear_tone3 = "👂🏽"
    ear_tone4 = "👂🏾"
    ear_tone5 = "👂🏿"
    ear_with_hearing_aid = "🦻"
    ear_with_hearing_aid_tone1 = "🦻🏻"
    ear_with_hearing_aid_light_skin_tone = "🦻🏻"
    ear_with_hearing_aid_tone2 = "🦻🏼"
    ear_with_hearing_aid_medium_light_skin_tone = "🦻🏼"
    ear_with_hearing_aid_tone3 = "🦻🏽"
    ear_with_hearing_aid_medium_skin_tone = "🦻🏽"
    ear_with_hearing_aid_tone4 = "🦻🏾"
    ear_with_hearing_aid_medium_dark_skin_tone = "🦻🏾"
    ear_with_hearing_aid_tone5 = "🦻🏿"
    ear_with_hearing_aid_dark_skin_tone = "🦻🏿"
    nose = "👃"
    nose_tone1 = "👃🏻"
    nose_tone2 = "👃🏼"
    nose_tone3 = "👃🏽"
    nose_tone4 = "👃🏾"
    nose_tone5 = "👃🏿"
    footprints = "👣"
    eye = "👁"
    eyes = "👀"
    brain = "🧠"
    speaking_head = "🗣"
    speaking_head_in_silhouette = "🗣"
    bust_in_silhouette = "👤"
    busts_in_silhouette = "👥"
    baby = "👶"
    baby_tone1 = "👶🏻"
    baby_tone2 = "👶🏼"
    baby_tone3 = "👶🏽"
    baby_tone4 = "👶🏾"
    baby_tone5 = "👶🏿"
    girl = "👧"
    girl_tone1 = "👧🏻"
    girl_tone2 = "👧🏼"
    girl_tone3 = "👧🏽"
    girl_tone4 = "👧🏾"
    girl_tone5 = "👧🏿"
    child = "🧒"
    child_tone1 = "🧒🏻"
    child_light_skin_tone = "🧒🏻"
    child_tone2 = "🧒🏼"
    child_medium_light_skin_tone = "🧒🏼"
    child_tone3 = "🧒🏽"
    child_medium_skin_tone = "🧒🏽"
    child_tone4 = "🧒🏾"
    child_medium_dark_skin_tone = "🧒🏾"
    child_tone5 = "🧒🏿"
    child_dark_skin_tone = "🧒🏿"
    boy = "👦"
    boy_tone1 = "👦🏻"
    boy_tone2 = "👦🏼"
    boy_tone3 = "👦🏽"
    boy_tone4 = "👦🏾"
    boy_tone5 = "👦🏿"
    woman = "👩"
    woman_tone1 = "👩🏻"
    woman_tone2 = "👩🏼"
    woman_tone3 = "👩🏽"
    woman_tone4 = "👩🏾"
    woman_tone5 = "👩🏿"
    adult = "🧑"
    adult_tone1 = "🧑🏻"
    adult_light_skin_tone = "🧑🏻"
    adult_tone2 = "🧑🏼"
    adult_medium_light_skin_tone = "🧑🏼"
    adult_tone3 = "🧑🏽"
    adult_medium_skin_tone = "🧑🏽"
    adult_tone4 = "🧑🏾"
    adult_medium_dark_skin_tone = "🧑🏾"
    adult_tone5 = "🧑🏿"
    adult_dark_skin_tone = "🧑🏿"
    man = "👨"
    man_tone1 = "👨🏻"
    man_tone2 = "👨🏼"
    man_tone3 = "👨🏽"
    man_tone4 = "👨🏾"
    man_tone5 = "👨🏿"
    woman_curly_haired = "👩🦱"
    woman_curly_haired_tone1 = "👩🏻🦱"
    woman_curly_haired_light_skin_tone = "👩🏻🦱"
    woman_curly_haired_tone2 = "👩🏼🦱"
    woman_curly_haired_medium_light_skin_tone = "👩🏼🦱"
    woman_curly_haired_tone3 = "👩🏽🦱"
    woman_curly_haired_medium_skin_tone = "👩🏽🦱"
    woman_curly_haired_tone4 = "👩🏾🦱"
    woman_curly_haired_medium_dark_skin_tone = "👩🏾🦱"
    woman_curly_haired_tone5 = "👩🏿🦱"
    woman_curly_haired_dark_skin_tone = "👩🏿🦱"
    man_curly_haired = "👨🦱"
    man_curly_haired_tone1 = "👨🏻🦱"
    man_curly_haired_light_skin_tone = "👨🏻🦱"
    man_curly_haired_tone2 = "👨🏼🦱"
    man_curly_haired_medium_light_skin_tone = "👨🏼🦱"
    man_curly_haired_tone3 = "👨🏽🦱"
    man_curly_haired_medium_skin_tone = "👨🏽🦱"
    man_curly_haired_tone4 = "👨🏾🦱"
    man_curly_haired_medium_dark_skin_tone = "👨🏾🦱"
    man_curly_haired_tone5 = "👨🏿🦱"
    man_curly_haired_dark_skin_tone = "👨🏿🦱"
    woman_red_haired = "👩🦰"
    woman_red_haired_tone1 = "👩🏻🦰"
    woman_red_haired_light_skin_tone = "👩🏻🦰"
    woman_red_haired_tone2 = "👩🏼🦰"
    woman_red_haired_medium_light_skin_tone = "👩🏼🦰"
    woman_red_haired_tone3 = "👩🏽🦰"
    woman_red_haired_medium_skin_tone = "👩🏽🦰"
    woman_red_haired_tone4 = "👩🏾🦰"
    woman_red_haired_medium_dark_skin_tone = "👩🏾🦰"
    woman_red_haired_tone5 = "👩🏿🦰"
    woman_red_haired_dark_skin_tone = "👩🏿🦰"
    man_red_haired = "👨🦰"
    man_red_haired_tone1 = "👨🏻🦰"
    man_red_haired_light_skin_tone = "👨🏻🦰"
    man_red_haired_tone2 = "👨🏼🦰"
    man_red_haired_medium_light_skin_tone = "👨🏼🦰"
    man_red_haired_tone3 = "👨🏽🦰"
    man_red_haired_medium_skin_tone = "👨🏽🦰"
    man_red_haired_tone4 = "👨🏾🦰"
    man_red_haired_medium_dark_skin_tone = "👨🏾🦰"
    man_red_haired_tone5 = "👨🏿🦰"
    man_red_haired_dark_skin_tone = "👨🏿🦰"
    blond_haired_woman = "👱♀"
    blond_haired_woman_tone1 = "👱🏻♀"
    blond_haired_woman_light_skin_tone = "👱🏻♀"
    blond_haired_woman_tone2 = "👱🏼♀"
    blond_haired_woman_medium_light_skin_tone = "👱🏼♀"
    blond_haired_woman_tone3 = "👱🏽♀"
    blond_haired_woman_medium_skin_tone = "👱🏽♀"
    blond_haired_woman_tone4 = "👱🏾♀"
    blond_haired_woman_medium_dark_skin_tone = "👱🏾♀"
    blond_haired_woman_tone5 = "👱🏿♀"
    blond_haired_woman_dark_skin_tone = "👱🏿♀"
    blond_haired_person = "👱"
    person_with_blond_hair = "👱"
    blond_haired_person_tone1 = "👱🏻"
    person_with_blond_hair_tone1 = "👱🏻"
    blond_haired_person_tone2 = "👱🏼"
    person_with_blond_hair_tone2 = "👱🏼"
    blond_haired_person_tone3 = "👱🏽"
    person_with_blond_hair_tone3 = "👱🏽"
    blond_haired_person_tone4 = "👱🏾"
    person_with_blond_hair_tone4 = "👱🏾"
    blond_haired_person_tone5 = "👱🏿"
    person_with_blond_hair_tone5 = "👱🏿"
    blond_haired_man = "👱♂"
    blond_haired_man_tone1 = "👱🏻♂"
    blond_haired_man_light_skin_tone = "👱🏻♂"
    blond_haired_man_tone2 = "👱🏼♂"
    blond_haired_man_medium_light_skin_tone = "👱🏼♂"
    blond_haired_man_tone3 = "👱🏽♂"
    blond_haired_man_medium_skin_tone = "👱🏽♂"
    blond_haired_man_tone4 = "👱🏾♂"
    blond_haired_man_medium_dark_skin_tone = "👱🏾♂"
    blond_haired_man_tone5 = "👱🏿♂"
    blond_haired_man_dark_skin_tone = "👱🏿♂"
    woman_white_haired = "👩🦳"
    woman_white_haired_tone1 = "👩🏻🦳"
    woman_white_haired_light_skin_tone = "👩🏻🦳"
    woman_white_haired_tone2 = "👩🏼🦳"
    woman_white_haired_medium_light_skin_tone = "👩🏼🦳"
    woman_white_haired_tone3 = "👩🏽🦳"
    woman_white_haired_medium_skin_tone = "👩🏽🦳"
    woman_white_haired_tone4 = "👩🏾🦳"
    woman_white_haired_medium_dark_skin_tone = "👩🏾🦳"
    woman_white_haired_tone5 = "👩🏿🦳"
    woman_white_haired_dark_skin_tone = "👩🏿🦳"
    man_white_haired = "👨🦳"
    man_white_haired_tone1 = "👨🏻🦳"
    man_white_haired_light_skin_tone = "👨🏻🦳"
    man_white_haired_tone2 = "👨🏼🦳"
    man_white_haired_medium_light_skin_tone = "👨🏼🦳"
    man_white_haired_tone3 = "👨🏽🦳"
    man_white_haired_medium_skin_tone = "👨🏽🦳"
    man_white_haired_tone4 = "👨🏾🦳"
    man_white_haired_medium_dark_skin_tone = "👨🏾🦳"
    man_white_haired_tone5 = "👨🏿🦳"
    man_white_haired_dark_skin_tone = "👨🏿🦳"
    woman_bald = "👩🦲"
    woman_bald_tone1 = "👩🏻🦲"
    woman_bald_light_skin_tone = "👩🏻🦲"
    woman_bald_tone2 = "👩🏼🦲"
    woman_bald_medium_light_skin_tone = "👩🏼🦲"
    woman_bald_tone3 = "👩🏽🦲"
    woman_bald_medium_skin_tone = "👩🏽🦲"
    woman_bald_tone4 = "👩🏾🦲"
    woman_bald_medium_dark_skin_tone = "👩🏾🦲"
    woman_bald_tone5 = "👩🏿🦲"
    woman_bald_dark_skin_tone = "👩🏿🦲"
    man_bald = "👨🦲"
    man_bald_tone1 = "👨🏻🦲"
    man_bald_light_skin_tone = "👨🏻🦲"
    man_bald_tone2 = "👨🏼🦲"
    man_bald_medium_light_skin_tone = "👨🏼🦲"
    man_bald_tone3 = "👨🏽🦲"
    man_bald_medium_skin_tone = "👨🏽🦲"
    man_bald_tone4 = "👨🏾🦲"
    man_bald_medium_dark_skin_tone = "👨🏾🦲"
    man_bald_tone5 = "👨🏿🦲"
    man_bald_dark_skin_tone = "👨🏿🦲"
    bearded_person = "🧔"
    bearded_person_tone1 = "🧔🏻"
    bearded_person_light_skin_tone = "🧔🏻"
    bearded_person_tone2 = "🧔🏼"
    bearded_person_medium_light_skin_tone = "🧔🏼"
    bearded_person_tone3 = "🧔🏽"
    bearded_person_medium_skin_tone = "🧔🏽"
    bearded_person_tone4 = "🧔🏾"
    bearded_person_medium_dark_skin_tone = "🧔🏾"
    bearded_person_tone5 = "🧔🏿"
    bearded_person_dark_skin_tone = "🧔🏿"
    older_woman = "👵"
    grandma = "👵"
    older_woman_tone1 = "👵🏻"
    grandma_tone1 = "👵🏻"
    older_woman_tone2 = "👵🏼"
    grandma_tone2 = "👵🏼"
    older_woman_tone3 = "👵🏽"
    grandma_tone3 = "👵🏽"
    older_woman_tone4 = "👵🏾"
    grandma_tone4 = "👵🏾"
    older_woman_tone5 = "👵🏿"
    grandma_tone5 = "👵🏿"
    older_adult = "🧓"
    older_adult_tone1 = "🧓🏻"
    older_adult_light_skin_tone = "🧓🏻"
    older_adult_tone2 = "🧓🏼"
    older_adult_medium_light_skin_tone = "🧓🏼"
    older_adult_tone3 = "🧓🏽"
    older_adult_medium_skin_tone = "🧓🏽"
    older_adult_tone4 = "🧓🏾"
    older_adult_medium_dark_skin_tone = "🧓🏾"
    older_adult_tone5 = "🧓🏿"
    older_adult_dark_skin_tone = "🧓🏿"
    older_man = "👴"
    older_man_tone1 = "👴🏻"
    older_man_tone2 = "👴🏼"
    older_man_tone3 = "👴🏽"
    older_man_tone4 = "👴🏾"
    older_man_tone5 = "👴🏿"
    man_with_chinese_cap = "👲"
    man_with_gua_pi_mao = "👲"
    man_with_chinese_cap_tone1 = "👲🏻"
    man_with_gua_pi_mao_tone1 = "👲🏻"
    man_with_chinese_cap_tone2 = "👲🏼"
    man_with_gua_pi_mao_tone2 = "👲🏼"
    man_with_chinese_cap_tone3 = "👲🏽"
    man_with_gua_pi_mao_tone3 = "👲🏽"
    man_with_chinese_cap_tone4 = "👲🏾"
    man_with_gua_pi_mao_tone4 = "👲🏾"
    man_with_chinese_cap_tone5 = "👲🏿"
    man_with_gua_pi_mao_tone5 = "👲🏿"
    person_wearing_turban = "👳"
    man_with_turban = "👳"
    person_wearing_turban_tone1 = "👳🏻"
    man_with_turban_tone1 = "👳🏻"
    person_wearing_turban_tone2 = "👳🏼"
    man_with_turban_tone2 = "👳🏼"
    person_wearing_turban_tone3 = "👳🏽"
    man_with_turban_tone3 = "👳🏽"
    person_wearing_turban_tone4 = "👳🏾"
    man_with_turban_tone4 = "👳🏾"
    person_wearing_turban_tone5 = "👳🏿"
    man_with_turban_tone5 = "👳🏿"
    woman_wearing_turban = "👳♀"
    woman_wearing_turban_tone1 = "👳🏻♀"
    woman_wearing_turban_light_skin_tone = "👳🏻♀"
    woman_wearing_turban_tone2 = "👳🏼♀"
    woman_wearing_turban_medium_light_skin_tone = "👳🏼♀"
    woman_wearing_turban_tone3 = "👳🏽♀"
    woman_wearing_turban_medium_skin_tone = "👳🏽♀"
    woman_wearing_turban_tone4 = "👳🏾♀"
    woman_wearing_turban_medium_dark_skin_tone = "👳🏾♀"
    woman_wearing_turban_tone5 = "👳🏿♀"
    woman_wearing_turban_dark_skin_tone = "👳🏿♀"
    man_wearing_turban = "👳♂"
    man_wearing_turban_tone1 = "👳🏻♂"
    man_wearing_turban_light_skin_tone = "👳🏻♂"
    man_wearing_turban_tone2 = "👳🏼♂"
    man_wearing_turban_medium_light_skin_tone = "👳🏼♂"
    man_wearing_turban_tone3 = "👳🏽♂"
    man_wearing_turban_medium_skin_tone = "👳🏽♂"
    man_wearing_turban_tone4 = "👳🏾♂"
    man_wearing_turban_medium_dark_skin_tone = "👳🏾♂"
    man_wearing_turban_tone5 = "👳🏿♂"
    man_wearing_turban_dark_skin_tone = "👳🏿♂"
    woman_with_headscarf = "🧕"
    woman_with_headscarf_tone1 = "🧕🏻"
    woman_with_headscarf_light_skin_tone = "🧕🏻"
    woman_with_headscarf_tone2 = "🧕🏼"
    woman_with_headscarf_medium_light_skin_tone = "🧕🏼"
    woman_with_headscarf_tone3 = "🧕🏽"
    woman_with_headscarf_medium_skin_tone = "🧕🏽"
    woman_with_headscarf_tone4 = "🧕🏾"
    woman_with_headscarf_medium_dark_skin_tone = "🧕🏾"
    woman_with_headscarf_tone5 = "🧕🏿"
    woman_with_headscarf_dark_skin_tone = "🧕🏿"
    police_officer = "👮"
    cop = "👮"
    police_officer_tone1 = "👮🏻"
    cop_tone1 = "👮🏻"
    police_officer_tone2 = "👮🏼"
    cop_tone2 = "👮🏼"
    police_officer_tone3 = "👮🏽"
    cop_tone3 = "👮🏽"
    police_officer_tone4 = "👮🏾"
    cop_tone4 = "👮🏾"
    police_officer_tone5 = "👮🏿"
    cop_tone5 = "👮🏿"
    woman_police_officer = "👮♀"
    woman_police_officer_tone1 = "👮🏻♀"
    woman_police_officer_light_skin_tone = "👮🏻♀"
    woman_police_officer_tone2 = "👮🏼♀"
    woman_police_officer_medium_light_skin_tone = "👮🏼♀"
    woman_police_officer_tone3 = "👮🏽♀"
    woman_police_officer_medium_skin_tone = "👮🏽♀"
    woman_police_officer_tone4 = "👮🏾♀"
    woman_police_officer_medium_dark_skin_tone = "👮🏾♀"
    woman_police_officer_tone5 = "👮🏿♀"
    woman_police_officer_dark_skin_tone = "👮🏿♀"
    man_police_officer = "👮♂"
    man_police_officer_tone1 = "👮🏻♂"
    man_police_officer_light_skin_tone = "👮🏻♂"
    man_police_officer_tone2 = "👮🏼♂"
    man_police_officer_medium_light_skin_tone = "👮🏼♂"
    man_police_officer_tone3 = "👮🏽♂"
    man_police_officer_medium_skin_tone = "👮🏽♂"
    man_police_officer_tone4 = "👮🏾♂"
    man_police_officer_medium_dark_skin_tone = "👮🏾♂"
    man_police_officer_tone5 = "👮🏿♂"
    man_police_officer_dark_skin_tone = "👮🏿♂"
    construction_worker = "👷"
    construction_worker_tone1 = "👷🏻"
    construction_worker_tone2 = "👷🏼"
    construction_worker_tone3 = "👷🏽"
    construction_worker_tone4 = "👷🏾"
    construction_worker_tone5 = "👷🏿"
    woman_construction_worker = "👷♀"
    woman_construction_worker_tone1 = "👷🏻♀"
    woman_construction_worker_light_skin_tone = "👷🏻♀"
    woman_construction_worker_tone2 = "👷🏼♀"
    woman_construction_worker_medium_light_skin_tone = "👷🏼♀"
    woman_construction_worker_tone3 = "👷🏽♀"
    woman_construction_worker_medium_skin_tone = "👷🏽♀"
    woman_construction_worker_tone4 = "👷🏾♀"
    woman_construction_worker_medium_dark_skin_tone = "👷🏾♀"
    woman_construction_worker_tone5 = "👷🏿♀"
    woman_construction_worker_dark_skin_tone = "👷🏿♀"
    man_construction_worker = "👷♂"
    man_construction_worker_tone1 = "👷🏻♂"
    man_construction_worker_light_skin_tone = "👷🏻♂"
    man_construction_worker_tone2 = "👷🏼♂"
    man_construction_worker_medium_light_skin_tone = "👷🏼♂"
    man_construction_worker_tone3 = "👷🏽♂"
    man_construction_worker_medium_skin_tone = "👷🏽♂"
    man_construction_worker_tone4 = "👷🏾♂"
    man_construction_worker_medium_dark_skin_tone = "👷🏾♂"
    man_construction_worker_tone5 = "👷🏿♂"
    man_construction_worker_dark_skin_tone = "👷🏿♂"
    guard = "💂"
    guardsman = "💂"
    guard_tone1 = "💂🏻"
    guardsman_tone1 = "💂🏻"
    guard_tone2 = "💂🏼"
    guardsman_tone2 = "💂🏼"
    guard_tone3 = "💂🏽"
    guardsman_tone3 = "💂🏽"
    guard_tone4 = "💂🏾"
    guardsman_tone4 = "💂🏾"
    guard_tone5 = "💂🏿"
    guardsman_tone5 = "💂🏿"
    woman_guard = "💂♀"
    woman_guard_tone1 = "💂🏻♀"
    woman_guard_light_skin_tone = "💂🏻♀"
    woman_guard_tone2 = "💂🏼♀"
    woman_guard_medium_light_skin_tone = "💂🏼♀"
    woman_guard_tone3 = "💂🏽♀"
    woman_guard_medium_skin_tone = "💂🏽♀"
    woman_guard_tone4 = "💂🏾♀"
    woman_guard_medium_dark_skin_tone = "💂🏾♀"
    woman_guard_tone5 = "💂🏿♀"
    woman_guard_dark_skin_tone = "💂🏿♀"
    man_guard = "💂♂"
    man_guard_tone1 = "💂🏻♂"
    man_guard_light_skin_tone = "💂🏻♂"
    man_guard_tone2 = "💂🏼♂"
    man_guard_medium_light_skin_tone = "💂🏼♂"
    man_guard_tone3 = "💂🏽♂"
    man_guard_medium_skin_tone = "💂🏽♂"
    man_guard_tone4 = "💂🏾♂"
    man_guard_medium_dark_skin_tone = "💂🏾♂"
    man_guard_tone5 = "💂🏿♂"
    man_guard_dark_skin_tone = "💂🏿♂"
    detective = "🕵"
    spy = "🕵"
    sleuth_or_spy = "🕵"
    detective_tone1 = "🕵🏻"
    spy_tone1 = "🕵🏻"
    sleuth_or_spy_tone1 = "🕵🏻"
    detective_tone2 = "🕵🏼"
    spy_tone2 = "🕵🏼"
    sleuth_or_spy_tone2 = "🕵🏼"
    detective_tone3 = "🕵🏽"
    spy_tone3 = "🕵🏽"
    sleuth_or_spy_tone3 = "🕵🏽"
    detective_tone4 = "🕵🏾"
    spy_tone4 = "🕵🏾"
    sleuth_or_spy_tone4 = "🕵🏾"
    detective_tone5 = "🕵🏿"
    spy_tone5 = "🕵🏿"
    sleuth_or_spy_tone5 = "🕵🏿"
    woman_detective = "🕵♀"
    woman_detective_tone1 = "🕵🏻♀"
    woman_detective_light_skin_tone = "🕵🏻♀"
    woman_detective_tone2 = "🕵🏼♀"
    woman_detective_medium_light_skin_tone = "🕵🏼♀"
    woman_detective_tone3 = "🕵🏽♀"
    woman_detective_medium_skin_tone = "🕵🏽♀"
    woman_detective_tone4 = "🕵🏾♀"
    woman_detective_medium_dark_skin_tone = "🕵🏾♀"
    woman_detective_tone5 = "🕵🏿♀"
    woman_detective_dark_skin_tone = "🕵🏿♀"
    man_detective = "🕵♂"
    man_detective_tone1 = "🕵🏻♂"
    man_detective_light_skin_tone = "🕵🏻♂"
    man_detective_tone2 = "🕵🏼♂"
    man_detective_medium_light_skin_tone = "🕵🏼♂"
    man_detective_tone3 = "🕵🏽♂"
    man_detective_medium_skin_tone = "🕵🏽♂"
    man_detective_tone4 = "🕵🏾♂"
    man_detective_medium_dark_skin_tone = "🕵🏾♂"
    man_detective_tone5 = "🕵🏿♂"
    man_detective_dark_skin_tone = "🕵🏿♂"
    woman_health_worker = "👩⚕"
    woman_health_worker_tone1 = "👩🏻⚕"
    woman_health_worker_light_skin_tone = "👩🏻⚕"
    woman_health_worker_tone2 = "👩🏼⚕"
    woman_health_worker_medium_light_skin_tone = "👩🏼⚕"
    woman_health_worker_tone3 = "👩🏽⚕"
    woman_health_worker_medium_skin_tone = "👩🏽⚕"
    woman_health_worker_tone4 = "👩🏾⚕"
    woman_health_worker_medium_dark_skin_tone = "👩🏾⚕"
    woman_health_worker_tone5 = "👩🏿⚕"
    woman_health_worker_dark_skin_tone = "👩🏿⚕"
    man_health_worker = "👨⚕"
    man_health_worker_tone1 = "👨🏻⚕"
    man_health_worker_light_skin_tone = "👨🏻⚕"
    man_health_worker_tone2 = "👨🏼⚕"
    man_health_worker_medium_light_skin_tone = "👨🏼⚕"
    man_health_worker_tone3 = "👨🏽⚕"
    man_health_worker_medium_skin_tone = "👨🏽⚕"
    man_health_worker_tone4 = "👨🏾⚕"
    man_health_worker_medium_dark_skin_tone = "👨🏾⚕"
    man_health_worker_tone5 = "👨🏿⚕"
    man_health_worker_dark_skin_tone = "👨🏿⚕"
    woman_farmer = "👩🌾"
    woman_farmer_tone1 = "👩🏻🌾"
    woman_farmer_light_skin_tone = "👩🏻🌾"
    woman_farmer_tone2 = "👩🏼🌾"
    woman_farmer_medium_light_skin_tone = "👩🏼🌾"
    woman_farmer_tone3 = "👩🏽🌾"
    woman_farmer_medium_skin_tone = "👩🏽🌾"
    woman_farmer_tone4 = "👩🏾🌾"
    woman_farmer_medium_dark_skin_tone = "👩🏾🌾"
    woman_farmer_tone5 = "👩🏿🌾"
    woman_farmer_dark_skin_tone = "👩🏿🌾"
    man_farmer = "👨🌾"
    man_farmer_tone1 = "👨🏻🌾"
    man_farmer_light_skin_tone = "👨🏻🌾"
    man_farmer_tone2 = "👨🏼🌾"
    man_farmer_medium_light_skin_tone = "👨🏼🌾"
    man_farmer_tone3 = "👨🏽🌾"
    man_farmer_medium_skin_tone = "👨🏽🌾"
    man_farmer_tone4 = "👨🏾🌾"
    man_farmer_medium_dark_skin_tone = "👨🏾🌾"
    man_farmer_tone5 = "👨🏿🌾"
    man_farmer_dark_skin_tone = "👨🏿🌾"
    woman_cook = "👩🍳"
    woman_cook_tone1 = "👩🏻🍳"
    woman_cook_light_skin_tone = "👩🏻🍳"
    woman_cook_tone2 = "👩🏼🍳"
    woman_cook_medium_light_skin_tone = "👩🏼🍳"
    woman_cook_tone3 = "👩🏽🍳"
    woman_cook_medium_skin_tone = "👩🏽🍳"
    woman_cook_tone4 = "👩🏾🍳"
    woman_cook_medium_dark_skin_tone = "👩🏾🍳"
    woman_cook_tone5 = "👩🏿🍳"
    woman_cook_dark_skin_tone = "👩🏿🍳"
    man_cook = "👨🍳"
    man_cook_tone1 = "👨🏻🍳"
    man_cook_light_skin_tone = "👨🏻🍳"
    man_cook_tone2 = "👨🏼🍳"
    man_cook_medium_light_skin_tone = "👨🏼🍳"
    man_cook_tone3 = "👨🏽🍳"
    man_cook_medium_skin_tone = "👨🏽🍳"
    man_cook_tone4 = "👨🏾🍳"
    man_cook_medium_dark_skin_tone = "👨🏾🍳"
    man_cook_tone5 = "👨🏿🍳"
    man_cook_dark_skin_tone = "👨🏿🍳"
    woman_student = "👩🎓"
    woman_student_tone1 = "👩🏻🎓"
    woman_student_light_skin_tone = "👩🏻🎓"
    woman_student_tone2 = "👩🏼🎓"
    woman_student_medium_light_skin_tone = "👩🏼🎓"
    woman_student_tone3 = "👩🏽🎓"
    woman_student_medium_skin_tone = "👩🏽🎓"
    woman_student_tone4 = "👩🏾🎓"
    woman_student_medium_dark_skin_tone = "👩🏾🎓"
    woman_student_tone5 = "👩🏿🎓"
    woman_student_dark_skin_tone = "👩🏿🎓"
    man_student = "👨🎓"
    man_student_tone1 = "👨🏻🎓"
    man_student_light_skin_tone = "👨🏻🎓"
    man_student_tone2 = "👨🏼🎓"
    man_student_medium_light_skin_tone = "👨🏼🎓"
    man_student_tone3 = "👨🏽🎓"
    man_student_medium_skin_tone = "👨🏽🎓"
    man_student_tone4 = "👨🏾🎓"
    man_student_medium_dark_skin_tone = "👨🏾🎓"
    man_student_tone5 = "👨🏿🎓"
    man_student_dark_skin_tone = "👨🏿🎓"
    woman_singer = "👩🎤"
    woman_singer_tone1 = "👩🏻🎤"
    woman_singer_light_skin_tone = "👩🏻🎤"
    woman_singer_tone2 = "👩🏼🎤"
    woman_singer_medium_light_skin_tone = "👩🏼🎤"
    woman_singer_tone3 = "👩🏽🎤"
    woman_singer_medium_skin_tone = "👩🏽🎤"
    woman_singer_tone4 = "👩🏾🎤"
    woman_singer_medium_dark_skin_tone = "👩🏾🎤"
    woman_singer_tone5 = "👩🏿🎤"
    woman_singer_dark_skin_tone = "👩🏿🎤"
    man_singer = "👨🎤"
    man_singer_tone1 = "👨🏻🎤"
    man_singer_light_skin_tone = "👨🏻🎤"
    man_singer_tone2 = "👨🏼🎤"
    man_singer_medium_light_skin_tone = "👨🏼🎤"
    man_singer_tone3 = "👨🏽🎤"
    man_singer_medium_skin_tone = "👨🏽🎤"
    man_singer_tone4 = "👨🏾🎤"
    man_singer_medium_dark_skin_tone = "👨🏾🎤"
    man_singer_tone5 = "👨🏿🎤"
    man_singer_dark_skin_tone = "👨🏿🎤"
    woman_teacher = "👩🏫"
    woman_teacher_tone1 = "👩🏻🏫"
    woman_teacher_light_skin_tone = "👩🏻🏫"
    woman_teacher_tone2 = "👩🏼🏫"
    woman_teacher_medium_light_skin_tone = "👩🏼🏫"
    woman_teacher_tone3 = "👩🏽🏫"
    woman_teacher_medium_skin_tone = "👩🏽🏫"
    woman_teacher_tone4 = "👩🏾🏫"
    woman_teacher_medium_dark_skin_tone = "👩🏾🏫"
    woman_teacher_tone5 = "👩🏿🏫"
    woman_teacher_dark_skin_tone = "👩🏿🏫"
    man_teacher = "👨🏫"
    man_teacher_tone1 = "👨🏻🏫"
    man_teacher_light_skin_tone = "👨🏻🏫"
    man_teacher_tone2 = "👨🏼🏫"
    man_teacher_medium_light_skin_tone = "👨🏼🏫"
    man_teacher_tone3 = "👨🏽🏫"
    man_teacher_medium_skin_tone = "👨🏽🏫"
    man_teacher_tone4 = "👨🏾🏫"
    man_teacher_medium_dark_skin_tone = "👨🏾🏫"
    man_teacher_tone5 = "👨🏿🏫"
    man_teacher_dark_skin_tone = "👨🏿🏫"
    woman_factory_worker = "👩🏭"
    woman_factory_worker_tone1 = "👩🏻🏭"
    woman_factory_worker_light_skin_tone = "👩🏻🏭"
    woman_factory_worker_tone2 = "👩🏼🏭"
    woman_factory_worker_medium_light_skin_tone = "👩🏼🏭"
    woman_factory_worker_tone3 = "👩🏽🏭"
    woman_factory_worker_medium_skin_tone = "👩🏽🏭"
    woman_factory_worker_tone4 = "👩🏾🏭"
    woman_factory_worker_medium_dark_skin_tone = "👩🏾🏭"
    woman_factory_worker_tone5 = "👩🏿🏭"
    woman_factory_worker_dark_skin_tone = "👩🏿🏭"
    man_factory_worker = "👨🏭"
    man_factory_worker_tone1 = "👨🏻🏭"
    man_factory_worker_light_skin_tone = "👨🏻🏭"
    man_factory_worker_tone2 = "👨🏼🏭"
    man_factory_worker_medium_light_skin_tone = "👨🏼🏭"
    man_factory_worker_tone3 = "👨🏽🏭"
    man_factory_worker_medium_skin_tone = "👨🏽🏭"
    man_factory_worker_tone4 = "👨🏾🏭"
    man_factory_worker_medium_dark_skin_tone = "👨🏾🏭"
    man_factory_worker_tone5 = "👨🏿🏭"
    man_factory_worker_dark_skin_tone = "👨🏿🏭"
    woman_technologist = "👩💻"
    woman_technologist_tone1 = "👩🏻💻"
    woman_technologist_light_skin_tone = "👩🏻💻"
    woman_technologist_tone2 = "👩🏼💻"
    woman_technologist_medium_light_skin_tone = "👩🏼💻"
    woman_technologist_tone3 = "👩🏽💻"
    woman_technologist_medium_skin_tone = "👩🏽💻"
    woman_technologist_tone4 = "👩🏾💻"
    woman_technologist_medium_dark_skin_tone = "👩🏾💻"
    woman_technologist_tone5 = "👩🏿💻"
    woman_technologist_dark_skin_tone = "👩🏿💻"
    man_technologist = "👨💻"
    man_technologist_tone1 = "👨🏻💻"
    man_technologist_light_skin_tone = "👨🏻💻"
    man_technologist_tone2 = "👨🏼💻"
    man_technologist_medium_light_skin_tone = "👨🏼💻"
    man_technologist_tone3 = "👨🏽💻"
    man_technologist_medium_skin_tone = "👨🏽💻"
    man_technologist_tone4 = "👨🏾💻"
    man_technologist_medium_dark_skin_tone = "👨🏾💻"
    man_technologist_tone5 = "👨🏿💻"
    man_technologist_dark_skin_tone = "👨🏿💻"
    woman_office_worker = "👩💼"
    woman_office_worker_tone1 = "👩🏻💼"
    woman_office_worker_light_skin_tone = "👩🏻💼"
    woman_office_worker_tone2 = "👩🏼💼"
    woman_office_worker_medium_light_skin_tone = "👩🏼💼"
    woman_office_worker_tone3 = "👩🏽💼"
    woman_office_worker_medium_skin_tone = "👩🏽💼"
    woman_office_worker_tone4 = "👩🏾💼"
    woman_office_worker_medium_dark_skin_tone = "👩🏾💼"
    woman_office_worker_tone5 = "👩🏿💼"
    woman_office_worker_dark_skin_tone = "👩🏿💼"
    man_office_worker = "👨💼"
    man_office_worker_tone1 = "👨🏻💼"
    man_office_worker_light_skin_tone = "👨🏻💼"
    man_office_worker_tone2 = "👨🏼💼"
    man_office_worker_medium_light_skin_tone = "👨🏼💼"
    man_office_worker_tone3 = "👨🏽💼"
    man_office_worker_medium_skin_tone = "👨🏽💼"
    man_office_worker_tone4 = "👨🏾💼"
    man_office_worker_medium_dark_skin_tone = "👨🏾💼"
    man_office_worker_tone5 = "👨🏿💼"
    man_office_worker_dark_skin_tone = "👨🏿💼"
    woman_mechanic = "👩🔧"
    woman_mechanic_tone1 = "👩🏻🔧"
    woman_mechanic_light_skin_tone = "👩🏻🔧"
    woman_mechanic_tone2 = "👩🏼🔧"
    woman_mechanic_medium_light_skin_tone = "👩🏼🔧"
    woman_mechanic_tone3 = "👩🏽🔧"
    woman_mechanic_medium_skin_tone = "👩🏽🔧"
    woman_mechanic_tone4 = "👩🏾🔧"
    woman_mechanic_medium_dark_skin_tone = "👩🏾🔧"
    woman_mechanic_tone5 = "👩🏿🔧"
    woman_mechanic_dark_skin_tone = "👩🏿🔧"
    man_mechanic = "👨🔧"
    man_mechanic_tone1 = "👨🏻🔧"
    man_mechanic_light_skin_tone = "👨🏻🔧"
    man_mechanic_tone2 = "👨🏼🔧"
    man_mechanic_medium_light_skin_tone = "👨🏼🔧"
    man_mechanic_tone3 = "👨🏽🔧"
    man_mechanic_medium_skin_tone = "👨🏽🔧"
    man_mechanic_tone4 = "👨🏾🔧"
    man_mechanic_medium_dark_skin_tone = "👨🏾🔧"
    man_mechanic_tone5 = "👨🏿🔧"
    man_mechanic_dark_skin_tone = "👨🏿🔧"
    woman_scientist = "👩🔬"
    woman_scientist_tone1 = "👩🏻🔬"
    woman_scientist_light_skin_tone = "👩🏻🔬"
    woman_scientist_tone2 = "👩🏼🔬"
    woman_scientist_medium_light_skin_tone = "👩🏼🔬"
    woman_scientist_tone3 = "👩🏽🔬"
    woman_scientist_medium_skin_tone = "👩🏽🔬"
    woman_scientist_tone4 = "👩🏾🔬"
    woman_scientist_medium_dark_skin_tone = "👩🏾🔬"
    woman_scientist_tone5 = "👩🏿🔬"
    woman_scientist_dark_skin_tone = "👩🏿🔬"
    man_scientist = "👨🔬"
    man_scientist_tone1 = "👨🏻🔬"
    man_scientist_light_skin_tone = "👨🏻🔬"
    man_scientist_tone2 = "👨🏼🔬"
    man_scientist_medium_light_skin_tone = "👨🏼🔬"
    man_scientist_tone3 = "👨🏽🔬"
    man_scientist_medium_skin_tone = "👨🏽🔬"
    man_scientist_tone4 = "👨🏾🔬"
    man_scientist_medium_dark_skin_tone = "👨🏾🔬"
    man_scientist_tone5 = "👨🏿🔬"
    man_scientist_dark_skin_tone = "👨🏿🔬"
    woman_artist = "👩🎨"
    woman_artist_tone1 = "👩🏻🎨"
    woman_artist_light_skin_tone = "👩🏻🎨"
    woman_artist_tone2 = "👩🏼🎨"
    woman_artist_medium_light_skin_tone = "👩🏼🎨"
    woman_artist_tone3 = "👩🏽🎨"
    woman_artist_medium_skin_tone = "👩🏽🎨"
    woman_artist_tone4 = "👩🏾🎨"
    woman_artist_medium_dark_skin_tone = "👩🏾🎨"
    woman_artist_tone5 = "👩🏿🎨"
    woman_artist_dark_skin_tone = "👩🏿🎨"
    man_artist = "👨🎨"
    man_artist_tone1 = "👨🏻🎨"
    man_artist_light_skin_tone = "👨🏻🎨"
    man_artist_tone2 = "👨🏼🎨"
    man_artist_medium_light_skin_tone = "👨🏼🎨"
    man_artist_tone3 = "👨🏽🎨"
    man_artist_medium_skin_tone = "👨🏽🎨"
    man_artist_tone4 = "👨🏾🎨"
    man_artist_medium_dark_skin_tone = "👨🏾🎨"
    man_artist_tone5 = "👨🏿🎨"
    man_artist_dark_skin_tone = "👨🏿🎨"
    woman_firefighter = "👩🚒"
    woman_firefighter_tone1 = "👩🏻🚒"
    woman_firefighter_light_skin_tone = "👩🏻🚒"
    woman_firefighter_tone2 = "👩🏼🚒"
    woman_firefighter_medium_light_skin_tone = "👩🏼🚒"
    woman_firefighter_tone3 = "👩🏽🚒"
    woman_firefighter_medium_skin_tone = "👩🏽🚒"
    woman_firefighter_tone4 = "👩🏾🚒"
    woman_firefighter_medium_dark_skin_tone = "👩🏾🚒"
    woman_firefighter_tone5 = "👩🏿🚒"
    woman_firefighter_dark_skin_tone = "👩🏿🚒"
    man_firefighter = "👨🚒"
    man_firefighter_tone1 = "👨🏻🚒"
    man_firefighter_light_skin_tone = "👨🏻🚒"
    man_firefighter_tone2 = "👨🏼🚒"
    man_firefighter_medium_light_skin_tone = "👨🏼🚒"
    man_firefighter_tone3 = "👨🏽🚒"
    man_firefighter_medium_skin_tone = "👨🏽🚒"
    man_firefighter_tone4 = "👨🏾🚒"
    man_firefighter_medium_dark_skin_tone = "👨🏾🚒"
    man_firefighter_tone5 = "👨🏿🚒"
    man_firefighter_dark_skin_tone = "👨🏿🚒"
    woman_pilot = "👩✈"
    woman_pilot_tone1 = "👩🏻✈"
    woman_pilot_light_skin_tone = "👩🏻✈"
    woman_pilot_tone2 = "👩🏼✈"
    woman_pilot_medium_light_skin_tone = "👩🏼✈"
    woman_pilot_tone3 = "👩🏽✈"
    woman_pilot_medium_skin_tone = "👩🏽✈"
    woman_pilot_tone4 = "👩🏾✈"
    woman_pilot_medium_dark_skin_tone = "👩🏾✈"
    woman_pilot_tone5 = "👩🏿✈"
    woman_pilot_dark_skin_tone = "👩🏿✈"
    man_pilot = "👨✈"
    man_pilot_tone1 = "👨🏻✈"
    man_pilot_light_skin_tone = "👨🏻✈"
    man_pilot_tone2 = "👨🏼✈"
    man_pilot_medium_light_skin_tone = "👨🏼✈"
    man_pilot_tone3 = "👨🏽✈"
    man_pilot_medium_skin_tone = "👨🏽✈"
    man_pilot_tone4 = "👨🏾✈"
    man_pilot_medium_dark_skin_tone = "👨🏾✈"
    man_pilot_tone5 = "👨🏿✈"
    man_pilot_dark_skin_tone = "👨🏿✈"
    woman_astronaut = "👩🚀"
    woman_astronaut_tone1 = "👩🏻🚀"
    woman_astronaut_light_skin_tone = "👩🏻🚀"
    woman_astronaut_tone2 = "👩🏼🚀"
    woman_astronaut_medium_light_skin_tone = "👩🏼🚀"
    woman_astronaut_tone3 = "👩🏽🚀"
    woman_astronaut_medium_skin_tone = "👩🏽🚀"
    woman_astronaut_tone4 = "👩🏾🚀"
    woman_astronaut_medium_dark_skin_tone = "👩🏾🚀"
    woman_astronaut_tone5 = "👩🏿🚀"
    woman_astronaut_dark_skin_tone = "👩🏿🚀"
    man_astronaut = "👨🚀"
    man_astronaut_tone1 = "👨🏻🚀"
    man_astronaut_light_skin_tone = "👨🏻🚀"
    man_astronaut_tone2 = "👨🏼🚀"
    man_astronaut_medium_light_skin_tone = "👨🏼🚀"
    man_astronaut_tone3 = "👨🏽🚀"
    man_astronaut_medium_skin_tone = "👨🏽🚀"
    man_astronaut_tone4 = "👨🏾🚀"
    man_astronaut_medium_dark_skin_tone = "👨🏾🚀"
    man_astronaut_tone5 = "👨🏿🚀"
    man_astronaut_dark_skin_tone = "👨🏿🚀"
    woman_judge = "👩⚖"
    woman_judge_tone1 = "👩🏻⚖"
    woman_judge_light_skin_tone = "👩🏻⚖"
    woman_judge_tone2 = "👩🏼⚖"
    woman_judge_medium_light_skin_tone = "👩🏼⚖"
    woman_judge_tone3 = "👩🏽⚖"
    woman_judge_medium_skin_tone = "👩🏽⚖"
    woman_judge_tone4 = "👩🏾⚖"
    woman_judge_medium_dark_skin_tone = "👩🏾⚖"
    woman_judge_tone5 = "👩🏿⚖"
    woman_judge_dark_skin_tone = "👩🏿⚖"
    man_judge = "👨⚖"
    man_judge_tone1 = "👨🏻⚖"
    man_judge_light_skin_tone = "👨🏻⚖"
    man_judge_tone2 = "👨🏼⚖"
    man_judge_medium_light_skin_tone = "👨🏼⚖"
    man_judge_tone3 = "👨🏽⚖"
    man_judge_medium_skin_tone = "👨🏽⚖"
    man_judge_tone4 = "👨🏾⚖"
    man_judge_medium_dark_skin_tone = "👨🏾⚖"
    man_judge_tone5 = "👨🏿⚖"
    man_judge_dark_skin_tone = "👨🏿⚖"
    bride_with_veil = "👰"
    bride_with_veil_tone1 = "👰🏻"
    bride_with_veil_tone2 = "👰🏼"
    bride_with_veil_tone3 = "👰🏽"
    bride_with_veil_tone4 = "👰🏾"
    bride_with_veil_tone5 = "👰🏿"
    man_in_tuxedo = "🤵"
    man_in_tuxedo_tone1 = "🤵🏻"
    tuxedo_tone1 = "🤵🏻"
    man_in_tuxedo_tone2 = "🤵🏼"
    tuxedo_tone2 = "🤵🏼"
    man_in_tuxedo_tone3 = "🤵🏽"
    tuxedo_tone3 = "🤵🏽"
    man_in_tuxedo_tone4 = "🤵🏾"
    tuxedo_tone4 = "🤵🏾"
    man_in_tuxedo_tone5 = "🤵🏿"
    tuxedo_tone5 = "🤵🏿"
    princess = "👸"
    princess_tone1 = "👸🏻"
    princess_tone2 = "👸🏼"
    princess_tone3 = "👸🏽"
    princess_tone4 = "👸🏾"
    princess_tone5 = "👸🏿"
    prince = "🤴"
    prince_tone1 = "🤴🏻"
    prince_tone2 = "🤴🏼"
    prince_tone3 = "🤴🏽"
    prince_tone4 = "🤴🏾"
    prince_tone5 = "🤴🏿"
    superhero = "🦸"
    superhero_tone1 = "🦸🏻"
    superhero_light_skin_tone = "🦸🏻"
    superhero_tone2 = "🦸🏼"
    superhero_medium_light_skin_tone = "🦸🏼"
    superhero_tone3 = "🦸🏽"
    superhero_medium_skin_tone = "🦸🏽"
    superhero_tone4 = "🦸🏾"
    superhero_medium_dark_skin_tone = "🦸🏾"
    superhero_tone5 = "🦸🏿"
    superhero_dark_skin_tone = "🦸🏿"
    woman_superhero = "🦸♀"
    woman_superhero_tone1 = "🦸🏻♀"
    woman_superhero_light_skin_tone = "🦸🏻♀"
    woman_superhero_tone2 = "🦸🏼♀"
    woman_superhero_medium_light_skin_tone = "🦸🏼♀"
    woman_superhero_tone3 = "🦸🏽♀"
    woman_superhero_medium_skin_tone = "🦸🏽♀"
    woman_superhero_tone4 = "🦸🏾♀"
    woman_superhero_medium_dark_skin_tone = "🦸🏾♀"
    woman_superhero_tone5 = "🦸🏿♀"
    woman_superhero_dark_skin_tone = "🦸🏿♀"
    man_superhero = "🦸♂"
    man_superhero_tone1 = "🦸🏻♂"
    man_superhero_light_skin_tone = "🦸🏻♂"
    man_superhero_tone2 = "🦸🏼♂"
    man_superhero_medium_light_skin_tone = "🦸🏼♂"
    man_superhero_tone3 = "🦸🏽♂"
    man_superhero_medium_skin_tone = "🦸🏽♂"
    man_superhero_tone4 = "🦸🏾♂"
    man_superhero_medium_dark_skin_tone = "🦸🏾♂"
    man_superhero_tone5 = "🦸🏿♂"
    man_superhero_dark_skin_tone = "🦸🏿♂"
    supervillain = "🦹"
    supervillain_tone1 = "🦹🏻"
    supervillain_light_skin_tone = "🦹🏻"
    supervillain_tone2 = "🦹🏼"
    supervillain_medium_light_skin_tone = "🦹🏼"
    supervillain_tone3 = "🦹🏽"
    supervillain_medium_skin_tone = "🦹🏽"
    supervillain_tone4 = "🦹🏾"
    supervillain_medium_dark_skin_tone = "🦹🏾"
    supervillain_tone5 = "🦹🏿"
    supervillain_dark_skin_tone = "🦹🏿"
    woman_supervillain = "🦹♀"
    woman_supervillain_tone1 = "🦹🏻♀"
    woman_supervillain_light_skin_tone = "🦹🏻♀"
    woman_supervillain_tone2 = "🦹🏼♀"
    woman_supervillain_medium_light_skin_tone = "🦹🏼♀"
    woman_supervillain_tone3 = "🦹🏽♀"
    woman_supervillain_medium_skin_tone = "🦹🏽♀"
    woman_supervillain_tone4 = "🦹🏾♀"
    woman_supervillain_medium_dark_skin_tone = "🦹🏾♀"
    woman_supervillain_tone5 = "🦹🏿♀"
    woman_supervillain_dark_skin_tone = "🦹🏿♀"
    man_supervillain = "🦹♂"
    man_supervillain_tone1 = "🦹🏻♂"
    man_supervillain_light_skin_tone = "🦹🏻♂"
    man_supervillain_tone2 = "🦹🏼♂"
    man_supervillain_medium_light_skin_tone = "🦹🏼♂"
    man_supervillain_tone3 = "🦹🏽♂"
    man_supervillain_medium_skin_tone = "🦹🏽♂"
    man_supervillain_tone4 = "🦹🏾♂"
    man_supervillain_medium_dark_skin_tone = "🦹🏾♂"
    man_supervillain_tone5 = "🦹🏿♂"
    man_supervillain_dark_skin_tone = "🦹🏿♂"
    mrs_claus = "🤶"
    mother_christmas = "🤶"
    mrs_claus_tone1 = "🤶🏻"
    mother_christmas_tone1 = "🤶🏻"
    mrs_claus_tone2 = "🤶🏼"
    mother_christmas_tone2 = "🤶🏼"
    mrs_claus_tone3 = "🤶🏽"
    mother_christmas_tone3 = "🤶🏽"
    mrs_claus_tone4 = "🤶🏾"
    mother_christmas_tone4 = "🤶🏾"
    mrs_claus_tone5 = "🤶🏿"
    mother_christmas_tone5 = "🤶🏿"
    santa = "🎅"
    santa_tone1 = "🎅🏻"
    santa_tone2 = "🎅🏼"
    santa_tone3 = "🎅🏽"
    santa_tone4 = "🎅🏾"
    santa_tone5 = "🎅🏿"
    mage = "🧙"
    mage_tone1 = "🧙🏻"
    mage_light_skin_tone = "🧙🏻"
    mage_tone2 = "🧙🏼"
    mage_medium_light_skin_tone = "🧙🏼"
    mage_tone3 = "🧙🏽"
    mage_medium_skin_tone = "🧙🏽"
    mage_tone4 = "🧙🏾"
    mage_medium_dark_skin_tone = "🧙🏾"
    mage_tone5 = "🧙🏿"
    mage_dark_skin_tone = "🧙🏿"
    woman_mage = "🧙♀"
    woman_mage_tone1 = "🧙🏻♀"
    woman_mage_light_skin_tone = "🧙🏻♀"
    woman_mage_tone2 = "🧙🏼♀"
    woman_mage_medium_light_skin_tone = "🧙🏼♀"
    woman_mage_tone3 = "🧙🏽♀"
    woman_mage_medium_skin_tone = "🧙🏽♀"
    woman_mage_tone4 = "🧙🏾♀"
    woman_mage_medium_dark_skin_tone = "🧙🏾♀"
    woman_mage_tone5 = "🧙🏿♀"
    woman_mage_dark_skin_tone = "🧙🏿♀"
    man_mage = "🧙♂"
    man_mage_tone1 = "🧙🏻♂"
    man_mage_light_skin_tone = "🧙🏻♂"
    man_mage_tone2 = "🧙🏼♂"
    man_mage_medium_light_skin_tone = "🧙🏼♂"
    man_mage_tone3 = "🧙🏽♂"
    man_mage_medium_skin_tone = "🧙🏽♂"
    man_mage_tone4 = "🧙🏾♂"
    man_mage_medium_dark_skin_tone = "🧙🏾♂"
    man_mage_tone5 = "🧙🏿♂"
    man_mage_dark_skin_tone = "🧙🏿♂"
    elf = "🧝"
    elf_tone1 = "🧝🏻"
    elf_light_skin_tone = "🧝🏻"
    elf_tone2 = "🧝🏼"
    elf_medium_light_skin_tone = "🧝🏼"
    elf_tone3 = "🧝🏽"
    elf_medium_skin_tone = "🧝🏽"
    elf_tone4 = "🧝🏾"
    elf_medium_dark_skin_tone = "🧝🏾"
    elf_tone5 = "🧝🏿"
    elf_dark_skin_tone = "🧝🏿"
    woman_elf = "🧝♀"
    woman_elf_tone1 = "🧝🏻♀"
    woman_elf_light_skin_tone = "🧝🏻♀"
    woman_elf_tone2 = "🧝🏼♀"
    woman_elf_medium_light_skin_tone = "🧝🏼♀"
    woman_elf_tone3 = "🧝🏽♀"
    woman_elf_medium_skin_tone = "🧝🏽♀"
    woman_elf_tone4 = "🧝🏾♀"
    woman_elf_medium_dark_skin_tone = "🧝🏾♀"
    woman_elf_tone5 = "🧝🏿♀"
    woman_elf_dark_skin_tone = "🧝🏿♀"
    man_elf = "🧝♂"
    man_elf_tone1 = "🧝🏻♂"
    man_elf_light_skin_tone = "🧝🏻♂"
    man_elf_tone2 = "🧝🏼♂"
    man_elf_medium_light_skin_tone = "🧝🏼♂"
    man_elf_tone3 = "🧝🏽♂"
    man_elf_medium_skin_tone = "🧝🏽♂"
    man_elf_tone4 = "🧝🏾♂"
    man_elf_medium_dark_skin_tone = "🧝🏾♂"
    man_elf_tone5 = "🧝🏿♂"
    man_elf_dark_skin_tone = "🧝🏿♂"
    vampire = "🧛"
    vampire_tone1 = "🧛🏻"
    vampire_light_skin_tone = "🧛🏻"
    vampire_tone2 = "🧛🏼"
    vampire_medium_light_skin_tone = "🧛🏼"
    vampire_tone3 = "🧛🏽"
    vampire_medium_skin_tone = "🧛🏽"
    vampire_tone4 = "🧛🏾"
    vampire_medium_dark_skin_tone = "🧛🏾"
    vampire_tone5 = "🧛🏿"
    vampire_dark_skin_tone = "🧛🏿"
    woman_vampire = "🧛♀"
    woman_vampire_tone1 = "🧛🏻♀"
    woman_vampire_light_skin_tone = "🧛🏻♀"
    woman_vampire_tone2 = "🧛🏼♀"
    woman_vampire_medium_light_skin_tone = "🧛🏼♀"
    woman_vampire_tone3 = "🧛🏽♀"
    woman_vampire_medium_skin_tone = "🧛🏽♀"
    woman_vampire_tone4 = "🧛🏾♀"
    woman_vampire_medium_dark_skin_tone = "🧛🏾♀"
    woman_vampire_tone5 = "🧛🏿♀"
    woman_vampire_dark_skin_tone = "🧛🏿♀"
    man_vampire = "🧛♂"
    man_vampire_tone1 = "🧛🏻♂"
    man_vampire_light_skin_tone = "🧛🏻♂"
    man_vampire_tone2 = "🧛🏼♂"
    man_vampire_medium_light_skin_tone = "🧛🏼♂"
    man_vampire_tone3 = "🧛🏽♂"
    man_vampire_medium_skin_tone = "🧛🏽♂"
    man_vampire_tone4 = "🧛🏾♂"
    man_vampire_medium_dark_skin_tone = "🧛🏾♂"
    man_vampire_tone5 = "🧛🏿♂"
    man_vampire_dark_skin_tone = "🧛🏿♂"
    zombie = "🧟"
    woman_zombie = "🧟♀"
    man_zombie = "🧟♂"
    genie = "🧞"
    woman_genie = "🧞♀"
    man_genie = "🧞♂"
    merperson = "🧜"
    merperson_tone1 = "🧜🏻"
    merperson_light_skin_tone = "🧜🏻"
    merperson_tone2 = "🧜🏼"
    merperson_medium_light_skin_tone = "🧜🏼"
    merperson_tone3 = "🧜🏽"
    merperson_medium_skin_tone = "🧜🏽"
    merperson_tone4 = "🧜🏾"
    merperson_medium_dark_skin_tone = "🧜🏾"
    merperson_tone5 = "🧜🏿"
    merperson_dark_skin_tone = "🧜🏿"
    mermaid = "🧜♀"
    mermaid_tone1 = "🧜🏻♀"
    mermaid_light_skin_tone = "🧜🏻♀"
    mermaid_tone2 = "🧜🏼♀"
    mermaid_medium_light_skin_tone = "🧜🏼♀"
    mermaid_tone3 = "🧜🏽♀"
    mermaid_medium_skin_tone = "🧜🏽♀"
    mermaid_tone4 = "🧜🏾♀"
    mermaid_medium_dark_skin_tone = "🧜🏾♀"
    mermaid_tone5 = "🧜🏿♀"
    mermaid_dark_skin_tone = "🧜🏿♀"
    merman = "🧜♂"
    merman_tone1 = "🧜🏻♂"
    merman_light_skin_tone = "🧜🏻♂"
    merman_tone2 = "🧜🏼♂"
    merman_medium_light_skin_tone = "🧜🏼♂"
    merman_tone3 = "🧜🏽♂"
    merman_medium_skin_tone = "🧜🏽♂"
    merman_tone4 = "🧜🏾♂"
    merman_medium_dark_skin_tone = "🧜🏾♂"
    merman_tone5 = "🧜🏿♂"
    merman_dark_skin_tone = "🧜🏿♂"
    fairy = "🧚"
    fairy_tone1 = "🧚🏻"
    fairy_light_skin_tone = "🧚🏻"
    fairy_tone2 = "🧚🏼"
    fairy_medium_light_skin_tone = "🧚🏼"
    fairy_tone3 = "🧚🏽"
    fairy_medium_skin_tone = "🧚🏽"
    fairy_tone4 = "🧚🏾"
    fairy_medium_dark_skin_tone = "🧚🏾"
    fairy_tone5 = "🧚🏿"
    fairy_dark_skin_tone = "🧚🏿"
    woman_fairy = "🧚♀"
    woman_fairy_tone1 = "🧚🏻♀"
    woman_fairy_light_skin_tone = "🧚🏻♀"
    woman_fairy_tone2 = "🧚🏼♀"
    woman_fairy_medium_light_skin_tone = "🧚🏼♀"
    woman_fairy_tone3 = "🧚🏽♀"
    woman_fairy_medium_skin_tone = "🧚🏽♀"
    woman_fairy_tone4 = "🧚🏾♀"
    woman_fairy_medium_dark_skin_tone = "🧚🏾♀"
    woman_fairy_tone5 = "🧚🏿♀"
    woman_fairy_dark_skin_tone = "🧚🏿♀"
    man_fairy = "🧚♂"
    man_fairy_tone1 = "🧚🏻♂"
    man_fairy_light_skin_tone = "🧚🏻♂"
    man_fairy_tone2 = "🧚🏼♂"
    man_fairy_medium_light_skin_tone = "🧚🏼♂"
    man_fairy_tone3 = "🧚🏽♂"
    man_fairy_medium_skin_tone = "🧚🏽♂"
    man_fairy_tone4 = "🧚🏾♂"
    man_fairy_medium_dark_skin_tone = "🧚🏾♂"
    man_fairy_tone5 = "🧚🏿♂"
    man_fairy_dark_skin_tone = "🧚🏿♂"
    angel = "👼"
    angel_tone1 = "👼🏻"
    angel_tone2 = "👼🏼"
    angel_tone3 = "👼🏽"
    angel_tone4 = "👼🏾"
    angel_tone5 = "👼🏿"
    pregnant_woman = "🤰"
    expecting_woman = "🤰"
    pregnant_woman_tone1 = "🤰🏻"
    expecting_woman_tone1 = "🤰🏻"
    pregnant_woman_tone2 = "🤰🏼"
    expecting_woman_tone2 = "🤰🏼"
    pregnant_woman_tone3 = "🤰🏽"
    expecting_woman_tone3 = "🤰🏽"
    pregnant_woman_tone4 = "🤰🏾"
    expecting_woman_tone4 = "🤰🏾"
    pregnant_woman_tone5 = "🤰🏿"
    expecting_woman_tone5 = "🤰🏿"
    breast_feeding = "🤱"
    breast_feeding_tone1 = "🤱🏻"
    breast_feeding_light_skin_tone = "🤱🏻"
    breast_feeding_tone2 = "🤱🏼"
    breast_feeding_medium_light_skin_tone = "🤱🏼"
    breast_feeding_tone3 = "🤱🏽"
    breast_feeding_medium_skin_tone = "🤱🏽"
    breast_feeding_tone4 = "🤱🏾"
    breast_feeding_medium_dark_skin_tone = "🤱🏾"
    breast_feeding_tone5 = "🤱🏿"
    breast_feeding_dark_skin_tone = "🤱🏿"
    person_bowing = "🙇"
    bow = "🙇"
    person_bowing_tone1 = "🙇🏻"
    bow_tone1 = "🙇🏻"
    person_bowing_tone2 = "🙇🏼"
    bow_tone2 = "🙇🏼"
    person_bowing_tone3 = "🙇🏽"
    bow_tone3 = "🙇🏽"
    person_bowing_tone4 = "🙇🏾"
    bow_tone4 = "🙇🏾"
    person_bowing_tone5 = "🙇🏿"
    bow_tone5 = "🙇🏿"
    woman_bowing = "🙇♀"
    woman_bowing_tone1 = "🙇🏻♀"
    woman_bowing_light_skin_tone = "🙇🏻♀"
    woman_bowing_tone2 = "🙇🏼♀"
    woman_bowing_medium_light_skin_tone = "🙇🏼♀"
    woman_bowing_tone3 = "🙇🏽♀"
    woman_bowing_medium_skin_tone = "🙇🏽♀"
    woman_bowing_tone4 = "🙇🏾♀"
    woman_bowing_medium_dark_skin_tone = "🙇🏾♀"
    woman_bowing_tone5 = "🙇🏿♀"
    woman_bowing_dark_skin_tone = "🙇🏿♀"
    man_bowing = "🙇♂"
    man_bowing_tone1 = "🙇🏻♂"
    man_bowing_light_skin_tone = "🙇🏻♂"
    man_bowing_tone2 = "🙇🏼♂"
    man_bowing_medium_light_skin_tone = "🙇🏼♂"
    man_bowing_tone3 = "🙇🏽♂"
    man_bowing_medium_skin_tone = "🙇🏽♂"
    man_bowing_tone4 = "🙇🏾♂"
    man_bowing_medium_dark_skin_tone = "🙇🏾♂"
    man_bowing_tone5 = "🙇🏿♂"
    man_bowing_dark_skin_tone = "🙇🏿♂"
    person_tipping_hand = "💁"
    information_desk_person = "💁"
    person_tipping_hand_tone1 = "💁🏻"
    information_desk_person_tone1 = "💁🏻"
    person_tipping_hand_tone2 = "💁🏼"
    information_desk_person_tone2 = "💁🏼"
    person_tipping_hand_tone3 = "💁🏽"
    information_desk_person_tone3 = "💁🏽"
    person_tipping_hand_tone4 = "💁🏾"
    information_desk_person_tone4 = "💁🏾"
    person_tipping_hand_tone5 = "💁🏿"
    information_desk_person_tone5 = "💁🏿"
    woman_tipping_hand = "💁♀"
    woman_tipping_hand_tone1 = "💁🏻♀"
    woman_tipping_hand_light_skin_tone = "💁🏻♀"
    woman_tipping_hand_tone2 = "💁🏼♀"
    woman_tipping_hand_medium_light_skin_tone = "💁🏼♀"
    woman_tipping_hand_tone3 = "💁🏽♀"
    woman_tipping_hand_medium_skin_tone = "💁🏽♀"
    woman_tipping_hand_tone4 = "💁🏾♀"
    woman_tipping_hand_medium_dark_skin_tone = "💁🏾♀"
    woman_tipping_hand_tone5 = "💁🏿♀"
    woman_tipping_hand_dark_skin_tone = "💁🏿♀"
    man_tipping_hand = "💁♂"
    man_tipping_hand_tone1 = "💁🏻♂"
    man_tipping_hand_light_skin_tone = "💁🏻♂"
    man_tipping_hand_tone2 = "💁🏼♂"
    man_tipping_hand_medium_light_skin_tone = "💁🏼♂"
    man_tipping_hand_tone3 = "💁🏽♂"
    man_tipping_hand_medium_skin_tone = "💁🏽♂"
    man_tipping_hand_tone4 = "💁🏾♂"
    man_tipping_hand_medium_dark_skin_tone = "💁🏾♂"
    man_tipping_hand_tone5 = "💁🏿♂"
    man_tipping_hand_dark_skin_tone = "💁🏿♂"
    person_gesturing_no = "🙅"
    no_good = "🙅"
    person_gesturing_no_tone1 = "🙅🏻"
    no_good_tone1 = "🙅🏻"
    person_gesturing_no_tone2 = "🙅🏼"
    no_good_tone2 = "🙅🏼"
    person_gesturing_no_tone3 = "🙅🏽"
    no_good_tone3 = "🙅🏽"
    person_gesturing_no_tone4 = "🙅🏾"
    no_good_tone4 = "🙅🏾"
    person_gesturing_no_tone5 = "🙅🏿"
    no_good_tone5 = "🙅🏿"
    woman_gesturing_no = "🙅♀"
    woman_gesturing_no_tone1 = "🙅🏻♀"
    woman_gesturing_no_light_skin_tone = "🙅🏻♀"
    woman_gesturing_no_tone2 = "🙅🏼♀"
    woman_gesturing_no_medium_light_skin_tone = "🙅🏼♀"
    woman_gesturing_no_tone3 = "🙅🏽♀"
    woman_gesturing_no_medium_skin_tone = "🙅🏽♀"
    woman_gesturing_no_tone4 = "🙅🏾♀"
    woman_gesturing_no_medium_dark_skin_tone = "🙅🏾♀"
    woman_gesturing_no_tone5 = "🙅🏿♀"
    woman_gesturing_no_dark_skin_tone = "🙅🏿♀"
    man_gesturing_no = "🙅♂"
    man_gesturing_no_tone1 = "🙅🏻♂"
    man_gesturing_no_light_skin_tone = "🙅🏻♂"
    man_gesturing_no_tone2 = "🙅🏼♂"
    man_gesturing_no_medium_light_skin_tone = "🙅🏼♂"
    man_gesturing_no_tone3 = "🙅🏽♂"
    man_gesturing_no_medium_skin_tone = "🙅🏽♂"
    man_gesturing_no_tone4 = "🙅🏾♂"
    man_gesturing_no_medium_dark_skin_tone = "🙅🏾♂"
    man_gesturing_no_tone5 = "🙅🏿♂"
    man_gesturing_no_dark_skin_tone = "🙅🏿♂"
    person_gesturing_ok = "🙆"
    ok_woman = "🙆"
    person_gesturing_ok_tone1 = "🙆🏻"
    ok_woman_tone1 = "🙆🏻"
    person_gesturing_ok_tone2 = "🙆🏼"
    ok_woman_tone2 = "🙆🏼"
    person_gesturing_ok_tone3 = "🙆🏽"
    ok_woman_tone3 = "🙆🏽"
    person_gesturing_ok_tone4 = "🙆🏾"
    ok_woman_tone4 = "🙆🏾"
    person_gesturing_ok_tone5 = "🙆🏿"
    ok_woman_tone5 = "🙆🏿"
    woman_gesturing_ok = "🙆♀"
    woman_gesturing_ok_tone1 = "🙆🏻♀"
    woman_gesturing_ok_light_skin_tone = "🙆🏻♀"
    woman_gesturing_ok_tone2 = "🙆🏼♀"
    woman_gesturing_ok_medium_light_skin_tone = "🙆🏼♀"
    woman_gesturing_ok_tone3 = "🙆🏽♀"
    woman_gesturing_ok_medium_skin_tone = "🙆🏽♀"
    woman_gesturing_ok_tone4 = "🙆🏾♀"
    woman_gesturing_ok_medium_dark_skin_tone = "🙆🏾♀"
    woman_gesturing_ok_tone5 = "🙆🏿♀"
    woman_gesturing_ok_dark_skin_tone = "🙆🏿♀"
    man_gesturing_ok = "🙆♂"
    man_gesturing_ok_tone1 = "🙆🏻♂"
    man_gesturing_ok_light_skin_tone = "🙆🏻♂"
    man_gesturing_ok_tone2 = "🙆🏼♂"
    man_gesturing_ok_medium_light_skin_tone = "🙆🏼♂"
    man_gesturing_ok_tone3 = "🙆🏽♂"
    man_gesturing_ok_medium_skin_tone = "🙆🏽♂"
    man_gesturing_ok_tone4 = "🙆🏾♂"
    man_gesturing_ok_medium_dark_skin_tone = "🙆🏾♂"
    man_gesturing_ok_tone5 = "🙆🏿♂"
    man_gesturing_ok_dark_skin_tone = "🙆🏿♂"
    person_raising_hand = "🙋"
    raising_hand = "🙋"
    person_raising_hand_tone1 = "🙋🏻"
    raising_hand_tone1 = "🙋🏻"
    person_raising_hand_tone2 = "🙋🏼"
    raising_hand_tone2 = "🙋🏼"
    person_raising_hand_tone3 = "🙋🏽"
    raising_hand_tone3 = "🙋🏽"
    person_raising_hand_tone4 = "🙋🏾"
    raising_hand_tone4 = "🙋🏾"
    person_raising_hand_tone5 = "🙋🏿"
    raising_hand_tone5 = "🙋🏿"
    woman_raising_hand = "🙋♀"
    woman_raising_hand_tone1 = "🙋🏻♀"
    woman_raising_hand_light_skin_tone = "🙋🏻♀"
    woman_raising_hand_tone2 = "🙋🏼♀"
    woman_raising_hand_medium_light_skin_tone = "🙋🏼♀"
    woman_raising_hand_tone3 = "🙋🏽♀"
    woman_raising_hand_medium_skin_tone = "🙋🏽♀"
    woman_raising_hand_tone4 = "🙋🏾♀"
    woman_raising_hand_medium_dark_skin_tone = "🙋🏾♀"
    woman_raising_hand_tone5 = "🙋🏿♀"
    woman_raising_hand_dark_skin_tone = "🙋🏿♀"
    man_raising_hand = "🙋♂"
    man_raising_hand_tone1 = "🙋🏻♂"
    man_raising_hand_light_skin_tone = "🙋🏻♂"
    man_raising_hand_tone2 = "🙋🏼♂"
    man_raising_hand_medium_light_skin_tone = "🙋🏼♂"
    man_raising_hand_tone3 = "🙋🏽♂"
    man_raising_hand_medium_skin_tone = "🙋🏽♂"
    man_raising_hand_tone4 = "🙋🏾♂"
    man_raising_hand_medium_dark_skin_tone = "🙋🏾♂"
    man_raising_hand_tone5 = "🙋🏿♂"
    man_raising_hand_dark_skin_tone = "🙋🏿♂"
    deaf_person = "🧏"
    deaf_person_tone1 = "🧏🏻"
    deaf_person_light_skin_tone = "🧏🏻"
    deaf_person_tone2 = "🧏🏼"
    deaf_person_medium_light_skin_tone = "🧏🏼"
    deaf_person_tone3 = "🧏🏽"
    deaf_person_medium_skin_tone = "🧏🏽"
    deaf_person_tone4 = "🧏🏾"
    deaf_person_medium_dark_skin_tone = "🧏🏾"
    deaf_person_tone5 = "🧏🏿"
    deaf_person_dark_skin_tone = "🧏🏿"
    deaf_woman = "🧏♀"
    deaf_woman_tone1 = "🧏🏻♀"
    deaf_woman_light_skin_tone = "🧏🏻♀"
    deaf_woman_tone2 = "🧏🏼♀"
    deaf_woman_medium_light_skin_tone = "🧏🏼♀"
    deaf_woman_tone3 = "🧏🏽♀"
    deaf_woman_medium_skin_tone = "🧏🏽♀"
    deaf_woman_tone4 = "🧏🏾♀"
    deaf_woman_medium_dark_skin_tone = "🧏🏾♀"
    deaf_woman_tone5 = "🧏🏿♀"
    deaf_woman_dark_skin_tone = "🧏🏿♀"
    deaf_man = "🧏♂"
    deaf_man_tone1 = "🧏🏻♂"
    deaf_man_light_skin_tone = "🧏🏻♂"
    deaf_man_tone2 = "🧏🏼♂"
    deaf_man_medium_light_skin_tone = "🧏🏼♂"
    deaf_man_tone3 = "🧏🏽♂"
    deaf_man_medium_skin_tone = "🧏🏽♂"
    deaf_man_tone4 = "🧏🏾♂"
    deaf_man_medium_dark_skin_tone = "🧏🏾♂"
    deaf_man_tone5 = "🧏🏿♂"
    deaf_man_dark_skin_tone = "🧏🏿♂"
    person_facepalming = "🤦"
    face_palm = "🤦"
    facepalm = "🤦"
    person_facepalming_tone1 = "🤦🏻"
    face_palm_tone1 = "🤦🏻"
    facepalm_tone1 = "🤦🏻"
    person_facepalming_tone2 = "🤦🏼"
    face_palm_tone2 = "🤦🏼"
    facepalm_tone2 = "🤦🏼"
    person_facepalming_tone3 = "🤦🏽"
    face_palm_tone3 = "🤦🏽"
    facepalm_tone3 = "🤦🏽"
    person_facepalming_tone4 = "🤦🏾"
    face_palm_tone4 = "🤦🏾"
    facepalm_tone4 = "🤦🏾"
    person_facepalming_tone5 = "🤦🏿"
    face_palm_tone5 = "🤦🏿"
    facepalm_tone5 = "🤦🏿"
    woman_facepalming = "🤦♀"
    woman_facepalming_tone1 = "🤦🏻♀"
    woman_facepalming_light_skin_tone = "🤦🏻♀"
    woman_facepalming_tone2 = "🤦🏼♀"
    woman_facepalming_medium_light_skin_tone = "🤦🏼♀"
    woman_facepalming_tone3 = "🤦🏽♀"
    woman_facepalming_medium_skin_tone = "🤦🏽♀"
    woman_facepalming_tone4 = "🤦🏾♀"
    woman_facepalming_medium_dark_skin_tone = "🤦🏾♀"
    woman_facepalming_tone5 = "🤦🏿♀"
    woman_facepalming_dark_skin_tone = "🤦🏿♀"
    man_facepalming = "🤦♂"
    man_facepalming_tone1 = "🤦🏻♂"
    man_facepalming_light_skin_tone = "🤦🏻♂"
    man_facepalming_tone2 = "🤦🏼♂"
    man_facepalming_medium_light_skin_tone = "🤦🏼♂"
    man_facepalming_tone3 = "🤦🏽♂"
    man_facepalming_medium_skin_tone = "🤦🏽♂"
    man_facepalming_tone4 = "🤦🏾♂"
    man_facepalming_medium_dark_skin_tone = "🤦🏾♂"
    man_facepalming_tone5 = "🤦🏿♂"
    man_facepalming_dark_skin_tone = "🤦🏿♂"
    person_shrugging = "🤷"
    shrug = "🤷"
    person_shrugging_tone1 = "🤷🏻"
    shrug_tone1 = "🤷🏻"
    person_shrugging_tone2 = "🤷🏼"
    shrug_tone2 = "🤷🏼"
    person_shrugging_tone3 = "🤷🏽"
    shrug_tone3 = "🤷🏽"
    person_shrugging_tone4 = "🤷🏾"
    shrug_tone4 = "🤷🏾"
    person_shrugging_tone5 = "🤷🏿"
    shrug_tone5 = "🤷🏿"
    woman_shrugging = "🤷♀"
    woman_shrugging_tone1 = "🤷🏻♀"
    woman_shrugging_light_skin_tone = "🤷🏻♀"
    woman_shrugging_tone2 = "🤷🏼♀"
    woman_shrugging_medium_light_skin_tone = "🤷🏼♀"
    woman_shrugging_tone3 = "🤷🏽♀"
    woman_shrugging_medium_skin_tone = "🤷🏽♀"
    woman_shrugging_tone4 = "🤷🏾♀"
    woman_shrugging_medium_dark_skin_tone = "🤷🏾♀"
    woman_shrugging_tone5 = "🤷🏿♀"
    woman_shrugging_dark_skin_tone = "🤷🏿♀"
    man_shrugging = "🤷♂"
    man_shrugging_tone1 = "🤷🏻♂"
    man_shrugging_light_skin_tone = "🤷🏻♂"
    man_shrugging_tone2 = "🤷🏼♂"
    man_shrugging_medium_light_skin_tone = "🤷🏼♂"
    man_shrugging_tone3 = "🤷🏽♂"
    man_shrugging_medium_skin_tone = "🤷🏽♂"
    man_shrugging_tone4 = "🤷🏾♂"
    man_shrugging_medium_dark_skin_tone = "🤷🏾♂"
    man_shrugging_tone5 = "🤷🏿♂"
    man_shrugging_dark_skin_tone = "🤷🏿♂"
    person_pouting = "🙎"
    person_with_pouting_face = "🙎"
    person_pouting_tone1 = "🙎🏻"
    person_with_pouting_face_tone1 = "🙎🏻"
    person_pouting_tone2 = "🙎🏼"
    person_with_pouting_face_tone2 = "🙎🏼"
    person_pouting_tone3 = "🙎🏽"
    person_with_pouting_face_tone3 = "🙎🏽"
    person_pouting_tone4 = "🙎🏾"
    person_with_pouting_face_tone4 = "🙎🏾"
    person_pouting_tone5 = "🙎🏿"
    person_with_pouting_face_tone5 = "🙎🏿"
    woman_pouting = "🙎♀"
    woman_pouting_tone1 = "🙎🏻♀"
    woman_pouting_light_skin_tone = "🙎🏻♀"
    woman_pouting_tone2 = "🙎🏼♀"
    woman_pouting_medium_light_skin_tone = "🙎🏼♀"
    woman_pouting_tone3 = "🙎🏽♀"
    woman_pouting_medium_skin_tone = "🙎🏽♀"
    woman_pouting_tone4 = "🙎🏾♀"
    woman_pouting_medium_dark_skin_tone = "🙎🏾♀"
    woman_pouting_tone5 = "🙎🏿♀"
    woman_pouting_dark_skin_tone = "🙎🏿♀"
    man_pouting = "🙎♂"
    man_pouting_tone1 = "🙎🏻♂"
    man_pouting_light_skin_tone = "🙎🏻♂"
    man_pouting_tone2 = "🙎🏼♂"
    man_pouting_medium_light_skin_tone = "🙎🏼♂"
    man_pouting_tone3 = "🙎🏽♂"
    man_pouting_medium_skin_tone = "🙎🏽♂"
    man_pouting_tone4 = "🙎🏾♂"
    man_pouting_medium_dark_skin_tone = "🙎🏾♂"
    man_pouting_tone5 = "🙎🏿♂"
    man_pouting_dark_skin_tone = "🙎🏿♂"
    person_frowning = "🙍"
    person_frowning_tone1 = "🙍🏻"
    person_frowning_tone2 = "🙍🏼"
    person_frowning_tone3 = "🙍🏽"
    person_frowning_tone4 = "🙍🏾"
    person_frowning_tone5 = "🙍🏿"
    woman_frowning = "🙍♀"
    woman_frowning_tone1 = "🙍🏻♀"
    woman_frowning_light_skin_tone = "🙍🏻♀"
    woman_frowning_tone2 = "🙍🏼♀"
    woman_frowning_medium_light_skin_tone = "🙍🏼♀"
    woman_frowning_tone3 = "🙍🏽♀"
    woman_frowning_medium_skin_tone = "🙍🏽♀"
    woman_frowning_tone4 = "🙍🏾♀"
    woman_frowning_medium_dark_skin_tone = "🙍🏾♀"
    woman_frowning_tone5 = "🙍🏿♀"
    woman_frowning_dark_skin_tone = "🙍🏿♀"
    man_frowning = "🙍♂"
    man_frowning_tone1 = "🙍🏻♂"
    man_frowning_light_skin_tone = "🙍🏻♂"
    man_frowning_tone2 = "🙍🏼♂"
    man_frowning_medium_light_skin_tone = "🙍🏼♂"
    man_frowning_tone3 = "🙍🏽♂"
    man_frowning_medium_skin_tone = "🙍🏽♂"
    man_frowning_tone4 = "🙍🏾♂"
    man_frowning_medium_dark_skin_tone = "🙍🏾♂"
    man_frowning_tone5 = "🙍🏿♂"
    man_frowning_dark_skin_tone = "🙍🏿♂"
    person_getting_haircut = "💇"
    haircut = "💇"
    person_getting_haircut_tone1 = "💇🏻"
    haircut_tone1 = "💇🏻"
    person_getting_haircut_tone2 = "💇🏼"
    haircut_tone2 = "💇🏼"
    person_getting_haircut_tone3 = "💇🏽"
    haircut_tone3 = "💇🏽"
    person_getting_haircut_tone4 = "💇🏾"
    haircut_tone4 = "💇🏾"
    person_getting_haircut_tone5 = "💇🏿"
    haircut_tone5 = "💇🏿"
    woman_getting_haircut = "💇♀"
    woman_getting_haircut_tone1 = "💇🏻♀"
    woman_getting_haircut_light_skin_tone = "💇🏻♀"
    woman_getting_haircut_tone2 = "💇🏼♀"
    woman_getting_haircut_medium_light_skin_tone = "💇🏼♀"
    woman_getting_haircut_tone3 = "💇🏽♀"
    woman_getting_haircut_medium_skin_tone = "💇🏽♀"
    woman_getting_haircut_tone4 = "💇🏾♀"
    woman_getting_haircut_medium_dark_skin_tone = "💇🏾♀"
    woman_getting_haircut_tone5 = "💇🏿♀"
    woman_getting_haircut_dark_skin_tone = "💇🏿♀"
    man_getting_haircut = "💇♂"
    man_getting_haircut_tone1 = "💇🏻♂"
    man_getting_haircut_light_skin_tone = "💇🏻♂"
    man_getting_haircut_tone2 = "💇🏼♂"
    man_getting_haircut_medium_light_skin_tone = "💇🏼♂"
    man_getting_haircut_tone3 = "💇🏽♂"
    man_getting_haircut_medium_skin_tone = "💇🏽♂"
    man_getting_haircut_tone4 = "💇🏾♂"
    man_getting_haircut_medium_dark_skin_tone = "💇🏾♂"
    man_getting_haircut_tone5 = "💇🏿♂"
    man_getting_haircut_dark_skin_tone = "💇🏿♂"
    person_getting_massage = "💆"
    massage = "💆"
    person_getting_massage_tone1 = "💆🏻"
    massage_tone1 = "💆🏻"
    person_getting_massage_tone2 = "💆🏼"
    massage_tone2 = "💆🏼"
    person_getting_massage_tone3 = "💆🏽"
    massage_tone3 = "💆🏽"
    person_getting_massage_tone4 = "💆🏾"
    massage_tone4 = "💆🏾"
    person_getting_massage_tone5 = "💆🏿"
    massage_tone5 = "💆🏿"
    woman_getting_face_massage = "💆♀"
    woman_getting_face_massage_tone1 = "💆🏻♀"
    woman_getting_face_massage_light_skin_tone = "💆🏻♀"
    woman_getting_face_massage_tone2 = "💆🏼♀"
    woman_getting_face_massage_medium_light_skin_tone = "💆🏼♀"
    woman_getting_face_massage_tone3 = "💆🏽♀"
    woman_getting_face_massage_medium_skin_tone = "💆🏽♀"
    woman_getting_face_massage_tone4 = "💆🏾♀"
    woman_getting_face_massage_medium_dark_skin_tone = "💆🏾♀"
    woman_getting_face_massage_tone5 = "💆🏿♀"
    woman_getting_face_massage_dark_skin_tone = "💆🏿♀"
    man_getting_face_massage = "💆♂"
    man_getting_face_massage_tone1 = "💆🏻♂"
    man_getting_face_massage_light_skin_tone = "💆🏻♂"
    man_getting_face_massage_tone2 = "💆🏼♂"
    man_getting_face_massage_medium_light_skin_tone = "💆🏼♂"
    man_getting_face_massage_tone3 = "💆🏽♂"
    man_getting_face_massage_medium_skin_tone = "💆🏽♂"
    man_getting_face_massage_tone4 = "💆🏾♂"
    man_getting_face_massage_medium_dark_skin_tone = "💆🏾♂"
    man_getting_face_massage_tone5 = "💆🏿♂"
    man_getting_face_massage_dark_skin_tone = "💆🏿♂"
    person_in_steamy_room = "🧖"
    person_in_steamy_room_tone1 = "🧖🏻"
    person_in_steamy_room_light_skin_tone = "🧖🏻"
    person_in_steamy_room_tone2 = "🧖🏼"
    person_in_steamy_room_medium_light_skin_tone = "🧖🏼"
    person_in_steamy_room_tone3 = "🧖🏽"
    person_in_steamy_room_medium_skin_tone = "🧖🏽"
    person_in_steamy_room_tone4 = "🧖🏾"
    person_in_steamy_room_medium_dark_skin_tone = "🧖🏾"
    person_in_steamy_room_tone5 = "🧖🏿"
    person_in_steamy_room_dark_skin_tone = "🧖🏿"
    woman_in_steamy_room = "🧖♀"
    woman_in_steamy_room_tone1 = "🧖🏻♀"
    woman_in_steamy_room_light_skin_tone = "🧖🏻♀"
    woman_in_steamy_room_tone2 = "🧖🏼♀"
    woman_in_steamy_room_medium_light_skin_tone = "🧖🏼♀"
    woman_in_steamy_room_tone3 = "🧖🏽♀"
    woman_in_steamy_room_medium_skin_tone = "🧖🏽♀"
    woman_in_steamy_room_tone4 = "🧖🏾♀"
    woman_in_steamy_room_medium_dark_skin_tone = "🧖🏾♀"
    woman_in_steamy_room_tone5 = "🧖🏿♀"
    woman_in_steamy_room_dark_skin_tone = "🧖🏿♀"
    man_in_steamy_room = "🧖♂"
    man_in_steamy_room_tone1 = "🧖🏻♂"
    man_in_steamy_room_light_skin_tone = "🧖🏻♂"
    man_in_steamy_room_tone2 = "🧖🏼♂"
    man_in_steamy_room_medium_light_skin_tone = "🧖🏼♂"
    man_in_steamy_room_tone3 = "🧖🏽♂"
    man_in_steamy_room_medium_skin_tone = "🧖🏽♂"
    man_in_steamy_room_tone4 = "🧖🏾♂"
    man_in_steamy_room_medium_dark_skin_tone = "🧖🏾♂"
    man_in_steamy_room_tone5 = "🧖🏿♂"
    man_in_steamy_room_dark_skin_tone = "🧖🏿♂"
    nail_care = "💅"
    nail_care_tone1 = "💅🏻"
    nail_care_tone2 = "💅🏼"
    nail_care_tone3 = "💅🏽"
    nail_care_tone4 = "💅🏾"
    nail_care_tone5 = "💅🏿"
    selfie = "🤳"
    selfie_tone1 = "🤳🏻"
    selfie_tone2 = "🤳🏼"
    selfie_tone3 = "🤳🏽"
    selfie_tone4 = "🤳🏾"
    selfie_tone5 = "🤳🏿"
    dancer = "💃"
    dancer_tone1 = "💃🏻"
    dancer_tone2 = "💃🏼"
    dancer_tone3 = "💃🏽"
    dancer_tone4 = "💃🏾"
    dancer_tone5 = "💃🏿"
    man_dancing = "🕺"
    male_dancer = "🕺"
    man_dancing_tone1 = "🕺🏻"
    male_dancer_tone1 = "🕺🏻"
    man_dancing_tone2 = "🕺🏼"
    male_dancer_tone2 = "🕺🏼"
    man_dancing_tone3 = "🕺🏽"
    male_dancer_tone3 = "🕺🏽"
    man_dancing_tone5 = "🕺🏿"
    male_dancer_tone5 = "🕺🏿"
    man_dancing_tone4 = "🕺🏾"
    male_dancer_tone4 = "🕺🏾"
    people_with_bunny_ears_partying = "👯"
    dancers = "👯"
    women_with_bunny_ears_partying = "👯♀"
    men_with_bunny_ears_partying = "👯♂"
    levitate = "🕴"
    man_in_business_suit_levitating = "🕴"
    levitate_tone1 = "🕴🏻"
    man_in_business_suit_levitating_tone1 = "🕴🏻"
    man_in_business_suit_levitating_light_skin_tone = "🕴🏻"
    levitate_tone2 = "🕴🏼"
    man_in_business_suit_levitating_tone2 = "🕴🏼"
    man_in_business_suit_levitating_medium_light_skin_tone = "🕴🏼"
    levitate_tone3 = "🕴🏽"
    man_in_business_suit_levitating_tone3 = "🕴🏽"
    man_in_business_suit_levitating_medium_skin_tone = "🕴🏽"
    levitate_tone4 = "🕴🏾"
    man_in_business_suit_levitating_tone4 = "🕴🏾"
    man_in_business_suit_levitating_medium_dark_skin_tone = "🕴🏾"
    levitate_tone5 = "🕴🏿"
    man_in_business_suit_levitating_tone5 = "🕴🏿"
    man_in_business_suit_levitating_dark_skin_tone = "🕴🏿"
    person_walking = "🚶"
    walking = "🚶"
    person_walking_tone1 = "🚶🏻"
    walking_tone1 = "🚶🏻"
    person_walking_tone2 = "🚶🏼"
    walking_tone2 = "🚶🏼"
    person_walking_tone3 = "🚶🏽"
    walking_tone3 = "🚶🏽"
    person_walking_tone4 = "🚶🏾"
    walking_tone4 = "🚶🏾"
    person_walking_tone5 = "🚶🏿"
    walking_tone5 = "🚶🏿"
    woman_walking = "🚶♀"
    woman_walking_tone1 = "🚶🏻♀"
    woman_walking_light_skin_tone = "🚶🏻♀"
    woman_walking_tone2 = "🚶🏼♀"
    woman_walking_medium_light_skin_tone = "🚶🏼♀"
    woman_walking_tone3 = "🚶🏽♀"
    woman_walking_medium_skin_tone = "🚶🏽♀"
    woman_walking_tone4 = "🚶🏾♀"
    woman_walking_medium_dark_skin_tone = "🚶🏾♀"
    woman_walking_tone5 = "🚶🏿♀"
    woman_walking_dark_skin_tone = "🚶🏿♀"
    man_walking = "🚶♂"
    man_walking_tone1 = "🚶🏻♂"
    man_walking_light_skin_tone = "🚶🏻♂"
    man_walking_tone2 = "🚶🏼♂"
    man_walking_medium_light_skin_tone = "🚶🏼♂"
    man_walking_tone3 = "🚶🏽♂"
    man_walking_medium_skin_tone = "🚶🏽♂"
    man_walking_tone4 = "🚶🏾♂"
    man_walking_medium_dark_skin_tone = "🚶🏾♂"
    man_walking_tone5 = "🚶🏿♂"
    man_walking_dark_skin_tone = "🚶🏿♂"
    person_running = "🏃"
    runner = "🏃"
    person_running_tone1 = "🏃🏻"
    runner_tone1 = "🏃🏻"
    person_running_tone2 = "🏃🏼"
    runner_tone2 = "🏃🏼"
    person_running_tone3 = "🏃🏽"
    runner_tone3 = "🏃🏽"
    person_running_tone4 = "🏃🏾"
    runner_tone4 = "🏃🏾"
    person_running_tone5 = "🏃🏿"
    runner_tone5 = "🏃🏿"
    woman_running = "🏃♀"
    woman_running_tone1 = "🏃🏻♀"
    woman_running_light_skin_tone = "🏃🏻♀"
    woman_running_tone2 = "🏃🏼♀"
    woman_running_medium_light_skin_tone = "🏃🏼♀"
    woman_running_tone3 = "🏃🏽♀"
    woman_running_medium_skin_tone = "🏃🏽♀"
    woman_running_tone4 = "🏃🏾♀"
    woman_running_medium_dark_skin_tone = "🏃🏾♀"
    woman_running_tone5 = "🏃🏿♀"
    woman_running_dark_skin_tone = "🏃🏿♀"
    man_running = "🏃♂"
    man_running_tone1 = "🏃🏻♂"
    man_running_light_skin_tone = "🏃🏻♂"
    man_running_tone2 = "🏃🏼♂"
    man_running_medium_light_skin_tone = "🏃🏼♂"
    man_running_tone3 = "🏃🏽♂"
    man_running_medium_skin_tone = "🏃🏽♂"
    man_running_tone4 = "🏃🏾♂"
    man_running_medium_dark_skin_tone = "🏃🏾♂"
    man_running_tone5 = "🏃🏿♂"
    man_running_dark_skin_tone = "🏃🏿♂"
    person_standing = "🧍"
    person_standing_tone1 = "🧍🏻"
    person_standing_light_skin_tone = "🧍🏻"
    person_standing_tone2 = "🧍🏼"
    person_standing_medium_light_skin_tone = "🧍🏼"
    person_standing_tone3 = "🧍🏽"
    person_standing_medium_skin_tone = "🧍🏽"
    person_standing_tone4 = "🧍🏾"
    person_standing_medium_dark_skin_tone = "🧍🏾"
    person_standing_tone5 = "🧍🏿"
    person_standing_dark_skin_tone = "🧍🏿"
    woman_standing = "🧍♀"
    woman_standing_tone1 = "🧍🏻♀"
    woman_standing_light_skin_tone = "🧍🏻♀"
    woman_standing_tone2 = "🧍🏼♀"
    woman_standing_medium_light_skin_tone = "🧍🏼♀"
    woman_standing_tone3 = "🧍🏽♀"
    woman_standing_medium_skin_tone = "🧍🏽♀"
    woman_standing_tone4 = "🧍🏾♀"
    woman_standing_medium_dark_skin_tone = "🧍🏾♀"
    woman_standing_tone5 = "🧍🏿♀"
    woman_standing_dark_skin_tone = "🧍🏿♀"
    man_standing = "🧍♂"
    man_standing_tone1 = "🧍🏻♂"
    man_standing_light_skin_tone = "🧍🏻♂"
    man_standing_tone2 = "🧍🏼♂"
    man_standing_medium_light_skin_tone = "🧍🏼♂"
    man_standing_tone3 = "🧍🏽♂"
    man_standing_medium_skin_tone = "🧍🏽♂"
    man_standing_tone4 = "🧍🏾♂"
    man_standing_medium_dark_skin_tone = "🧍🏾♂"
    man_standing_tone5 = "🧍🏿♂"
    man_standing_dark_skin_tone = "🧍🏿♂"
    person_kneeling = "🧎"
    person_kneeling_tone1 = "🧎🏻"
    person_kneeling_light_skin_tone = "🧎🏻"
    person_kneeling_tone2 = "🧎🏼"
    person_kneeling_medium_light_skin_tone = "🧎🏼"
    person_kneeling_tone3 = "🧎🏽"
    person_kneeling_medium_skin_tone = "🧎🏽"
    person_kneeling_tone4 = "🧎🏾"
    person_kneeling_medium_dark_skin_tone = "🧎🏾"
    person_kneeling_tone5 = "🧎🏿"
    person_kneeling_dark_skin_tone = "🧎🏿"
    woman_kneeling = "🧎♀"
    woman_kneeling_tone1 = "🧎🏻♀"
    woman_kneeling_light_skin_tone = "🧎🏻♀"
    woman_kneeling_tone2 = "🧎🏼♀"
    woman_kneeling_medium_light_skin_tone = "🧎🏼♀"
    woman_kneeling_tone3 = "🧎🏽♀"
    woman_kneeling_medium_skin_tone = "🧎🏽♀"
    woman_kneeling_tone4 = "🧎🏾♀"
    woman_kneeling_medium_dark_skin_tone = "🧎🏾♀"
    woman_kneeling_tone5 = "🧎🏿♀"
    woman_kneeling_dark_skin_tone = "🧎🏿♀"
    man_kneeling = "🧎♂"
    man_kneeling_tone1 = "🧎🏻♂"
    man_kneeling_light_skin_tone = "🧎🏻♂"
    man_kneeling_tone2 = "🧎🏼♂"
    man_kneeling_medium_light_skin_tone = "🧎🏼♂"
    man_kneeling_tone3 = "🧎🏽♂"
    man_kneeling_medium_skin_tone = "🧎🏽♂"
    man_kneeling_tone4 = "🧎🏾♂"
    man_kneeling_medium_dark_skin_tone = "🧎🏾♂"
    man_kneeling_tone5 = "🧎🏿♂"
    man_kneeling_dark_skin_tone = "🧎🏿♂"
    woman_with_probing_cane = "👩🦯"
    woman_with_probing_cane_tone1 = "👩🏻🦯"
    woman_with_probing_cane_light_skin_tone = "👩🏻🦯"
    woman_with_probing_cane_tone2 = "👩🏼🦯"
    woman_with_probing_cane_medium_light_skin_tone = "👩🏼🦯"
    woman_with_probing_cane_tone3 = "👩🏽🦯"
    woman_with_probing_cane_medium_skin_tone = "👩🏽🦯"
    woman_with_probing_cane_tone4 = "👩🏾🦯"
    woman_with_probing_cane_medium_dark_skin_tone = "👩🏾🦯"
    woman_with_probing_cane_tone5 = "👩🏿🦯"
    woman_with_probing_cane_dark_skin_tone = "👩🏿🦯"
    man_with_probing_cane = "👨🦯"
    man_with_probing_cane_tone1 = "👨🏻🦯"
    man_with_probing_cane_light_skin_tone = "👨🏻🦯"
    man_with_probing_cane_tone2 = "👨🏼🦯"
    man_with_probing_cane_medium_light_skin_tone = "👨🏼🦯"
    man_with_probing_cane_tone3 = "👨🏽🦯"
    man_with_probing_cane_medium_skin_tone = "👨🏽🦯"
    man_with_probing_cane_tone4 = "👨🏾🦯"
    man_with_probing_cane_medium_dark_skin_tone = "👨🏾🦯"
    man_with_probing_cane_tone5 = "👨🏿🦯"
    man_with_probing_cane_dark_skin_tone = "👨🏿🦯"
    woman_in_motorized_wheelchair = "👩🦼"
    woman_in_motorized_wheelchair_tone1 = "👩🏻🦼"
    woman_in_motorized_wheelchair_light_skin_tone = "👩🏻🦼"
    woman_in_motorized_wheelchair_tone2 = "👩🏼🦼"
    woman_in_motorized_wheelchair_medium_light_skin_tone = "👩🏼🦼"
    woman_in_motorized_wheelchair_tone3 = "👩🏽🦼"
    woman_in_motorized_wheelchair_medium_skin_tone = "👩🏽🦼"
    woman_in_motorized_wheelchair_tone4 = "👩🏾🦼"
    woman_in_motorized_wheelchair_medium_dark_skin_tone = "👩🏾🦼"
    woman_in_motorized_wheelchair_tone5 = "👩🏿🦼"
    woman_in_motorized_wheelchair_dark_skin_tone = "👩🏿🦼"
    man_in_motorized_wheelchair = "👨🦼"
    man_in_motorized_wheelchair_tone1 = "👨🏻🦼"
    man_in_motorized_wheelchair_light_skin_tone = "👨🏻🦼"
    man_in_motorized_wheelchair_tone2 = "👨🏼🦼"
    man_in_motorized_wheelchair_medium_light_skin_tone = "👨🏼🦼"
    man_in_motorized_wheelchair_tone3 = "👨🏽🦼"
    man_in_motorized_wheelchair_medium_skin_tone = "👨🏽🦼"
    man_in_motorized_wheelchair_tone4 = "👨🏾🦼"
    man_in_motorized_wheelchair_medium_dark_skin_tone = "👨🏾🦼"
    man_in_motorized_wheelchair_tone5 = "👨🏿🦼"
    man_in_motorized_wheelchair_dark_skin_tone = "👨🏿🦼"
    woman_in_manual_wheelchair = "👩🦽"
    woman_in_manual_wheelchair_tone1 = "👩🏻🦽"
    woman_in_manual_wheelchair_light_skin_tone = "👩🏻🦽"
    woman_in_manual_wheelchair_tone2 = "👩🏼🦽"
    woman_in_manual_wheelchair_medium_light_skin_tone = "👩🏼🦽"
    woman_in_manual_wheelchair_tone3 = "👩🏽🦽"
    woman_in_manual_wheelchair_medium_skin_tone = "👩🏽🦽"
    woman_in_manual_wheelchair_tone4 = "👩🏾🦽"
    woman_in_manual_wheelchair_medium_dark_skin_tone = "👩🏾🦽"
    woman_in_manual_wheelchair_tone5 = "👩🏿🦽"
    woman_in_manual_wheelchair_dark_skin_tone = "👩🏿🦽"
    man_in_manual_wheelchair = "👨🦽"
    man_in_manual_wheelchair_tone1 = "👨🏻🦽"
    man_in_manual_wheelchair_light_skin_tone = "👨🏻🦽"
    man_in_manual_wheelchair_tone2 = "👨🏼🦽"
    man_in_manual_wheelchair_medium_light_skin_tone = "👨🏼🦽"
    man_in_manual_wheelchair_tone3 = "👨🏽🦽"
    man_in_manual_wheelchair_medium_skin_tone = "👨🏽🦽"
    man_in_manual_wheelchair_tone4 = "👨🏾🦽"
    man_in_manual_wheelchair_medium_dark_skin_tone = "👨🏾🦽"
    man_in_manual_wheelchair_tone5 = "👨🏿🦽"
    man_in_manual_wheelchair_dark_skin_tone = "👨🏿🦽"
    people_holding_hands = "🧑🤝🧑"
    couple = "👫"
    two_women_holding_hands = "👭"
    two_men_holding_hands = "👬"
    couple_with_heart = "💑"
    couple_with_heart_woman_man = "👩❤👨"
    couple_ww = "👩❤👩"
    couple_with_heart_ww = "👩❤👩"
    couple_mm = "👨❤👨"
    couple_with_heart_mm = "👨❤👨"
    couplekiss = "💏"
    kiss_woman_man = "👩❤💋👨"
    kiss_ww = "👩❤💋👩"
    couplekiss_ww = "👩❤💋👩"
    kiss_mm = "👨❤💋👨"
    couplekiss_mm = "👨❤💋👨"
    family = "👪"
    family_man_woman_boy = "👨👩👦"
    family_mwg = "👨👩👧"
    family_mwgb = "👨👩👧👦"
    family_mwbb = "👨👩👦👦"
    family_mwgg = "👨👩👧👧"
    family_wwb = "👩👩👦"
    family_wwg = "👩👩👧"
    family_wwgb = "👩👩👧👦"
    family_wwbb = "👩👩👦👦"
    family_wwgg = "👩👩👧👧"
    family_mmb = "👨👨👦"
    family_mmg = "👨👨👧"
    family_mmgb = "👨👨👧👦"
    family_mmbb = "👨👨👦👦"
    family_mmgg = "👨👨👧👧"
    family_woman_boy = "👩👦"
    family_woman_girl = "👩👧"
    family_woman_girl_boy = "👩👧👦"
    family_woman_boy_boy = "👩👦👦"
    family_woman_girl_girl = "👩👧👧"
    family_man_boy = "👨👦"
    family_man_girl = "👨👧"
    family_man_girl_boy = "👨👧👦"
    family_man_boy_boy = "👨👦👦"
    family_man_girl_girl = "👨👧👧"
    yarn = "🧶"
    thread = "🧵"
    coat = "🧥"
    lab_coat = "🥼"
    safety_vest = "🦺"
    womans_clothes = "👚"
    shirt = "👕"
    jeans = "👖"
    shorts = "🩳"
    necktie = "👔"
    dress = "👗"
    bikini = "👙"
    one_piece_swimsuit = "🩱"
    kimono = "👘"
    sari = "🥻"
    womans_flat_shoe = "🥿"
    high_heel = "👠"
    sandal = "👡"
    boot = "👢"
    ballet_shoes = "🩰"
    mans_shoe = "👞"
    athletic_shoe = "👟"
    hiking_boot = "🥾"
    briefs = "🩲"
    socks = "🧦"
    gloves = "🧤"
    scarf = "🧣"
    tophat = "🎩"
    billed_cap = "🧢"
    womans_hat = "👒"
    mortar_board = "🎓"
    helmet_with_cross = "⛑"
    helmet_with_white_cross = "⛑"
    crown = "👑"
    ring = "💍"
    pouch = "👝"
    purse = "👛"
    handbag = "👜"
    briefcase = "💼"
    school_satchel = "🎒"
    luggage = "🧳"
    eyeglasses = "👓"
    dark_sunglasses = "🕶"
    goggles = "🥽"
    diving_mask = "🤿"
    closed_umbrella = "🌂"
    dog = "🐶"
    cat = "🐱"
    mouse = "🐭"
    hamster = "🐹"
    rabbit = "🐰"
    fox = "🦊"
    fox_face = "🦊"
    bear = "🐻"
    panda_face = "🐼"
    koala = "🐨"
    tiger = "🐯"
    lion_face = "🦁"
    lion = "🦁"
    cow = "🐮"
    pig = "🐷"
    pig_nose = "🐽"
    frog = "🐸"
    monkey_face = "🐵"
    see_no_evil = "🙈"
    hear_no_evil = "🙉"
    speak_no_evil = "🙊"
    monkey = "🐒"
    chicken = "🐔"
    penguin = "🐧"
    bird = "🐦"
    baby_chick = "🐤"
    hatching_chick = "🐣"
    hatched_chick = "🐥"
    duck = "🦆"
    eagle = "🦅"
    owl = "🦉"
    bat = "🦇"
    wolf = "🐺"
    boar = "🐗"
    horse = "🐴"
    unicorn = "🦄"
    unicorn_face = "🦄"
    bee = "🐝"
    bug = "🐛"
    butterfly = "🦋"
    snail = "🐌"
    shell = "🐚"
    beetle = "🐞"
    ant = "🐜"
    mosquito = "🦟"
    cricket = "🦗"
    spider = "🕷"
    spider_web = "🕸"
    scorpion = "🦂"
    turtle = "🐢"
    snake = "🐍"
    lizard = "🦎"
    t_rex = "🦖"
    sauropod = "🦕"
    octopus = "🐙"
    squid = "🦑"
    shrimp = "🦐"
    lobster = "🦞"
    oyster = "🦪"
    crab = "🦀"
    blowfish = "🐡"
    tropical_fish = "🐠"
    fish = "🐟"
    dolphin = "🐬"
    whale = "🐳"
    whale2 = "🐋"
    shark = "🦈"
    crocodile = "🐊"
    tiger2 = "🐅"
    leopard = "🐆"
    zebra = "🦓"
    gorilla = "🦍"
    orangutan = "🦧"
    elephant = "🐘"
    hippopotamus = "🦛"
    rhino = "🦏"
    rhinoceros = "🦏"
    dromedary_camel = "🐪"
    camel = "🐫"
    giraffe = "🦒"
    kangaroo = "🦘"
    water_buffalo = "🐃"
    ox = "🐂"
    cow2 = "🐄"
    racehorse = "🐎"
    pig2 = "🐖"
    ram = "🐏"
    llama = "🦙"
    sheep = "🐑"
    goat = "🐐"
    deer = "🦌"
    dog2 = "🐕"
    guide_dog = "🦮"
    service_dog = "🐕🦺"
    poodle = "🐩"
    cat2 = "🐈"
    rooster = "🐓"
    turkey = "🦃"
    peacock = "🦚"
    parrot = "🦜"
    swan = "🦢"
    flamingo = "🦩"
    dove = "🕊"
    dove_of_peace = "🕊"
    rabbit2 = "🐇"
    sloth = "🦥"
    otter = "🦦"
    skunk = "🦨"
    raccoon = "🦝"
    badger = "🦡"
    mouse2 = "🐁"
    rat = "🐀"
    chipmunk = "🐿"
    hedgehog = "🦔"
    feet = "🐾"
    paw_prints = "🐾"
    dragon = "🐉"
    dragon_face = "🐲"
    cactus = "🌵"
    christmas_tree = "🎄"
    evergreen_tree = "🌲"
    deciduous_tree = "🌳"
    palm_tree = "🌴"
    seedling = "🌱"
    herb = "🌿"
    shamrock = "☘"
    four_leaf_clover = "🍀"
    bamboo = "🎍"
    tanabata_tree = "🎋"
    leaves = "🍃"
    fallen_leaf = "🍂"
    maple_leaf = "🍁"
    mushroom = "🍄"
    ear_of_rice = "🌾"
    bouquet = "💐"
    tulip = "🌷"
    rose = "🌹"
    wilted_rose = "🥀"
    wilted_flower = "🥀"
    hibiscus = "🌺"
    cherry_blossom = "🌸"
    blossom = "🌼"
    sunflower = "🌻"
    sun_with_face = "🌞"
    full_moon_with_face = "🌝"
    first_quarter_moon_with_face = "🌛"
    last_quarter_moon_with_face = "🌜"
    new_moon_with_face = "🌚"
    full_moon = "🌕"
    waning_gibbous_moon = "🌖"
    last_quarter_moon = "🌗"
    waning_crescent_moon = "🌘"
    new_moon = "🌑"
    waxing_crescent_moon = "🌒"
    first_quarter_moon = "🌓"
    waxing_gibbous_moon = "🌔"
    crescent_moon = "🌙"
    earth_americas = "🌎"
    earth_africa = "🌍"
    earth_asia = "🌏"
    ringed_planet = "🪐"
    dizzy = "💫"
    star = "⭐"
    star2 = "🌟"
    sparkles = "✨"
    zap = "⚡"
    comet = "☄"
    boom = "💥"
    fire = "🔥"
    flame = "🔥"
    cloud_tornado = "🌪"
    cloud_with_tornado = "🌪"
    rainbow = "🌈"
    sunny = "☀"
    white_sun_small_cloud = "🌤"
    white_sun_with_small_cloud = "🌤"
    partly_sunny = "⛅"
    white_sun_cloud = "🌥"
    white_sun_behind_cloud = "🌥"
    cloud = "☁"
    white_sun_rain_cloud = "🌦"
    white_sun_behind_cloud_with_rain = "🌦"
    cloud_rain = "🌧"
    cloud_with_rain = "🌧"
    thunder_cloud_rain = "⛈"
    thunder_cloud_and_rain = "⛈"
    cloud_lightning = "🌩"
    cloud_with_lightning = "🌩"
    cloud_snow = "🌨"
    cloud_with_snow = "🌨"
    snowflake = "❄"
    snowman2 = "☃"
    snowman = "⛄"
    wind_blowing_face = "🌬"
    dash = "💨"
    droplet = "💧"
    sweat_drops = "💦"
    umbrella = "☔"
    umbrella2 = "☂"
    ocean = "🌊"
    fog = "🌫"
    green_apple = "🍏"
    apple = "🍎"
    pear = "🍐"
    tangerine = "🍊"
    lemon = "🍋"
    banana = "🍌"
    watermelon = "🍉"
    grapes = "🍇"
    strawberry = "🍓"
    melon = "🍈"
    cherries = "🍒"
    peach = "🍑"
    mango = "🥭"
    pineapple = "🍍"
    coconut = "🥥"
    kiwi = "🥝"
    kiwifruit = "🥝"
    tomato = "🍅"
    eggplant = "🍆"
    avocado = "🥑"
    broccoli = "🥦"
    leafy_green = "🥬"
    cucumber = "🥒"
    hot_pepper = "🌶"
    corn = "🌽"
    carrot = "🥕"
    onion = "🧅"
    garlic = "🧄"
    potato = "🥔"
    sweet_potato = "🍠"
    croissant = "🥐"
    bagel = "🥯"
    bread = "🍞"
    french_bread = "🥖"
    baguette_bread = "🥖"
    pretzel = "🥨"
    cheese = "🧀"
    cheese_wedge = "🧀"
    egg = "🥚"
    cooking = "🍳"
    pancakes = "🥞"
    waffle = "🧇"
    bacon = "🥓"
    cut_of_meat = "🥩"
    poultry_leg = "🍗"
    meat_on_bone = "🍖"
    hotdog = "🌭"
    hot_dog = "🌭"
    hamburger = "🍔"
    fries = "🍟"
    pizza = "🍕"
    sandwich = "🥪"
    falafel = "🧆"
    stuffed_flatbread = "🥙"
    stuffed_pita = "🥙"
    taco = "🌮"
    burrito = "🌯"
    salad = "🥗"
    green_salad = "🥗"
    shallow_pan_of_food = "🥘"
    paella = "🥘"
    canned_food = "🥫"
    spaghetti = "🍝"
    ramen = "🍜"
    stew = "🍲"
    curry = "🍛"
    sushi = "🍣"
    bento = "🍱"
    dumpling = "🥟"
    fried_shrimp = "🍤"
    rice_ball = "🍙"
    rice = "🍚"
    rice_cracker = "🍘"
    fish_cake = "🍥"
    fortune_cookie = "🥠"
    moon_cake = "🥮"
    oden = "🍢"
    dango = "🍡"
    shaved_ice = "🍧"
    ice_cream = "🍨"
    icecream = "🍦"
    pie = "🥧"
    cupcake = "🧁"
    cake = "🍰"
    birthday = "🎂"
    custard = "🍮"
    pudding = "🍮"
    flan = "🍮"
    lollipop = "🍭"
    candy = "🍬"
    chocolate_bar = "🍫"
    popcorn = "🍿"
    doughnut = "🍩"
    cookie = "🍪"
    chestnut = "🌰"
    peanuts = "🥜"
    shelled_peanut = "🥜"
    honey_pot = "🍯"
    butter = "🧈"
    milk = "🥛"
    glass_of_milk = "🥛"
    baby_bottle = "🍼"
    coffee = "☕"
    tea = "🍵"
    mate = "🧉"
    cup_with_straw = "🥤"
    beverage_box = "🧃"
    ice_cube = "🧊"
    sake = "🍶"
    beer = "🍺"
    beers = "🍻"
    champagne_glass = "🥂"
    clinking_glass = "🥂"
    wine_glass = "🍷"
    tumbler_glass = "🥃"
    whisky = "🥃"
    cocktail = "🍸"
    tropical_drink = "🍹"
    champagne = "🍾"
    bottle_with_popping_cork = "🍾"
    spoon = "🥄"
    fork_and_knife = "🍴"
    fork_knife_plate = "🍽"
    fork_and_knife_with_plate = "🍽"
    bowl_with_spoon = "🥣"
    takeout_box = "🥡"
    chopsticks = "🥢"
    salt = "🧂"
    soccer = "⚽"
    basketball = "🏀"
    football = "🏈"
    baseball = "⚾"
    softball = "🥎"
    tennis = "🎾"
    volleyball = "🏐"
    rugby_football = "🏉"
    flying_disc = "🥏"
    eight_ball = "🎱"
    ping_pong = "🏓"
    table_tennis = "🏓"
    badminton = "🏸"
    hockey = "🏒"
    field_hockey = "🏑"
    lacrosse = "🥍"
    cricket_game = "🏏"
    cricket_bat_ball = "🏏"
    goal = "🥅"
    goal_net = "🥅"
    golf = "⛳"
    bow_and_arrow = "🏹"
    archery = "🏹"
    fishing_pole_and_fish = "🎣"
    boxing_glove = "🥊"
    boxing_gloves = "🥊"
    martial_arts_uniform = "🥋"
    karate_uniform = "🥋"
    running_shirt_with_sash = "🎽"
    skateboard = "🛹"
    sled = "🛷"
    parachute = "🪂"
    ice_skate = "⛸"
    curling_stone = "🥌"
    ski = "🎿"
    skier = "⛷"
    snowboarder = "🏂"
    snowboarder_tone1 = "🏂🏻"
    snowboarder_light_skin_tone = "🏂🏻"
    snowboarder_tone2 = "🏂🏼"
    snowboarder_medium_light_skin_tone = "🏂🏼"
    snowboarder_tone3 = "🏂🏽"
    snowboarder_medium_skin_tone = "🏂🏽"
    snowboarder_tone4 = "🏂🏾"
    snowboarder_medium_dark_skin_tone = "🏂🏾"
    snowboarder_tone5 = "🏂🏿"
    snowboarder_dark_skin_tone = "🏂🏿"
    person_lifting_weights = "🏋"
    lifter = "🏋"
    weight_lifter = "🏋"
    person_lifting_weights_tone1 = "🏋🏻"
    lifter_tone1 = "🏋🏻"
    weight_lifter_tone1 = "🏋🏻"
    person_lifting_weights_tone2 = "🏋🏼"
    lifter_tone2 = "🏋🏼"
    weight_lifter_tone2 = "🏋🏼"
    person_lifting_weights_tone3 = "🏋🏽"
    lifter_tone3 = "🏋🏽"
    weight_lifter_tone3 = "🏋🏽"
    person_lifting_weights_tone4 = "🏋🏾"
    lifter_tone4 = "🏋🏾"
    weight_lifter_tone4 = "🏋🏾"
    person_lifting_weights_tone5 = "🏋🏿"
    lifter_tone5 = "🏋🏿"
    weight_lifter_tone5 = "🏋🏿"
    woman_lifting_weights = "🏋♀"
    woman_lifting_weights_tone1 = "🏋🏻♀"
    woman_lifting_weights_light_skin_tone = "🏋🏻♀"
    woman_lifting_weights_tone2 = "🏋🏼♀"
    woman_lifting_weights_medium_light_skin_tone = "🏋🏼♀"
    woman_lifting_weights_tone3 = "🏋🏽♀"
    woman_lifting_weights_medium_skin_tone = "🏋🏽♀"
    woman_lifting_weights_tone4 = "🏋🏾♀"
    woman_lifting_weights_medium_dark_skin_tone = "🏋🏾♀"
    woman_lifting_weights_tone5 = "🏋🏿♀"
    woman_lifting_weights_dark_skin_tone = "🏋🏿♀"
    man_lifting_weights = "🏋♂"
    man_lifting_weights_tone1 = "🏋🏻♂"
    man_lifting_weights_light_skin_tone = "🏋🏻♂"
    man_lifting_weights_tone2 = "🏋🏼♂"
    man_lifting_weights_medium_light_skin_tone = "🏋🏼♂"
    man_lifting_weights_tone3 = "🏋🏽♂"
    man_lifting_weights_medium_skin_tone = "🏋🏽♂"
    man_lifting_weights_tone4 = "🏋🏾♂"
    man_lifting_weights_medium_dark_skin_tone = "🏋🏾♂"
    man_lifting_weights_tone5 = "🏋🏿♂"
    man_lifting_weights_dark_skin_tone = "🏋🏿♂"
    people_wrestling = "🤼"
    wrestlers = "🤼"
    wrestling = "🤼"
    women_wrestling = "🤼♀"
    men_wrestling = "🤼♂"
    person_doing_cartwheel = "🤸"
    cartwheel = "🤸"
    person_doing_cartwheel_tone1 = "🤸🏻"
    cartwheel_tone1 = "🤸🏻"
    person_doing_cartwheel_tone2 = "🤸🏼"
    cartwheel_tone2 = "🤸🏼"
    person_doing_cartwheel_tone3 = "🤸🏽"
    cartwheel_tone3 = "🤸🏽"
    person_doing_cartwheel_tone4 = "🤸🏾"
    cartwheel_tone4 = "🤸🏾"
    person_doing_cartwheel_tone5 = "🤸🏿"
    cartwheel_tone5 = "🤸🏿"
    woman_cartwheeling = "🤸♀"
    woman_cartwheeling_tone1 = "🤸🏻♀"
    woman_cartwheeling_light_skin_tone = "🤸🏻♀"
    woman_cartwheeling_tone2 = "🤸🏼♀"
    woman_cartwheeling_medium_light_skin_tone = "🤸🏼♀"
    woman_cartwheeling_tone3 = "🤸🏽♀"
    woman_cartwheeling_medium_skin_tone = "🤸🏽♀"
    woman_cartwheeling_tone4 = "🤸🏾♀"
    woman_cartwheeling_medium_dark_skin_tone = "🤸🏾♀"
    woman_cartwheeling_tone5 = "🤸🏿♀"
    woman_cartwheeling_dark_skin_tone = "🤸🏿♀"
    man_cartwheeling = "🤸♂"
    man_cartwheeling_tone1 = "🤸🏻♂"
    man_cartwheeling_light_skin_tone = "🤸🏻♂"
    man_cartwheeling_tone2 = "🤸🏼♂"
    man_cartwheeling_medium_light_skin_tone = "🤸🏼♂"
    man_cartwheeling_tone3 = "🤸🏽♂"
    man_cartwheeling_medium_skin_tone = "🤸🏽♂"
    man_cartwheeling_tone4 = "🤸🏾♂"
    man_cartwheeling_medium_dark_skin_tone = "🤸🏾♂"
    man_cartwheeling_tone5 = "🤸🏿♂"
    man_cartwheeling_dark_skin_tone = "🤸🏿♂"
    person_bouncing_ball = "⛹"
    basketball_player = "⛹"
    person_with_ball = "⛹"
    person_bouncing_ball_tone1 = "⛹🏻"
    basketball_player_tone1 = "⛹🏻"
    person_with_ball_tone1 = "⛹🏻"
    person_bouncing_ball_tone2 = "⛹🏼"
    basketball_player_tone2 = "⛹🏼"
    person_with_ball_tone2 = "⛹🏼"
    person_bouncing_ball_tone3 = "⛹🏽"
    basketball_player_tone3 = "⛹🏽"
    person_with_ball_tone3 = "⛹🏽"
    person_bouncing_ball_tone4 = "⛹🏾"
    basketball_player_tone4 = "⛹🏾"
    person_with_ball_tone4 = "⛹🏾"
    person_bouncing_ball_tone5 = "⛹🏿"
    basketball_player_tone5 = "⛹🏿"
    person_with_ball_tone5 = "⛹🏿"
    woman_bouncing_ball = "⛹♀"
    woman_bouncing_ball_tone1 = "⛹🏻♀"
    woman_bouncing_ball_light_skin_tone = "⛹🏻♀"
    woman_bouncing_ball_tone2 = "⛹🏼♀"
    woman_bouncing_ball_medium_light_skin_tone = "⛹🏼♀"
    woman_bouncing_ball_tone3 = "⛹🏽♀"
    woman_bouncing_ball_medium_skin_tone = "⛹🏽♀"
    woman_bouncing_ball_tone4 = "⛹🏾♀"
    woman_bouncing_ball_medium_dark_skin_tone = "⛹🏾♀"
    woman_bouncing_ball_tone5 = "⛹🏿♀"
    woman_bouncing_ball_dark_skin_tone = "⛹🏿♀"
    man_bouncing_ball = "⛹♂"
    man_bouncing_ball_tone1 = "⛹🏻♂"
    man_bouncing_ball_light_skin_tone = "⛹🏻♂"
    man_bouncing_ball_tone2 = "⛹🏼♂"
    man_bouncing_ball_medium_light_skin_tone = "⛹🏼♂"
    man_bouncing_ball_tone3 = "⛹🏽♂"
    man_bouncing_ball_medium_skin_tone = "⛹🏽♂"
    man_bouncing_ball_tone4 = "⛹🏾♂"
    man_bouncing_ball_medium_dark_skin_tone = "⛹🏾♂"
    man_bouncing_ball_tone5 = "⛹🏿♂"
    man_bouncing_ball_dark_skin_tone = "⛹🏿♂"
    person_fencing = "🤺"
    fencer = "🤺"
    fencing = "🤺"
    person_playing_handball = "🤾"
    handball = "🤾"
    person_playing_handball_tone1 = "🤾🏻"
    handball_tone1 = "🤾🏻"
    person_playing_handball_tone2 = "🤾🏼"
    handball_tone2 = "🤾🏼"
    person_playing_handball_tone3 = "🤾🏽"
    handball_tone3 = "🤾🏽"
    person_playing_handball_tone4 = "🤾🏾"
    handball_tone4 = "🤾🏾"
    person_playing_handball_tone5 = "🤾🏿"
    handball_tone5 = "🤾🏿"
    woman_playing_handball = "🤾♀"
    woman_playing_handball_tone1 = "🤾🏻♀"
    woman_playing_handball_light_skin_tone = "🤾🏻♀"
    woman_playing_handball_tone2 = "🤾🏼♀"
    woman_playing_handball_medium_light_skin_tone = "🤾🏼♀"
    woman_playing_handball_tone3 = "🤾🏽♀"
    woman_playing_handball_medium_skin_tone = "🤾🏽♀"
    woman_playing_handball_tone4 = "🤾🏾♀"
    woman_playing_handball_medium_dark_skin_tone = "🤾🏾♀"
    woman_playing_handball_tone5 = "🤾🏿♀"
    woman_playing_handball_dark_skin_tone = "🤾🏿♀"
    man_playing_handball = "🤾♂"
    man_playing_handball_tone1 = "🤾🏻♂"
    man_playing_handball_light_skin_tone = "🤾🏻♂"
    man_playing_handball_tone2 = "🤾🏼♂"
    man_playing_handball_medium_light_skin_tone = "🤾🏼♂"
    man_playing_handball_tone3 = "🤾🏽♂"
    man_playing_handball_medium_skin_tone = "🤾🏽♂"
    man_playing_handball_tone4 = "🤾🏾♂"
    man_playing_handball_medium_dark_skin_tone = "🤾🏾♂"
    man_playing_handball_tone5 = "🤾🏿♂"
    man_playing_handball_dark_skin_tone = "🤾🏿♂"
    person_golfing = "🏌"
    golfer = "🏌"
    person_golfing_tone1 = "🏌🏻"
    person_golfing_light_skin_tone = "🏌🏻"
    person_golfing_tone2 = "🏌🏼"
    person_golfing_medium_light_skin_tone = "🏌🏼"
    person_golfing_tone3 = "🏌🏽"
    person_golfing_medium_skin_tone = "🏌🏽"
    person_golfing_tone4 = "🏌🏾"
    person_golfing_medium_dark_skin_tone = "🏌🏾"
    person_golfing_tone5 = "🏌🏿"
    person_golfing_dark_skin_tone = "🏌🏿"
    woman_golfing = "🏌♀"
    woman_golfing_tone1 = "🏌🏻♀"
    woman_golfing_light_skin_tone = "🏌🏻♀"
    woman_golfing_tone2 = "🏌🏼♀"
    woman_golfing_medium_light_skin_tone = "🏌🏼♀"
    woman_golfing_tone3 = "🏌🏽♀"
    woman_golfing_medium_skin_tone = "🏌🏽♀"
    woman_golfing_tone4 = "🏌🏾♀"
    woman_golfing_medium_dark_skin_tone = "🏌🏾♀"
    woman_golfing_tone5 = "🏌🏿♀"
    woman_golfing_dark_skin_tone = "🏌🏿♀"
    man_golfing = "🏌♂"
    man_golfing_tone1 = "🏌🏻♂"
    man_golfing_light_skin_tone = "🏌🏻♂"
    man_golfing_tone2 = "🏌🏼♂"
    man_golfing_medium_light_skin_tone = "🏌🏼♂"
    man_golfing_tone3 = "🏌🏽♂"
    man_golfing_medium_skin_tone = "🏌🏽♂"
    man_golfing_tone4 = "🏌🏾♂"
    man_golfing_medium_dark_skin_tone = "🏌🏾♂"
    man_golfing_tone5 = "🏌🏿♂"
    man_golfing_dark_skin_tone = "🏌🏿♂"
    horse_racing = "🏇"
    horse_racing_tone1 = "🏇🏻"
    horse_racing_tone2 = "🏇🏼"
    horse_racing_tone3 = "🏇🏽"
    horse_racing_tone4 = "🏇🏾"
    horse_racing_tone5 = "🏇🏿"
    person_in_lotus_position = "🧘"
    person_in_lotus_position_tone1 = "🧘🏻"
    person_in_lotus_position_light_skin_tone = "🧘🏻"
    person_in_lotus_position_tone2 = "🧘🏼"
    person_in_lotus_position_medium_light_skin_tone = "🧘🏼"
    person_in_lotus_position_tone3 = "🧘🏽"
    person_in_lotus_position_medium_skin_tone = "🧘🏽"
    person_in_lotus_position_tone4 = "🧘🏾"
    person_in_lotus_position_medium_dark_skin_tone = "🧘🏾"
    person_in_lotus_position_tone5 = "🧘🏿"
    person_in_lotus_position_dark_skin_tone = "🧘🏿"
    woman_in_lotus_position = "🧘♀"
    woman_in_lotus_position_tone1 = "🧘🏻♀"
    woman_in_lotus_position_light_skin_tone = "🧘🏻♀"
    woman_in_lotus_position_tone2 = "🧘🏼♀"
    woman_in_lotus_position_medium_light_skin_tone = "🧘🏼♀"
    woman_in_lotus_position_tone3 = "🧘🏽♀"
    woman_in_lotus_position_medium_skin_tone = "🧘🏽♀"
    woman_in_lotus_position_tone4 = "🧘🏾♀"
    woman_in_lotus_position_medium_dark_skin_tone = "🧘🏾♀"
    woman_in_lotus_position_tone5 = "🧘🏿♀"
    woman_in_lotus_position_dark_skin_tone = "🧘🏿♀"
    man_in_lotus_position = "🧘♂"
    man_in_lotus_position_tone1 = "🧘🏻♂"
    man_in_lotus_position_light_skin_tone = "🧘🏻♂"
    man_in_lotus_position_tone2 = "🧘🏼♂"
    man_in_lotus_position_medium_light_skin_tone = "🧘🏼♂"
    man_in_lotus_position_tone3 = "🧘🏽♂"
    man_in_lotus_position_medium_skin_tone = "🧘🏽♂"
    man_in_lotus_position_tone4 = "🧘🏾♂"
    man_in_lotus_position_medium_dark_skin_tone = "🧘🏾♂"
    man_in_lotus_position_tone5 = "🧘🏿♂"
    man_in_lotus_position_dark_skin_tone = "🧘🏿♂"
    person_surfing = "🏄"
    surfer = "🏄"
    person_surfing_tone1 = "🏄🏻"
    surfer_tone1 = "🏄🏻"
    person_surfing_tone2 = "🏄🏼"
    surfer_tone2 = "🏄🏼"
    person_surfing_tone3 = "🏄🏽"
    surfer_tone3 = "🏄🏽"
    person_surfing_tone4 = "🏄🏾"
    surfer_tone4 = "🏄🏾"
    person_surfing_tone5 = "🏄🏿"
    surfer_tone5 = "🏄🏿"
    woman_surfing = "🏄♀"
    woman_surfing_tone1 = "🏄🏻♀"
    woman_surfing_light_skin_tone = "🏄🏻♀"
    woman_surfing_tone2 = "🏄🏼♀"
    woman_surfing_medium_light_skin_tone = "🏄🏼♀"
    woman_surfing_tone3 = "🏄🏽♀"
    woman_surfing_medium_skin_tone = "🏄🏽♀"
    woman_surfing_tone4 = "🏄🏾♀"
    woman_surfing_medium_dark_skin_tone = "🏄🏾♀"
    woman_surfing_tone5 = "🏄🏿♀"
    woman_surfing_dark_skin_tone = "🏄🏿♀"
    man_surfing = "🏄♂"
    man_surfing_tone1 = "🏄🏻♂"
    man_surfing_light_skin_tone = "🏄🏻♂"
    man_surfing_tone2 = "🏄🏼♂"
    man_surfing_medium_light_skin_tone = "🏄🏼♂"
    man_surfing_tone3 = "🏄🏽♂"
    man_surfing_medium_skin_tone = "🏄🏽♂"
    man_surfing_tone4 = "🏄🏾♂"
    man_surfing_medium_dark_skin_tone = "🏄🏾♂"
    man_surfing_tone5 = "🏄🏿♂"
    man_surfing_dark_skin_tone = "🏄🏿♂"
    person_swimming = "🏊"
    swimmer = "🏊"
    person_swimming_tone1 = "🏊🏻"
    swimmer_tone1 = "🏊🏻"
    person_swimming_tone2 = "🏊🏼"
    swimmer_tone2 = "🏊🏼"
    person_swimming_tone3 = "🏊🏽"
    swimmer_tone3 = "🏊🏽"
    person_swimming_tone4 = "🏊🏾"
    swimmer_tone4 = "🏊🏾"
    person_swimming_tone5 = "🏊🏿"
    swimmer_tone5 = "🏊🏿"
    woman_swimming = "🏊♀"
    woman_swimming_tone1 = "🏊🏻♀"
    woman_swimming_light_skin_tone = "🏊🏻♀"
    woman_swimming_tone2 = "🏊🏼♀"
    woman_swimming_medium_light_skin_tone = "🏊🏼♀"
    woman_swimming_tone3 = "🏊🏽♀"
    woman_swimming_medium_skin_tone = "🏊🏽♀"
    woman_swimming_tone4 = "🏊🏾♀"
    woman_swimming_medium_dark_skin_tone = "🏊🏾♀"
    woman_swimming_tone5 = "🏊🏿♀"
    woman_swimming_dark_skin_tone = "🏊🏿♀"
    man_swimming = "🏊♂"
    man_swimming_tone1 = "🏊🏻♂"
    man_swimming_light_skin_tone = "🏊🏻♂"
    man_swimming_tone2 = "🏊🏼♂"
    man_swimming_medium_light_skin_tone = "🏊🏼♂"
    man_swimming_tone3 = "🏊🏽♂"
    man_swimming_medium_skin_tone = "🏊🏽♂"
    man_swimming_tone4 = "🏊🏾♂"
    man_swimming_medium_dark_skin_tone = "🏊🏾♂"
    man_swimming_tone5 = "🏊🏿♂"
    man_swimming_dark_skin_tone = "🏊🏿♂"
    person_playing_water_polo = "🤽"
    water_polo = "🤽"
    person_playing_water_polo_tone1 = "🤽🏻"
    water_polo_tone1 = "🤽🏻"
    person_playing_water_polo_tone2 = "🤽🏼"
    water_polo_tone2 = "🤽🏼"
    person_playing_water_polo_tone3 = "🤽🏽"
    water_polo_tone3 = "🤽🏽"
    person_playing_water_polo_tone4 = "🤽🏾"
    water_polo_tone4 = "🤽🏾"
    person_playing_water_polo_tone5 = "🤽🏿"
    water_polo_tone5 = "🤽🏿"
    woman_playing_water_polo = "🤽♀"
    woman_playing_water_polo_tone1 = "🤽🏻♀"
    woman_playing_water_polo_light_skin_tone = "🤽🏻♀"
    woman_playing_water_polo_tone2 = "🤽🏼♀"
    woman_playing_water_polo_medium_light_skin_tone = "🤽🏼♀"
    woman_playing_water_polo_tone3 = "🤽🏽♀"
    woman_playing_water_polo_medium_skin_tone = "🤽🏽♀"
    woman_playing_water_polo_tone4 = "🤽🏾♀"
    woman_playing_water_polo_medium_dark_skin_tone = "🤽🏾♀"
    woman_playing_water_polo_tone5 = "🤽🏿♀"
    woman_playing_water_polo_dark_skin_tone = "🤽🏿♀"
    man_playing_water_polo = "🤽♂"
    man_playing_water_polo_tone1 = "🤽🏻♂"
    man_playing_water_polo_light_skin_tone = "🤽🏻♂"
    man_playing_water_polo_tone2 = "🤽🏼♂"
    man_playing_water_polo_medium_light_skin_tone = "🤽🏼♂"
    man_playing_water_polo_tone3 = "🤽🏽♂"
    man_playing_water_polo_medium_skin_tone = "🤽🏽♂"
    man_playing_water_polo_tone4 = "🤽🏾♂"
    man_playing_water_polo_medium_dark_skin_tone = "🤽🏾♂"
    man_playing_water_polo_tone5 = "🤽🏿♂"
    man_playing_water_polo_dark_skin_tone = "🤽🏿♂"
    person_rowing_boat = "🚣"
    rowboat = "🚣"
    person_rowing_boat_tone1 = "🚣🏻"
    rowboat_tone1 = "🚣🏻"
    person_rowing_boat_tone2 = "🚣🏼"
    rowboat_tone2 = "🚣🏼"
    person_rowing_boat_tone3 = "🚣🏽"
    rowboat_tone3 = "🚣🏽"
    person_rowing_boat_tone4 = "🚣🏾"
    rowboat_tone4 = "🚣🏾"
    person_rowing_boat_tone5 = "🚣🏿"
    rowboat_tone5 = "🚣🏿"
    woman_rowing_boat = "🚣♀"
    woman_rowing_boat_tone1 = "🚣🏻♀"
    woman_rowing_boat_light_skin_tone = "🚣🏻♀"
    woman_rowing_boat_tone2 = "🚣🏼♀"
    woman_rowing_boat_medium_light_skin_tone = "🚣🏼♀"
    woman_rowing_boat_tone3 = "🚣🏽♀"
    woman_rowing_boat_medium_skin_tone = "🚣🏽♀"
    woman_rowing_boat_tone4 = "🚣🏾♀"
    woman_rowing_boat_medium_dark_skin_tone = "🚣🏾♀"
    woman_rowing_boat_tone5 = "🚣🏿♀"
    woman_rowing_boat_dark_skin_tone = "🚣🏿♀"
    man_rowing_boat = "🚣♂"
    man_rowing_boat_tone1 = "🚣🏻♂"
    man_rowing_boat_light_skin_tone = "🚣🏻♂"
    man_rowing_boat_tone2 = "🚣🏼♂"
    man_rowing_boat_medium_light_skin_tone = "🚣🏼♂"
    man_rowing_boat_tone3 = "🚣🏽♂"
    man_rowing_boat_medium_skin_tone = "🚣🏽♂"
    man_rowing_boat_tone4 = "🚣🏾♂"
    man_rowing_boat_medium_dark_skin_tone = "🚣🏾♂"
    man_rowing_boat_tone5 = "🚣🏿♂"
    man_rowing_boat_dark_skin_tone = "🚣🏿♂"
    person_climbing = "🧗"
    person_climbing_tone1 = "🧗🏻"
    person_climbing_light_skin_tone = "🧗🏻"
    person_climbing_tone2 = "🧗🏼"
    person_climbing_medium_light_skin_tone = "🧗🏼"
    person_climbing_tone3 = "🧗🏽"
    person_climbing_medium_skin_tone = "🧗🏽"
    person_climbing_tone4 = "🧗🏾"
    person_climbing_medium_dark_skin_tone = "🧗🏾"
    person_climbing_tone5 = "🧗🏿"
    person_climbing_dark_skin_tone = "🧗🏿"
    woman_climbing = "🧗♀"
    woman_climbing_tone1 = "🧗🏻♀"
    woman_climbing_light_skin_tone = "🧗🏻♀"
    woman_climbing_tone2 = "🧗🏼♀"
    woman_climbing_medium_light_skin_tone = "🧗🏼♀"
    woman_climbing_tone3 = "🧗🏽♀"
    woman_climbing_medium_skin_tone = "🧗🏽♀"
    woman_climbing_tone4 = "🧗🏾♀"
    woman_climbing_medium_dark_skin_tone = "🧗🏾♀"
    woman_climbing_tone5 = "🧗🏿♀"
    woman_climbing_dark_skin_tone = "🧗🏿♀"
    man_climbing = "🧗♂"
    man_climbing_tone1 = "🧗🏻♂"
    man_climbing_light_skin_tone = "🧗🏻♂"
    man_climbing_tone2 = "🧗🏼♂"
    man_climbing_medium_light_skin_tone = "🧗🏼♂"
    man_climbing_tone3 = "🧗🏽♂"
    man_climbing_medium_skin_tone = "🧗🏽♂"
    man_climbing_tone4 = "🧗🏾♂"
    man_climbing_medium_dark_skin_tone = "🧗🏾♂"
    man_climbing_tone5 = "🧗🏿♂"
    man_climbing_dark_skin_tone = "🧗🏿♂"
    person_mountain_biking = "🚵"
    mountain_bicyclist = "🚵"
    person_mountain_biking_tone1 = "🚵🏻"
    mountain_bicyclist_tone1 = "🚵🏻"
    person_mountain_biking_tone2 = "🚵🏼"
    mountain_bicyclist_tone2 = "🚵🏼"
    person_mountain_biking_tone3 = "🚵🏽"
    mountain_bicyclist_tone3 = "🚵🏽"
    person_mountain_biking_tone4 = "🚵🏾"
    mountain_bicyclist_tone4 = "🚵🏾"
    person_mountain_biking_tone5 = "🚵🏿"
    mountain_bicyclist_tone5 = "🚵🏿"
    woman_mountain_biking = "🚵♀"
    woman_mountain_biking_tone1 = "🚵🏻♀"
    woman_mountain_biking_light_skin_tone = "🚵🏻♀"
    woman_mountain_biking_tone2 = "🚵🏼♀"
    woman_mountain_biking_medium_light_skin_tone = "🚵🏼♀"
    woman_mountain_biking_tone3 = "🚵🏽♀"
    woman_mountain_biking_medium_skin_tone = "🚵🏽♀"
    woman_mountain_biking_tone4 = "🚵🏾♀"
    woman_mountain_biking_medium_dark_skin_tone = "🚵🏾♀"
    woman_mountain_biking_tone5 = "🚵🏿♀"
    woman_mountain_biking_dark_skin_tone = "🚵🏿♀"
    man_mountain_biking = "🚵♂"
    man_mountain_biking_tone1 = "🚵🏻♂"
    man_mountain_biking_light_skin_tone = "🚵🏻♂"
    man_mountain_biking_tone2 = "🚵🏼♂"
    man_mountain_biking_medium_light_skin_tone = "🚵🏼♂"
    man_mountain_biking_tone3 = "🚵🏽♂"
    man_mountain_biking_medium_skin_tone = "🚵🏽♂"
    man_mountain_biking_tone4 = "🚵🏾♂"
    man_mountain_biking_medium_dark_skin_tone = "🚵🏾♂"
    man_mountain_biking_tone5 = "🚵🏿♂"
    man_mountain_biking_dark_skin_tone = "🚵🏿♂"
    person_biking = "🚴"
    bicyclist = "🚴"
    person_biking_tone1 = "🚴🏻"
    bicyclist_tone1 = "🚴🏻"
    person_biking_tone2 = "🚴🏼"
    bicyclist_tone2 = "🚴🏼"
    person_biking_tone3 = "🚴🏽"
    bicyclist_tone3 = "🚴🏽"
    person_biking_tone4 = "🚴🏾"
    bicyclist_tone4 = "🚴🏾"
    person_biking_tone5 = "🚴🏿"
    bicyclist_tone5 = "🚴🏿"
    woman_biking = "🚴♀"
    woman_biking_tone1 = "🚴🏻♀"
    woman_biking_light_skin_tone = "🚴🏻♀"
    woman_biking_tone2 = "🚴🏼♀"
    woman_biking_medium_light_skin_tone = "🚴🏼♀"
    woman_biking_tone3 = "🚴🏽♀"
    woman_biking_medium_skin_tone = "🚴🏽♀"
    woman_biking_tone4 = "🚴🏾♀"
    woman_biking_medium_dark_skin_tone = "🚴🏾♀"
    woman_biking_tone5 = "🚴🏿♀"
    woman_biking_dark_skin_tone = "🚴🏿♀"
    man_biking = "🚴♂"
    man_biking_tone1 = "🚴🏻♂"
    man_biking_light_skin_tone = "🚴🏻♂"
    man_biking_tone2 = "🚴🏼♂"
    man_biking_medium_light_skin_tone = "🚴🏼♂"
    man_biking_tone3 = "🚴🏽♂"
    man_biking_medium_skin_tone = "🚴🏽♂"
    man_biking_tone4 = "🚴🏾♂"
    man_biking_medium_dark_skin_tone = "🚴🏾♂"
    man_biking_tone5 = "🚴🏿♂"
    man_biking_dark_skin_tone = "🚴🏿♂"
    trophy = "🏆"
    first_place = "🥇"
    first_place_medal = "🥇"
    second_place = "🥈"
    second_place_medal = "🥈"
    third_place = "🥉"
    third_place_medal = "🥉"
    medal = "🏅"
    sports_medal = "🏅"
    military_medal = "🎖"
    rosette = "🏵"
    reminder_ribbon = "🎗"
    ticket = "🎫"
    tickets = "🎟"
    admission_tickets = "🎟"
    circus_tent = "🎪"
    person_juggling = "🤹"
    juggling = "🤹"
    juggler = "🤹"
    person_juggling_tone1 = "🤹🏻"
    juggling_tone1 = "🤹🏻"
    juggler_tone1 = "🤹🏻"
    person_juggling_tone2 = "🤹🏼"
    juggling_tone2 = "🤹🏼"
    juggler_tone2 = "🤹🏼"
    person_juggling_tone3 = "🤹🏽"
    juggling_tone3 = "🤹🏽"
    juggler_tone3 = "🤹🏽"
    person_juggling_tone4 = "🤹🏾"
    juggling_tone4 = "🤹🏾"
    juggler_tone4 = "🤹🏾"
    person_juggling_tone5 = "🤹🏿"
    juggling_tone5 = "🤹🏿"
    juggler_tone5 = "🤹🏿"
    woman_juggling = "🤹♀"
    woman_juggling_tone1 = "🤹🏻♀"
    woman_juggling_light_skin_tone = "🤹🏻♀"
    woman_juggling_tone2 = "🤹🏼♀"
    woman_juggling_medium_light_skin_tone = "🤹🏼♀"
    woman_juggling_tone3 = "🤹🏽♀"
    woman_juggling_medium_skin_tone = "🤹🏽♀"
    woman_juggling_tone4 = "🤹🏾♀"
    woman_juggling_medium_dark_skin_tone = "🤹🏾♀"
    woman_juggling_tone5 = "🤹🏿♀"
    woman_juggling_dark_skin_tone = "🤹🏿♀"
    man_juggling = "🤹♂"
    man_juggling_tone1 = "🤹🏻♂"
    man_juggling_light_skin_tone = "🤹🏻♂"
    man_juggling_tone2 = "🤹🏼♂"
    man_juggling_medium_light_skin_tone = "🤹🏼♂"
    man_juggling_tone3 = "🤹🏽♂"
    man_juggling_medium_skin_tone = "🤹🏽♂"
    man_juggling_tone4 = "🤹🏾♂"
    man_juggling_medium_dark_skin_tone = "🤹🏾♂"
    man_juggling_tone5 = "🤹🏿♂"
    man_juggling_dark_skin_tone = "🤹🏿♂"
    performing_arts = "🎭"
    art = "🎨"
    clapper = "🎬"
    microphone = "🎤"
    headphones = "🎧"
    musical_score = "🎼"
    musical_keyboard = "🎹"
    drum = "🥁"
    drum_with_drumsticks = "🥁"
    saxophone = "🎷"
    trumpet = "🎺"
    banjo = "🪕"
    guitar = "🎸"
    violin = "🎻"
    game_die = "🎲"
    chess_pawn = "♟"
    dart = "🎯"
    kite = "🪁"
    yo_yo = "🪀"
    bowling = "🎳"
    video_game = "🎮"
    slot_machine = "🎰"
    jigsaw = "🧩"
    red_car = "🚗"
    taxi = "🚕"
    blue_car = "🚙"
    bus = "🚌"
    trolleybus = "🚎"
    race_car = "🏎"
    racing_car = "🏎"
    police_car = "🚓"
    ambulance = "🚑"
    fire_engine = "🚒"
    minibus = "🚐"
    truck = "🚚"
    articulated_lorry = "🚛"
    tractor = "🚜"
    auto_rickshaw = "🛺"
    motor_scooter = "🛵"
    motorbike = "🛵"
    motorcycle = "🏍"
    racing_motorcycle = "🏍"
    scooter = "🛴"
    bike = "🚲"
    motorized_wheelchair = "🦼"
    manual_wheelchair = "🦽"
    rotating_light = "🚨"
    oncoming_police_car = "🚔"
    oncoming_bus = "🚍"
    oncoming_automobile = "🚘"
    oncoming_taxi = "🚖"
    aerial_tramway = "🚡"
    mountain_cableway = "🚠"
    suspension_railway = "🚟"
    railway_car = "🚃"
    train = "🚋"
    mountain_railway = "🚞"
    monorail = "🚝"
    bullettrain_side = "🚄"
    bullettrain_front = "🚅"
    light_rail = "🚈"
    steam_locomotive = "🚂"
    train2 = "🚆"
    metro = "🚇"
    tram = "🚊"
    station = "🚉"
    airplane = "✈"
    airplane_departure = "🛫"
    airplane_arriving = "🛬"
    airplane_small = "🛩"
    small_airplane = "🛩"
    seat = "💺"
    satellite_orbital = "🛰"
    rocket = "🚀"
    flying_saucer = "🛸"
    helicopter = "🚁"
    canoe = "🛶"
    kayak = "🛶"
    sailboat = "⛵"
    speedboat = "🚤"
    motorboat = "🛥"
    cruise_ship = "🛳"
    passenger_ship = "🛳"
    ferry = "⛴"
    ship = "🚢"
    anchor = "⚓"
    fuelpump = "⛽"
    construction = "🚧"
    vertical_traffic_light = "🚦"
    traffic_light = "🚥"
    busstop = "🚏"
    map = "🗺"
    world_map = "🗺"
    moyai = "🗿"
    statue_of_liberty = "🗽"
    tokyo_tower = "🗼"
    european_castle = "🏰"
    japanese_castle = "🏯"
    stadium = "🏟"
    ferris_wheel = "🎡"
    roller_coaster = "🎢"
    carousel_horse = "🎠"
    fountain = "⛲"
    beach_umbrella = "⛱"
    umbrella_on_ground = "⛱"
    beach = "🏖"
    beach_with_umbrella = "🏖"
    island = "🏝"
    desert_island = "🏝"
    desert = "🏜"
    volcano = "🌋"
    mountain = "⛰"
    mountain_snow = "🏔"
    snow_capped_mountain = "🏔"
    mount_fuji = "🗻"
    camping = "🏕"
    tent = "⛺"
    house = "🏠"
    house_with_garden = "🏡"
    homes = "🏘"
    house_buildings = "🏘"
    house_abandoned = "🏚"
    derelict_house_building = "🏚"
    construction_site = "🏗"
    building_construction = "🏗"
    factory = "🏭"
    office = "🏢"
    department_store = "🏬"
    post_office = "🏣"
    european_post_office = "🏤"
    hospital = "🏥"
    bank = "🏦"
    hotel = "🏨"
    convenience_store = "🏪"
    school = "🏫"
    love_hotel = "🏩"
    wedding = "💒"
    classical_building = "🏛"
    church = "⛪"
    mosque = "🕌"
    hindu_temple = "🛕"
    synagogue = "🕍"
    kaaba = "🕋"
    shinto_shrine = "⛩"
    railway_track = "🛤"
    railroad_track = "🛤"
    motorway = "🛣"
    japan = "🗾"
    rice_scene = "🎑"
    park = "🏞"
    national_park = "🏞"
    sunrise = "🌅"
    sunrise_over_mountains = "🌄"
    stars = "🌠"
    sparkler = "🎇"
    fireworks = "🎆"
    city_sunset = "🌇"
    city_sunrise = "🌇"
    city_dusk = "🌆"
    cityscape = "🏙"
    night_with_stars = "🌃"
    milky_way = "🌌"
    bridge_at_night = "🌉"
    foggy = "🌁"
    watch = "⌚"
    iphone = "📱"
    calling = "📲"
    computer = "💻"
    keyboard = "⌨"
    desktop = "🖥"
    desktop_computer = "🖥"
    printer = "🖨"
    mouse_three_button = "🖱"
    three_button_mouse = "🖱"
    trackball = "🖲"
    joystick = "🕹"
    compression = "🗜"
    minidisc = "💽"
    floppy_disk = "💾"
    cd = "💿"
    dvd = "📀"
    vhs = "📼"
    camera = "📷"
    camera_with_flash = "📸"
    video_camera = "📹"
    movie_camera = "🎥"
    projector = "📽"
    film_projector = "📽"
    film_frames = "🎞"
    telephone_receiver = "📞"
    telephone = "☎"
    pager = "📟"
    fax = "📠"
    tv = "📺"
    radio = "📻"
    microphone2 = "🎙"
    studio_microphone = "🎙"
    level_slider = "🎚"
    control_knobs = "🎛"
    compass = "🧭"
    stopwatch = "⏱"
    timer = "⏲"
    timer_clock = "⏲"
    alarm_clock = "⏰"
    clock = "🕰"
    mantlepiece_clock = "🕰"
    hourglass = "⌛"
    hourglass_flowing_sand = "⏳"
    satellite = "📡"
    battery = "🔋"
    electric_plug = "🔌"
    bulb = "💡"
    flashlight = "🔦"
    candle = "🕯"
    fire_extinguisher = "🧯"
    oil = "🛢"
    oil_drum = "🛢"
    money_with_wings = "💸"
    dollar = "💵"
    yen = "💴"
    euro = "💶"
    pound = "💷"
    moneybag = "💰"
    credit_card = "💳"
    gem = "💎"
    scales = "⚖"
    toolbox = "🧰"
    wrench = "🔧"
    hammer = "🔨"
    hammer_pick = "⚒"
    hammer_and_pick = "⚒"
    tools = "🛠"
    hammer_and_wrench = "🛠"
    pick = "⛏"
    nut_and_bolt = "🔩"
    gear = "⚙"
    bricks = "🧱"
    chains = "⛓"
    magnet = "🧲"
    gun = "🔫"
    bomb = "💣"
    firecracker = "🧨"
    axe = "🪓"
    razor = "🪒"
    knife = "🔪"
    dagger = "🗡"
    dagger_knife = "🗡"
    crossed_swords = "⚔"
    shield = "🛡"
    smoking = "🚬"
    coffin = "⚰"
    urn = "⚱"
    funeral_urn = "⚱"
    amphora = "🏺"
    diya_lamp = "🪔"
    crystal_ball = "🔮"
    prayer_beads = "📿"
    nazar_amulet = "🧿"
    barber = "💈"
    alembic = "⚗"
    telescope = "🔭"
    microscope = "🔬"
    hole = "🕳"
    probing_cane = "🦯"
    stethoscope = "🩺"
    adhesive_bandage = "🩹"
    pill = "💊"
    syringe = "💉"
    drop_of_blood = "🩸"
    dna = "🧬"
    microbe = "🦠"
    petri_dish = "🧫"
    test_tube = "🧪"
    thermometer = "🌡"
    chair = "🪑"
    broom = "🧹"
    basket = "🧺"
    roll_of_paper = "🧻"
    toilet = "🚽"
    potable_water = "🚰"
    shower = "🚿"
    bathtub = "🛁"
    bath = "🛀"
    bath_tone1 = "🛀🏻"
    bath_tone2 = "🛀🏼"
    bath_tone3 = "🛀🏽"
    bath_tone4 = "🛀🏾"
    bath_tone5 = "🛀🏿"
    soap = "🧼"
    sponge = "🧽"
    squeeze_bottle = "🧴"
    bellhop = "🛎"
    bellhop_bell = "🛎"
    key = "🔑"
    key2 = "🗝"
    old_key = "🗝"
    door = "🚪"
    couch = "🛋"
    couch_and_lamp = "🛋"
    bed = "🛏"
    sleeping_accommodation = "🛌"
    person_in_bed_tone1 = "🛌🏻"
    person_in_bed_light_skin_tone = "🛌🏻"
    person_in_bed_tone2 = "🛌🏼"
    person_in_bed_medium_light_skin_tone = "🛌🏼"
    person_in_bed_tone3 = "🛌🏽"
    person_in_bed_medium_skin_tone = "🛌🏽"
    person_in_bed_tone4 = "🛌🏾"
    person_in_bed_medium_dark_skin_tone = "🛌🏾"
    person_in_bed_tone5 = "🛌🏿"
    person_in_bed_dark_skin_tone = "🛌🏿"
    teddy_bear = "🧸"
    frame_photo = "🖼"
    frame_with_picture = "🖼"
    shopping_bags = "🛍"
    shopping_cart = "🛒"
    shopping_trolley = "🛒"
    gift = "🎁"
    balloon = "🎈"
    flags = "🎏"
    ribbon = "🎀"
    confetti_ball = "🎊"
    tada = "🎉"
    dolls = "🎎"
    izakaya_lantern = "🏮"
    wind_chime = "🎐"
    red_envelope = "🧧"
    envelope = "✉"
    envelope_with_arrow = "📩"
    incoming_envelope = "📨"
    e_mail = "📧"
    email = "📧"
    love_letter = "💌"
    inbox_tray = "📥"
    outbox_tray = "📤"
    package = "📦"
    label = "🏷"
    mailbox_closed = "📪"
    mailbox = "📫"
    mailbox_with_mail = "📬"
    mailbox_with_no_mail = "📭"
    postbox = "📮"
    postal_horn = "📯"
    scroll = "📜"
    page_with_curl = "📃"
    page_facing_up = "📄"
    bookmark_tabs = "📑"
    receipt = "🧾"
    bar_chart = "📊"
    chart_with_upwards_trend = "📈"
    chart_with_downwards_trend = "📉"
    notepad_spiral = "🗒"
    spiral_note_pad = "🗒"
    calendar_spiral = "🗓"
    spiral_calendar_pad = "🗓"
    calendar = "📆"
    date = "📅"
    wastebasket = "🗑"
    card_index = "📇"
    card_box = "🗃"
    card_file_box = "🗃"
    ballot_box = "🗳"
    ballot_box_with_ballot = "🗳"
    file_cabinet = "🗄"
    clipboard = "📋"
    file_folder = "📁"
    open_file_folder = "📂"
    dividers = "🗂"
    card_index_dividers = "🗂"
    newspaper2 = "🗞"
    rolled_up_newspaper = "🗞"
    newspaper = "📰"
    notebook = "📓"
    notebook_with_decorative_cover = "📔"
    ledger = "📒"
    closed_book = "📕"
    green_book = "📗"
    blue_book = "📘"
    orange_book = "📙"
    books = "📚"
    book = "📖"
    bookmark = "🔖"
    safety_pin = "🧷"
    link = "🔗"
    paperclip = "📎"
    paperclips = "🖇"
    linked_paperclips = "🖇"
    triangular_ruler = "📐"
    straight_ruler = "📏"
    abacus = "🧮"
    pushpin = "📌"
    round_pushpin = "📍"
    scissors = "✂"
    pen_ballpoint = "🖊"
    lower_left_ballpoint_pen = "🖊"
    pen_fountain = "🖋"
    lower_left_fountain_pen = "🖋"
    black_nib = "✒"
    paintbrush = "🖌"
    lower_left_paintbrush = "🖌"
    crayon = "🖍"
    lower_left_crayon = "🖍"
    pencil = "📝"
    memo = "📝"
    pencil2 = "✏"
    mag = "🔍"
    mag_right = "🔎"
    lock_with_ink_pen = "🔏"
    closed_lock_with_key = "🔐"
    lock = "🔒"
    unlock = "🔓"
    heart = "❤"
    orange_heart = "🧡"
    yellow_heart = "💛"
    green_heart = "💚"
    blue_heart = "💙"
    purple_heart = "💜"
    black_heart = "🖤"
    brown_heart = "🤎"
    white_heart = "🤍"
    broken_heart = "💔"
    heart_exclamation = "❣"
    heavy_heart_exclamation_mark_ornament = "❣"
    two_hearts = "💕"
    revolving_hearts = "💞"
    heartbeat = "💓"
    heartpulse = "💗"
    sparkling_heart = "💖"
    cupid = "💘"
    gift_heart = "💝"
    heart_decoration = "💟"
    peace = "☮"
    peace_symbol = "☮"
    cross = "✝"
    latin_cross = "✝"
    star_and_crescent = "☪"
    om_symbol = "🕉"
    wheel_of_dharma = "☸"
    star_of_david = "✡"
    six_pointed_star = "🔯"
    menorah = "🕎"
    yin_yang = "☯"
    orthodox_cross = "☦"
    place_of_worship = "🛐"
    worship_symbol = "🛐"
    ophiuchus = "⛎"
    aries = "♈"
    taurus = "♉"
    gemini = "♊"
    cancer = "♋"
    leo = "♌"
    virgo = "♍"
    libra = "♎"
    scorpius = "♏"
    sagittarius = "♐"
    capricorn = "♑"
    aquarius = "♒"
    pisces = "♓"
    id = "🆔"
    atom = "⚛"
    atom_symbol = "⚛"
    accept = "🉑"
    radioactive = "☢"
    radioactive_sign = "☢"
    biohazard = "☣"
    biohazard_sign = "☣"
    mobile_phone_off = "📴"
    vibration_mode = "📳"
    u6709 = "🈶"
    u7121 = "🈚"
    u7533 = "🈸"
    u55b6 = "🈺"
    u6708 = "🈷"
    eight_pointed_black_star = "✴"
    vs = "🆚"
    white_flower = "💮"
    ideograph_advantage = "🉐"
    secret = "㊙"
    congratulations = "㊗"
    u6e80 = "🈵"
    u5272 = "🈹"
    u7981 = "🈲"
    a = "🅰"
    b = "🅱"
    ab = "🆎"
    cl = "🆑"
    o2 = "🅾"
    sos = "🆘"
    x = "❌"
    o = "⭕"
    octagonal_sign = "🛑"
    stop_sign = "🛑"
    no_entry = "⛔"
    name_badge = "📛"
    no_entry_sign = "🚫"
    anger = "💢"
    hotsprings = "♨"
    no_pedestrians = "🚷"
    do_not_litter = "🚯"
    no_bicycles = "🚳"
    non_potable_water = "🚱"
    underage = "🔞"
    no_mobile_phones = "📵"
    no_smoking = "🚭"
    exclamation = "❗"
    grey_exclamation = "❕"
    question = "❓"
    grey_question = "❔"
    bangbang = "‼"
    interrobang = "⁉"
    low_brightness = "🔅"
    high_brightness = "🔆"
    part_alternation_mark = "〽"
    warning = "⚠"
    children_crossing = "🚸"
    trident = "🔱"
    fleur_de_lis = "⚜"
    beginner = "🔰"
    recycle = "♻"
    white_check_mark = "✅"
    u6307 = "🈯"
    chart = "💹"
    sparkle = "❇"
    eight_spoked_asterisk = "✳"
    negative_squared_cross_mark = "❎"
    globe_with_meridians = "🌐"
    diamond_shape_with_a_dot_inside = "💠"
    m = "Ⓜ"
    cyclone = "🌀"
    zzz = "💤"
    atm = "🏧"
    wc = "🚾"
    wheelchair = "♿"
    parking = "🅿"
    u7a7a = "🈳"
    sa = "🈂"
    customs = "🛃"
    baggage_claim = "🛄"
    left_luggage = "🛅"
    mens = "🚹"
    womens = "🚺"
    baby_symbol = "🚼"
    restroom = "🚻"
    put_litter_in_its_place = "🚮"
    cinema = "🎦"
    signal_strength = "📶"
    koko = "🈁"
    symbols = "🔣"
    information_source = "ℹ"
    abc = "🔤"
    abcd = "🔡"
    capital_abcd = "🔠"
    ng = "🆖"
    ok = "🆗"
    up = "🆙"
    cool = "🆒"
    new = "🆕"
    free = "🆓"
    zero = "0️⃣"
    one = "1️⃣"
    two = "2️⃣"
    three = "3️⃣"
    four = "4️⃣"
    five = "5️⃣"
    six = "6️⃣"
    seven = "7️⃣"
    eight = "8️⃣"
    nine = "9️⃣"
    keycap_ten = "🔟"
    hash = "#️⃣"
    keycap_asterisk = "*️⃣"
    eject = "⏏"
    eject_symbol = "⏏"
    arrow_forward = "▶"
    pause_button = "⏸"
    double_vertical_bar = "⏸"
    play_pause = "⏯"
    stop_button = "⏹"
    record_button = "⏺"
    track_next = "⏭"
    next_track = "⏭"
    track_previous = "⏮"
    previous_track = "⏮"
    fast_forward = "⏩"
    rewind = "⏪"
    arrow_double_up = "⏫"
    arrow_double_down = "⏬"
    arrow_backward = "◀"
    arrow_up_small = "🔼"
    arrow_down_small = "🔽"
    arrow_right = "➡"
    arrow_left = "⬅"
    arrow_up = "⬆"
    arrow_down = "⬇"
    arrow_upper_right = "↗"
    arrow_lower_right = "↘"
    arrow_lower_left = "↙"
    arrow_upper_left = "↖"
    arrow_up_down = "↕"
    left_right_arrow = "↔"
    arrow_right_hook = "↪"
    leftwards_arrow_with_hook = "↩"
    arrow_heading_up = "⤴"
    arrow_heading_down = "⤵"
    twisted_rightwards_arrows = "🔀"
    repeat = "🔁"
    repeat_one = "🔂"
    arrows_counterclockwise = "🔄"
    arrows_clockwise = "🔃"
    musical_note = "🎵"
    notes = "🎶"
    heavy_plus_sign = "➕"
    heavy_minus_sign = "➖"
    heavy_division_sign = "➗"
    heavy_multiplication_x = "✖"
    infinity = "♾"
    heavy_dollar_sign = "💲"
    currency_exchange = "💱"
    tm = "™"
    copyright = "©"
    registered = "®"
    wavy_dash = "〰"
    curly_loop = "➰"
    loop = "➿"
    end = "🔚"
    back = "🔙"
    on = "🔛"
    top = "🔝"
    soon = "🔜"
    heavy_check_mark = "✔"
    ballot_box_with_check = "☑"
    radio_button = "🔘"
    white_circle = "⚪"
    black_circle = "⚫"
    red_circle = "🔴"
    blue_circle = "🔵"
    brown_circle = "🟤"
    purple_circle = "🟣"
    green_circle = "🟢"
    yellow_circle = "🟡"
    orange_circle = "🟠"
    small_red_triangle = "🔺"
    small_red_triangle_down = "🔻"
    small_orange_diamond = "🔸"
    small_blue_diamond = "🔹"
    large_orange_diamond = "🔶"
    large_blue_diamond = "🔷"
    white_square_button = "🔳"
    black_square_button = "🔲"
    black_small_square = "▪"
    white_small_square = "▫"
    black_medium_small_square = "◾"
    white_medium_small_square = "◽"
    black_medium_square = "◼"
    white_medium_square = "◻"
    black_large_square = "⬛"
    white_large_square = "⬜"
    orange_square = "🟧"
    blue_square = "🟦"
    red_square = "🟥"
    brown_square = "🟫"
    purple_square = "🟪"
    green_square = "🟩"
    yellow_square = "🟨"
    speaker = "🔈"
    mute = "🔇"
    sound = "🔉"
    loud_sound = "🔊"
    bell = "🔔"
    no_bell = "🔕"
    mega = "📣"
    loudspeaker = "📢"
    speech_left = "🗨"
    left_speech_bubble = "🗨"
    eye_in_speech_bubble = "👁🗨"
    speech_balloon = "💬"
    thought_balloon = "💭"
    anger_right = "🗯"
    right_anger_bubble = "🗯"
    spades = "♠"
    clubs = "♣"
    hearts = "♥"
    diamonds = "♦"
    black_joker = "🃏"
    flower_playing_cards = "🎴"
    mahjong = "🀄"
    clock1 = "🕐"
    clock2 = "🕑"
    clock3 = "🕒"
    clock4 = "🕓"
    clock5 = "🕔"
    clock6 = "🕕"
    clock7 = "🕖"
    clock8 = "🕗"
    clock9 = "🕘"
    clock10 = "🕙"
    clock11 = "🕚"
    clock12 = "🕛"
    clock130 = "🕜"
    clock230 = "🕝"
    clock330 = "🕞"
    clock430 = "🕟"
    clock530 = "🕠"
    clock630 = "🕡"
    clock730 = "🕢"
    clock830 = "🕣"
    clock930 = "🕤"
    clock1030 = "🕥"
    clock1130 = "🕦"
    clock1230 = "🕧"
    female_sign = "♀"
    male_sign = "♂"
    medical_symbol = "⚕"
    regional_indicator_z = "🇿"
    regional_indicator_y = "🇾"
    regional_indicator_x = "🇽"
    regional_indicator_w = "🇼"
    regional_indicator_v = "🇻"
    regional_indicator_u = "🇺"
    regional_indicator_t = "🇹"
    regional_indicator_s = "🇸"
    regional_indicator_r = "🇷"
    regional_indicator_q = "🇶"
    regional_indicator_p = "🇵"
    regional_indicator_o = "🇴"
    regional_indicator_n = "🇳"
    regional_indicator_m = "🇲"
    regional_indicator_l = "🇱"
    regional_indicator_k = "🇰"
    regional_indicator_j = "🇯"
    regional_indicator_i = "🇮"
    regional_indicator_h = "🇭"
    regional_indicator_g = "🇬"
    regional_indicator_f = "🇫"
    regional_indicator_e = "🇪"
    regional_indicator_d = "🇩"
    regional_indicator_c = "🇨"
    regional_indicator_b = "🇧"
    regional_indicator_a = "🇦"
    flag_white = "🏳"
    flag_black = "🏴"
    checkered_flag = "🏁"
    triangular_flag_on_post = "🚩"
    rainbow_flag = "🏳🌈"
    gay_pride_flag = "🏳🌈"
    pirate_flag = "🏴☠"
    flag_af = "🇦🇫"
    flag_ax = "🇦🇽"
    flag_al = "🇦🇱"
    flag_dz = "🇩🇿"
    flag_as = "🇦🇸"
    flag_ad = "🇦🇩"
    flag_ao = "🇦🇴"
    flag_ai = "🇦🇮"
    flag_aq = "🇦🇶"
    flag_ag = "🇦🇬"
    flag_ar = "🇦🇷"
    flag_am = "🇦🇲"
    flag_aw = "🇦🇼"
    flag_au = "🇦🇺"
    flag_at = "🇦🇹"
    flag_az = "🇦🇿"
    flag_bs = "🇧🇸"
    flag_bh = "🇧🇭"
    flag_bd = "🇧🇩"
    flag_bb = "🇧🇧"
    flag_by = "🇧🇾"
    flag_be = "🇧🇪"
    flag_bz = "🇧🇿"
    flag_bj = "🇧🇯"
    flag_bm = "🇧🇲"
    flag_bt = "🇧🇹"
    flag_bo = "🇧🇴"
    flag_ba = "🇧🇦"
    flag_bw = "🇧🇼"
    flag_br = "🇧🇷"
    flag_io = "🇮🇴"
    flag_vg = "🇻🇬"
    flag_bn = "🇧🇳"
    flag_bg = "🇧🇬"
    flag_bf = "🇧🇫"
    flag_bi = "🇧🇮"
    flag_kh = "🇰🇭"
    flag_cm = "🇨🇲"
    flag_ca = "🇨🇦"
    flag_ic = "🇮🇨"
    flag_cv = "🇨🇻"
    flag_bq = "🇧🇶"
    flag_ky = "🇰🇾"
    flag_cf = "🇨🇫"
    flag_td = "🇹🇩"
    flag_cl = "🇨🇱"
    flag_cn = "🇨🇳"
    flag_cx = "🇨🇽"
    flag_cc = "🇨🇨"
    flag_co = "🇨🇴"
    flag_km = "🇰🇲"
    flag_cg = "🇨🇬"
    flag_cd = "🇨🇩"
    flag_ck = "🇨🇰"
    flag_cr = "🇨🇷"
    flag_ci = "🇨🇮"
    flag_hr = "🇭🇷"
    flag_cu = "🇨🇺"
    flag_cw = "🇨🇼"
    flag_cy = "🇨🇾"
    flag_cz = "🇨🇿"
    flag_dk = "🇩🇰"
    flag_dj = "🇩🇯"
    flag_dm = "🇩🇲"
    flag_do = "🇩🇴"
    flag_ec = "🇪🇨"
    flag_eg = "🇪🇬"
    flag_sv = "🇸🇻"
    flag_gq = "🇬🇶"
    flag_er = "🇪🇷"
    flag_ee = "🇪🇪"
    flag_et = "🇪🇹"
    flag_eu = "🇪🇺"
    flag_fk = "🇫🇰"
    flag_fo = "🇫🇴"
    flag_fj = "🇫🇯"
    flag_fi = "🇫🇮"
    flag_fr = "🇫🇷"
    flag_gf = "🇬🇫"
    flag_pf = "🇵🇫"
    flag_tf = "🇹🇫"
    flag_ga = "🇬🇦"
    flag_gm = "🇬🇲"
    flag_ge = "🇬🇪"
    flag_de = "🇩🇪"
    flag_gh = "🇬🇭"
    flag_gi = "🇬🇮"
    flag_gr = "🇬🇷"
    flag_gl = "🇬🇱"
    flag_gd = "🇬🇩"
    flag_gp = "🇬🇵"
    flag_gu = "🇬🇺"
    flag_gt = "🇬🇹"
    flag_gg = "🇬🇬"
    flag_gn = "🇬🇳"
    flag_gw = "🇬🇼"
    flag_gy = "🇬🇾"
    flag_ht = "🇭🇹"
    flag_hn = "🇭🇳"
    flag_hk = "🇭🇰"
    flag_hu = "🇭🇺"
    flag_is = "🇮🇸"
    flag_in = "🇮🇳"
    flag_id = "🇮🇩"
    flag_ir = "🇮🇷"
    flag_iq = "🇮🇶"
    flag_ie = "🇮🇪"
    flag_im = "🇮🇲"
    flag_il = "🇮🇱"
    flag_it = "🇮🇹"
    flag_jm = "🇯🇲"
    flag_jp = "🇯🇵"
    crossed_flags = "🎌"
    flag_je = "🇯🇪"
    flag_jo = "🇯🇴"
    flag_kz = "🇰🇿"
    flag_ke = "🇰🇪"
    flag_ki = "🇰🇮"
    flag_xk = "🇽🇰"
    flag_kw = "🇰🇼"
    flag_kg = "🇰🇬"
    flag_la = "🇱🇦"
    flag_lv = "🇱🇻"
    flag_lb = "🇱🇧"
    flag_ls = "🇱🇸"
    flag_lr = "🇱🇷"
    flag_ly = "🇱🇾"
    flag_li = "🇱🇮"
    flag_lt = "🇱🇹"
    flag_lu = "🇱🇺"
    flag_mo = "🇲🇴"
    flag_mk = "🇲🇰"
    flag_mg = "🇲🇬"
    flag_mw = "🇲🇼"
    flag_my = "🇲🇾"
    flag_mv = "🇲🇻"
    flag_ml = "🇲🇱"
    flag_mt = "🇲🇹"
    flag_mh = "🇲🇭"
    flag_mq = "🇲🇶"
    flag_mr = "🇲🇷"
    flag_mu = "🇲🇺"
    flag_yt = "🇾🇹"
    flag_mx = "🇲🇽"
    flag_fm = "🇫🇲"
    flag_md = "🇲🇩"
    flag_mc = "🇲🇨"
    flag_mn = "🇲🇳"
    flag_me = "🇲🇪"
    flag_ms = "🇲🇸"
    flag_ma = "🇲🇦"
    flag_mz = "🇲🇿"
    flag_mm = "🇲🇲"
    flag_na = "🇳🇦"
    flag_nr = "🇳🇷"
    flag_np = "🇳🇵"
    flag_nl = "🇳🇱"
    flag_nc = "🇳🇨"
    flag_nz = "🇳🇿"
    flag_ni = "🇳🇮"
    flag_ne = "🇳🇪"
    flag_ng = "🇳🇬"
    flag_nu = "🇳🇺"
    flag_nf = "🇳🇫"
    flag_kp = "🇰🇵"
    flag_mp = "🇲🇵"
    flag_no = "🇳🇴"
    flag_om = "🇴🇲"
    flag_pk = "🇵🇰"
    flag_pw = "🇵🇼"
    flag_ps = "🇵🇸"
    flag_pa = "🇵🇦"
    flag_pg = "🇵🇬"
    flag_py = "🇵🇾"
    flag_pe = "🇵🇪"
    flag_ph = "🇵🇭"
    flag_pn = "🇵🇳"
    flag_pl = "🇵🇱"
    flag_pt = "🇵🇹"
    flag_pr = "🇵🇷"
    flag_qa = "🇶🇦"
    flag_re = "🇷🇪"
    flag_ro = "🇷🇴"
    flag_ru = "🇷🇺"
    flag_rw = "🇷🇼"
    flag_ws = "🇼🇸"
    flag_sm = "🇸🇲"
    flag_st = "🇸🇹"
    flag_sa = "🇸🇦"
    flag_sn = "🇸🇳"
    flag_rs = "🇷🇸"
    flag_sc = "🇸🇨"
    flag_sl = "🇸🇱"
    flag_sg = "🇸🇬"
    flag_sx = "🇸🇽"
    flag_sk = "🇸🇰"
    flag_si = "🇸🇮"
    flag_gs = "🇬🇸"
    flag_sb = "🇸🇧"
    flag_so = "🇸🇴"
    flag_za = "🇿🇦"
    flag_kr = "🇰🇷"
    flag_ss = "🇸🇸"
    flag_es = "🇪🇸"
    flag_lk = "🇱🇰"
    flag_bl = "🇧🇱"
    flag_sh = "🇸🇭"
    flag_kn = "🇰🇳"
    flag_lc = "🇱🇨"
    flag_pm = "🇵🇲"
    flag_vc = "🇻🇨"
    flag_sd = "🇸🇩"
    flag_sr = "🇸🇷"
    flag_sz = "🇸🇿"
    flag_se = "🇸🇪"
    flag_ch = "🇨🇭"
    flag_sy = "🇸🇾"
    flag_tw = "🇹🇼"
    flag_tj = "🇹🇯"
    flag_tz = "🇹🇿"
    flag_th = "🇹🇭"
    flag_tl = "🇹🇱"
    flag_tg = "🇹🇬"
    flag_tk = "🇹🇰"
    flag_to = "🇹🇴"
    flag_tt = "🇹🇹"
    flag_tn = "🇹🇳"
    flag_tr = "🇹🇷"
    flag_tm = "🇹🇲"
    flag_tc = "🇹🇨"
    flag_vi = "🇻🇮"
    flag_tv = "🇹🇻"
    flag_ug = "🇺🇬"
    flag_ua = "🇺🇦"
    flag_ae = "🇦🇪"
    flag_gb = "🇬🇧"
    england = "🏴"
    scotland = "🏴"
    wales = "🏴"
    flag_us = "🇺🇸"
    flag_uy = "🇺🇾"
    flag_uz = "🇺🇿"
    flag_vu = "🇻🇺"
    flag_va = "🇻🇦"
    flag_ve = "🇻🇪"
    flag_vn = "🇻🇳"
    flag_wf = "🇼🇫"
    flag_eh = "🇪🇭"
    flag_ye = "🇾🇪"
    flag_zm = "🇿🇲"
    flag_zw = "🇿🇼"
    flag_ac = "🇦🇨"
    flag_bv = "🇧🇻"
    flag_cp = "🇨🇵"
    flag_ea = "🇪🇦"
    flag_dg = "🇩🇬"
    flag_hm = "🇭🇲"
    flag_mf = "🇲🇫"
    flag_sj = "🇸🇯"
    flag_ta = "🇹🇦"
    flag_um = "🇺🇲"
    united_nations = "🇺🇳"


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
