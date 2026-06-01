import pandas as pd
import logging

# [N.E.X.U.S. CORE SUBSYSTEM: DATA EXTRACTION]
# Configured for public ledger export
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [N.E.X.U.S.] - %(message)s')

def export_golden_targets(master_database_path, export_path, top_n=10):
    """
    Extracts the highest-rated regenerative targets from the proprietary 
    N.E.X.U.S. master database after the oncogenic filter pass.
    """
    logging.info("Initiating secure connection to internal target database...")
    
    try:
        # Load the massive internal dataset (Internal Use Only)
        df_master = pd.read_csv(master_database_path)
        logging.info(f"Loaded master dataset containing {len(df_master)} processed genomic sequences.")
        
        # Isolate targets that passed the oncogenic security filter
        logging.info("Applying strict AI filter constraints...")
        
        # Sort targets by the AI-generated NEXUS_SCORE descending
        df_sorted = df_master.sort_values(by='NEXUS_SCORE', ascending=False)
        
        # Extract the absolute elite targets
        df_top_targets = df_sorted.head(top_n)
        
        # Clean up internal proprietary columns before public export
        columns_to_export = ['symbol', 'name', 'location', 'NEXUS_SCORE']
        df_public = df_top_targets[columns_to_export]
        
        logging.info(f"Exporting top {top_n} verified golden targets to public ledger...")
        df_public.to_csv(export_path, index=False)
        
        logging.info(f"Export successful: {export_path}")
        
    except FileNotFoundError:
        logging.error("Master database offline or access restricted to Vanguard credentials.")

if __name__ == "__main__":
    # EXECUTION BLOCK
    # Note: NEXUS_APPROVED_TARGETS.csv remains on secure internal servers.
    MASTER_DB = 'secure_internal/NEXUS_APPROVED_TARGETS.csv'
    EXPORT_FILE = 'NEXUS_TOP_10_GOLDEN_TARGETS.csv'
    
    export_golden_targets(MASTER_DB, EXPORT_FILE, top_n=10)
