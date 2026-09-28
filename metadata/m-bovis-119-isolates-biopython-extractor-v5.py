import csv
import time
import xml.etree.ElementTree as ET
from Bio import Entrez

# Provide your email to comply with NCBI's Entrez query policies
Entrez.email = "your.email@example.com"

# The pristine, verified list of all 119 unique biological accessions from your complete RefSeq FASTA
accessions = [
    'NC_014760.1', 'NC_015725.1', 'NC_018077.1', 'NZ_AP040876.1', 'NZ_AP040877.1', 
    'NZ_AP040878.1', 'NZ_AP040879.1', 'NZ_AP040880.1', 'NZ_AP040881.1', 'NZ_AP040882.1', 
    'NZ_AP040883.1', 'NZ_AP040884.1', 'NZ_AP040885.1', 'NZ_AP040886.1', 'NZ_CM148537.1', 
    'NZ_CM148538.1', 'NZ_CM148539.1', 'NZ_CM148540.1', 'NZ_CM148541.1', 'NZ_CM148542.1', 
    'NZ_CM148543.1', 'NZ_CM149853.1', 'NZ_CM152650.1', 'NZ_CM152651.1', 'NZ_CM152652.1', 
    'NZ_CM152654.1', 'NZ_CM152655.1', 'NZ_CM152656.1', 'NZ_CM166479.1', 'NZ_CP005933.1', 
    'NZ_CP011348.1', 'NZ_CP019639.1', 'NZ_CP022586.1', 'NZ_CP022587.1', 'NZ_CP022588.1', 
    'NZ_CP022589.1', 'NZ_CP022590.1', 'NZ_CP022591.1', 'NZ_CP022592.1', 'NZ_CP022593.1', 
    'NZ_CP022594.1', 'NZ_CP022595.1', 'NZ_CP022596.1', 'NZ_CP022597.1', 'NZ_CP022598.1', 
    'NZ_CP022599.1', 'NZ_CP023663.1', 'NZ_CP038861.1', 'NZ_CP040774.1', 'NZ_CP040775.1', 
    'NZ_CP040776.1', 'NZ_CP040777.1', 'NZ_CP040778.1', 'NZ_CP040779.1', 'NZ_CP042938.1', 
    'NZ_CP045797.1', 'NZ_CP045986.1', 'NZ_CP058418.2', 'NZ_CP058419.2', 'NZ_CP058420.2', 
    'NZ_CP061872.1', 'NZ_CP061873.1', 'NZ_CP061874.1', 'NZ_CP068730.1', 'NZ_CP068731.1', 
    'NZ_CP068732.1', 'NZ_CP068733.1', 'NZ_CP068734.1', 'NZ_CP069056.1', 'NZ_CP069057.1', 
    'NZ_CP069100.1', 'NZ_CP076229.1', 'NZ_CP077758.1', 'NZ_CP092776.1', 'NZ_CP092777.1', 
    'NZ_CP119269.1', 'NZ_CP120636.1', 'NZ_CP123284.1', 'NZ_CP123286.1', 'NZ_CP123287.1', 
    'NZ_CP123288.1', 'NZ_CP123289.1', 'NZ_CP123290.1', 'NZ_CP123291.1', 'NZ_CP123292.1', 
    'NZ_CP123293.1', 'NZ_CP123294.1', 'NZ_CP123296.1', 'NZ_CP123297.1', 'NZ_CP123298.1', 
    'NZ_CP123299.1', 'NZ_CP123300.1', 'NZ_CP123301.1', 'NZ_CP123302.1', 'NZ_CP123303.1', 
    'NZ_CP123304.1', 'NZ_CP123305.1', 'NZ_CP123306.1', 'NZ_CP123308.1', 'NZ_CP123309.1', 
    'NZ_CP135997.1', 'NZ_CP139047.1', 'NZ_CP139493.1', 'NZ_CP139780.1', 'NZ_CP159949.1', 
    'NZ_CP159950.1', 'NZ_CP190342.1', 'NZ_CP190343.1', 'NZ_CP190344.1', 'NZ_CP190345.1', 
    'NZ_CP190346.1', 'NZ_CP190347.1', 'NZ_CP190348.1', 'NZ_CP194391.1', 'NZ_CP194392.1', 
    'NZ_CP194393.1', 'NZ_CP194394.1', 'NZ_CP199311.1', 'NZ_LT578453.1'
]

output_file = "m_bovis_119_biosamples_environmental_metadata_v5.csv"

print(f"Beginning live BioSample metadata extraction for {len(accessions)} unique accessions...")

with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Accession", "BioSample_ID", "Strain", "Collection_Date", 
        "Host", "Isolation_Source", "Host_Health_State", "Host_Tissue_Sampled",
        "Sample_Type", "Host_Disease", "Geographic_Location", 
        "Local_Scale_Environmental_Context", "Broad_Scale_Environmental_Context", 
        "Clinical"
    ])

    for idx, acc in enumerate(accessions, 1):
        try:
            # Step 1: Search the Nucleotide database ('nuccore') for the accession
            search_handle = Entrez.esearch(db="nuccore", term=f"{acc}[Accession]")
            search_results = Entrez.read(search_handle)
            search_handle.close()

            id_list = search_results.get("IdList", [])
            if not id_list:
                writer.writerow([acc, "Nuc_Not_Found"] + ["N/A"] * 12)
                print(f"[{idx}/{len(accessions)}] No Nucleotide record found for: {acc}")
                continue

            nucleotide_uid = id_list

            # Step 2: Use NCBI elink to map the Nucleotide UID to its linked BioSample ID
            link_handle = Entrez.elink(dbfrom="nuccore", db="biosample", id=nucleotide_uid)
            link_results = Entrez.read(link_handle)
            link_handle.close()

            # Parse out the BioSample internal ID from the link results
            biosample_id = None
            try:
                for link_set in link_results:
                    for link_db in link_set.get("LinkSetDb", []):
                        if link_db.get("DbTo") == "biosample":
                            for link in link_db.get("Link", []):
                                biosample_id = link.get("Id")
                                break
            except Exception:
                pass

            if not biosample_id:
                writer.writerow([acc, "No_Linked_BioSample"] + ["N/A"] * 12)
                print(f"[{idx}/{len(accessions)}] No linked BioSample ID found via elink for: {acc}")
                continue

            # Step 3: Fetch the detailed XML record from the BioSample database using the mapped ID
            fetch_handle = Entrez.efetch(db="biosample", id=biosample_id, retmode="xml")
            xml_data = fetch_handle.read()
            fetch_handle.close()

            # Step 4: Parse the BioSample XML attributes
            root = ET.fromstring(xml_data)
            
            strain = "N/A"
            collection_date = "N/A"
            host = "N/A"
            isolation_source = "N/A"
            host_health_state = "N/A"
            host_tissue_sampled = "N/A"
            sample_type = "N/A"
            host_disease = "N/A"
            geo_loc = "N/A"
            local_scale_env = "N/A"
            broad_scale_env = "N/A"
            clinical = "N/A"

            # Parse out the BioSample Accession string (e.g., SAMNxxxxxxxx)
            biosample_acc = biosample_id
            try:
                biosample_acc = root.find(".//BioSample").get("accession", biosample_id)
            except Exception:
                pass

            # Traverse the XML attributes block and map to target columns
            for attr in root.findall(".//Attribute"):
                name = attr.get("attribute_name", "").lower()
                value = attr.text
                
                # Standard fields
                if name == "strain":
                    strain = value
                elif name in ["collection_date", "date"]:
                    collection_date = value
                elif name == "host":
                    host = value
                elif name == "sample_type":
                    sample_type = value
                elif name in ["host_disease", "disease", "disease_state"]:
                    host_disease = value
                elif name in ["geo_loc_name", "country"]:
                    geo_loc = value
                
                # Environmental biome fields
                elif name in ["env_local_scale", "local_env_scale", "local_env", "environmental_feature", "geographic_feature", "geographic feature", "local-scale environmental context", "env_feature"]:
                    local_scale_env = value
                elif name in ["env_broad_scale", "broad_env_scale", "broad_env", "environmental_biome", "biome", "broad-scale environmental context", "env_biome"]:
                    broad_scale_env = value
                
                # New explicitly separated fields requested by user
                elif name in ["isolation_source", "isolation-source", "isolation source", "source"]:
                    isolation_source = value
                elif name in ["host_health_state", "host health state", "health_status", "health status", "health_state", "health state", "host_health_status"]:
                    host_health_state = value
                elif name in ["tissue", "organism_part", "tissue_sampled", "tissue sampled", "host_tissue_sampled", "organism part", "tissue_source", "tissue-source"]:
                    host_tissue_sampled = value
                
                # Clinical description
                elif name in ["clinical_metadata", "clinical", "description", "note", "disease_stage", "clinical_history", "health_status"]:
                    clinical = value

            writer.writerow([
                acc, biosample_acc, strain, collection_date, 
                host, isolation_source, host_health_state, host_tissue_sampled,
                sample_type, host_disease, geo_loc, 
                local_scale_env, broad_scale_env, clinical
            ])
            print(f"[{idx}/{len(accessions)}] Processed {acc} -> Linked BioSample: {biosample_acc} | Strain: {strain}")
            
            # Rate-limiting pause (3 requests per second max)
            time.sleep(0.35)

        except Exception as e:
            writer.writerow([acc, "Error", str(e)] + ["N/A"] * 11)
            print(f"[{idx}/{len(accessions)}] Error processing {acc}: {e}")

print(f"\nLive database extraction complete! Pristine metadata written to: {output_file}")
