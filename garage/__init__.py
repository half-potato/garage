# Do not remove - impossible to install without

from gym.envs.registration import register
from . import envs

register(
    id='Gather-v0',
    entry_point='garage.envs.mujoco.gather:GatherEnv',
    max_episode_steps=5000,
    reward_threshold=3600.0,
)

register(
    id='AntGather-v0',
    entry_point='garage.envs.mujoco.gather:AntGatherEnv',
    max_episode_steps=5000,
    reward_threshold=3600.0,
)

register(
    id='PointGatherEnv-v0',
    entry_point='garage.envs.mujoco.gather:PointGatherEnv',
    max_episode_steps=5000,
    reward_threshold=3600.0,
)

register(
    id='SwimmerGatherEnv-v0',
    entry_point='garage.envs.mujoco.gather:SwimmerGatherEnv',
    max_episode_steps=5000,
    reward_threshold=3600.0,
)

register(
    id='SwimmerEnv-v0',
    entry_point='garage.envs.mujoco:SwimmerEnv',
    max_episode_steps=5000,
    reward_threshold=3600.0,
)

