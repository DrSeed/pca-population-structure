# Pca Population Structure

Hand a population geneticist a genotype matrix and the first thing they do is run PCA. Why? Because ancestry is written into the correlations between variants — and PCA reads it straight out in two dimensions.

## Why This Matters

Population structure is a confounder in every genetic association study: if your cases and controls differ in ancestry, you will get false hits that have nothing to do with disease. PCA on genotypes exposes that structure so you can correct for it — and when ancestry labels are missing, it is how you infer them in the first place.

## How It Works

1. Encode each genotype as 0, 1, or 2 copies of the variant.
2. Run PCA across individuals.
3. Plot PC1 against PC2 — individuals cluster by shared ancestry.

## What the Demo Shows

![Demo](figures/demo.png)

The demo simulates three populations with different allele-frequency profiles. On the PCA they separate into three distinct clouds — precisely the structure you would adjust for before testing a single association.

## Run It

```bash
pip install -r requirements.txt
python demo.py
```

> Demonstrated on synthetic data, so the whole thing is reproducible with no external downloads.
