import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import seaborn as sns
import os
import json
os.environ['PATH'] = "/Library/TeX/texbin:" + os.environ.get('PATH', '')
mpl.rcParams['text.usetex'] = True
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = ['Computer Modern Roman']
mpl.rcParams['text.latex.preamble'] = r'\usepackage{lmodern}\usepackage[T1]{fontenc}'

# Load fancy names
with open('data/names.json', 'r') as f:
    names = json.load(f)
    
exclude={"Dominica":54,
         "Grenada":55,
         "Saint Lucia":56,
         "Saint Vincent and the Grenadines":57,
         "Antigua & Barbuda":58,
         "Saint Kitts and Nevis":60,
         "Monaco":221,
         "Liechtenstein":223,
         "San Marino":331,
         "Andorra":232,
         "Abkhazia":396,
         "South Ossetia":397,
         "São Tomé and Principe":403,
         "Seychelles":591,
         "Vanuatu":935,
         "Kiribati":970,
         "Nauru":971,
         "Tonga":972,
         "Tuvalu":973,
         "Marshall Islands":983,
         "Palau":986,
         "Micronesia":987,
         "Samoa":990,
         "German Democratic Republic":265,
         "Czechoslovakia":315,
         "Yugoslavia":345,
         "Abkhazia":396,
         "South Ossetia":397,
         "Yemen, People's Republic of":680,
         "Taiwan":713, 
         "Bahamas":31,
         "Belize":80,
         "Brunei Darussalam":835, 
         "Kosovo":347, 
         "Democratic Peoples Republic of Korea":731} 

demog_theme=['pop','pop_density','pop_density_id','urb_share','rural_share','pop_male_share','pop_male_share_0_14','pop_male_share_15_19','pop_male_share_20_24','pop_male_share_25_29','pop_male_share_30_34','group_counts','group_counts_id','monopoly_share','monopoly_share_id','discriminated_share','discriminated_share_id','powerless_share','powerless_share_id','dominant_share','dominant_share_id','ethnic_frac','ethnic_frac_id','rel_frac','rel_frac_id','lang_frac','lang_frac_id','race_frac','race_frac_id']
geog_theme=['land','land_id','forest','forest_id','temp','temp_id','co2','co2_id','percip','percip_id','waterstress','waterstress_id','agri_land','agri_land_id','arable_land','arable_land_id','rugged','soil','desert','tropical','cont_africa','cont_asia','no_neigh','d_neighbors_non_dem','libdem_id_neigh']
econ_theme=['natres_share','natres_share_id','oil_share','oil_share_id','gas_share','gas_share_id','coal_share','coal_share_id','forest_share','forest_share_id','minerals_share','minerals_share_id','gdp','gdp_id','gni','gni_id','gdp_growth','gdp_growth_id','unemploy','unemploy_id','unemploy_male','unemploy_male_id','inflat','inflat_id','conprice','conprice_id','undernour','undernour_id','foodprod','foodprod_id','water_rural','water_rural_id','water_urb','water_urb_id','agri_share','agri_share_id','trade_share','trade_share_id','fert','lifeexp_female','lifeexp_male','pop_growth','pop_growth_id','inf_mort','exports','exports_id','imports','imports_id','primary_female','primary_female_id','primary_male','primary_male_id','second_female','second_female_id','second_male','second_male_id','tert_female','tert_female_id','tert_male','tert_male_id','eys','eys_id','eys_male','eys_male_id','eys_female','eys_female_id','mys','mys_id','mys_male','mys_male_id','mys_female','mys_female_id']
pol_theme=['armedforces_share','armedforces_share_id','milex_share','milex_share_id','corruption','corruption_id', 'effectiveness', 'effectiveness_id', 'polvio','polvio_id','regu','regu_id','law','law_id','account','account_id','tax','tax_id','broadband','broadband_id','telephone','telephone_id','internet_use','internet_use_id','mobile','mobile_id','polyarchy','libdem','libdem_id','partipdem','delibdem','egaldem','civlib','phyvio','pollib','privlib','execon','execon_id','exgender','exgender_id','exgeo','exgeo_id','expol','expol_id','exsoc','exsoc_id','shutdown','shutdown_id','filter','filter_id','tenure_months','tenure_months_id','dem_duration','dem_duration_id','elections','elections_id','lastelection','lastelection_id']

########################
### Load evaluations ###
########################

# Civil war 
base_war_evals=pd.read_csv("out/base_war_evals_df.csv",index_col=0)
history_war_evals=pd.read_csv("out/history_war_evals_df.csv",index_col=0)
demog_war_evals=pd.read_csv("out/demog_war_evals_df.csv",index_col=0)
geog_war_evals=pd.read_csv("out/geog_war_evals_df.csv",index_col=0)
econ_war_evals=pd.read_csv("out/econ_war_evals_df.csv",index_col=0)
pol_war_evals=pd.read_csv("out/pol_war_evals_df.csv",index_col=0)
evals_war_ensemble_df=pd.read_csv("out/evals_war_ensemble_df.csv",index_col=0)
ensemble_war=pd.read_csv("out/ensemble_war.csv",index_col=0)

# Check prevalence
print(ensemble_war["d_civil_war"].loc[(ensemble_war["year"]>=2019)&(ensemble_war["year"]<=2023)].mean())

# Civil Conflict
base_conflict_evals=pd.read_csv("out/base_conflict_evals_df.csv",index_col=0)
history_conflict_evals=pd.read_csv("out/history_conflict_evals_df.csv",index_col=0)
demog_conflict_evals=pd.read_csv("out/demog_conflict_evals_df.csv",index_col=0)
geog_conflict_evals=pd.read_csv("out/geog_conflict_evals_df.csv",index_col=0)
econ_conflict_evals=pd.read_csv("out/econ_conflict_evals_df.csv",index_col=0)
pol_conflict_evals=pd.read_csv("out/pol_conflict_evals_df.csv",index_col=0)
evals_conflict_ensemble_df=pd.read_csv("out/evals_conflict_ensemble_df.csv",index_col=0)
ensemble_conflict=pd.read_csv("out/ensemble_conflict.csv",index_col=0)

# Check prevalence
print(ensemble_conflict["d_civil_conflict"].loc[(ensemble_conflict["year"]>=2019)&(ensemble_conflict["year"]<=2023)].mean())

# Protest
base_protest_evals=pd.read_csv("out/base_protest_evals_df.csv",index_col=0)
history_protest_evals=pd.read_csv("out/history_protest_evals_df.csv",index_col=0)
demog_protest_evals=pd.read_csv("out/demog_protest_evals_df.csv",index_col=0)
geog_protest_evals=pd.read_csv("out/geog_protest_evals_df.csv",index_col=0)
econ_protest_evals=pd.read_csv("out/econ_protest_evals_df.csv",index_col=0)
pol_protest_evals=pd.read_csv("out/pol_protest_evals_df.csv",index_col=0)
evals_protest_ensemble_df=pd.read_csv("out/evals_protest_ensemble_df.csv",index_col=0)
ensemble_protest=pd.read_csv("out/ensemble_protest.csv",index_col=0)

# Check prevalence
print(ensemble_protest["d_protest"].loc[(ensemble_protest["year"]>=2019)&(ensemble_protest["year"]<=2023)].mean())

# Riots
base_riot_evals=pd.read_csv("out/base_riot_evals_df.csv",index_col=0)
history_riot_evals=pd.read_csv("out/history_riot_evals_df.csv",index_col=0)
demog_riot_evals=pd.read_csv("out/demog_riot_evals_df.csv",index_col=0)
geog_riot_evals=pd.read_csv("out/geog_riot_evals_df.csv",index_col=0)
econ_riot_evals=pd.read_csv("out/econ_riot_evals_df.csv",index_col=0)
pol_riot_evals=pd.read_csv("out/pol_riot_evals_df.csv",index_col=0)
evals_riot_ensemble_df=pd.read_csv("out/evals_riot_ensemble_df.csv",index_col=0)
ensemble_riot=pd.read_csv("out/ensemble_riot.csv",index_col=0)

# Check prevalence
print(ensemble_riot["d_riot"].loc[(ensemble_riot["year"]>=2019)&(ensemble_riot["year"]<=2023)].mean())

# Terrorism
base_terror_evals=pd.read_csv("out/base_terror_evals_df.csv",index_col=0)
history_terror_evals=pd.read_csv("out/history_terror_evals_df.csv",index_col=0)
demog_terror_evals=pd.read_csv("out/demog_terror_evals_df.csv",index_col=0)
geog_terror_evals=pd.read_csv("out/geog_terror_evals_df.csv",index_col=0)
econ_terror_evals=pd.read_csv("out/econ_terror_evals_df.csv",index_col=0)
pol_terror_evals=pd.read_csv("out/pol_terror_evals_df.csv",index_col=0)
evals_terror_ensemble_df=pd.read_csv("out/evals_terror_ensemble_df.csv",index_col=0)
ensemble_terror=pd.read_csv("out/ensemble_terror.csv",index_col=0)

# Check prevalence
print(ensemble_terror["d_terror"].loc[(ensemble_terror["year"]>=2019)&(ensemble_terror["year"]<=2023)].mean())

# SB
base_sb_evals=pd.read_csv("out/base_sb_evals_df.csv",index_col=0)
history_sb_evals=pd.read_csv("out/history_sb_evals_df.csv",index_col=0)
demog_sb_evals=pd.read_csv("out/demog_sb_evals_df.csv",index_col=0)
geog_sb_evals=pd.read_csv("out/geog_sb_evals_df.csv",index_col=0)
econ_sb_evals=pd.read_csv("out/econ_sb_evals_df.csv",index_col=0)
pol_sb_evals=pd.read_csv("out/pol_sb_evals_df.csv",index_col=0)
evals_sb_ensemble_df=pd.read_csv("out/evals_sb_ensemble_df.csv",index_col=0)
ensemble_sb=pd.read_csv("out/ensemble_sb.csv",index_col=0)

# Check prevalence
print(ensemble_sb["d_sb"].loc[(ensemble_sb["year"]>=2019)&(ensemble_sb["year"]<=2023)].mean())

# NS
base_ns_evals=pd.read_csv("out/base_ns_evals_df.csv",index_col=0)
history_ns_evals=pd.read_csv("out/history_ns_evals_df.csv",index_col=0)
demog_ns_evals=pd.read_csv("out/demog_ns_evals_df.csv",index_col=0)
geog_ns_evals=pd.read_csv("out/geog_ns_evals_df.csv",index_col=0)
econ_ns_evals=pd.read_csv("out/econ_ns_evals_df.csv",index_col=0)
pol_ns_evals=pd.read_csv("out/pol_ns_evals_df.csv",index_col=0)
evals_ns_ensemble_df=pd.read_csv("out/evals_ns_ensemble_df.csv",index_col=0)
ensemble_ns=pd.read_csv("out/ensemble_ns.csv",index_col=0)

# Check prevalence
print(ensemble_ns["d_ns"].loc[(ensemble_ns["year"]>=2019)&(ensemble_ns["year"]<=2023)].mean())

# OSV
base_osv_evals=pd.read_csv("out/base_osv_evals_df.csv",index_col=0)
history_osv_evals=pd.read_csv("out/history_osv_evals_df.csv",index_col=0)
demog_osv_evals=pd.read_csv("out/demog_osv_evals_df.csv",index_col=0)
geog_osv_evals=pd.read_csv("out/geog_osv_evals_df.csv",index_col=0)
econ_osv_evals=pd.read_csv("out/econ_osv_evals_df.csv",index_col=0)
pol_osv_evals=pd.read_csv("out/pol_osv_evals_df.csv",index_col=0)
evals_osv_ensemble_df=pd.read_csv("out/evals_osv_ensemble_df.csv",index_col=0)
ensemble_osv=pd.read_csv("out/ensemble_osv.csv",index_col=0)

# Check prevalence
print(ensemble_osv["d_osv"].loc[(ensemble_osv["year"]>=2019)&(ensemble_osv["year"]<=2023)].mean())

##################
### Final Plot ###
##################

# Brier score

# Get evaluations in list of list
evals = [
    [evals_war_ensemble_df["0"].iloc[0],history_war_evals["0"].iloc[0],demog_war_evals["0"].iloc[0],geog_war_evals["0"].iloc[0],econ_war_evals["0"].iloc[0],pol_war_evals["0"].iloc[0]],
    [evals_conflict_ensemble_df["0"].iloc[0],history_conflict_evals["0"].iloc[0],demog_conflict_evals["0"].iloc[0],geog_conflict_evals["0"].iloc[0],econ_conflict_evals["0"].iloc[0],pol_conflict_evals["0"].iloc[0]],
    [evals_protest_ensemble_df["0"].iloc[0],history_protest_evals["0"].iloc[0],demog_protest_evals["0"].iloc[0],geog_protest_evals["0"].iloc[0],econ_protest_evals["0"].iloc[0],pol_protest_evals["0"].iloc[0]],
    [evals_riot_ensemble_df["0"].iloc[0],history_riot_evals["0"].iloc[0],demog_riot_evals["0"].iloc[0],geog_riot_evals["0"].iloc[0],econ_riot_evals["0"].iloc[0],pol_riot_evals["0"].iloc[0]],
    [evals_terror_ensemble_df["0"].iloc[0],history_terror_evals["0"].iloc[0],demog_terror_evals["0"].iloc[0],geog_terror_evals["0"].iloc[0],econ_terror_evals["0"].iloc[0],pol_terror_evals["0"].iloc[0]],
    [evals_sb_ensemble_df["0"].iloc[0],history_sb_evals["0"].iloc[0],demog_sb_evals["0"].iloc[0],geog_sb_evals["0"].iloc[0],econ_sb_evals["0"].iloc[0],pol_sb_evals["0"].iloc[0]],
    [evals_ns_ensemble_df["0"].iloc[0],history_ns_evals["0"].iloc[0],demog_ns_evals["0"].iloc[0],geog_ns_evals["0"].iloc[0],econ_ns_evals["0"].iloc[0],pol_ns_evals["0"].iloc[0]],
    [evals_osv_ensemble_df["0"].iloc[0],history_osv_evals["0"].iloc[0],demog_osv_evals["0"].iloc[0],geog_osv_evals["0"].iloc[0],econ_osv_evals["0"].iloc[0],pol_osv_evals["0"].iloc[0]]]
   
# Define colors  
colors=["dimgray","lightgray","forestgreen","lightgreen","steelblue","lightblue","purple","violet"]

# Initiate plot
fig, ax = plt.subplots(figsize=(14, 5))
ax.margins(x=0.02)

# Define start of each grouped bar section (over outcomes)
# There are eight outcomes, and 6 themes, and each bar has width 0.5
# then add 0.5 as space to next grouped bars
bar_start = np.arange(8)*(6 * 0.5 + 0.5)

# Loop over outcomes
for i,outcome in enumerate(evals):
    print(outcome)

    # Get x values, start values, and then add range within grouped bar 
    x = bar_start[i] + [0,0.5,1,1.5,2,2.5]
    
    # Add bar plot
    bars = ax.bar(x,outcome,width=0.5,color=colors[i],edgecolor='black')
    
    # Mark ensemble with ///
    bars[0].set_hatch("///")
    bars[0].set_edgecolor("black")   

# Add y labels
ax.set_ylabel("Brier score",size=15)
ax.set_yticks([0,0.025,0.05,0.075,0.1,0.125,0.15,0.175,0.2],[0,0.025,0.05,0.075,0.1,0.125,0.15,0.175,0.2],size=15)
ax.set_ylim([0,0.22])

# Add x-ticks
ax.set_xticks([0,0.5,1,1.5,2,2.5,3.5,4,4.5,5,5.5,6,7,7.5,8,8.5,9,9.5,10.5,11,11.5,12,12.5,13,14,14.5,15,15.5,16,16.5,17.5,18,18.5,19,19.5,20,21,21.5,22,22.5,23,23.5,24.5,25,25.5,26,26.5,27],
              ["Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics"],size=17,rotation=45,ha="right", va="top",color="black")

# Add titles
ax.text(0,0.222,"1,000-fatality",size=15)
ax.text(3.8,0.222,"25-fatality",size=15)
ax.text(7.6,0.222,"Protest",size=15)
ax.text(11.2,0.222,"Riots",size=15)
ax.text(14.4,0.222,"Terrorism",size=15)
ax.text(18.1,0.222,"Battles",size=15)
ax.text(21.3,0.222,"Non-state",size=15)
ax.text(25,0.222,"One-sided",size=15)

# Add ensemble evals
ax.text(-0.6,round(evals_war_ensemble_df["0"].iloc[0],4),round(evals_war_ensemble_df["0"].iloc[0],4),size=15)
ax.text(2.88,round(evals_conflict_ensemble_df["0"].iloc[0],4),round(evals_conflict_ensemble_df["0"].iloc[0],4),size=15)
ax.text(6.4,round(evals_protest_ensemble_df["0"].iloc[0],4),round(evals_protest_ensemble_df["0"].iloc[0],4),size=15)
ax.text(9.9,round(evals_riot_ensemble_df["0"].iloc[0],4),round(evals_riot_ensemble_df["0"].iloc[0],4),size=15)
ax.text(13.41,round(evals_terror_ensemble_df["0"].iloc[0],4),round(evals_terror_ensemble_df["0"].iloc[0],4),size=15)
ax.text(16.9,round(evals_sb_ensemble_df["0"].iloc[0],4),round(evals_sb_ensemble_df["0"].iloc[0],4),size=15)
ax.text(20.4,round(evals_ns_ensemble_df["0"].iloc[0],4),round(evals_ns_ensemble_df["0"].iloc[0],4),size=15)
ax.text(23.9,round(evals_osv_ensemble_df["0"].iloc[0],4),round(evals_osv_ensemble_df["0"].iloc[0],4),size=15)

# Save
plt.tight_layout()
plt.savefig("out/struc_evals_brier_bars.eps",dpi=100,bbox_inches="tight",)
plt.show()


# AUPR

# Get evaluations in list of list
evals = [
    [evals_war_ensemble_df["0"].iloc[1],history_war_evals["0"].iloc[1],demog_war_evals["0"].iloc[1],geog_war_evals["0"].iloc[1],econ_war_evals["0"].iloc[1],pol_war_evals["0"].iloc[1]],
    [evals_conflict_ensemble_df["0"].iloc[1],history_conflict_evals["0"].iloc[1],demog_conflict_evals["0"].iloc[1],geog_conflict_evals["0"].iloc[1],econ_conflict_evals["0"].iloc[1],pol_conflict_evals["0"].iloc[1]],
    [evals_protest_ensemble_df["0"].iloc[1],history_protest_evals["0"].iloc[1],demog_protest_evals["0"].iloc[1],geog_protest_evals["0"].iloc[1],econ_protest_evals["0"].iloc[1],pol_protest_evals["0"].iloc[1]],
    [evals_riot_ensemble_df["0"].iloc[1],history_riot_evals["0"].iloc[1],demog_riot_evals["0"].iloc[1],geog_riot_evals["0"].iloc[1],econ_riot_evals["0"].iloc[1],pol_riot_evals["0"].iloc[1]],
    [evals_terror_ensemble_df["0"].iloc[1],history_terror_evals["0"].iloc[1],demog_terror_evals["0"].iloc[1],geog_terror_evals["0"].iloc[1],econ_terror_evals["0"].iloc[1],pol_terror_evals["0"].iloc[1]],
    [evals_sb_ensemble_df["0"].iloc[1],history_sb_evals["0"].iloc[1],demog_sb_evals["0"].iloc[1],geog_sb_evals["0"].iloc[1],econ_sb_evals["0"].iloc[1],pol_sb_evals["0"].iloc[1]],
    [evals_ns_ensemble_df["0"].iloc[1],history_ns_evals["0"].iloc[1],demog_ns_evals["0"].iloc[1],geog_ns_evals["0"].iloc[1],econ_ns_evals["0"].iloc[1],pol_ns_evals["0"].iloc[1]],
    [evals_osv_ensemble_df["0"].iloc[1],history_osv_evals["0"].iloc[1],demog_osv_evals["0"].iloc[1],geog_osv_evals["0"].iloc[1],econ_osv_evals["0"].iloc[1],pol_osv_evals["0"].iloc[1]]]
   
# Define colors  
colors=["dimgray","lightgray","forestgreen","lightgreen","steelblue","lightblue","purple","violet"]

# Initiate plot
fig, ax = plt.subplots(figsize=(14, 5))
ax.margins(x=0.02)

# Define start of each grouped bar section (over outcomes)
# There are eight outcomes, and 6 themes, and each bar has width 0.5
# then add 0.5 as space to next grouped bars
bar_start = np.arange(8)*(6 * 0.5 + 0.5)

# Loop over outcomes
for i,outcome in enumerate(evals):
    print(outcome)

    # Get x values, start values, and then add range within grouped bar 
    x = bar_start[i] + [0,0.5,1,1.5,2,2.5]
    
    # Add bar plot
    bars = ax.bar(x,outcome,width=0.5,color=colors[i],edgecolor='black')
    
    # Mark ensemble with ///
    bars[0].set_hatch("///")
    bars[0].set_edgecolor("black")   

# Add y labels
ax.set_ylabel("AUPR",size=15)
ax.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],size=15)
ax.set_ylim([0.39,1.02])

# Add x-ticks
ax.set_xticks([0,0.5,1,1.5,2,2.5,3.5,4,4.5,5,5.5,6,7,7.5,8,8.5,9,9.5,10.5,11,11.5,12,12.5,13,14,14.5,15,15.5,16,16.5,17.5,18,18.5,19,19.5,20,21,21.5,22,22.5,23,23.5,24.5,25,25.5,26,26.5,27],
              ["Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics"],size=17,rotation=45,ha="right", va="top",color="black")

# Add titles
ax.text(0,1.03,"1,000-fatality",size=15)
ax.text(3.8,1.03,"25-fatality",size=15)
ax.text(7.6,1.03,"Protest",size=15)
ax.text(11.2,1.03,"Riots",size=15)
ax.text(14.4,1.03,"Terrorism",size=15)
ax.text(18.1,1.03,"Battles",size=15)
ax.text(21.3,1.03,"Non-state",size=15)
ax.text(25,1.03,"One-sided",size=15)

# Add ensemble evals
ax.text(-0.6,round(evals_war_ensemble_df["0"].iloc[1],4),round(evals_war_ensemble_df["0"].iloc[1],4),size=15)
ax.text(2.88,round(evals_conflict_ensemble_df["0"].iloc[1],4),round(evals_conflict_ensemble_df["0"].iloc[1],4),size=15)
ax.text(6.4,round(evals_protest_ensemble_df["0"].iloc[1],4),round(evals_protest_ensemble_df["0"].iloc[1],4),size=15)
ax.text(9.9,round(evals_riot_ensemble_df["0"].iloc[1],4),round(evals_riot_ensemble_df["0"].iloc[1],4),size=15)
ax.text(13.41,round(evals_terror_ensemble_df["0"].iloc[1],4),round(evals_terror_ensemble_df["0"].iloc[1],4),size=15)
ax.text(16.9,round(evals_sb_ensemble_df["0"].iloc[1],4),round(evals_sb_ensemble_df["0"].iloc[1],4),size=15)
ax.text(20.4,round(evals_ns_ensemble_df["0"].iloc[1],4),round(evals_ns_ensemble_df["0"].iloc[1],4),size=15)
ax.text(23.9,round(evals_osv_ensemble_df["0"].iloc[1],4),round(evals_osv_ensemble_df["0"].iloc[1],4),size=15)

# Save
plt.tight_layout()
plt.savefig("out/struc_evals_aupr_bars.eps",dpi=100,bbox_inches="tight",)
plt.show()


# AUROC 

# Get evaluations in list of list
evals = [
    [evals_war_ensemble_df["0"].iloc[2],history_war_evals["0"].iloc[2],demog_war_evals["0"].iloc[2],geog_war_evals["0"].iloc[2],econ_war_evals["0"].iloc[2],pol_war_evals["0"].iloc[2]],
    [evals_conflict_ensemble_df["0"].iloc[2],history_conflict_evals["0"].iloc[2],demog_conflict_evals["0"].iloc[2],geog_conflict_evals["0"].iloc[2],econ_conflict_evals["0"].iloc[2],pol_conflict_evals["0"].iloc[2]],
    [evals_protest_ensemble_df["0"].iloc[2],history_protest_evals["0"].iloc[2],demog_protest_evals["0"].iloc[2],geog_protest_evals["0"].iloc[2],econ_protest_evals["0"].iloc[2],pol_protest_evals["0"].iloc[2]],
    [evals_riot_ensemble_df["0"].iloc[2],history_riot_evals["0"].iloc[2],demog_riot_evals["0"].iloc[2],geog_riot_evals["0"].iloc[2],econ_riot_evals["0"].iloc[2],pol_riot_evals["0"].iloc[2]],
    [evals_terror_ensemble_df["0"].iloc[2],history_terror_evals["0"].iloc[2],demog_terror_evals["0"].iloc[2],geog_terror_evals["0"].iloc[2],econ_terror_evals["0"].iloc[2],pol_terror_evals["0"].iloc[2]],
    [evals_sb_ensemble_df["0"].iloc[2],history_sb_evals["0"].iloc[2],demog_sb_evals["0"].iloc[2],geog_sb_evals["0"].iloc[2],econ_sb_evals["0"].iloc[2],pol_sb_evals["0"].iloc[2]],
    [evals_ns_ensemble_df["0"].iloc[2],history_ns_evals["0"].iloc[2],demog_ns_evals["0"].iloc[2],geog_ns_evals["0"].iloc[2],econ_ns_evals["0"].iloc[2],pol_ns_evals["0"].iloc[2]],
    [evals_osv_ensemble_df["0"].iloc[2],history_osv_evals["0"].iloc[2],demog_osv_evals["0"].iloc[2],geog_osv_evals["0"].iloc[2],econ_osv_evals["0"].iloc[2],pol_osv_evals["0"].iloc[2]]]
       
# Define colors  
colors=["dimgray","lightgray","forestgreen","lightgreen","steelblue","lightblue","purple","violet"]

# Initiate plor
fig, ax = plt.subplots(figsize=(14, 5))
ax.margins(x=0.02)

# Define start of each grouped bar section (over outcomes)
# There are eight outcomes, and 6 themes, and each bar has width 0.5
# then add 0.5 as space to next grouped bars
bar_start = np.arange(8)*(6 * 0.5 + 0.5)

# Loop over outcomes
for i,outcome in enumerate(evals):

    # Get x values, start values, and then add range within grouped bar 
    x = bar_start[i] + [0,0.5,1,1.5,2,2.5]
    
    # Add bar plot
    bars = ax.bar(x,outcome,width=0.5,color=colors[i],edgecolor='black')
    bars[0].set_hatch("///")
    bars[0].set_edgecolor("black")  
    
# Add y labels
ax.set_ylabel("AUROC",size=15)
ax.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],[0,0.1,0.2,0.3,0.4,0.5,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],size=15)
ax.set_ylim([0.65,1.02])

# Add x-ticks
ax.set_xticks([0,0.5,1,1.5,2,2.5,3.5,4,4.5,5,5.5,6,7,7.5,8,8.5,9,9.5,10.5,11,11.5,12,12.5,13,14,14.5,15,15.5,16,16.5,17.5,18,18.5,19,19.5,20,21,21.5,22,22.5,23,23.5,24.5,25,25.5,26,26.5,27],
              ["Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics"],size=17,rotation=45,ha="right", va="top",)

# Add titles
ax.text(0,1.03,"1,000-fatality",size=15)
ax.text(3.8,1.03,"25-fatality",size=15)
ax.text(7.6,1.03,"Protest",size=15)
ax.text(11.2,1.03,"Riots",size=15)
ax.text(14.4,1.03,"Terrorism",size=15)
ax.text(18.1,1.03,"Battles",size=15)
ax.text(21.3,1.03,"Non-state",size=15)
ax.text(25,1.03,"One-sided",size=15)

# Add ensemble evals
ax.text(-0.6,round(evals_war_ensemble_df["0"].iloc[2],4),round(evals_war_ensemble_df["0"].iloc[2],4),size=15)
ax.text(2.88,round(evals_conflict_ensemble_df["0"].iloc[2],4),round(evals_conflict_ensemble_df["0"].iloc[2],4),size=15)
ax.text(6.4,round(evals_protest_ensemble_df["0"].iloc[2],4),round(evals_protest_ensemble_df["0"].iloc[2],4),size=15)
ax.text(9.9,round(evals_riot_ensemble_df["0"].iloc[2],4),round(evals_riot_ensemble_df["0"].iloc[2],4),size=15)
ax.text(13.41,round(evals_terror_ensemble_df["0"].iloc[2],4),round(evals_terror_ensemble_df["0"].iloc[2],4),size=15)
ax.text(16.9,round(evals_sb_ensemble_df["0"].iloc[2],4),round(evals_sb_ensemble_df["0"].iloc[2],4),size=15)
ax.text(20.4,round(evals_ns_ensemble_df["0"].iloc[2],4),round(evals_ns_ensemble_df["0"].iloc[2],4),size=15)
ax.text(23.9,round(evals_osv_ensemble_df["0"].iloc[2],4),round(evals_osv_ensemble_df["0"].iloc[2],4),size=15)

# Save
plt.tight_layout()
plt.savefig("out/struc_evals_auroc_bars.eps",dpi=100,bbox_inches="tight",)
plt.show()


# Accuracy 

# Get evaluations in list of list
evals = [
    [evals_war_ensemble_df["0"].iloc[3],history_war_evals["0"].iloc[3],demog_war_evals["0"].iloc[3],geog_war_evals["0"].iloc[3],econ_war_evals["0"].iloc[3],pol_war_evals["0"].iloc[3]],
    [evals_conflict_ensemble_df["0"].iloc[3],history_conflict_evals["0"].iloc[3],demog_conflict_evals["0"].iloc[3],geog_conflict_evals["0"].iloc[3],econ_conflict_evals["0"].iloc[3],pol_conflict_evals["0"].iloc[3]],
    [evals_protest_ensemble_df["0"].iloc[3],history_protest_evals["0"].iloc[3],demog_protest_evals["0"].iloc[3],geog_protest_evals["0"].iloc[3],econ_protest_evals["0"].iloc[3],pol_protest_evals["0"].iloc[3]],
    [evals_riot_ensemble_df["0"].iloc[3],history_riot_evals["0"].iloc[3],demog_riot_evals["0"].iloc[3],geog_riot_evals["0"].iloc[3],econ_riot_evals["0"].iloc[3],pol_riot_evals["0"].iloc[3]],
    [evals_terror_ensemble_df["0"].iloc[3],history_terror_evals["0"].iloc[3],demog_terror_evals["0"].iloc[3],geog_terror_evals["0"].iloc[3],econ_terror_evals["0"].iloc[3],pol_terror_evals["0"].iloc[3]],
    [evals_sb_ensemble_df["0"].iloc[3],history_sb_evals["0"].iloc[3],demog_sb_evals["0"].iloc[3],geog_sb_evals["0"].iloc[3],econ_sb_evals["0"].iloc[3],pol_sb_evals["0"].iloc[3]],
    [evals_ns_ensemble_df["0"].iloc[3],history_ns_evals["0"].iloc[3],demog_ns_evals["0"].iloc[3],geog_ns_evals["0"].iloc[3],econ_ns_evals["0"].iloc[3],pol_ns_evals["0"].iloc[3]],
    [evals_osv_ensemble_df["0"].iloc[3],history_osv_evals["0"].iloc[3],demog_osv_evals["0"].iloc[3],geog_osv_evals["0"].iloc[3],econ_osv_evals["0"].iloc[3],pol_osv_evals["0"].iloc[3]]]
       
# Define colors  
colors=["dimgray","lightgray","forestgreen","lightgreen","steelblue","lightblue","purple","violet"]

# Initiate plor
fig, ax = plt.subplots(figsize=(14, 5))
ax.margins(x=0.02)

# Define start of each grouped bar section (over outcomes)
# There are eight outcomes, and 6 themes, and each bar has width 0.5
# then add 0.5 as space to next grouped bars
bar_start = np.arange(8)*(6 * 0.5 + 0.5)

# Loop over outcomes
for i,outcome in enumerate(evals):

    # Get x values, start values, and then add range within grouped bar 
    x = bar_start[i] + [0,0.5,1,1.5,2,2.5]
    
    # Add bar plot
    bars = ax.bar(x,outcome,width=0.5,color=colors[i],edgecolor='black')
    bars[0].set_hatch("///")
    bars[0].set_edgecolor("black")  
    
# Add y labels
ax.set_ylabel("Balanced accuracy",size=15)
ax.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],size=15)
ax.set_ylim([0.4,1])

# Add x-ticks
ax.set_xticks([0,0.5,1,1.5,2,2.5,3.5,4,4.5,5,5.5,6,7,7.5,8,8.5,9,9.5,10.5,11,11.5,12,12.5,13,14,14.5,15,15.5,16,16.5,17.5,18,18.5,19,19.5,20,21,21.5,22,22.5,23,23.5,24.5,25,25.5,26,26.5,27],
              ["Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics","Ensemble","Conflict History","Demography","Geography","Economy","Politics"],size=17,rotation=45,ha="right", va="top",)

# Add titles
ax.text(0,1.01,"1,000-fatality",size=15,color="white")
#ax.text(3.8,1.01,"25-fatality",size=15)
#ax.text(7.6,1.01,"Protest",size=15)
#ax.text(11.2,1.01,"Riots",size=15)
#ax.text(14.4,1.01,"Terrorism",size=15)
#ax.text(18.1,1.01,"Battles",size=15)
#ax.text(21.3,1.01,"Non-state",size=15)
#ax.text(25,1.01,"One-sided",size=15)

# Add ensemble evals
ax.text(-0.6,round(evals_war_ensemble_df["0"].iloc[3],4),round(evals_war_ensemble_df["0"].iloc[3],4),size=15)
ax.text(2.88,round(evals_conflict_ensemble_df["0"].iloc[3],4),round(evals_conflict_ensemble_df["0"].iloc[3],4),size=15)
ax.text(6.4,round(evals_protest_ensemble_df["0"].iloc[3],4),round(evals_protest_ensemble_df["0"].iloc[3],4),size=15)
ax.text(9.9,round(evals_riot_ensemble_df["0"].iloc[3],4),round(evals_riot_ensemble_df["0"].iloc[3],4),size=15)
ax.text(13.41,round(evals_terror_ensemble_df["0"].iloc[3],4),round(evals_terror_ensemble_df["0"].iloc[3],4),size=15)
ax.text(16.9,round(evals_sb_ensemble_df["0"].iloc[3],4),round(evals_sb_ensemble_df["0"].iloc[3],4),size=15)
ax.text(20.4,round(evals_ns_ensemble_df["0"].iloc[3],4),round(evals_ns_ensemble_df["0"].iloc[3],4),size=15)
ax.text(23.9,round(evals_osv_ensemble_df["0"].iloc[3],4),round(evals_osv_ensemble_df["0"].iloc[3],4),size=15)

# Save
plt.tight_layout()
plt.savefig("out/struc_evals_accuracy_bars.eps",dpi=100,bbox_inches="tight",)
plt.show()
    
    
# Tabels for Appendix #

# AUROC
print(f"{round(base_war_evals['0'].iloc[2],5)} &  {round(history_war_evals['0'].iloc[2],5)} &  {round(demog_war_evals['0'].iloc[2],5)} & {round(geog_war_evals['0'].iloc[2],5)} &  {round(econ_war_evals['0'].iloc[2],5)} &  {round(pol_war_evals['0'].iloc[2],5)}& {round(evals_war_ensemble_df['0'].iloc[2],5)}")
print(f"{round(base_conflict_evals['0'].iloc[2],5)} &   {round(history_conflict_evals['0'].iloc[2],5)} &  {round(demog_conflict_evals['0'].iloc[2],5)} &  {round(geog_conflict_evals['0'].iloc[2],5)} &   {round(econ_conflict_evals['0'].iloc[2],5)} &  {round(pol_conflict_evals['0'].iloc[2],5)}&  {round(evals_conflict_ensemble_df['0'].iloc[2],5)}")
print(f"{round(base_protest_evals['0'].iloc[2],5)} &  {round(history_protest_evals['0'].iloc[2],5)} &  {round(demog_protest_evals['0'].iloc[2],5)} &  {round(geog_protest_evals['0'].iloc[2],5)} &  {round(econ_protest_evals['0'].iloc[2],5)} &  {round(pol_protest_evals['0'].iloc[2],5)}&  {round(evals_protest_ensemble_df['0'].iloc[2],5)}")
print(f"{round(base_riot_evals['0'].iloc[2],5)} &  {round(history_riot_evals['0'].iloc[2],5)} & {round(demog_riot_evals['0'].iloc[2],5)} &  {round(geog_riot_evals['0'].iloc[2],5)} & {round(econ_riot_evals['0'].iloc[2],5)} & {round(pol_riot_evals['0'].iloc[2],5)}& {round(evals_riot_ensemble_df['0'].iloc[2],5)}")
print(f"{round(base_terror_evals['0'].iloc[2],5)} &  {round(history_terror_evals['0'].iloc[2],5)} &  {round(demog_terror_evals['0'].iloc[2],5)} &   {round(geog_terror_evals['0'].iloc[2],5)} &  {round(econ_terror_evals['0'].iloc[2],5)} &  {round(pol_terror_evals['0'].iloc[2],5)}&  {round(evals_terror_ensemble_df['0'].iloc[2],5)}")
print(f"{round(base_sb_evals['0'].iloc[2],5)} &  {round(history_sb_evals['0'].iloc[2],5)} &  {round(demog_sb_evals['0'].iloc[2],5)} &  {round(geog_sb_evals['0'].iloc[2],5)} &  {round(econ_sb_evals['0'].iloc[2],5)} &  {round(pol_sb_evals['0'].iloc[2],5)}&  {round(evals_sb_ensemble_df['0'].iloc[2],5)}")
print(f"{round(base_ns_evals['0'].iloc[2],5)} &   {round(history_ns_evals['0'].iloc[2],5)} &   {round(demog_ns_evals['0'].iloc[2],5)} &   {round(geog_ns_evals['0'].iloc[2],5)} &    {round(econ_ns_evals['0'].iloc[2],5)} &  {round(pol_ns_evals['0'].iloc[2],5)}&  {round(evals_ns_ensemble_df['0'].iloc[2],5)}")  
print(f"{round(base_osv_evals['0'].iloc[2],5)} &   {round(history_osv_evals['0'].iloc[2],5)} &  {round(demog_osv_evals['0'].iloc[2],5)} &  {round(geog_osv_evals['0'].iloc[2],5)} &  {round(econ_osv_evals['0'].iloc[2],5)} &  {round(pol_osv_evals['0'].iloc[2],5)}&  {round(evals_osv_ensemble_df['0'].iloc[2],5)}")    
 
# AUPR
print(f"{round(base_war_evals['0'].iloc[1],5)} &  {round(history_war_evals['0'].iloc[1],5)} & {round(demog_war_evals['0'].iloc[1],5)} &  {round(geog_war_evals['0'].iloc[1],5)} &  {round(econ_war_evals['0'].iloc[1],5)} &  {round(pol_war_evals['0'].iloc[1],5)}&  {round(evals_war_ensemble_df['0'].iloc[1],5)}")
print(f"{round(base_conflict_evals['0'].iloc[1],5)} &  {round(history_conflict_evals['0'].iloc[1],5)} &  {round(demog_conflict_evals['0'].iloc[1],5)} &   {round(geog_conflict_evals['0'].iloc[1],5)} &  {round(econ_conflict_evals['0'].iloc[1],5)} &  {round(pol_conflict_evals['0'].iloc[1],5)}&  {round(evals_conflict_ensemble_df['0'].iloc[1],5)}")
print(f"{round(base_protest_evals['0'].iloc[1],5)} & {round(history_protest_evals['0'].iloc[1],5)} &  {round(demog_protest_evals['0'].iloc[1],5)} &  {round(geog_protest_evals['0'].iloc[1],5)} & {round(econ_protest_evals['0'].iloc[1],5)} &  {round(pol_protest_evals['0'].iloc[1],5)}&  {round(evals_protest_ensemble_df['0'].iloc[1],5)}")
print(f"{round(base_riot_evals['0'].iloc[1],5)} &  {round(history_riot_evals['0'].iloc[1],5)} &  {round(demog_riot_evals['0'].iloc[1],5)} &  {round(geog_riot_evals['0'].iloc[1],5)} &  {round(econ_riot_evals['0'].iloc[1],5)} & {round(pol_riot_evals['0'].iloc[1],5)}& {round(evals_riot_ensemble_df['0'].iloc[1],5)}")
print(f"{round(base_terror_evals['0'].iloc[1],5)} &  {round(history_terror_evals['0'].iloc[1],5)} &  {round(demog_terror_evals['0'].iloc[1],5)} &  {round(geog_terror_evals['0'].iloc[1],5)} &  {round(econ_terror_evals['0'].iloc[1],5)} &  {round(pol_terror_evals['0'].iloc[1],5)}& {round(evals_terror_ensemble_df['0'].iloc[1],5)}")
print(f"{round(base_sb_evals['0'].iloc[1],5)} &  {round(history_sb_evals['0'].iloc[1],5)} &  {round(demog_sb_evals['0'].iloc[1],5)} &  {round(geog_sb_evals['0'].iloc[1],5)} &  {round(econ_sb_evals['0'].iloc[1],5)} & {round(pol_sb_evals['0'].iloc[1],5)}&  {round(evals_sb_ensemble_df['0'].iloc[1],5)}")
print(f"{round(base_ns_evals['0'].iloc[1],5)} & {round(history_ns_evals['0'].iloc[1],5)} &   {round(demog_ns_evals['0'].iloc[1],5)} &  {round(geog_ns_evals['0'].iloc[1],5)} &   {round(econ_ns_evals['0'].iloc[1],5)} &  {round(pol_ns_evals['0'].iloc[1],5)}& {round(evals_ns_ensemble_df['0'].iloc[1],5)}")      
print(f"{round(base_osv_evals['0'].iloc[1],5)} &  {round(history_osv_evals['0'].iloc[1],5)} &  {round(demog_osv_evals['0'].iloc[1],5)} &  {round(geog_osv_evals['0'].iloc[1],5)} &  {round(econ_osv_evals['0'].iloc[1],5)} &  {round(pol_osv_evals['0'].iloc[1],5)}&  {round(evals_osv_ensemble_df['0'].iloc[1],5)}")        

# Brier
print(f"{round(base_war_evals['0'].iloc[0],5)} &  {round(history_war_evals['0'].iloc[0],5)} &  {round(demog_war_evals['0'].iloc[0],5)} &  {round(geog_war_evals['0'].iloc[0],5)} &  {round(econ_war_evals['0'].iloc[0],5)} &  {round(pol_war_evals['0'].iloc[0],5)} &  {round(evals_war_ensemble_df['0'].iloc[0],5)} ")
print(f"{round(base_conflict_evals['0'].iloc[0],5)} &  {round(history_conflict_evals['0'].iloc[0],5)} &  {round(demog_conflict_evals['0'].iloc[0],5)} &  {round(geog_conflict_evals['0'].iloc[0],5)} &  {round(econ_conflict_evals['0'].iloc[0],5)} & {round(pol_conflict_evals['0'].iloc[0],5)} & {round(evals_conflict_ensemble_df['0'].iloc[0],5)} ")
print(f"{round(base_protest_evals['0'].iloc[0],5)} &  {round(history_protest_evals['0'].iloc[0],5)} & {round(demog_protest_evals['0'].iloc[0],5)} &  {round(geog_protest_evals['0'].iloc[0],5)} &   {round(econ_protest_evals['0'].iloc[0],5)} &   {round(pol_protest_evals['0'].iloc[0],5)}&  {round(evals_protest_ensemble_df['0'].iloc[0],5)}")
print(f"{round(base_riot_evals['0'].iloc[0],5)} & {round(history_riot_evals['0'].iloc[0],5)} &  {round(demog_riot_evals['0'].iloc[0],5)} &   {round(geog_riot_evals['0'].iloc[0],5)} &  {round(econ_riot_evals['0'].iloc[0],5)} &   {round(pol_riot_evals['0'].iloc[0],5)} &  {round(evals_riot_ensemble_df['0'].iloc[0],5)}")
print(f"{round(base_terror_evals['0'].iloc[0],5)} & {round(history_terror_evals['0'].iloc[0],5)} &  {round(demog_terror_evals['0'].iloc[0],5)} &   {round(geog_terror_evals['0'].iloc[0],5)} &  {round(econ_terror_evals['0'].iloc[0],5)} &  {round(pol_terror_evals['0'].iloc[0],5)}& {round(evals_terror_ensemble_df['0'].iloc[0],5)}")
print(f"{round(base_sb_evals['0'].iloc[0],5)} &  {round(history_sb_evals['0'].iloc[0],5)} &  {round(demog_sb_evals['0'].iloc[0],5)} &  {round(geog_sb_evals['0'].iloc[0],5)} & {round(econ_sb_evals['0'].iloc[0],5)} &  {round(pol_sb_evals['0'].iloc[0],5)}& {round(evals_sb_ensemble_df['0'].iloc[0],5)}")
print(f"{round(base_ns_evals['0'].iloc[0],5)} &  {round(history_ns_evals['0'].iloc[0],5)} &  {round(demog_ns_evals['0'].iloc[0],5)} &   {round(geog_ns_evals['0'].iloc[0],5)} &  {round(econ_ns_evals['0'].iloc[0],5)} &  {round(pol_ns_evals['0'].iloc[0],5)} & {round(evals_ns_ensemble_df['0'].iloc[0],5)}")      
print(f"{round(base_osv_evals['0'].iloc[0],5)} &  {round(history_osv_evals['0'].iloc[0],5)} &  {round(demog_osv_evals['0'].iloc[0],5)} &  {round(geog_osv_evals['0'].iloc[0],5)} &  {round(econ_osv_evals['0'].iloc[0],5)} & {round(pol_osv_evals['0'].iloc[0],5)}&  {round(evals_osv_ensemble_df['0'].iloc[0],5)}")            
     
# Accuracy
print(f"{round(base_war_evals['0'].iloc[3],5)} &  {round(history_war_evals['0'].iloc[3],5)} &  {round(demog_war_evals['0'].iloc[3],5)} &  {round(geog_war_evals['0'].iloc[3],5)} &  {round(econ_war_evals['0'].iloc[3],5)} &  {round(pol_war_evals['0'].iloc[3],5)} &  {round(evals_war_ensemble_df['0'].iloc[3],5)} ")
print(f"{round(base_conflict_evals['0'].iloc[3],5)} &  {round(history_conflict_evals['0'].iloc[3],5)} &  {round(demog_conflict_evals['0'].iloc[3],5)} &  {round(geog_conflict_evals['0'].iloc[3],5)} &  {round(econ_conflict_evals['0'].iloc[3],5)} & {round(pol_conflict_evals['0'].iloc[3],5)} & {round(evals_conflict_ensemble_df['0'].iloc[3],5)} ")
print(f"{round(base_protest_evals['0'].iloc[3],5)} &  {round(history_protest_evals['0'].iloc[3],5)} & {round(demog_protest_evals['0'].iloc[3],5)} &  {round(geog_protest_evals['0'].iloc[3],5)} &   {round(econ_protest_evals['0'].iloc[3],5)} &   {round(pol_protest_evals['0'].iloc[3],5)}&  {round(evals_protest_ensemble_df['0'].iloc[3],5)}")
print(f"{round(base_riot_evals['0'].iloc[3],5)} & {round(history_riot_evals['0'].iloc[3],5)} &  {round(demog_riot_evals['0'].iloc[3],5)} &   {round(geog_riot_evals['0'].iloc[3],5)} &  {round(econ_riot_evals['0'].iloc[3],5)} &   {round(pol_riot_evals['0'].iloc[3],5)} &  {round(evals_riot_ensemble_df['0'].iloc[3],5)}")
print(f"{round(base_terror_evals['0'].iloc[3],5)} & {round(history_terror_evals['0'].iloc[3],5)} &  {round(demog_terror_evals['0'].iloc[3],5)} &   {round(geog_terror_evals['0'].iloc[3],5)} &  {round(econ_terror_evals['0'].iloc[3],5)} &  {round(pol_terror_evals['0'].iloc[3],5)}& {round(evals_terror_ensemble_df['0'].iloc[3],5)}")
print(f"{round(base_sb_evals['0'].iloc[3],5)} &  {round(history_sb_evals['0'].iloc[3],5)} &  {round(demog_sb_evals['0'].iloc[3],5)} &  {round(geog_sb_evals['0'].iloc[3],5)} & {round(econ_sb_evals['0'].iloc[3],5)} &  {round(pol_sb_evals['0'].iloc[3],5)}& {round(evals_sb_ensemble_df['0'].iloc[3],5)}")
print(f"{round(base_ns_evals['0'].iloc[3],5)} &  {round(history_ns_evals['0'].iloc[3],5)} &  {round(demog_ns_evals['0'].iloc[3],5)} &   {round(geog_ns_evals['0'].iloc[3],5)} &  {round(econ_ns_evals['0'].iloc[3],5)} &  {round(pol_ns_evals['0'].iloc[3],5)} & {round(evals_ns_ensemble_df['0'].iloc[3],5)}")      
print(f"{round(base_osv_evals['0'].iloc[3],5)} &  {round(history_osv_evals['0'].iloc[3],5)} &  {round(demog_osv_evals['0'].iloc[3],5)} &  {round(geog_osv_evals['0'].iloc[3],5)} &  {round(econ_osv_evals['0'].iloc[3],5)} & {round(pol_osv_evals['0'].iloc[3],5)}&  {round(evals_osv_ensemble_df['0'].iloc[3],5)}")            
     
                            ########################
                            ### Conflict History ###
                            ########################

# Load shap values
history_protest_shap=pd.read_csv("out/history_protest_shap.csv",index_col=[0])
history_riot_shap=pd.read_csv("out/history_riot_shap.csv",index_col=[0])
history_terror_shap=pd.read_csv("out/history_terror_shap.csv",index_col=[0])
history_sb_shap=pd.read_csv("out/history_sb_shap.csv",index_col=[0])
history_ns_shap=pd.read_csv("out/history_ns_shap.csv",index_col=[0])
history_osv_shap=pd.read_csv("out/history_osv_shap.csv",index_col=[0])

##########################
### Feature importance ###
##########################

# For each feature per outcome, obtain the absolute shap value and remove variables
# with _id, because these are the ones indicating whether an observation is imputed, 
# and are therefore not of prime interest.

s_protest = pd.DataFrame(list(zip(['d_protest_lag1',"d_protest_zeros_growth","d_neighbors_proteset_lag1","regime_duration"],np.abs(history_protest_shap).mean())),columns=['Feature','Protest'])
# Rename variables before merging so that they match
s_protest.loc[s_protest["Feature"]=="d_protest_lag1","Feature"]="d_lag1"
s_protest.loc[s_protest["Feature"]=="d_protest_zeros_growth","Feature"]="d_zeros_growth"
s_protest.loc[s_protest["Feature"]=="d_neighbors_proteset_lag1","Feature"]="d_neighbors_lag1"
shap_conflict_hist = s_protest[~s_protest['Feature'].str.contains('_id')]

s_riot = pd.DataFrame(list(zip(['d_riot_lag1',"d_riot_zeros_growth","d_neighbors_riot_lag1",'regime_duration'],np.abs(history_riot_shap).mean())),columns=['Feature','Riot'])
# Rename variables before merging so that they match
s_riot.loc[s_riot["Feature"]=="d_riot_lag1","Feature"]="d_lag1"
s_riot.loc[s_riot["Feature"]=="d_riot_zeros_growth","Feature"]="d_zeros_growth"
s_riot.loc[s_riot["Feature"]=="d_neighbors_riot_lag1","Feature"]="d_neighbors_lag1"
shap_conflict_hist = pd.merge(shap_conflict_hist, s_riot[~s_riot['Feature'].str.contains('_id')],on=["Feature"])

s_remote = pd.DataFrame(list(zip(['d_terrorism_lag1',"d_terrorism_zeros_growth","d_neighbors_terror_lag1",'regime_duration'],np.abs(history_terror_shap).mean())),columns=['Feature','Terrorism'])
# Rename variables before merging so that they match
s_remote.loc[s_remote["Feature"]=="d_terrorism_lag1","Feature"]="d_lag1"
s_remote.loc[s_remote["Feature"]=="d_terrorism_zeros_growth","Feature"]="d_zeros_growth"
s_remote.loc[s_remote["Feature"]=="d_neighbors_terror_lag1","Feature"]="d_neighbors_lag1"
shap_conflict_hist = pd.merge(shap_conflict_hist, s_remote[~s_remote['Feature'].str.contains('_id')],on=["Feature"])

s_sb = pd.DataFrame(list(zip(['d_sb_lag1',"d_sb_zeros_growth","d_neighbors_sb_lag1",'regime_duration'],np.abs(history_sb_shap).mean())),columns=['Feature','State-based'])
# Rename variables before merging so that they match
s_sb.loc[s_sb["Feature"]=="d_sb_lag1","Feature"]="d_lag1"
s_sb.loc[s_sb["Feature"]=="d_sb_zeros_growth","Feature"]="d_zeros_growth"
s_sb.loc[s_sb["Feature"]=="d_neighbors_sb_lag1","Feature"]="d_neighbors_lag1"
shap_conflict_hist = pd.merge(shap_conflict_hist, s_sb[~s_sb['Feature'].str.contains('_id')],on=["Feature"])

s_osv = pd.DataFrame(list(zip(['d_osv_lag1',"d_osv_zeros_growth","d_neighbors_osv_lag1",'regime_duration'],np.abs(history_osv_shap).mean())),columns=['Feature','One-sided'])
# Rename variables before merging so that they match
s_osv.loc[s_osv["Feature"]=="d_osv_lag1","Feature"]="d_lag1"
s_osv.loc[s_osv["Feature"]=="d_osv_zeros_growth","Feature"]="d_zeros_growth"
s_osv.loc[s_osv["Feature"]=="d_neighbors_osv_lag1","Feature"]="d_neighbors_lag1"
shap_conflict_hist = pd.merge(shap_conflict_hist, s_osv[~s_osv['Feature'].str.contains('_id')],on=["Feature"])

s_ns = pd.DataFrame(list(zip(['d_ns_lag1',"d_ns_zeros_growth","d_neighbors_ns_lag1",'regime_duration'],np.abs(history_ns_shap).mean())),columns=['Feature','Non-state'])
# Rename variables before merging so that they match
s_ns.loc[s_ns["Feature"]=="d_ns_lag1","Feature"]="d_lag1"
s_ns.loc[s_ns["Feature"]=="d_ns_zeros_growth","Feature"]="d_zeros_growth"
s_ns.loc[s_ns["Feature"]=="d_neighbors_ns_lag1","Feature"]="d_neighbors_lag1"
shap_conflict_hist = pd.merge(shap_conflict_hist, s_ns[~s_ns['Feature'].str.contains('_id')],on=["Feature"])

# Min-max normalize shap values

# Remove column with feature name, min-max normalize, and add column with feature name again.
shap_conflict_hist_s=shap_conflict_hist.iloc[:, 1:]
shap_conflict_hist_s = (shap_conflict_hist_s-shap_conflict_hist_s.min())/(shap_conflict_hist_s.max()-shap_conflict_hist_s.min())
shap_conflict_hist_s["Feature"]=shap_conflict_hist["Feature"]

# Sort features by the sum across outcomes 
shap_conflict_hist_s=shap_conflict_hist_s.loc[shap_conflict_hist_s.iloc[:, :-1].sum(axis=1).sort_values().index]

# Remove feature name for plotting
shap_conflict_hist_ss=shap_conflict_hist_s.iloc[:, :-1]

# Get fancy names from names file for plot
var_list=list(shap_conflict_hist_s["Feature"])
for c,i in zip(var_list,range(len(var_list))):
    if var_list[i]==c:
        var_list[i]=names[c]

# Plot SHAP importance in barplot
fig, ax = plt.subplots(figsize=(10, 5))
colors = ["forestgreen","lightgreen","steelblue","lightblue","purple","violet"]

# Loop over outcomes
base = [0,0,0,0]
for i,out in zip(range(6),(shap_conflict_hist_ss.columns)):
    # For each outcome, plot the size of the shap value for each feature
    ax.barh([0,1,2,3],shap_conflict_hist_ss[out],left=base,height=0.8,label=out,color=colors[i])
    # Update base with shap values 
    base += shap_conflict_hist_ss[out]

# Add legend, ticks, labels and save
entries = [mpatches.Patch(color='forestgreen',label='Protest'),mpatches.Patch(color='lightgreen',label='Riots'),mpatches.Patch(color='steelblue',label='Terrorism'),mpatches.Patch(color='lightblue',label='Battles'),mpatches.Patch(color='purple',label='Non-state'),mpatches.Patch(color='violet', label='One-sided')]
leg = ax.legend(handles=entries,title='',loc='center left',bbox_to_anchor=(-0.3, -0.2),frameon=False,fontsize=15,title_fontsize=20,ncol=6,columnspacing=0.5)
ax.set_yticks([0,1,2,3],var_list,size=20)
ax.set_xticks([0,1,2,3,4,5,6],[0,1,2,3,4,5,6],size=15)
ax.set_xlabel("SHAP Values",size=20)
plt.savefig("out/struc_imp_conflict_history.png",dpi=100,bbox_inches="tight")
plt.show()
 
############################ 
### Violine plot for t-1 ###      
############################ 

# Plot
fig,ax = plt.subplots(figsize=(12, 8))

# Protest # 
# Subset data to ACLED coverage
base=pd.read_csv("data/data_out/acled_cy_protest.csv",index_col=0)
base=base[["year","gw_codes"]][~base['gw_codes'].isin(list(exclude.values()))]
x=pd.read_csv("out/df_conf_hist_full.csv",index_col=0)
x=pd.merge(left=base,right=x,on=["year","gw_codes"],how="left")

# Add shap values and plot
x["shaps_protest"]=history_protest_shap.iloc[:, 0]
sns.violinplot(x="d_protest_lag1",y="shaps_protest",data=x,inner=None,color=colors[0],density_norm="width")

# Riots #
# Add shap values and plot
x["shaps_riot"]=history_riot_shap.iloc[:, 0].reset_index(drop=True)
x["d_riot_lag1"]=x["d_riot_lag1"]+2 # to move plots to the right
sns.violinplot(x="d_riot_lag1",y="shaps_riot",data=x,inner=None,color=colors[1],density_norm="width")
    
# Terrorism # 
# Subset data to GTD coverage
x=pd.read_csv("out/df_conf_hist_full.csv",index_col=0)
x=x.loc[x["year"]<2021].reset_index(drop=True)
x=x.loc[x["year"]!=1993].reset_index(drop=True)

# Add shap values and plot
x["d_terror_lag1"]=x["d_terror_lag1"]+4 # to move plots to the right
x["shaps_terror"]=history_terror_shap.iloc[:, 0]
sns.violinplot(x="d_terror_lag1",y="shaps_terror",data=x,inner=None,color=colors[2],density_norm="width")

# SB #
# Add shap values and plot
x=pd.read_csv("out/df_conf_hist_full.csv",index_col=0)
x["d_sb_lag1"]=x["d_sb_lag1"]+6 # to move plots to the right
x["shaps_sb"]=history_sb_shap.iloc[:, 0]
sns.violinplot(x="d_sb_lag1",y="shaps_sb",data=x,inner=None,color=colors[3],density_norm="width")

# NS #
# Add shap values and plot
x["d_ns_lag1"]=x["d_ns_lag1"]+8 # to move plots to the right
x["shaps_ns"]=history_ns_shap.iloc[:, 0]
sns.violinplot(x="d_ns_lag1",y="shaps_ns",data=x,inner=None,color=colors[4],density_norm="width")

# OSV #
# Add shap values and plot
x["d_osv_lag1"]=x["d_osv_lag1"]+10 # to move plots to the right
x["shaps_osv"]=history_osv_shap.iloc[:, 0]
sns.violinplot(x="d_osv_lag1",y="shaps_osv",data=x,inner=None,color=colors[5],density_norm="width")

# Add ticks, labels and save
ax.set_xlabel(" ",size=20)
ax.set_yticks([-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8],[-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8],size=20)
ax.set_xticks([],[])
ax.set_ylabel("SHAP value",size=20)
ax.set_xlim([-1,12])
ax.text(0,-0.385,"Protest",fontsize=20)
ax.text(2.1,-0.385,"Riots",fontsize=20)
ax.text(3.8,-0.385,"Terrorism",fontsize=20)
ax.text(6,-0.385,"Battles",fontsize=20)
ax.text(8,-0.385,"Non-state",fontsize=20)
ax.text(10,-0.385,"One-sided",fontsize=20)
plt.savefig("out/struc_shap_t1.png",dpi=100,bbox_inches="tight")
plt.show()  


                                ##################
                                ### Demography ###
                                ##################
                                
# Load shap values
demog_protest_shap=pd.read_csv("out/demog_protest_shap.csv",index_col=[0])
demog_riot_shap=pd.read_csv("out/demog_riot_shap.csv",index_col=[0])
demog_terror_shap=pd.read_csv("out/demog_terror_shap.csv",index_col=[0])
demog_sb_shap=pd.read_csv("out/demog_sb_shap.csv",index_col=[0])
demog_ns_shap=pd.read_csv("out/demog_ns_shap.csv",index_col=[0])
demog_osv_shap=pd.read_csv("out/demog_osv_shap.csv",index_col=[0])

##########################
### Feature importance ###
##########################

# For each feature per outcome, obtain the absolute shap value and remove variables
# with _id, because these are the ones indicating whether an observation is imputed, 
# and are therefore not of prime interest.

s_protest = pd.DataFrame(list(zip(demog_theme,np.abs(demog_protest_shap).mean())),columns=['Feature','Protest'])
shap_demog_hist = s_protest[~s_protest['Feature'].str.contains('_id')]

s_riot = pd.DataFrame(list(zip(demog_theme,np.abs(demog_riot_shap).mean())),columns=['Feature','Riot'])
shap_demog_hist = pd.merge(shap_demog_hist, s_riot[~s_riot['Feature'].str.contains('_id')],on=["Feature"])

s_remote = pd.DataFrame(list(zip(demog_theme,np.abs(demog_terror_shap).mean())),columns=['Feature','Terrorism'])
shap_demog_hist = pd.merge(shap_demog_hist, s_remote[~s_remote['Feature'].str.contains('_id')],on=["Feature"])

s_sb = pd.DataFrame(list(zip(demog_theme,np.abs(demog_sb_shap).mean())),columns=['Feature','State-based'])
shap_demog_hist = pd.merge(shap_demog_hist, s_sb[~s_sb['Feature'].str.contains('_id')],on=["Feature"])

s_osv = pd.DataFrame(list(zip(demog_theme,np.abs(demog_osv_shap).mean())),columns=['Feature','One-sided'])
shap_demog_hist = pd.merge(shap_demog_hist,s_osv[~s_osv['Feature'].str.contains('_id')],on=["Feature"])

s_ns = pd.DataFrame(list(zip(demog_theme,np.abs(demog_ns_shap).mean())),columns=['Feature','Non-state'])
shap_demog_hist = pd.merge(shap_demog_hist, s_ns[~s_ns['Feature'].str.contains('_id')],on=["Feature"])

# Min-max normalize shap values

# Remove column with feature name, min-max normalize, and add column with feature name again.
shap_demog_hist_s=shap_demog_hist.iloc[:, 1:]
shap_demog_hist_s = (shap_demog_hist_s-shap_demog_hist_s.min())/(shap_demog_hist_s.max()-shap_demog_hist_s.min())
shap_demog_hist_s["Feature"]=shap_demog_hist["Feature"]

# Sort features by the sum across outcomes 
shap_demog_hist_s=shap_demog_hist_s.loc[shap_demog_hist_s.iloc[:, :-1].sum(axis=1).sort_values().index]

# Remove feature name for plotting, and only keep top 5 most important variables
shap_demog_hist_ss=shap_demog_hist_s.iloc[:, :-1][-5:]

# Get fancy names from names file
var_list=list(shap_demog_hist_s["Feature"][-5:])
for c,i in zip(var_list,range(len(var_list))):
    if var_list[i]==c:
        var_list[i]=names[c]
 
# Plot SHAP importance in barplot
fig, ax = plt.subplots(figsize=(10, 6))
colors = ["forestgreen","lightgreen","steelblue","lightblue","purple","violet"]

# Loop over outcomes
base = [0,0,0,0,0]
for i,out in zip(range(6),(shap_demog_hist_ss.columns)):
    # For each outcome, plot the relative size of the shap value for each feature
    ax.barh([0,1,2,3,4], shap_demog_hist_ss[out],left=base,height=0.8,label=out,color=colors[i])
    # update start with shap values 
    base += shap_demog_hist_ss[out]

# Add legend, ticks, labels and save
entries = [mpatches.Patch(color='forestgreen',label='Protest'),mpatches.Patch(color='lightgreen',label='Riots'),mpatches.Patch(color='steelblue',label='Terrorism'),mpatches.Patch(color='lightblue',label='Battles'),mpatches.Patch(color='purple',label='Non-state'),mpatches.Patch(color='violet',label='One-sided')]
leg = ax.legend(handles=entries,title='',loc='center left',bbox_to_anchor=(-0.3, -0.2),frameon=False,fontsize=15,title_fontsize=20,ncol=6,columnspacing=0.5)
ax.set_yticks([0,1,2,3,4],var_list,size=20)
ax.set_xticks([0,1,2,3,4,5,6],[0,1,2,3,4,5,6],size=15)
ax.set_xlabel("SHAP Values",size=20)
plt.savefig("out/struc_imp_demog.png",dpi=100,bbox_inches="tight")
plt.show()

########################################
### Violine plot for population size ###
########################################

# For continuous variables, the values are binned to allow for easier interpretation. 
# The number of bins is specified based on the range of x.

# Check column
demog_theme[0] # ---> log-transform

# Plot
fig,ax = plt.subplots(figsize=(12, 8))

# Protest # 
# Subset data to ACLED coverage
base=pd.read_csv("data/data_out/acled_cy_protest.csv",index_col=0)
base = base[["year","gw_codes"]][~base['gw_codes'].isin(list(exclude.values()))]
x=pd.read_csv("out/df_demog_full.csv",index_col=0)
x["pop"]=np.log(x["pop"]+1) # log-transform
x=pd.merge(left=base,right=x,on=["year","gw_codes"],how="left")

# Add shap values, bin and plot
x["shaps_protest"]=demog_protest_shap.iloc[:, 0]
x["pop_bin"] = pd.cut(x["pop"],bins=5,labels=[0,1,2,3,4]).astype(float)
sns.violinplot(x="pop_bin",y="shaps_protest",data=x,inner=None,color=colors[0],density_norm="width")

# Riots #
# Add shap values, bin and plot
x["pop_bin"] = pd.cut(x["pop"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["pop_bin"] = x["pop_bin"]+5 # to move plots to the right
x["shaps_riot"]=demog_riot_shap.iloc[:, 0]
sns.violinplot(x="pop_bin",y="shaps_riot",data=x,inner=None,color=colors[1],density_norm="width")

# Terrorism # 
# Subset data to GTD coverage
x=pd.read_csv("out/df_demog_full.csv",index_col=0)
x["pop"]=np.log(x["pop"]+1) # log-transform
x=x.loc[x["year"]<2021].reset_index(drop=True)
x=x.loc[x["year"]!=1993].reset_index(drop=True)

# Add shap values, bin and plot
x["shaps_terror"]=demog_terror_shap.iloc[:, 0]
x["pop_bin"] = pd.cut(x["pop"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["pop_bin"] = x["pop_bin"]+10 # to move plots to the right
sns.violinplot(x="pop_bin",y="shaps_terror",data=x,inner=None,color=colors[2],density_norm="width")

# SB #
# Add shap values, bin and plot
x=pd.read_csv("out/df_demog_full.csv",index_col=0)
x["pop"]=np.log(x["pop"]+1) # log-transform
x["shaps_sb"]=demog_sb_shap.iloc[:, 0]
x["pop_bin"] = pd.cut(x["pop"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["pop_bin"] = x["pop_bin"]+15 # to move plots to the right
sns.violinplot(x="pop_bin",y="shaps_sb",data=x,inner=None,color=colors[3],density_norm="width")

# NS #
# Add shap values, bin and plot
x["shaps_ns"]=demog_ns_shap.iloc[:, 0]
x["pop_bin"] = pd.cut(x["pop"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["pop_bin"] = x["pop_bin"]+20 # to move plots to the right
sns.violinplot(x="pop_bin",y="shaps_ns",data=x,inner=None,color=colors[4],density_norm="width")

# OSV #
# Add shap values, bin and plot
x["shaps_osv"]=demog_osv_shap.iloc[:, 0]
x["pop_bin"] = pd.cut(x["pop"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["pop_bin"] = x["pop_bin"]+25 # to move plots to the right
sns.violinplot(x="pop_bin",y="shaps_osv",data=x,inner=None,color=colors[5],density_norm="width")

# Add ticks, labels and save
ax.set_xlabel(" ",size=20)
ax.set_ylabel("SHAP value",size=20)
ax.set_yticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6],[-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6],size=20)
ax.set_ylim(-0.52, 0.62) 
ax.set_xlim(-1, 30) 
ax.set_xticks([],[])   
ax.text(1,-0.563,"Protest",fontsize=20)
ax.text(6,-0.563,"Riots",fontsize=20)
ax.text(10.2,-0.563,"Terrorism",fontsize=20)
ax.text(15.6,-0.563,"Battles",fontsize=20)
ax.text(20.5,-0.563,"Non-state",fontsize=20)
ax.text(25.3,-0.563,"One-sided",fontsize=20)         
plt.savefig("out/struc_shap_scatter_pop.png",dpi=100,bbox_inches="tight")
plt.show()

########################################
### Violine plot for male share 0-14 ###
########################################

# For continuous variables, the values are binned to allow for easier interpretation. 
# The number of bins is specified based on the range of x.

# Check column
demog_theme[6]

# Plot
fig,ax = plt.subplots(figsize=(12, 8))

# Protest # 
# Subset data to ACLED coverage
base=pd.read_csv("data/data_out/acled_cy_protest.csv",index_col=0)
base = base[["year","gw_codes"]][~base['gw_codes'].isin(list(exclude.values()))]
x=pd.read_csv("out/df_demog_full.csv",index_col=0)
x=pd.merge(left=base,right=x,on=["year","gw_codes"],how="left")

# Add shap values, bin and plot
x["shaps_protest"]=demog_protest_shap.iloc[:, 6]
x["pop_male_share_0_14_bin"] = pd.cut(x["pop_male_share_0_14"],bins=5,labels=[0,1,2,3,4]).astype(float)
sns.violinplot(x="pop_male_share_0_14_bin",y="shaps_protest",data=x,inner=None,color=colors[0],density_norm="width")

# Riots #
# Add shap values, bin and plot
x["pop_male_share_0_14_bin"] = pd.cut(x["pop_male_share_0_14"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["pop_male_share_0_14_bin"] = x["pop_male_share_0_14_bin"]+5 # to move plots to the right
x["shaps_riot"]=demog_riot_shap.iloc[:, 6]
sns.violinplot(x="pop_male_share_0_14_bin",y="shaps_riot",data=x,inner=None,color=colors[1],density_norm="width")

# Terrorism # 
# Subset data to GTD coverage
x=pd.read_csv("out/df_demog_full.csv",index_col=0)
x=x.loc[x["year"]<2021].reset_index(drop=True)
x=x.loc[x["year"]!=1993].reset_index(drop=True)

# Add shap values, bin and plot
x["shaps_terror"]=demog_terror_shap.iloc[:, 6]
x["pop_male_share_0_14_bin"] = pd.cut(x["pop_male_share_0_14"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["pop_male_share_0_14_bin"] = x["pop_male_share_0_14_bin"]+10 # to move plots to the right
sns.violinplot(x="pop_male_share_0_14_bin",y="shaps_terror",data=x,inner=None,color=colors[2],density_norm="width")

# SB #
# Add shap values, bin and plot
x=pd.read_csv("out/df_demog_full.csv",index_col=0)
x["shaps_sb"]=demog_sb_shap.iloc[:, 6]
x["pop_male_share_0_14_bin"] = pd.cut(x["pop_male_share_0_14"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["pop_male_share_0_14_bin"] = x["pop_male_share_0_14_bin"]+15 # to move plots to the right
sns.violinplot(x="pop_male_share_0_14_bin",y="shaps_sb",data=x,inner=None,color=colors[3],density_norm="width")

# NS #
# Add shap values, bin and plot
x["shaps_ns"]=demog_ns_shap.iloc[:, 6]
x["pop_male_share_0_14_bin"] = pd.cut(x["pop_male_share_0_14"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["pop_male_share_0_14_bin"] = x["pop_male_share_0_14_bin"]+20 # to move plots to the right
sns.violinplot(x="pop_male_share_0_14_bin",y="shaps_ns",data=x,inner=None,color=colors[4],density_norm="width")

# OSV #
# Add shap values, bin and plot
x["pop_male_share_0_14_bin"] = pd.cut(x["pop_male_share_0_14"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["pop_male_share_0_14_bin"] = x["pop_male_share_0_14_bin"]+25 # to move plots to the right
x["shaps_osv"]=demog_osv_shap.iloc[:, 6]
sns.violinplot(x="pop_male_share_0_14_bin",y="shaps_osv",data=x,inner=None,color=colors[5],density_norm="width")

# Add ticks, labels and save
ax.set_xlabel(" ",size=20)
ax.set_ylabel("SHAP value",size=20)
ax.set_xticks([],[])
ax.set_ylim(-0.32, 0.45)  
ax.set_xlim(-1, 30) 
ax.set_yticks([-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4],[-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4],size=20)
ax.text(1,-0.346,"Protest",fontsize=20)
ax.text(6,-0.346,"Riots",fontsize=20)
ax.text(10.2,-0.346,"Terrorism",fontsize=20)
ax.text(15.9,-0.346,"Battles",fontsize=20)
ax.text(20.5,-0.346,"Non-state",fontsize=20)
ax.text(25.3,-0.346,"One-sided",fontsize=20) 
plt.savefig("out/struc_shap_pop_male_share_0_14.png",dpi=100,bbox_inches="tight")
plt.show()    


                            ###################
                            ### Environment ###
                            ###################

# Load shap values
geog_protest_shap=pd.read_csv("out/geog_protest_shap.csv",index_col=[0])
geog_riot_shap=pd.read_csv("out/geog_riot_shap.csv",index_col=[0])
geog_terror_shap=pd.read_csv("out/geog_terror_shap.csv",index_col=[0])
geog_sb_shap=pd.read_csv("out/geog_sb_shap.csv",index_col=[0])
geog_ns_shap=pd.read_csv("out/geog_ns_shap.csv",index_col=[0])
geog_osv_shap=pd.read_csv("out/geog_osv_shap.csv",index_col=[0])

##########################
### Feature importance ###
##########################

# For each feature per outcome, obtain the absolute shap value and remove variables
# with _id, because these are the ones indicating whether an observation is imputed, 
# and are therefore not of prime interest.

s_protest = pd.DataFrame(list(zip(geog_theme, np.abs(geog_protest_shap.mean()))),columns=['Feature','Protest'])
shap_geog_hist = s_protest[~s_protest['Feature'].str.contains('_id')]

s_riot = pd.DataFrame(list(zip(geog_theme, np.abs(geog_riot_shap).mean())),columns=['Feature','Riot'])
shap_geog_hist = pd.merge(shap_geog_hist, s_riot[~s_riot['Feature'].str.contains('_id')],on=["Feature"])

s_remote = pd.DataFrame(list(zip(geog_theme, np.abs(geog_terror_shap).mean())),columns=['Feature','Terrorism'])
shap_geog_hist = pd.merge(shap_geog_hist, s_remote[~s_remote['Feature'].str.contains('_id')],on=["Feature"])

s_sb = pd.DataFrame(list(zip(geog_theme, np.abs(geog_sb_shap).mean())),columns=['Feature','State-based'])
shap_geog_hist = pd.merge(shap_geog_hist, s_sb[~s_sb['Feature'].str.contains('_id')],on=["Feature"])

s_osv = pd.DataFrame(list(zip(geog_theme, np.abs(geog_osv_shap).mean())),columns=['Feature','One-sided'])
shap_geog_hist = pd.merge(shap_geog_hist, s_osv[~s_osv['Feature'].str.contains('_id')],on=["Feature"])

s_ns = pd.DataFrame(list(zip(geog_theme, np.abs(geog_ns_shap).mean())),columns=['Feature','Non-state'])
shap_geog_hist = pd.merge(shap_geog_hist, s_ns[~s_ns['Feature'].str.contains('_id')],on=["Feature"])

# Min-max normalize shap value

# Remove column with feature name, min-max normalize, and add column with feature name again.
shap_geog_hist_s=shap_geog_hist.iloc[:, 1:]
shap_geog_hist_s = (shap_geog_hist_s-shap_geog_hist_s.min())/(shap_geog_hist_s.max()-shap_geog_hist_s.min())
shap_geog_hist_s["Feature"]=shap_geog_hist["Feature"]

# Sort features by the sum across outcomes 
shap_geog_hist_s=shap_geog_hist_s.loc[shap_geog_hist_s.iloc[:, :-1].sum(axis=1).sort_values().index]

# Remove feature name for plotting and subset the top 8 most important variables
shap_geog_hist_ss=shap_geog_hist_s.iloc[:, :-1][-9:]

# Get fancy names from names file
var_list=list(shap_geog_hist_s["Feature"][-9:])
for c,i in zip(var_list,range(len(var_list))):
    if var_list[i]==c:
        var_list[i]=names[c]

# Plot SHAP importance in barplot
colors = ["forestgreen","lightgreen","steelblue","lightblue","purple","violet"]
fig, ax = plt.subplots(figsize=(10, 6))

base=[0,0,0,0,0,0,0,0,0]
# Loop over outcomes
for i,out in zip(range(6),(shap_geog_hist_ss.columns)):
    # For each outcome, plot the relative size of the shap value for each feature
    ax.barh([0,1,2,3,4,5,6,7,8],shap_geog_hist_ss[out],left=base,height=0.8,label=out,color=colors[i])
    # update start with shap values 
    base += shap_geog_hist_ss[out]

# Add legend, ticks, labels and save
entries = [mpatches.Patch(color='forestgreen',label='Protest'),mpatches.Patch(color='lightgreen',label='Riots'),mpatches.Patch(color='steelblue',label='Terrorism'),mpatches.Patch(color='lightblue',label='Battles'),mpatches.Patch(color='purple',label='Non-state'),mpatches.Patch(color='violet', label='One-sided')]
leg = ax.legend(handles=entries,title='',loc='center left',bbox_to_anchor=(-0.3, -0.2),frameon=False,fontsize=15,title_fontsize=20,ncol=6,columnspacing=0.5)
ax.set_yticks([0,1,2,3,4,5,6,7,8],var_list,size=20)
ax.set_xticks([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5],[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5],size=15)
ax.set_xlabel("SHAP Values",size=20)
plt.savefig("out/struc_imp_geog.png",dpi=100,bbox_inches="tight")
plt.show()

####################################
### Violine plot for waterstress ### 
####################################

# For continuous variables, the values are binned to allow for easier interpretation. 
# The number of bins is specified based on the range of x.

# Check column
geog_theme[10] # ---> log-transform

# Plot
fig,ax = plt.subplots(figsize=(12, 8))

# Protest # 
# Subset data to ACLED coverage
base=pd.read_csv("data/data_out/acled_cy_protest.csv",index_col=0)
base = base[["year","gw_codes"]][~base['gw_codes'].isin(list(exclude.values()))]
x=pd.read_csv("out/df_geog_full.csv",index_col=0)
x["waterstress"]=np.log(x["waterstress"]+1) # log transform
x=pd.merge(left=base,right=x,on=["year","gw_codes"],how="left")

# Add shap values, bin and plot
x["shaps_protest"]=geog_protest_shap.iloc[:, 10]
x["waterstress_bin"] = pd.cut(x["waterstress"],bins=5,labels=[0,1,2,3,4]).astype(float)
sns.violinplot(x="waterstress_bin",y="shaps_protest",data=x,inner=None,color=colors[0],density_norm="width")

# Riots #
# Add shap values, bin and plot
x["shaps_riot"]=geog_riot_shap.iloc[:, 10]
x["waterstress_bin"] = pd.cut(x["waterstress"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["waterstress_bin"] = x["waterstress_bin"]+5 # to move plots to the right
sns.violinplot(x="waterstress_bin",y="shaps_riot",data=x,inner=None,color=colors[1],density_norm="width")

# Terrorism # 
# Subset data to GTD coverage
x=pd.read_csv("out/df_geog_full.csv",index_col=0)
x["waterstress"]=np.log(x["waterstress"]+1) # log transform
x=x.loc[x["year"]<2021].reset_index(drop=True)
x=x.loc[x["year"]!=1993].reset_index(drop=True)

# Add shap values, bin and plot
x["shaps_terror"]=geog_terror_shap.iloc[:, 10]
x["waterstress_bin"] = pd.cut(x["waterstress"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["waterstress_bin"] = x["waterstress_bin"]+10 # to move plots to the right
sns.violinplot(x="waterstress_bin",y="shaps_terror",data=x,inner=None,color=colors[2],density_norm="width")

# SB #
# Add shap values, bin and plot
x=pd.read_csv("out/df_geog_full.csv",index_col=0)
x["waterstress"]=np.log(x["waterstress"]+1) # log transform
x["shaps_sb"]=geog_sb_shap.iloc[:, 10]
x["waterstress_bin"] = pd.cut(x["waterstress"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["waterstress_bin"] = x["waterstress_bin"]+15 # to move plots to the right
sns.violinplot(x="waterstress_bin",y="shaps_sb",data=x,inner=None,color=colors[3],density_norm="width")

# NS #
# Add shap values, bin and plot
x["shaps_ns"]=geog_ns_shap.iloc[:, 10]
x["waterstress_bin"] = pd.cut(x["waterstress"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["waterstress_bin"] = x["waterstress_bin"]+20 # to move plots to the right
sns.violinplot(x="waterstress_bin",y="shaps_ns",data=x,inner=None,color=colors[4],density_norm="width")

# OSV #
# Add shap values, bin and plot
x["shaps_osv"]=geog_osv_shap.iloc[:, 10]
x["waterstress_bin"] = pd.cut(x["waterstress"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["waterstress_bin"] = x["waterstress_bin"]+25 # to move plots to the right
sns.violinplot(x="waterstress_bin",y="shaps_osv",data=x,inner=None,color=colors[5],density_norm="width")

# Add ticks, labels and save
plt.xlabel(" ",size=20)
plt.ylabel("SHAP value",size=20)
ax.set_yticks([-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4],[-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4],size=20)
ax.set_xticks([],[])
ax.set_xlim([-1,30])
ax.set_ylim(-0.3, 0.37)   
ax.text(1,-0.323,"Protest",fontsize=20)
ax.text(6,-0.323,"Riots",fontsize=20)
ax.text(10.2,-0.323,"Terrorism",fontsize=20)
ax.text(15.9,-0.323,"Battles",fontsize=20)
ax.text(20.5,-0.323,"Non-state",fontsize=20)
ax.text(25.3,-0.323,"One-sided",fontsize=20)               
plt.savefig("out/struc_shap_scatter_geog_waterstress.png",dpi=100,bbox_inches="tight")
plt.show()


                                ###############
                                ### Economy ###
                                ###############

# Load shap values
econ_protest_shap=pd.read_csv("out/econ_protest_shap.csv",index_col=[0])
econ_riot_shap=pd.read_csv("out/econ_riot_shap.csv",index_col=[0])
econ_terror_shap=pd.read_csv("out/econ_terror_shap.csv",index_col=[0])
econ_sb_shap=pd.read_csv("out/econ_sb_shap.csv",index_col=[0])
econ_ns_shap=pd.read_csv("out/econ_ns_shap.csv",index_col=[0])
econ_osv_shap=pd.read_csv("out/econ_osv_shap.csv",index_col=[0])

##########################
### Feature importance ###
##########################

# For each feature per outcome, obtain the absolute shap value and remove variables
# with _id, because these are the ones indicating whether an observation is imputed, 
# and are therefore not of prime interest.

s_protest = pd.DataFrame(list(zip(econ_theme, np.abs(econ_protest_shap).mean())),columns=['Feature','Protest'])
shap_econ = s_protest[~s_protest['Feature'].str.contains('_id')]

s_riot = pd.DataFrame(list(zip(econ_theme, np.abs(econ_riot_shap).mean())),columns=['Feature','Riot'])
shap_econ = pd.merge(shap_econ, s_riot[~s_riot['Feature'].str.contains('_id')],on=["Feature"])

s_remote = pd.DataFrame(list(zip(econ_theme, np.abs(econ_terror_shap).mean())),columns=['Feature','Terrorism'])
shap_econ = pd.merge(shap_econ, s_remote[~s_remote['Feature'].str.contains('_id')],on=["Feature"])

s_sb = pd.DataFrame(list(zip(econ_theme, np.abs(econ_sb_shap).mean())),columns=['Feature','State-based'])
shap_econ = pd.merge(shap_econ, s_sb[~s_sb['Feature'].str.contains('_id')],on=["Feature"])

s_osv = pd.DataFrame(list(zip(econ_theme, np.abs(econ_osv_shap).mean())),columns=['Feature','One-sided'])
shap_econ = pd.merge(shap_econ, s_osv[~s_osv['Feature'].str.contains('_id')],on=["Feature"])

s_ns = pd.DataFrame(list(zip(econ_theme, np.abs(econ_ns_shap).mean())),columns=['Feature','Non-state'])
shap_econ = pd.merge(shap_econ, s_ns[~s_ns['Feature'].str.contains('_id')],on=["Feature"])

# Min-max normalize shap values

# Remove column with feature name, min-max normalize, and add column with feature name again.
shap_econ_s=shap_econ.iloc[:, 1:]
shap_econ_s = (shap_econ_s-shap_econ_s.min())/(shap_econ_s.max()-shap_econ_s.min())
shap_econ_s["Feature"]=shap_econ["Feature"]

# Sort features by the sum across outcomes 
shap_econ_s=shap_econ_s.loc[shap_econ_s.iloc[:, :-1].sum(axis=1).sort_values().index]

# Remove feature name for plotting and subset the top 15 most important variables 
shap_econ_ss=shap_econ_s.iloc[:, :-1][-15:]

# Get fancy names from names file
var_list=list(shap_econ_s["Feature"][-15:])
for c,i in zip(var_list,range(len(var_list))):
    if var_list[i]==c:
        var_list[i]=names[c]

# Plot SHAP importance in barplot
colors = ["forestgreen","lightgreen","steelblue","lightblue","purple","violet"]
fig, ax = plt.subplots(figsize=(10, 6))

# Loop over outcomes
base = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i,out in zip(range(6),(shap_econ_ss.columns)):
    # For each outcome, plot the relative size of the shap value for each feature
    ax.barh([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],shap_econ_ss[out],left=base,height=0.8,label=out,color=colors[i])
    # update start with shap values 
    base += shap_econ_ss[out]

# Add legend, ticks, labels and save
entries = [mpatches.Patch(color='forestgreen',label='Protest'),mpatches.Patch(color='lightgreen',label='Riots'),mpatches.Patch(color='steelblue',label='Terrorism'),mpatches.Patch(color='lightblue',label='Battles'),mpatches.Patch(color='purple',label='Non-state'),mpatches.Patch(color='violet', label='One-sided')]
leg = ax.legend(handles=entries,title='',loc='center left',bbox_to_anchor=(-0.3, -0.2),frameon=False,fontsize=15,title_fontsize=20,ncol=6,columnspacing=0.5)
ax.set_yticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],var_list,size=20)
ax.set_xticks([0,0.5,1,1.5,2,2.5,3,3.5,4],[0,0.5,1,1.5,2,2.5,3,3.5,4],size=15)
ax.set_xlabel("SHAP Values",size=20)
plt.savefig("out/struc_imp_econ.png",dpi=100,bbox_inches="tight")
plt.show()


#######################################
### Violine plot for consumer price ###
#######################################

# For continuous variables, the values are binned to allow for easier interpretation. 
# The number of bins is specified based on the range of x.

# Check columns
econ_theme[24] # ---> log-transform

# Plot
fig,ax = plt.subplots(figsize=(12, 8))

# Protest # 
# Subset data to ACLED coverage
base=pd.read_csv("data/data_out/acled_cy_protest.csv",index_col=0)
base = base[["year","gw_codes"]][~base['gw_codes'].isin(list(exclude.values()))]
x=pd.read_csv("out/df_econ_full.csv",index_col=0)
x["conprice"]=np.log(x["conprice"]+1) # log transform
x=pd.merge(left=base,right=x,on=["year","gw_codes"],how="left")

# Add shap values, bin and plot
x["shaps_protest"]=econ_protest_shap.iloc[:, 24]
x["conprice_bin"] = pd.cut(x["conprice"],bins=5,labels=[0,1,2,3,4]).astype(float)
sns.violinplot(x="conprice_bin",y="shaps_protest",data=x,inner=None,color=colors[0],density_norm="width")

# Riots #
# Add shap values, bin and plot
x["shaps_riot"]=econ_riot_shap.iloc[:, 24]
x["conprice_bin"] = pd.cut(x["conprice"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["conprice_bin"] = x["conprice_bin"]+5 # to move plots to the right
sns.violinplot(x="conprice_bin",y="shaps_riot",data=x,inner=None,color=colors[1],density_norm="width")

# Terrorism # 
# Subset data to GTD coverage
x=pd.read_csv("out/df_econ_full.csv",index_col=0)
x["conprice"]=np.log(x["conprice"]+1) # log transform
x=x.loc[x["year"]<2021].reset_index(drop=True)
x=x.loc[x["year"]!=1993].reset_index(drop=True)

# Add shap values, bin and plot
x["shaps_terror"]=econ_terror_shap.iloc[:, 24]
x["conprice_bin"] = pd.cut(x["conprice"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["conprice_bin"] = x["conprice_bin"]+10 # to move plots to the right
sns.violinplot(x="conprice_bin",y="shaps_terror",data=x,inner=None,color=colors[2],density_norm="width")

# SB #
# Add shap values, bin and plot
x=pd.read_csv("out/df_econ_full.csv",index_col=0)
x["conprice"]=np.log(x["conprice"]+1) # log transform
x["shaps_sb"]=econ_sb_shap.iloc[:, 24]
x["conprice_bin"] = pd.cut(x["conprice"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["conprice_bin"] = x["conprice_bin"]+15 # to move plots to the right
sns.violinplot(x="conprice_bin",y="shaps_sb",data=x,inner=None,color=colors[3],density_norm="width")

# NS #
# Add shap values, bin and plot
x["shaps_ns"]=econ_ns_shap.iloc[:, 24]
x["conprice_bin"] = pd.cut(x["conprice"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["conprice_bin"] = x["conprice_bin"]+20 # to move plots to the right
sns.violinplot(x="conprice_bin",y="shaps_ns",data=x,inner=None,color=colors[4],density_norm="width")

# OSV #
# Add shap values, bin and plot
x["shaps_osv"]=econ_osv_shap.iloc[:, 24]
x["conprice_bin"] = pd.cut(x["conprice"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["conprice_bin"] = x["conprice_bin"]+25 # to move plots to the right
sns.violinplot(x="conprice_bin",y="shaps_osv",data=x,inner=None,color=colors[5],density_norm="width")

# Add ticks, labels and save
ax.set_xlabel(" ",size=20)
ax.set_ylabel("SHAP value",size=20)
ax.set_yticks([-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5],[-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5],size=20)
ax.set_xticks([],[])
ax.set_ylim(-0.3,0.53)
ax.set_xlim(-1,30)
ax.text(1,-0.33,"Protest",fontsize=20)
ax.text(6,-0.33,"Riots",fontsize=20)
ax.text(10.2,-0.33,"Terrorism",fontsize=20)
ax.text(15.9,-0.33,"Battles",fontsize=20)
ax.text(20.5,-0.33,"Non-state",fontsize=20)
ax.text(25.3,-0.33,"One-sided",fontsize=20)   
plt.savefig("out/struc_shap_scatter_conprice.png",dpi=100,bbox_inches="tight")
plt.show()

##########################################
### Violine plot for schooling, female ###
##########################################

# For continuous variables, the values are binned to allow for easier interpretation. 
# The number of bins is specified based on the range of x.

# Check column
econ_theme[64]

# Plot
fig,ax = plt.subplots(figsize=(12, 8))

# Protest # 
# Subset data to ACLED coverage
base=pd.read_csv("data/data_out/acled_cy_protest.csv",index_col=0)
base = base[["year","gw_codes"]][~base['gw_codes'].isin(list(exclude.values()))]
x=pd.read_csv("out/df_econ_full.csv",index_col=0)
x=pd.merge(left=base,right=x,on=["year","gw_codes"],how="left")

# Add shap values, bin and plot
x["shaps_protest"]=econ_protest_shap.iloc[:, 64]
x["eys_female_bin"] = pd.cut(x["eys_female"],bins=5,labels=[0,1,2,3,4]).astype(float)
sns.violinplot(x="eys_female_bin",y="shaps_protest",data=x,inner=None,color=colors[0],density_norm="width")

# Riots #
# Add shap values, bin and plot
x["shaps_riot"]=econ_riot_shap.iloc[:, 64]
x["eys_female_bin"] = pd.cut(x["eys_female"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["eys_female_bin"] = x["eys_female_bin"]+5 # to move plots to the right
sns.violinplot(x="eys_female_bin",y="shaps_riot",data=x,inner=None,color=colors[1],density_norm="width")

# Terrorism # 
# Subset data to GTD coverage
x=pd.read_csv("out/df_econ_full.csv",index_col=0)
x=x.loc[x["year"]<2021].reset_index(drop=True)
x=x.loc[x["year"]!=1993].reset_index(drop=True)

# Add shap values, bin and plot
x["shaps_terror"]=econ_terror_shap.iloc[:, 64]
x["eys_female_bin"] = pd.cut(x["eys_female"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["eys_female_bin"] = x["eys_female_bin"]+10 # to move plots to the right
sns.violinplot(x="eys_female_bin",y="shaps_terror",data=x,inner=None,color=colors[2],density_norm="width")

# SB #
# Add shap values, bin and plot
x=pd.read_csv("out/df_econ_full.csv",index_col=0)
x["shaps_sb"]=econ_sb_shap.iloc[:, 64]
x["eys_female_bin"] = pd.cut(x["eys_female"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["eys_female_bin"] = x["eys_female_bin"]+15 # to move plots to the right
sns.violinplot(x="eys_female_bin",y="shaps_sb",data=x,inner=None,color=colors[3],density_norm="width")

# NS #
# Add shap values, bin and plot
x["shaps_ns"]=econ_ns_shap.iloc[:, 64]
x["eys_female_bin"] = pd.cut(x["eys_female"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["eys_female_bin"] = x["eys_female_bin"]+20 # to move plots to the right
sns.violinplot(x="eys_female_bin",y="shaps_ns",data=x,inner=None,color=colors[4],density_norm="width")

# OSV #
# Add shap values, bin and plot
x["shaps_osv"]=econ_osv_shap.iloc[:, 64]
x["eys_female_bin"] = pd.cut(x["eys_female"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["eys_female_bin"] = x["eys_female_bin"]+25 # to move plots to the right
sns.violinplot(x="eys_female_bin",y="shaps_osv",data=x,inner=None,color=colors[5],density_norm="width")

# Add ticks, labels and save
ax.set_xlabel(" ",size=20)
ax.set_ylabel("SHAP value",size=20)
ax.set_yticks([-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4],[-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4],size=20)
ax.set_ylim(-0.17, 0.4)  
ax.set_xticks([],[])
ax.set_xlim(-1,30)
ax.text(1,-0.189,"Protest",fontsize=20)
ax.text(6,-0.189,"Riots",fontsize=20)
ax.text(10.2,-0.189,"Terrorism",fontsize=20)
ax.text(15.9,-0.189,"Battles",fontsize=20)
ax.text(20.5,-0.189,"Non-state",fontsize=20)
ax.text(25.3,-0.189,"One-sided",fontsize=20) 
plt.savefig("out/struc_shap_scatter_econ_eys_female.png",dpi=100,bbox_inches="tight")
plt.show()



############################
### Violine plot for oil ###
############################

# For continuous variables, the values are binned to allow for easier interpretation. 
# The number of bins is specified based on the range of x.

# Check column
econ_theme[2] # ---> log-transform

# Plot
fig,ax = plt.subplots(figsize=(12, 8))

# Protest # 
# Subset data to ACLED coverage
base=pd.read_csv("data/data_out/acled_cy_protest.csv",index_col=0)
base = base[["year","gw_codes"]][~base['gw_codes'].isin(list(exclude.values()))]
x=pd.read_csv("out/df_econ_full.csv",index_col=0)
x["oil_share"]=np.log(x["oil_share"]+1) # log transform
x=pd.merge(left=base,right=x,on=["year","gw_codes"],how="left")

# Add shap values, bin and plot
x["shaps_protest"]=econ_protest_shap.iloc[:, 2]
x["oil_share_bin"] = pd.cut(x["oil_share"],bins=4,labels=[0,1,2,3]).astype(float)
sns.violinplot(x="oil_share_bin",y="shaps_protest",data=x,inner=None,color=colors[0],density_norm="width")

# Riots #
# Add shap values, bin and plot
x["shaps_riot"]=econ_riot_shap.iloc[:, 2]
x["oil_share_bin"] = pd.cut(x["oil_share"],bins=4,labels=[0,1,2,3]).astype(float)
x["oil_share_bin"] = x["oil_share_bin"]+4 # to move plots to the right
sns.violinplot(x="oil_share_bin",y="shaps_riot",data=x,inner=None,color=colors[1],density_norm="width")

# Terrorism # 
# Subset data to GTD coverage
x=pd.read_csv("out/df_econ_full.csv",index_col=0)
x["oil_share"]=np.log(x["oil_share"]+1) # log transform
x=x.loc[x["year"]<2021].reset_index(drop=True)
x=x.loc[x["year"]!=1993].reset_index(drop=True)

# Add shap values, bin and plot
x["shaps_terror"]=econ_terror_shap.iloc[:, 2]
x["oil_share_bin"] = pd.cut(x["oil_share"],bins=4,labels=[0,1,2,3]).astype(float)
x["oil_share_bin"] = x["oil_share_bin"]+8 # to move plots to the right
sns.violinplot(x="oil_share_bin",y="shaps_terror",data=x,inner=None,color=colors[2],density_norm="width")

# SB #
# Add shap values, bin and plot
x=pd.read_csv("out/df_econ_full.csv",index_col=0)
x["oil_rents"]=np.log(x["oil_share"]+1) # log transform
x["shaps_sb"]=econ_sb_shap.iloc[:, 2]
x["oil_share_bin"] = pd.cut(x["oil_share"],bins=4,labels=[0,1,2,3]).astype(float)
x["oil_share_bin"] = x["oil_share_bin"]+12 # to move plots to the right
sns.violinplot(x="oil_share_bin",y="shaps_sb",data=x,inner=None,color=colors[3],density_norm="width")

# NS #
# Add shap values, bin and plot
x["shaps_ns"]=econ_ns_shap.iloc[:, 2]
x["oil_share_bin"] = pd.cut(x["oil_share"],bins=4,labels=[0,1,2,3]).astype(float)
x["oil_share_bin"] = x["oil_share_bin"]+16 # to move plots to the right
sns.violinplot(x="oil_share_bin",y="shaps_ns",data=x,inner=None,color=colors[4],density_norm="width")

# OSV #
# Add shap values, bin and plot
x["shaps_osv"]=econ_osv_shap.iloc[:, 2]
x["oil_share_bin"] = pd.cut(x["oil_share"],bins=4,labels=[0,1,2,3]).astype(float)
x["oil_share_bin"] = x["oil_share_bin"]+20 # to move plots to the right
sns.violinplot(x="oil_share_bin",y="shaps_osv",data=x,inner=None,color=colors[5],density_norm="width")

# Add ticks, labels and save
ax.set_xlabel(" ",size=20)
ax.set_ylabel("SHAP value",size=20)
ax.set_xticks([],[])
ax.set_yticks([-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25],[-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25],size=20)
ax.set_xlim(-1,24)         
ax.set_ylim(-0.1, 0.25)  
ax.text(0.4,-0.112,"Protest",fontsize=20)
ax.text(4.4,-0.112,"Riots",fontsize=20)
ax.text(8.2,-0.112,"Terrorism",fontsize=20)
ax.text(12.5,-0.112,"Battles",fontsize=20)
ax.text(16.2,-0.112,"Non-state",fontsize=20)
ax.text(20.3,-0.112,"One-sided",fontsize=20)   
plt.savefig("out/struc_shap_scatter_econ_oil.png",dpi=100,bbox_inches="tight")
plt.show()

                                ##############
                                ### Regime ###
                                ##############

# Load shap values
pol_protest_shap=pd.read_csv("out/pol_protest_shap.csv",index_col=[0])
pol_riot_shap=pd.read_csv("out/pol_riot_shap.csv",index_col=[0])
pol_terror_shap=pd.read_csv("out/pol_terror_shap.csv",index_col=[0])
pol_sb_shap=pd.read_csv("out/pol_sb_shap.csv",index_col=[0])
pol_ns_shap=pd.read_csv("out/pol_ns_shap.csv",index_col=[0])
pol_osv_shap=pd.read_csv("out/pol_osv_shap.csv",index_col=[0])

### Feature importance ###

# For each feature per outcome, obtain the absolute shap value and remove variables
# with _id, because these are the ones indicating whether an observation is imputed, 
# and are therefore not of prime interest.

s_protest = pd.DataFrame(list(zip(pol_theme, np.abs(pol_protest_shap).mean())),columns=['Feature','Protest'])
shap_pol = s_protest[~s_protest['Feature'].str.contains('_id')]

s_riot = pd.DataFrame(list(zip(pol_theme, np.abs(pol_riot_shap).mean())),columns=['Feature','Riot'])
shap_pol = pd.merge(shap_pol, s_riot[~s_riot['Feature'].str.contains('_id')],on=["Feature"])

s_remote = pd.DataFrame(list(zip(pol_theme, np.abs(pol_terror_shap).mean())),columns=['Feature','Terrorism'])
shap_pol = pd.merge(shap_pol, s_remote[~s_remote['Feature'].str.contains('_id')],on=["Feature"])

s_sb = pd.DataFrame(list(zip(pol_theme, np.abs(pol_sb_shap).mean())),columns=['Feature','State-based'])
shap_pol = pd.merge(shap_pol, s_sb[~s_sb['Feature'].str.contains('_id')],on=["Feature"])

s_osv = pd.DataFrame(list(zip(pol_theme, np.abs(pol_osv_shap).mean())),columns=['Feature','One-sided'])
shap_pol = pd.merge(shap_pol, s_osv[~s_osv['Feature'].str.contains('_id')],on=["Feature"])

s_ns = pd.DataFrame(list(zip(pol_theme, np.abs(pol_ns_shap).mean())),columns=['Feature','Non-state'])
shap_pol = pd.merge(shap_pol, s_ns[~s_ns['Feature'].str.contains('_id')],on=["Feature"])

# Min-max normalize shap values

# Remove column with feature name, min-max normalize, and add column with feature name again.
shap_pol_s=shap_pol.iloc[:, 1:]
shap_pol_s = (shap_pol_s-shap_pol_s.min())/(shap_pol_s.max()-shap_pol_s.min())
shap_pol_s["Feature"]=shap_pol["Feature"]

# Sort features by the sum across outcomes 
shap_pol_s=shap_pol_s.loc[shap_pol_s.iloc[:, :-1].sum(axis=1).sort_values().index]

# Remove feature name for plotting and keep top 5 features with highest importance
shap_pol_ss=shap_pol_s.iloc[:, :-1][-5:]

# Get fancy names from names file
var_list=list(shap_pol_s["Feature"][-5:])
for c,i in zip(var_list,range(len(var_list))):
    if var_list[i]==c:
        var_list[i]=names[c]

# Plot SHAP importance in barplot
colors = ["forestgreen","lightgreen","steelblue","lightblue","purple","violet"]
fig, ax = plt.subplots(figsize=(10, 6))

# Loop over outcomes
base = [0,0,0,0,0]
for i,out in zip(range(6),(shap_pol_ss.columns)):
    # For each outcome, plot the relative size of the shap value for each feature
    ax.barh([0,1,2,3,4],shap_pol_ss[out],left=base,height=0.8,label=out,color=colors[i])
    # update start with shap values 
    base += shap_pol_ss[out]

# Add legend, ticks, labels and save
entries = [mpatches.Patch(color='forestgreen',label='Protest'),mpatches.Patch(color='lightgreen',label='Riots'),mpatches.Patch(color='steelblue',label='Terrorism'),mpatches.Patch(color='lightblue',label='Battles'),mpatches.Patch(color='purple',label='Non-state'),mpatches.Patch(color='violet', label='One-sided')]
leg = ax.legend(handles=entries,title='',loc='center left',bbox_to_anchor=(-0.3, -0.2),frameon=False,fontsize=15,title_fontsize=20,ncol=6,columnspacing=0.5)
ax.set_yticks([0,1,2,3,4],var_list,size=20)
ax.set_xticks([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5],[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5],size=15)
ax.set_xlabel("SHAP Values",size=20)
plt.savefig("out/struc_imp_pol.png",dpi=100,bbox_inches="tight")
plt.show()


###############################
### Violine plot for mobile ###
###############################

# For continuous variables, the values are binned to allow for easier interpretation. 
# The number of bins is specified based on the range of x.

# Check column
pol_theme[24]

# Plot
fig,ax = plt.subplots(figsize=(12, 8))

# Protest # 
# Subset data to ACLED coverage
base=pd.read_csv("data/data_out/acled_cy_protest.csv",index_col=0)
base = base[["year","gw_codes"]][~base['gw_codes'].isin(list(exclude.values()))]
x=pd.read_csv("out/df_pol_full.csv",index_col=0)
x=pd.merge(left=base,right=x,on=["year","gw_codes"],how="left")

# Add shap values, bin and plot
x["shaps_protest"]=pol_protest_shap.iloc[:, 24]
x["mobile_bin"] = pd.cut(x["mobile"],bins=5,labels=[0,1,2,3,4]).astype(float)
sns.violinplot(x="mobile_bin",y="shaps_protest",data=x,inner=None,color=colors[0],density_norm="width")

# Riots #
# Add shap values, bin and plot
x["shaps_riot"]=pol_riot_shap.iloc[:, 24]
x["mobile_bin"] = pd.cut(x["mobile"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["mobile_bin"] = x["mobile_bin"]+5 # to move plots to the right
sns.violinplot(x="mobile_bin",y="shaps_riot",data=x,inner=None,color=colors[1],density_norm="width")

# Terrorism # 
# Subset data to GTD coverage
x=pd.read_csv("out/df_pol_full.csv",index_col=0)
x=x.loc[x["year"]<2021].reset_index(drop=True)
x=x.loc[x["year"]!=1993].reset_index(drop=True)

# Add shap values, bin and plot
x["shaps_terror"]=pol_terror_shap.iloc[:, 24]
x["mobile_bin"] = pd.cut(x["mobile"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["mobile_bin"] = x["mobile_bin"]+10 # to move plots to the right
sns.violinplot(x="mobile_bin",y="shaps_terror",data=x,inner=None,color=colors[2],density_norm="width")

# SB #
# Add shap values, bin and plot
x=pd.read_csv("out/df_pol_full.csv",index_col=0)
x["shaps_sb"]=pol_sb_shap.iloc[:, 24]
x["mobile_bin"] = pd.cut(x["mobile"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["mobile_bin"] = x["mobile_bin"]+15 # to move plots to the right
sns.violinplot(x="mobile_bin",y="shaps_sb",data=x,inner=None,color=colors[3],density_norm="width")

# NS #
# Add shap values, bin and plot
x["shaps_ns"]=pol_ns_shap.iloc[:, 24]
x["mobile_bin"] = pd.cut(x["mobile"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["mobile_bin"] = x["mobile_bin"]+20 # to move plots to the right
sns.violinplot(x="mobile_bin",y="shaps_ns",data=x,inner=None,color=colors[4],density_norm="width")

# OSV #
# Add shap values, bin and plot
x["shaps_osv"]=pol_osv_shap.iloc[:, 24]
x["mobile_bin"] = pd.cut(x["mobile"],bins=5,labels=[0,1,2,3,4]).astype(float)
x["mobile_bin"] = x["mobile_bin"]+25 # to move plots to the right
sns.violinplot(x="mobile_bin",y="shaps_osv",data=x,inner=None,color=colors[5],density_norm="width")

# Add ticks, labels and save
ax.set_xlabel(" ",size=20)
ax.set_ylabel("SHAP value",size=20)
ax.set_yticks([-0.25,-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4],[-0.25,-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4],size=20)
ax.set_xticks([],[])
ax.set_xlim(-1,30)
ax.set_ylim(-0.2, 0.2)   
ax.text(1,-0.214,"Protest",fontsize=20)
ax.text(6,-0.214,"Riots",fontsize=20)
ax.text(10.2,-0.214,"Terrorism",fontsize=20)
ax.text(15.9,-0.214,"Battles",fontsize=20)
ax.text(20.5,-0.214,"Non-state",fontsize=20)
ax.text(25.3,-0.214,"One-sided",fontsize=20)                  
plt.savefig("out/struc_shap_scatter_pol_mobile.png",dpi=100,bbox_inches="tight")
plt.show()








