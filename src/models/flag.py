class _BitField(int):
    def bitwise_matches(self, match_against: int) -> bool:
        x = 1 << match_against
        return self & x == x


class ChannelFlag(_BitField):
    # https://discord.com/developers/docs/resources/channel#channel-object-channel-flags

    @property
    def pinned(self) -> bool:
        return self.bitwise_matches(1)


class SystemChannelFlags(_BitField):
    def supress_join_notifications(self) -> bool:
        return self.bitwise_matches(0)

    def supress_premium_subscriptions(self) -> bool:
        return self.bitwise_matches(1)

    def supress_guild_reminder_notifications(self) -> bool:
        return self.bitwise_matches(2)

    def supress_join_notification_replies(self) -> bool:
        return self.bitwise_matches(3)


class MessageFlags(_BitField):
    @property
    def cross_posted(self) -> bool:
        return self.bitwise_matches(0)

    @property
    def is_cross_post(self) -> bool:
        return self.bitwise_matches(1)

    @property
    def supress_embeds(self) -> bool:
        return self.bitwise_matches(2)

    @property
    def source_message_deleted(self) -> bool:
        return self.bitwise_matches(3)

    @property
    def urgent(self) -> bool:
        return self.bitwise_matches(4)

    @property
    def has_thread(self) -> bool:
        return self.bitwise_matches(5)

    @property
    def ephemeral(self) -> bool:
        return self.bitwise_matches(6)

    @property
    def loading(self) -> bool:
        return self.bitwise_matches(7)

    @property
    def failed_to_mention_some_roles_in_thread(self) -> bool:
        return self.bitwise_matches(8)


class Permissions(_BitField):
    @property
    def create_instant_invite(self) -> bool:
        return self.bitwise_matches(0)

    @property
    def kick_members(self) -> bool:
        return self.bitwise_matches(1)

    @property
    def ban_members(self) -> bool:
        return self.bitwise_matches(2)

    @property
    def administrator(self) -> bool:
        return self.bitwise_matches(3)

    @property
    def manage_channels(self) -> bool:
        return self.bitwise_matches(4)

    @property
    def manage_guild(self) -> bool:
        return self.bitwise_matches(5)

    @property
    def add_reactions(self) -> bool:
        return self.bitwise_matches(6)

    @property
    def view_audit_log(self) -> bool:
        return self.bitwise_matches(7)

    @property
    def priority_speaker(self) -> bool:
        return self.bitwise_matches(8)

    @property
    def stream(self) -> bool:
        return self.bitwise_matches(9)

    @property
    def read_messages(self) -> bool:
        return self.bitwise_matches(10)

    @property
    def send_messages(self) -> bool:
        return self.bitwise_matches(11)

    @property
    def send_tts_messages(self) -> bool:
        return self.bitwise_matches(12)

    @property
    def manage_messages(self) -> bool:
        return self.bitwise_matches(13)

    @property
    def embed_links(self) -> bool:
        return self.bitwise_matches(14)

    @property
    def attach_files(self) -> bool:
        return self.bitwise_matches(15)

    @property
    def read_message_history(self) -> bool:
        return self.bitwise_matches(16)

    @property
    def mention_everyone(self) -> bool:
        return self.bitwise_matches(17)

    @property
    def external_emojis(self) -> bool:
        return self.bitwise_matches(18)

    @property
    def view_guild_insights(self) -> bool:
        return self.bitwise_matches(19)

    @property
    def connect(self) -> bool:
        return self.bitwise_matches(20)

    @property
    def speak(self) -> bool:
        return self.bitwise_matches(21)

    @property
    def mute_members(self) -> bool:
        return self.bitwise_matches(22)

    @property
    def deafen_members(self) -> bool:
        return self.bitwise_matches(23)

    @property
    def move_members(self) -> bool:
        return self.bitwise_matches(24)

    @property
    def use_voice_activation(self) -> bool:
        return self.bitwise_matches(25)

    @property
    def change_nickname(self) -> bool:
        return self.bitwise_matches(26)

    @property
    def manage_nicknames(self) -> bool:
        return self.bitwise_matches(27)

    @property
    def manage_roles(self) -> bool:
        return self.bitwise_matches(28)

    @property
    def manage_webhooks(self) -> bool:
        return self.bitwise_matches(29)

    @property
    def manage_emojis(self) -> bool:
        return self.bitwise_matches(30)

    @property
    def use_slash_commands(self) -> bool:
        return self.bitwise_matches(31)

    @property
    def request_to_speak(self) -> bool:
        return self.bitwise_matches(32)


class UserFlags(_BitField):
    # https://discord.com/developers/docs/resources/user#user-object-user-flags

    @property
    def staff(self) -> bool:
        return self.bitwise_matches(0)

    @property
    def partner(self) -> bool:
        return self.bitwise_matches(1)

    @property
    def hype_squad(self) -> bool:
        return self.bitwise_matches(2)

    @property
    def bug_hunter_level_1(self) -> bool:
        return self.bitwise_matches(3)

    @property
    def hypesquad_online_house_1(self) -> bool:
        return self.bitwise_matches(6)

    @property
    def hypesquad_online_house_2(self) -> bool:
        return self.bitwise_matches(7)

    @property
    def hypesquad_online_house_3(self) -> bool:
        return self.bitwise_matches(8)

    @property
    def premium_early_supporter(self) -> bool:
        return self.bitwise_matches(9)

    @property
    def team_pseudo_user(self) -> bool:
        return self.bitwise_matches(10)

    @property
    def bug_hunter_level_2(self) -> bool:
        return self.bitwise_matches(14)

    @property
    def verified_bot(self) -> bool:
        return self.bitwise_matches(16)

    @property
    def early_verified_developer(self) -> bool:
        return self.bitwise_matches(17)

    @property
    def certified_moderator(self) -> bool:
        return self.bitwise_matches(18)

    @property
    def bot_http_interactions(self) -> bool:
        return self.bitwise_matches(19)
