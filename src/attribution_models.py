#%%

def last_click_attribution(group):
    last_click = group[group['click'] == 1].sort_values('timestamp').iloc[-1:]
    return last_click[['conversion_id', 'campaign']].assign(weight=1.0)

last_click_results = conversion_paths.apply(last_click_attribution).reset_index(drop=True)


