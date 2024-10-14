import asyncio
import malloy
from malloy.data.bigquery import BigQueryConnection


async def main():
    with malloy.Runtime() as runtime:
        runtime.add_connection(BigQueryConnection())

        data = await runtime.load_source("""
            source:my_source is bigquery.table('proj.dataset.my_data') extend {
                measure:
                sale_count is count()
            }
            """).run(query="""
            run: my_source -> {
                group_by: sold_date
                aggregate: sale_count
                }
            """)

        dataframe = data.to_dataframe()
        print(dataframe.head())

if __name__ == "__main__":
  asyncio.run(main())