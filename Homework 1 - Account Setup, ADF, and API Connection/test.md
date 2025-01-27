# HW1: Azure Account Setup & API Connection

## Part 1: Azure Account Setup
**Objective:**

Set up an Azure account and the foundational resources necessary for the subsequent homework assignments. This involves creating a Resource Group, Storage Account, Blob Storage container, Data Factory, and creating an OpenWeather account for an API key.
#### 1. Sign Up for an Azure Student Account
1. Visit the [Azure Student Free Account website](https://azure.microsoft.com/en-us/free/students) and click on “Activate your student benefits.”
2. Follow the prompts to sign up for a new Azure student account. You might need to verify your student status through your educational institution’s email. Note that Azure offers *$100* in credits for 12 months and a range of free services.
3. Make sure to select the **Azure Student Subscription** (and not the BU IS&T subscription)
Using your existing Data Factory, you will:

#### 2. Set Up a Resource Group within your Subscription
> 💡 
[Resource groups](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources) are logical containers where you can deploy and manage Azure resources like virtual machines, web apps, databases, and storage accounts. Similar to the folder system inside your laptop/personal computer, it helps organize related Azure resources  that work together to support a specific application or service.
>
<div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
  <img src="images/create%20a%20resource%20group%20part%201.png" alt="Part 1" style="width: 30%; max-width: 400px; height: auto;">
  <img src="images/create%20a%20resource%20group%20part%202.png" alt="Part 2" style="width: 30%; max-width: 400px; height: auto;">
  <img src="images/create%20a%20resource%20group%20part%203.png" alt="Part 3" style="width: 30%; max-width: 400px; height: auto;">
</div>

#### 3. Create a Data Lake Storage Gen 2 Account
> 💡
[Data Lake Storage Gen 2](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) is a set of capabilities dedicated to big data analytics built on top of [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview). It provides file system semantics, file-level security, and scale on top of Azure Blob Storage’s low-cost, tiered storage, with high availability/disaster recovery capabilities.
*A good analogy is to think of Blob Storage as a pile of books, whereas Data Lake Storage Gen 2 is putting that pile into a library, giving order/hierarchy to the unstructured pile of data files.*
>
Configuration Settings:
1. **Region**: ‘(US) East US 2’
2. **Performance**: Standard (for general-purpose storage)
3. **Redundancy**: Locally redundant storage (LRS) is sufficient for this homework
4. **Advanced**: Enable "Hierarchical namespace", which enables Data Lake Storage Gen 2 features on top of your Blob Storage.
<div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
  <img src="images/create storage account step 1.png" alt="Part 1" style="width: 30%; max-width: 400px; height: auto;">
  <img src="images/create storage account step 2.png" alt="Part 2" style="width: 30%; max-width: 400px; height: auto;">
</div>
<div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
  <img src="images/create storage account step 3.png" alt="Part 3" style="width: 30%; max-width: 400px; height: auto;">
  <img src="images/create storage account step 4.png" alt="Part 3" style="width: 30%; max-width: 400px; height: auto;">
</div>

>💡 
[Data redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) is the practice of storing multiple copies of the same data in different locations or systems. While having multiple copies of data might seem inefficient, it ensures that the data remains available and reliable across different regions and in the case of database failure.
<u>Designing Data-Intensive Applications</u> by Martin Kleppmann describes the reasoning behind data redundancy well:
*"Replication is used to keep a copy of the same data on multiple machines, which can serve several purposes: to increase **availability** (allowing the system to continue working even if some parts of it are down), to increase **read throughput** (by load balancing reads across replicas), and to **reduce latency** (by keeping data geographically close to users)…”*
In the context of our Azure use case,  we will be using the cheapest redundancy, **LRS**, which maintains three synchronous copies within a single data center. It does not replicate across other data centers/regions, and is the most at-risk in terms of data unavailability events.

#### 4. Create a Blob Storage Container within your Storage Account
This can be done by navigating to the storage browser within the Azure Blob Storage sidebar menu, and creating a container. If hierarchal namespace (Data Lake V2 Feature) wasn’t enabled, you would have noticed the ability to create a flat container, but not a container stored within a container (nested containers).
<div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
  <img src="images/create storage account step 4.png" alt="Part 3" style="width: 50%; height: auto;">
</div>

#### 5. Create a Azure Data Factory within your Resource Group
> 💡
Azure Data Factory(ADF) is a cloud-based data integration service that is designed to orchestrate and automate data movement and transformation across various data sources and destinations. It is cost effective (pay as you use) and scalable for enterprise data needs.
<div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
  <img src="images/create an adf.png" alt="Part 3" style="width: 50%; height: auto;">
</div>

#### 6. (Optional) Create and Connect a Git Repository
[Github](https://learn.microsoft.com/en-us/azure/data-factory/connector-github?tabs=data-factory) can be connected directly with your ADF environment to automate the build, test, and deployment process of pipelines. For homework purposes, this step is not necessary, but is an option you can consider for your future projects.
<div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
  <img src="images/create github connection to adf.png" style="width: 90%; height: auto;">
</div>

#### 7. Sign Up for OpenWeatherMap Free Access
We will be pulling from the OpenWeatherMap API for both stream data and batch processed data. This API provides access to current weather data, forecasts, and historical weather data for any location worldwide. 
1. **Create an OpenWeatherMap Account**:
    - Visit the [OpenWeatherMap for Education website](https://openweathermap.org/our-initiatives) and follow the steps to sign up for an account.
    - Provide the necessary information to verify your student status and gain free access to their services.
<div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
  <img src="images/create an open weather account.png" style="width: 80%; height: auto;">
</div>

#### 8. Grant Instructors Access to Resource Group
In order for your assignments to be graded, the instructors require access to view your resource group containing your assignment work. Below is a series of screenshots detailing how to properly grant instructors access.
<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; flex-wrap: wrap; text-align: center;">
  <img src="images\grant instructors part 1.png" alt="Grant Instructors Part 1" style="max-width: 50%; height: auto;">
  <i style ="max-width: 50%; height: auto;" >Within the resource group menu, there is a submenu called Access Control, where you can add/remove role assignments to the overall resource.</i>
  <img src="images\grant instructors part 2.png" alt="Grant Instructors Part 1" style="max-width: 50%; height: auto;">
  <i style ="max-width: 50%; height: auto;" >Amongst the roles you can assign, we want to assign instructors “Contributor” over the entire resource group. This allows instructors to view any resource created within the resource group.</i>
  <img src="images\grant instructors part 3.png" alt="Grant Instructors Part 3" style="max-width: 50%; height: auto;">
  <i style ="max-width: 50%; height: auto;" >We then want to assign access to the relevant instructors.</i>
<img src="images\grant instructors part 4.png" alt="Grant Instructors Part 3" style="max-width: 50%; height: auto;">
  <i style ="max-width: 50%; height: auto;" >We then ensure that the assignment type is both “Active” and “Permanent” </i>
</div>

## Part 2: Connecting to the API via the ADF
**Objective:**
Ingest weekly historical weather and air pollution data from the OpenWeather APIs into Azure Data Lake Storage using Azure Data Factory. We want at least a **year’s worth of this weekly data**, and will have to model our pipelines to account for the API call restrictions. This involves using the API key within ADF, ADF linked services, building & running pipelines, monitoring the data ingestion process, and pushing configurations to a GitHub repository. 

*Before we start, we need to first learn about Data Lakehouse, as well as the Medallion Lakehouse Architecture.*

> 💡 
A [Data Lakehouse](https://learn.microsoft.com/en-us/azure/databricks/lakehouse/) is a data management system that combines the best features of data lakes (scalability, flexibility) and data warehouses (structure, performance) all under a single architecture. 
>

> 💡
[Medallion Lakehouse Architecture](https://learn.microsoft.com/en-us/azure/databricks/lakehouse/medallion) is a data management and analytics architecture pattern used in modern Data Lakehouse environments. This architecture is designed to organize and manage data efficiently as it flows through different stages, typically referred to as Bronze, Silver, and Gold layers. Refer to the documentation on the specific differences of the layers.
>

> 💡 
Originally, the various assignments utilized the Azure Key Vault service to securely contain API keys. Having unencrypted API keys within pipelines/code is a security issue, but for our homework purposes we want to avoid complicating processes. Identity management and permission sets will be discussed in class, but not required for the homework.
>
#### 1. Create an ADF Pipeline for Data Ingestion
Now, we have to create pipelines to ingest the historical data into our ADLS storage. The pipeline must ingest the following historical weather & air pollution data:
- Location: Boston *(this can be done by identifying the longitude and latitude coordinates of the Boston area)*
- Frequency: Hourly
- Time Frame: Data from approximately **one year ago to yesterday**, ensuring coverage for roughly 11 months.

For better organization and maintenance, we want to create **two separate pipelines** for weather data and air pollution data ingestion. We are going to start with the Historical Weather Pipeline.
##### For Each Activity
Due to the API restrictions, we have a maximum amount of data we can get per API call. Thus, our pipeline will have to make multiple API calls through [Copy Data](https://learn.microsoft.com/en-us/azure/data-factory/quickstart-hello-world-copy-data-tool) activities within a [ForEach](https://learn.microsoft.com/en-us/azure/data-factory/control-flow-for-each-activity) loop, where the source collects data from the API and sinks it into local storage.
<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; flex-wrap: wrap; text-align: center;">
  <img src="images\foreach activity.png" alt="Grant Instructors Part 1" style="max-width: 50%; height: auto;">
  <i style ="max-width: 60%; height: auto;" ></i>
  </div>

To make **multiple API calls** within ADF, we need to utilize the [**ForEach**](https://learn.microsoft.com/en-us/azure/data-factory/control-flow-for-each-activity) activity flow, which will repeat the **‘Copy’** activity for the specified dates. This activity is used to iterate over a collection and executes specified activities in a loop. The loop implementation of this activity is similar to ForEach looping structure in programming languages. Ensure  the **Sequential** option is checked if you want the iterations to run one after another. If you want them to run in parallel, leave it unchecked.

The **Items**   property (within the ForEach loop) is used in Azure Data Factory or Azure Synapse Pipelines for iterating over a collection of values. It defines the list of values or objects that a loop will iterate over.
>💡
The main [difference](https://learn.microsoft.com/en-us/azure/data-factory/concepts-parameters-variables) is that pipeline parameters cannot be modified during a pipeline run, whereas pipeline variables are values that can be set and modified during a pipeline run via “set variable activity”. For the purpose of this assignment, you will need a variable/parameter to define the range in which the ForEach loop should run. 
<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; flex-wrap: wrap; text-align: center;">
  <img src="images\parameter vs variable.png" alt="Grant Instructors Part 1" style="max-width: 50%; height: auto;">
  <i style ="max-width: 50%; height: auto;" >You can access Parameters of a pipeline by simply clicking an empty area in the pipeline window, and the menu would appear.</i>
  </div>

##### Linked Service Setup
After creating a new Activity in the pipeline orchestration menu, you can click “+New” in the Linked Service menu under “Source” and “Sink”.
<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; flex-wrap: wrap; text-align: center;">
  <img src="images\linked service +new.png" alt="Grant Instructors Part 1" style="max-width: 50%; height: auto;">
  <i style ="max-width: 50%; height: auto;" ></i>
  </div>

>💡 
[Linked services](https://learn.microsoft.com/en-us/azure/data-factory/concepts-linked-services?tabs=data-factory) refer to connections to external resources/services, enabling the platform to interact with those sources. The true power of linked services comes from their *reusability in different pipelines/dataflows.*
For example, if you are copying data from an Azure SQL Database to an Azure Blob Storage, linked services must be first defined for the SQL Database and for the Azure Blob Storage. After creating these services, if you need to reference those same datasets for different transformations/dataflows, you can just reference the created linked services instead of making the connections from scratch again.
We will be creating ADF linked services for all resources we will be using. 

>💡[**REST vs HTTP:**](https://learn.microsoft.com/en-us/azure/data-factory/connector-http?tabs=data-factory)
You have two choices when creating linked services connecting to the OpenWeather API:
[REST](https://learn.microsoft.com/en-us/azure/data-factory/connector-rest?tabs=data-factory) connector specifically support copying data from RESTful APIs, following the REST architectural principles. 
[HTTP](https://learn.microsoft.com/en-us/azure/data-factory/connector-http?tabs=data-factory) connector is generic to retrieve data from any HTTP endpoint, e.g. to download file. It’s requests are unstructured compared to REST, and requires specific mapping to adhere to API requests.
Before REST connector becomes available for an API, you may use the HTTP connector to copy data from RESTful APIs, which is supported but less functional comparing to REST connector. For the purpose of the homework, we will be using the **HTTP** connector. The only difference being that with a REST dataset, you wouldn’t initially specify the datatype whereas with HTTP you would (JSON).


>💡
[Anonymous authentication](https://learn.microsoft.com/en-us/iis/configuration/system.webserver/security/authentication/anonymousauthentication) allows users to access resources or applications without providing any identity verification (e.g., username or password). It is typically used for public-facing applications or websites where user identity is not necessary for basic access.

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
SELECT
 *
FROM <cbsComplaints>
WHERE DATEA = CONVERT(Date, GETDATE() - 1)
```

> 💡: The "GETDATE() - 1" is a SQL command specifying Today's date -1 day, aka yesterday. However, if your latest file download is prior to today, or happens to fall on a weekend, you will have to change the "-1" to the most recent day where records exist in the source dataset. (-2, -5, -7, etc for the number of days back)

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
