tropical-genetic/
│
├── data/
│   ├── raw_submissions/
│   ├── labeled_blocks/
│   └── training/
│
├── model/
│   ├── dataset.py
│   ├── train_model.py
│   ├── model.bin   (trained classifier)
│   └── tokenizer/
│
├── template/
│   ├── journal_template.tex
│   └── notatebox_style.tex
│
├── engine/
│   ├── parse_tex.py
│   ├── classify_blocks.py
│   ├── apply_template.py
│   ├── qc_citations.py
│   └── cli.py   (main entry point)
│
├── output/
│
└── requirements.txt
