from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
p = ROOT / 'data/tornadoes.csv'
d=pd.read_csv(p)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'bold','figure.facecolor':'#f8f8f5','axes.facecolor':'#f8f8f5'})
fig, axs=plt.subplots(2,2,figsize=(13,9),layout='constrained')
fig.suptitle('Tornadoes in the dataset',fontsize=21,fontweight='bold',x=.065,ha='left')
months=d.month.value_counts().sort_index(); ax=axs[0,0]
ax.bar(range(12),months.values,color=['#d98b56' if x==5 else '#456f78' for x in months.index]); ax.set_xticks(range(12),['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']); ax.set_title('May stands out'); ax.set_ylabel('Recorded tornadoes'); ax.text(4,1059+25,'1,059',ha='center',weight='bold'); ax.set_ylim(0,1200)
states=d.start_state.value_counts().head(8).sort_values(); ax=axs[0,1]; ax.barh(states.index,states.values,color='#456f78'); ax.set_title('Most common starting states'); ax.set_xlabel('Recorded tornadoes'); ax.bar_label(ax.containers[0],padding=4); ax.set_xlim(0,650)
rated=d.dropna(subset=['ef_rating']); counts=rated.ef_rating.value_counts().sort_index(); ax=axs[1,0]; ax.bar(range(5),counts.values,color='#456f78'); ax.set_xticks(range(5),['EF0','EF1','EF2','EF3','EF4']); ax.set_title('Most rated tornadoes are EF0 or EF1'); ax.set_ylabel('Recorded tornadoes'); ax.bar_label(ax.containers[0],padding=4,fmt='%d'); ax.set_ylim(0,2850); ax.text(.98,.92,'111 records unrated\nNo EF5 recorded',ha='right',va='top',transform=ax.transAxes,color='#555')
ax=axs[1,1]; deaths=rated.groupby('ef_rating').fatalities.sum().reindex(range(5),fill_value=0); ax.bar(range(5),deaths.values,color='#c46a44'); ax.set_xticks(range(5),['EF0','EF1','EF2','EF3','EF4']); ax.set_title('Fatalities concentrate at higher ratings'); ax.set_ylabel('Recorded fatalities'); ax.bar_label(ax.containers[0],padding=4,fmt='%d'); ax.set_ylim(0,48)
for ax in axs.flat: ax.grid(axis='y',alpha=.13); ax.set_axisbelow(True)
fig.savefig(ROOT / 'figures/tornado_eda.png',dpi=180,bbox_inches='tight')
