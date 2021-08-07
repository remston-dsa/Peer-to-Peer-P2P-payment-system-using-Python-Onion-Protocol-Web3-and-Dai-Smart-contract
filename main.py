from streamlit import cli as stcli
import p2p_payment as p2p
import streamlit as st
from datetime import *
import sys


if __name__ == '__main__':
    if st._is_running_with_streamlit:
    	st.markdown('# P2P Payment')
    	sender=st.text_input('Sender', '0x60980DCbb13185b898e644302bf0296E1666bBc4')
    	recipient=st.text_input('Recipient')
    	amount=st.number_input('Amount', min_value=0.0)

    	if st.button('Transfer DAI'):
    		if len(recipient) and amount:
	    		p2p.create_transaction(recipient=recipient, amount=int(amount))
	    		st.markdown('Transaction Successful')
	    		
	    		st.write({
	    			'Sender': sender,
	    			'Recipient': recipient,
	    			'Amount': amount,
	    			'Tx_Time': datetime.now().strftime('%m/%d/%y, %H:%M:%S'),
	    			'Status': 'Successful'
	    			})
	    	else:
	    		st.markdown('Transaction Unsuccessful')
	    		st.write({
	    			'Sender': sender,
	    			'Recipient': recipient,
	    			'Amount': amount,
	    			'Tx_Time': datetime.now().strftime('%m/%d/%y, %H:%M:%S'),
	    			'Status': 'Unsuccessful'
	    			})

    else:
        sys.argv=["streamlit","run","main.py"]
        sys.exit(stcli.main())