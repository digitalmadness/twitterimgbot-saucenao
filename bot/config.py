import os
import configparser
import codecs

'''get out of here stalker, edit settings.txt'''

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
config = configparser.ConfigParser() 
config.readfp(codecs.open('settings.txt','r',encoding='utf8'))
twitter_config = config['Twitter']
saucenao_config = config['Saucenao']
app_config = config['App']
autofollow_config = config['Autofollow']
api_key = twitter_config['api_key']
secret_key = twitter_config['secret_key']
token = twitter_config['token']
secret_token = twitter_config['secret_token']
source_folder = app_config['image_folder']
discard_size = int(app_config['discard_pic_if_less_than_x_kilobytes'])
interval = int(app_config['time_between_tweets'])
proxy = app_config['proxy']
min_followers = int(autofollow_config['minimum_followers_to_consider'])
custom_following_limit = int(autofollow_config['custom_following_limit'])
custom_unfollowing_limit = int(autofollow_config['custom_unfollowing_limit'])   
api_key_saucenao = saucenao_config['api_key_saucenao']
search_phrase = autofollow_config['search_phrase']
neural_opt = bool(int(app_config['enable_neural_network']))
unfollow_opt = bool(int(autofollow_config['enable_unfollow']))
followback_opt = bool(int(autofollow_config['follow_those_who_already_follow_you']))
like_opt = bool(int(autofollow_config['like_all_found_tweets']))
instafollowback_opt = bool(int(autofollow_config['instant_followback_in_stream_mode']))
unfollow_nofilter_opt = bool(int(autofollow_config['unfollow_people_doenst_followed_by_this_script']))
anime_avi_opt = bool(int(autofollow_config['follow_only_people_with_anime_profile_pictures']))
likeback_opt = bool(int(autofollow_config['when_user_likes_your_tweet_likeback_his_last_tweet']))
alt_config = config['AltAccount']
alt_key_saucenao = alt_config['api_key_saucenao_alt']
api_key_alt = alt_config['api_key_alt']
secret_key_alt = alt_config['secret_key_alt']
token_alt = alt_config['token_alt']
secret_token_alt = alt_config['secret_token_alt']
source_folder_alt = alt_config['image_folder_alt']
