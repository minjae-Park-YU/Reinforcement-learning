import gym
import readchar

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

arrow_keys = {
    '\x1b[A' : UP,
    '\x1b[B': DOWN,
    '\x1b[C': RIGHT,
    '\x1b[D': LEFT}

env = gym.make('FrozenLake-v0') # slippery 옵션이 활성화된 기본 FrozenLake 불러오기
env.render()
env.reset()   # 강의자료에는 없었지만, 이 부분 없으면 step이 진행이 안됨
while True:
    key = readchar.readkey()
    if key not in arrow_keys.keys():
        print("Game abroted!")
        break

    action = arrow_keys[key]
    state, reward, done, info = env.step(action)
    env.render()
    print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)

    if done:
        print("Finished with reward", reward)
        break