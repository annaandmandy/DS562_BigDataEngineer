# HW1: Azure Account Setup & API Connection

**Objective:**

Set up an Azure account and the foundational resources necessary for the subsequent homework assignments. This involves creating a Resource Group, Storage Account, Blob Storage container, Data Factory, and connecting a Git repository.


## Part 1: Azure Account Setup
#### 1. Sign Up for an Azure Student Account
1. Visit the [Azure Student Free Account website](https://azure.microsoft.com/en-us/free/students) and click on “Activate your student benefits.”
2. Follow the prompts to sign up for a new Azure student account. You might need to verify your student status through your educational institution’s email. Note that Azure offers *$100* in credits for 12 months and a range of free services.
3. Make sure to select the **Azure Student Subscription** (and not the BU IS&T subscription)
Using your existing Data Factory, you will:

#### 2. Set Up a Resource Group within your Subscription
> **NOTE** - What is a Resource Group?  
[Resource groups](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources) are logical containers where you can deploy and manage Azure resources like virtual machines, web apps, databases, and storage accounts. Similar to the folder system inside your laptop/personal computer, it helps organize related Azure resources  that work together to support a specific application or service.
>
<div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
  <img src="images/create%20a%20resource%20group%20part%201.png" alt="Part 1" style="width: 30%; max-width: 400px; height: auto;">
  <img src="images/create%20a%20resource%20group%20part%202.png" alt="Part 2" style="width: 30%; max-width: 400px; height: auto;">
  <img src="images/create%20a%20resource%20group%20part%203.png" alt="Part 3" style="width: 30%; max-width: 400px; height: auto;">
</div>

#### 3. Create a Data Lake Storage Gen 2 Account
> **NOTE** - What is a Data Lake Storage Account?  
[Data Lake Storage Gen 2](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) is a set of capabilities dedicated to big data analytics built on top of [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview). It provides file system semantics, file-level security, and scale on top of Azure Blob Storage’s low-cost, tiered storage, with high availability/disaster recovery capabilities.
*A good analogy is to think of Blob Storage as a pile of books, whereas Data Lake Storage Gen 2 is putting that pile into a library, giving order/hierarchy to the unstructured pile of data files.*

>




> **Hint** Download the Homework1c.pdf file from the ‘Transforming and Staging’ folder in this repository and review its contents.










## Steps to Complete Homework 1c

> For this course, you will use the “Azure for Students” offer provided by Microsoft. This offer allows for a $100 credit that can be replenished once a year as long as a student email address is being used. You will be expected to manage your budget. By adhering closely to the instructions outlined in the homework assignments, you will remain within the $100 credit limit. However, any expenses incurred beyond this allocation will be your responsibility.  

### Step 1: Set Up Your SQL Server and Database
Once again, you should use the `bash fromTemplate.sh` script from the [top-level ReadMe.md file](https://github.com/cseferlis/OMDSMod4/blob/main/README.md) for creating your SQL Server, using the following command to deploy resources, remembering to replace your resource group, template and parameter details as with Homework 1c:

```azurecli-interactive
az deployment group create --resource-group <resource-group-name> --template-file <path-to-template.json> --parameters <path-to-parameters.json>
```

### Step 2: Create Your Database Table
Use the `Complaints Reference File` to set up your table attributes with the correct data types. It is recommended to use `NVARCHAR` for text columns to handle Unicode characters. The reference file specifies the lengths of each of the attributes (columns) when defining your database table.

### Step 3: Load Data with Azure Data Factory
1. Use Azure Data Factory to create a pipeline that includes:
   - **Transformation**: Convert the `DateA` column from text to a date (not datetime) format.
   - **Loading**: Insert the data into the `<initials>Complaints` table.

### Step 4: Query and Export Results
After loading the data, run the following query in your SQL Server, making sure to replace the table name with the name you created for your table in your database:

```sql
SELECT *
FROM <cbsComplaints>
WHERE DATEA = CONVERT(Date, GETDATE() - 1)
```

> **Note**: The "GETDATE() - 1" is a SQL command specifying Today's date -1 day, aka yesterday. However, if your latest file download is prior to today, or happens to fall on a weekend, you will have to change the "-1" to the most recent day where records exist in the source dataset. (-2, -5, -7, etc for the number of days back)

Output the results to a file and save it as a PDF for submission.

## Reference Documents and Tools
- [Getting Started with Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/quickstart-create-data-factory)
- [Creating a Storage Account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal)
- [Creating a Database in Azure SQL Server Using Your Existing SQL Server](https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart?view=azuresql&tabs=azure-portal)
- [Creating a Table in an Azure SQL Database](https://www.edureka.co/community/62364/how-to-create-table-in-azure-sql-database)
- [Complaints Data File](https://static.nhtsa.gov/odi/ffdd/cmpl/FLAT_CMPL.zip)
- [Complaints Reference File](https://static.nhtsa.gov/odi/ffdd/cmpl/Import_Instructions_Excel_All.pdf)
- [Copy Tool](https://docs.microsoft.com/en-us/azure/data-factory/copy-activity-overview)
- [Data Flow](https://docs.microsoft.com/en-us/azure/data-factory/concepts-data-flow-overview)

---

## Submission

> Submit the following as proof of your work:

**IMPORTANT:** Ensure your BU account information is visible in the top right corner of your screenshots for verification.

1. **Screenshot of Query Execution in Azure SQL Database** 
   - <img src="../../images/hw1c/hw3-screenshot.png" alt="Screenshot" width="400">

2. **PDF of SQL Query Output** Typically you can expect approximately a couple hundred records added per day, so if you are getting more, check your query, else, if you have zero, you may need to go back further with your GETDATE command.

Save the screenshots as `.png` or `.jpg` files and upload them through the course submission portal for Homework 1c. For a further explanation on how to submit your assignment on Gradescope, refer to the Blackboard page or request support from your Learning Facilitator.

---

## Points to Consider 🤔
- How do you use the `Complaints Reference File` to create a table in Azure SQL Database?
- How do you use the `Copy Tool` to load data from Azure Storage to Azure SQL Database?
- How do you handle rows with missing values?
- What happens if the data in the txt file does not adhere to the datatype you've set for your SQL database table?
- What if the header column names differ from table column names?
- What is the current format of the file, the delimiter, and the number of columns?
- How do you map columns and change their data types?

---

Ensure you understand each step and reach out with any questions!
