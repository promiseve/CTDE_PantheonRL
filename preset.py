
def preset(args, preset_id):
    if preset_id == 1:
        if not args.tensorboard_log:
            args.tensorboard_log = 'logs'
        if not args.tensorboard_name:
            args.tensorboard_name = '%s-%s-%s%s-%d' % (
                args.env, args.env_config['layout_name'], args.ego, args.alt[0], args.seed)
        if not args.ego_save:
            args.ego_save = 'models/%s-%s-%s-ego-%d' % (
                args.env, args.env_config['layout_name'], args.ego, args.seed)
        if not args.alt_save:
            args.alt_save = 'models/%s-%s-%s-alt-%d' % (
                args.env, args.env_config['layout_name'], args.alt[0], args.seed)
        # if not args.record:
        #     args.record = 'trajs/%s-%s-%s%s-%d' % (args.env, args.env_config['layout_name'], args.ego, args.alt[0], args.seed)
    else:
        raise Exception("Invalid preset id")
    return args


"""
Partner Adaptation Workflow:

# Train bunch of partners
python3 trainer.py OvercookedMultiEnv-v0 PPO PPO --env-config '{"layout_name":"simple_o"}' --seed 10 --preset 1
python3 trainer.py OvercookedMultiEnv-v0 PPO PPO --env-config '{"layout_name":"simple_o"}' --seed 11 --preset 1
python3 trainer.py OvercookedMultiEnv-v0 PPO PPO --env-config '{"layout_name":"simple_o"}' --seed 12 --preset 1
python3 trainer.py OvercookedMultiEnv-v0 PPO PPO --env-config '{"layout_name":"simple_o"}' --seed 13 --preset 1
python3 trainer.py OvercookedMultiEnv-v0 PPO PPO --env-config '{"layout_name":"simple_o"}' --seed 14 --preset 1


# Train to play against group of partners
python3 trainer.py OvercookedMultiEnv-v0 PPO FIXED FIXED FIXED FIXED --alt-config \
    '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-10"}' \
    '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-11"}' \
    '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-12"}' \
    '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-13"}' \
    --env-config '{"layout_name":"simple_o"}' --seed 20 -t 1000000 --preset 1

python3 trainer.py OvercookedMultiEnv-v0 ModularAlgorithm FIXED FIXED FIXED FIXED --ego-config '{"marginal_reg_coef": 0.5}' --alt-config \
    '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-10"}' \
    '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-11"}' \
    '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-12"}' \
    '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-13"}' \
    --env-config '{"layout_name":"simple_o"}' --seed 21 -t 1000000 --preset 1


# Adapt to new partner
python3 trainer.py OvercookedMultiEnv-v0 PPO FIXED --alt-config '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-14"}' --env-config '{"layout_name":"simple_o"}' --seed 30 --preset 1

python3 trainer.py OvercookedMultiEnv-v0 LOAD FIXED --ego-config '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-ego-20"}' --alt-config '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-14"}' --env-config '{"layout_name":"simple_o"}' --seed 31 --preset 1

python3 trainer.py OvercookedMultiEnv-v0 LOAD FIXED --ego-config '{"type":"ModularAlgorithm", "location":"models/OvercookedMultiEnv-v0-simple_o-ModularAlgorithm-ego-21"}' --alt-config '{"type":"PPO", "location":"models/OvercookedMultiEnv-v0-simple_o-PPO-alt-14"}' --env-config '{"layout_name":"simple_o"}' --seed 32 --preset 1










"""
