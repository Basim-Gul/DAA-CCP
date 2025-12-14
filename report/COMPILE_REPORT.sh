#!/bin/bash
# Script to compile comprehensive assignment report

OUTPUT="Assignment03_Complete_Report.md"

cat > "$OUTPUT" << 'REPORT_START'
---
title: "Assignment 03: Application of the Knapsack Problem in Air Flight Optimization"
subtitle: "Comprehensive Implementation and Analysis"
author: "Basim Gul"
course: "Design and Analysis of Algorithms (CSC-321)"
semester: "BS(CS)-5"  
instructor: "Dr. Muhammad Tariq Siddique"
university: "COMSATS University Islamabad"
date: "December 14, 2025"
---

<div style="page-break-after: always;"></div>

# Title Page

<div style="text-align: center; padding: 100px 0;">

# ASSIGNMENT 03

## Application of the Knapsack Problem
## in Air Flight Cargo Optimization

---

### Comprehensive Implementation and Analysis

---

**Submitted By:**  
**Basim Gul**  
BS(CS)-5  

**Course:**  
Design and Analysis of Algorithms (CSC-321)

**Instructor:**  
Dr. Muhammad Tariq Siddique

**Department of Computer Science**  
**COMSATS University Islamabad**

**Date of Submission:**  
December 14, 2025

</div>

<div style="page-break-after: always;"></div>

# Declaration

I hereby declare that the work presented in this report is my own and has been completed in accordance with the academic integrity policies of COMSATS University Islamabad.

**Student Name:** Basim Gul  
**Signature:** _______________  
**Date:** December 14, 2025

<div style="page-break-after: always;"></div>

# Acknowledgments

I would like to express my sincere gratitude to:

- **Dr. Muhammad Tariq Siddique**, my course instructor, for his guidance and valuable insights throughout this assignment
- **Department of Computer Science**, COMSATS University Islamabad, for providing excellent computing resources
- **Python and Matplotlib communities** for their excellent open-source tools
- **My classmates** for helpful discussions on algorithm analysis

<div style="page-break-after: always;"></div>

REPORT_START

echo "Report compiled with $(wc -l < "$OUTPUT") lines"

