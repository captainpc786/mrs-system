mkdir -p ~/.streamlit/

echo "\
[serveer]\n\
port =$PORt\n\
enableCORS =false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml