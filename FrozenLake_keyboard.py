# 콘솔에서 실행해야함
# import sys, tty, termios -> 리눅스, 맥에서 사용하는 모듈
import msvcrt # -> 윈도우에서 사용하는 모듈
import gym
from gym.envs.registration import register

class _Getch:
    def __call__(self):
        keyy = msvcrt.getch()
        return msvcrt.getch()

inkey = _Getch()

# MACROS
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

# Key mapping
arrow_keys = {  # 윈도우에서 키를 할당하기 위해서 쓰는 문자 리눅스, 맥이랑 다름
    b'H': UP,
    b'P': DOWN,
    b'M': RIGHT,
    b'K': LEFT
}

# Register FrozenLake with is_slippery False
register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False}
)

env = gym.make('FrozenLake-v3')
env.render() # Show the initial board

while True:
    # Choose an action from keyboard
    key = inkey()
    if key not in arrow_keys.keys():
        print("Game abroted!")
        break

    action = arrow_keys[key]
    state, reward, done, info = env.step(action)
    env.render() # Show the board after action
    print("state: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)

    if done:
        print("Finished with reward", reward)
        break
