import gym
import numpy as np
import matplotlib.pyplot as plt
from gym.envs.registration import register
import random as pr
def rargmax(vector):
    """ if the number of maximum values are more than two, choosing random value in maximum """
    m = np.amax(vector)                  # array의 최댓값 반환 함수
    indices = np.nonzero(vector == m)[0] # vector의 배열중에 0이 아닌 m(최댓값)을 가지는 인덱스를 반환시킴, [0]의 의미는array 형태가 아니라 리스트 형태로return 하려고 쓴것
    return pr.choice(indices)

register(id='FrozenLake-v3',
         entry_point='gym.envs.toy_text:FrozenLakeEnv',
         kwargs={'map_name':'4x4','is_slippery':False})

env = gym.make('FrozenLake-v3')

# Q 만들기
Q = np.zeros([env.observation_space.n, env.action_space.n])
# 학습 횟수
num_episodes = 2000

# 학습 알고리즘 만들기
rList = [] # 리워드 확인용
for i in range(num_episodes):
    state = env.reset()
    rAll = 0
    done = False
    # Q-Table learning 알고리즘
    while not done:
        action = rargmax(Q[state, :])
        new_state, reward, done,_ = env.step(action)
        Q[state, action] = reward + np.max(Q[new_state, :])
        rAll += reward
        state = new_state
    rList.append(rAll)

print("Success rate: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print("LEFT DOWN RIGHT UP")
print(Q)
plt.bar(range(len(rList)), rList, color="blue")
plt.show()